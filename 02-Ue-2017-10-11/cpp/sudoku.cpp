/*
Program solving sudokus:

Masterplan -
 1- being able to read sudoku data
 2- save data into suitable array of vector or sth. similar
 3- solve sudoku data using some clever strategy (or brute force)
 4- export solved sudoku into new file

Structure -
 define class Sudoku
 methods for im-/exporting and solving
*/


#include <iostream>
#include <stdio.h>
#include <fstream>
#include "sudoku.h"
#include <string>
#include <cstdlib> // for exit()

using namespace std;

 
Sudoku::Sudoku() 
{
    // initialise array: entire 0th dimension 'false'
    // indicating that no number is known
    // all other: 'true'
    // indicating that all numbers 1-9 are possibly true
    for(int i = 0; i < 81; i++) {
        for(int e = 0; e < 10; e++) {
            grid[i/9][i%9][e] = (e ? true : false);
        }
    }
    printf("\n ichbineinsudoku\n");
}

int Sudoku::import()
{
    ifstream sudo_in ("sudokus/sudoku_a_1.dat");
//    ifstream sudo_in ("sudokus/ku20060924.sudo");

    if (!sudo_in) {
        exit(1);
        // end process if file cannot be openend
    }
    for(int i = 0; sudo_in; i++) {
        string strInput;
        sudo_in >> strInput;
        int entry = atoi(strInput.c_str());
        if (entry) {
            // number known, #th entry = 'true', others = 'false'
            grid[i/9][i%9][ 0 ] = true; 
            for(int e = 1; e < 10; e++) {
                grid[i/9][i%9][e] = ( (e == entry) ? true : false);
            // set #th entry = 'false' in all other elements...
            // ...of this line, row and block:
            }
            setOthers(i, entry);
        }
    }
    sudo_in.close();
    return 0;
}

std::ostream& operator<< (std::ostream &out, const Sudoku &sudoku)
{
    for(int i = 0; i < 81; i++) {
        if (sudoku.grid[i/9][i%9][0]) {
            for(int e = 1; e < 10; e++) {
                if (sudoku.grid[i/9][i%9][e]) {
                    printf("%i", e);
                    break;
                }
            }
        }else{
            printf("%i", 0);
        }
        printf( (i%3 == 2) ? "  " : " ");
        printf( (i%9 == 8) ? "\n" : " ");
        printf( (i%27 == 26) ? "\n" : "");
    }
    return out;
}

int Sudoku::checkElement(int x, int y)
{
    int fin = 0;
    for(int e = 1; e < 10; e++) {
        if (grid[x][y][e]) {
            fin++;
        }
        if (fin == 1) grid[x][y][e] = true;
    }
    return 0;
}

int Sudoku::setOthers(int i, int entry)
{
    for(int k = 0; k < 9; k++) {
    // set other elements in line:
        if (k != i%9 && !grid[i/9][k][0]) {
            grid[i/9][k][entry] = false;
            checkElement(i/9, k);
        }
    // set other elements in row:
        if (k != i/9 && !grid[k][i%9][0]) {
            grid[k][i%9][entry] = false;
            checkElement(k, i%9);
        }
    }
    cout << "Element " << i/9 << ", " << i%9 << endl;
    for(int a = (i/9)/3*3; a < (i/9)/3*3+3; a++) {
        for(int b = (i%9)/3*3; b < (i%9)/3*3+3; b++) {
            cout << "line " << a << ", row " << b << endl;
            if (a != i/9 && b != i%9 && !grid[a][b][0]) {
                grid[a][b][entry] = false;
                checkElement(a, b);
            }
        }
    }
    return 0;
}

int Sudoku::magic()
{
    cout << grid;
    return 0;
}
