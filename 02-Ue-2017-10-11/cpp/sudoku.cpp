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

int Sudoku::import(const char* lFile)
{
    ifstream sudo_in (lFile);

    if (!sudo_in) {
        exit(1);
        // end process if file cannot be openend
    }
    string strInput;
    sudo_in >> strInput;
    if( strInput.length() <= 1 ) {
        int i = 0;
        do {
            int entry = atoi(strInput.c_str());
            if (entry) {
                setElement(i, entry);
                setOthers(i);
            }
            sudo_in >> strInput;
            i++;
        } while (sudo_in); 
    } else {
        for(int i = 0; i < 81; i++) {
            char input = strInput[i];
            int entry = input - '0';
            if (entry) {
                setElement(i, entry);
                setOthers(i);
            }
        }
    }
    sudo_in.close();
    magicApplied = 0;
    return 0;
}

std::ostream& operator<< (std::ostream &out, const Sudoku &sudoku)
{
    int fin = 0;
    for(int l = 0; l >= 0; l--) {
//        cout <<l<<l<<l<<l<<l<<l<<l<<l<<l<< endl;
        for(int i = 0; i < 81; i++) {
            cout << sudoku.grid[i][l];
            if (sudoku.grid[i][l] == 0) fin = 1;
            printf( (i%3 == 2) ? "  " : " ");
            printf( (i%9 == 8) ? "\n" : " ");
            printf( (i%27 == 26) ? "\n" : "");
        }
        cout << endl;
    }
    if (fin == 1 && sudoku.magicApplied) cout << "This sudoku is resistant to magic :(" << endl;
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
        setOthers(i);
//        cout << "wow" << endl;
        return solo;
    }
    cout << "Element has no future!!" << endl;
    exit(1);
}

int Sudoku::setOthers(int i)
{
    for(int k = 0; k < 9; k++) {
    // set other elements in line:
        if ((i/9)*9+k != i) {
            grid[(i/9)*9+k][ grid[i][0] ] = 0;
            checkElement(i/9+k);
        }
    // set other elements in row:
        if (k*9+i%9 != i) {
            grid[k*9+i%9][ grid[i][0] ] = 0;
            checkElement(k*9+i%9);
        }
    }
    // set other elements in block:
    for(int a = ((i/9)/3)*3; a < ((i/9)/3)*3+3; a++) {
        for(int b = ((i%9)/3)*3; b < ((i%9)/3)*3+3; b++) {
            if (a*9+b != i) {
                grid[a*9+b][ grid[i][0] ] = 0;
                checkElement(a*9+b);
            }
        }
    }
    return 0;
}

int Sudoku::magic()
{
    // check whether there are any numbers that can only exist
    // in a single element of a line/row/box
    int solo = -1;
    int magicHappened = 0;
    cout << "Here comes the magic..." << endl;

    for(int j = 0; j < 9; j++) {
        for(int e = 1; e < 10; e++) {
            for(int k = 0; k < 9; k++) {
        // check in line:
                if ( checkElement(j*9+k) == e ) {
                    solo = -2;
//                    cout << "@" << j << k <<" #" << e << "  already known (line)" << endl;
                    break;
                }
                if (grid[j*9+k][e]) {
                    if (solo == -1) solo = k;
                    else {
                        solo = -3;
//                        cout << "@" << j << k <<" #" << e <<" no magic possible (line)" << endl;
                        break;
                    }
                }
            }
            if (solo >= 0) {
                setElement( j*9+solo, e);
                setOthers( j*9+solo );
//                cout << "@" << j << solo <<" #" << e << " MAGIC happended!!! (line)" << endl;
            magicHappened = 1;
            }
            if (solo == -1) {
                cout << "Neither already known, nor anywhere possible! (line)" << endl;
                exit(1);
            }
            solo = -1;

            for(int k = 0; k < 9; k++) {
        // check in row:
                if ( checkElement(k*9+j) == e ) {
                    solo = -2;
//                    cout << "@" << k << j <<" #" << e << "  already known (row)" << endl;
                    break;
                }
                if (grid[k*9+j][e]) {
                    if (solo == -1) solo = k;
                    else {
                        solo = -3;
//                        cout << "@" << k << j <<" #" << e <<"no magic possible (row)" << endl;
                        break;
                    }
                }
            }
            if (solo >= 0) {
                setElement( solo*9+j, e);
                setOthers( solo*9+j );
//                cout << "@" << solo << j <<" #" << e << " MAGIC happended!!! (row)" << endl;
            magicHappened = 1;
            }
            if (solo == -1) {
                cout << solo << j << " Number " << e << " Neither already known, nor anywhere possible! (row)" << endl;
                cout << this;
                return 1;
            }
            solo = -1;
        }
    }

//    cout << endl << "Start of mega box checking!!! SOLO: " << solo << endl << endl;

    for(int j = 0; j < 55; j+= 27) {
        for(int k = 0; k < 3; k ++) {
            int i = j+k*3; 
            for(int e = 1; e < 10; e++) {
                for(int a = ((i/9)/3)*3; a < ((i/9)/3)*3+3; a++) {
                    for(int b = ((i%9)/3)*3; b < ((i%9)/3)*3+3; b++) {

                        if ( checkElement(a*9+b) == e ) {
                            solo = -2;
//                            cout << "@" << a << b <<" #" << e << "  already known (box)" << endl;
                            break;
                        }
                        if (grid[a*9+b][e]) {
                            if (solo == -1) solo = (a*9+b);
                            else {
                                solo = -3;
//                                cout << "@" << a << b <<" #" << e <<"no magic possible (box)" << endl;
                                break;
                            }
                        }
                    }
                }
                if (solo >= 0) {
                    setElement( solo, e);
                    setOthers( solo );
//                    cout << "@" << solo/9 << solo%9 <<" #" << e << " MAGIC happended!!! (box)" << endl;
                magicHappened = 1;
                }
                if (solo == -1) {
                    cout << solo/9 << solo%9 << " Number " << e << " Neither already known, nor anywhere possible! (box)" << endl;
                    return 1;
                }
                solo = -1;
            }
        }
    }

    magicApplied = 1;
    return magicHappened;

}
