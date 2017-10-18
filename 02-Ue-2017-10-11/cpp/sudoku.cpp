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

using namespace std;

 
Sudoku::Sudoku() 
{
    printf("ichbineinsudoku\n");
    for(int i = 0; i < 9; i++) {
        for(int j = 0; j < 9; j++){
            for(int e = 0; e < 10; e++) {
                grid[i][j][e] = (e ? false : true);
                std::printf(grid[i][j][e] ? "true\n" : "false\n");
            }
        }
    }
}

int Sudoku::magic()
{
    cout << grid;
    return 0;
}
