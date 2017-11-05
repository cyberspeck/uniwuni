/*
Masterplan -
 1- being able to read sudoku data
 2- save data into suitable array of vector or sth. similar
 3- solve sudoku data using some clever strategy (or brute force)
 4- export solved sudoku into new file
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
        cout << entry;
        if (entry) {
            setElement(i, entry);
            setOthers(i);
        }
    }
    sudo_in.close();
    return 0;
}

std::ostream& operator<< (std::ostream &out, const Sudoku &sudoku)
{
    for(int i = 0; i < 81; i++) {
        cout << sudoku.grid[i][0];
        printf( (i%3 == 2) ? "  " : " ");
        printf( (i%9 == 8) ? "\n" : " ");
        printf( (i%27 == 26) ? "\n" : "");
    }
    return out;
}

int Sudoku::setElement(int i, int entry)
{
    grid[i][0] = entry;
    for(int e = 1; e < 10; e++) grid[i][e] = (e == entry) ? 1 : 0;
    return 0;
}

int Sudoku::checkElement(int i)
{
    if (grid[i][0]) return grid[i][0];

    int solo = 0;
    for(int e = 1; e < 10; e++) {
        if (grid[i][e]) {
            if (!solo) solo = e;
            else return 0;
        }
    }

    if (solo) {
        grid[i][0] = solo;
//        setOthers(i);
        cout << "wow" << endl;
        return solo;
    }
    cout << "Element has no future!!" << endl;
    exit(1);
}

int Sudoku::setOthers(int i)
{
    for(int k = 0; k < 9; k++) {
    // set other elements in line:
        grid[i/9+k][ grid[i][0] ] = 0;
        checkElement(i/9+k);
    // set other elements in row:
        grid[k*9+i%9][ grid[i][0] ] = 0;
        checkElement(k*9+i%9);
    }
    // set other elements in block:
    for(int a = ((i/9)/3)*3; a < ((i/9)/3)*3+3; a++) {
        for(int b = ((i%9)/3)*3; b < ((i%9)/3)*3+3; b++) {
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
    int solo = 0;

    for(int j = 0; j < 9; j++) {
        for(int e = 1; e < 10; e++) {
            for(int k = 0; k < 9; k++) {
        // check in line:
                if (grid[j*9+k][0] == e) {
                    solo = -1;
            // already known, continue with next e
                    break;
                }
                if (grid[j*9+k][e]) {
                    if (!solo) solo = k;
                    else {
                        solo = -2;
            // no magic possible, continue with next e
                        break;
                    }
                }
            }
            if (solo < 0) continue;
            if (solo) {
                setElement( j*9+solo, e);
                setOthers( j*9+solo );
            } else {
                cout << "Neither already known, nor anywhere possible! (line)" << endl;
                exit(1);
            }

            for(int k = 0; k < 9; k++) {
        // check in row:
                if (grid[k*9+j][0] == e) {
                    solo = -1;
            // already known, continue with next e
                    break;
                }
                if (grid[k*9+j][e]) {
                    if (!solo) solo = k;
                    else {
                        solo = -2;
            // no magic possible, continue with next e
                        break;
                    }
                }
            }
            if (solo < 0) continue;
            if (solo) {
                setElement( solo*9+j, e);
                setOthers( solo*9+j );
            } else {
                cout << "Neither already known, nor anywhere possible! (row)" << endl;
                exit(1);
            }
        }
    }
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
    for(int i = 0; i < 81; i++) {
        if ( !grid[i][0] ) {
            for(int e = 0; e < 10; e++) {

            }
        }
    }
    cout << grid;
    return 0;
}

