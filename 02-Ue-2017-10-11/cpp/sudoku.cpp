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

using namespace std;

 
Sudoku::Sudoku() 
{
    for(int i = 0; i < 9; i++) {
        for(int j = 0; j < 9; j++){
            for(int e = 0; e < 10; e++) {
                grid[i][j][e] = (e ? true : false);
                std::printf(grid[i][j][e] ? "true\n" : "false\n");
            }
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
    if (sudo_in.is_open()) {
        while (getline (sudo_in, line) ) {
            cout << line << endl;
        }
    }
    sudo_in.close();
    return 0;
}
