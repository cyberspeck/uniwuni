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
    for(int i = 0; i < 80; i++) {
        for(int e = 0; e < 10; e++) {
            grid[i/9][i%9][e] = (e ? true : false);
            printf("grid[%i][%i][%i] - ", i/9, i%9, e);
            printf(grid[i/9][i%9][e] ? "true\n" : "false\n");
        }
    }
    printf("\n ichbineinsudoku\n");
}

int Sudoku::magic()
{
    cout << grid;
    return 0;
}

int Sudoku::import()
{
    string line;
    ifstream sudo_in ("sudokus/sudoku_a_1.dat");
//    ifstream sudo_in ("sudokus/ku20060924.sudo");

    if (!sudo_in) {
        exit(1);
    }
    while (sudo_in) {
        string strInput;
        sudo_in >> strInput;
        int entry = atoi(strInput.c_str());
        for(int i = 0; i < 80; i++) {
            grid[i/9][i%9][ 0 ] = (entry ? false : true);
            for(int e = 1; e < 10; e++) {
                grid[i%3][i%9][ e ] = ( (e == entry) ? true : false);
                printf("grid[%i][%i][%i] - ", i/9, i%9, e);
                printf(grid[i/9][i%9][e] ? "true\n" : "false\n");
            }
        }
    }
    sudo_in.close();
    return 0;
}
