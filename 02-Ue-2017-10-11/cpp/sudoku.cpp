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
    printf("ichbineinsudoku");
}

int Sudoku::magic()
{
    grid = 1;
    cout << grid;
    return grid;
}
