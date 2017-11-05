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
            grid[i][e] = (e ? true : false);
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
            grid[i][ 0 ] = entry; 
            for(int e = 1; e < 10; e++) {
                grid[i][e] = ( (e == entry) ? 1 : 0);
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
//        if (sudoku.grid[i][0]) {
//            for(int e = 1; e < 10; e++) {
//                if (sudoku.grid[i][e]) {
//                    printf("%i", e);
//                    break;
//                }
//            }
//        }else{
//            printf("%i", 0);
//        }
        cout << sudoku.grid[i][0];
        printf( (i%3 == 2) ? "  " : " ");
        printf( (i%9 == 8) ? "\n" : " ");
        printf( (i%27 == 26) ? "\n" : "");
    }
    return out;
}

int Sudoku::checkElement(int i)
{
    if (grid[i][0]) return grid[i][0];

    int entry = 0;
    for(int e = 1; e < 10; e++) {
        if (grid[i][e]) {
            if (!entry) entry = e;
            else {
               return 0;
            }
        }
    }

    if (!entry) {
        cout << "Sudoku broken!" << endl;
        return -1;
    } else {
        if (!grid[i][0]) {
            grid[i][0] = 1;
            setOthers(i);
        }
        return entry;
    }
    exit(-1);
}

int Sudoku::setOthers(int i)
{
    int remember = 0;
    for(int k = 0; k < 9; k++) {
    // set other elements in line:
        grid[i/9+k][ grid[i][0] ] = 0;
        checkElement(i/9+k);
    // set other elements in row:
        grid[k*9+i%9][ grid[i][0] ] = 0;
        checkElement(k*9+i%9);
    }
    // set other elements in block:
    for(int a = (i/9)/3*3; a < (i/9)/3*3+3; a++) {
        for(int b = (i%9)/3*3; b < (i%9)/3*3+3; b++) {
            grid[a*9+b][ grid[i][0] ] = 0;
            checkElement(a*9+b);
        }
    }
    return 0;
}

int Sudoku::magic()
{
    // check whether there are any numbers that can only exist
    // in a single element of a line/row/box
    int solo[10];
    solo[0] = 0;
    for(int i = 1; i < 10; i++) solo[i] = 0;

    for(int i = 0; i < 81; i++) {
        for(int k = 0; k < 9; k++) {
        // check in line:
            if ( k != i%9 && !checkElement(i/9+k) ) {
                grid[i/9+k][entry] = false;
                if ( checkElement(i/9+k) == 2) {
                    exit(2);
                }
            }
        // check in row:
            if ( k != i/9 && !checkElement(k*9+i%9) ) {
                grid[k*9+i%9][entry] = false;
                if ( checkElement(k*9+i%9) == 2) {
                    exit(2);
                }
            }
        }
        // check in box:
        cout << "Element " << i/9 << ", " << i%9 << endl;
        for(int a = (i/9)/3*3; a < (i/9)/3*3+3; a++) {
            for(int b = (i%9)/3*3; b < (i%9)/3*3+3; b++) {
                cout << "line " << a << ", row " << b << endl;
                if (a != i/9 && b != i%9 && !grid[a*9+b][0]) {
                    grid[a*9+b][entry] = false;
                    if ( checkElement(a*9+b) == 2) {
                        exit(2);
                    }
                }
            }
        }
    }
    return 0;

    cout << grid;
    return 0;

}

int Sudoku::clone(int mother[][10], int daughter[][10])
{
    for(int i = 0; i < 81; i++) {
        for(int e = 0; e < 10; e++) {
            daughter[i*9][e] = mother[i*9][e];
        }
    }
    return 0;
}

int Sudoku::force()
{
    int grid_old[81][10];
    clone(grid, grid_old);
    int grid_buffer[81];
    for(int i = 0; i < 81; i++) {
        if ( !grid[i][0] ) {
            for(int e = 0; e < 10; e++) {

            }
        }
    }
    cout << grid;
    return 0;
}

