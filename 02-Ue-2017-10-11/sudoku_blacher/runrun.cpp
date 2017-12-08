#include <iostream>
#include <stdio.h>
#include "sudoku.h"

#include <fstream>
#include <string>
#include <cstdlib> // for exit()

using namespace std;

int main(int argc, char* argv[]) {

    if (argc != 2) {
        cout << argc << "Usage: " << argv[0] << " path-to-sudoku" << endl;
        cout << "e.g. 'sudokus/sudoku_a_1.dat'" << endl;
        return 1;
    }

    string lFileStr;
//    string sFile;
    try {
        lFileStr = argv[1];
//        sFile = argv[2];
    }

    catch(exception& exception) {
        // Print the corresponding error message.
        cout << exception.what() << endl;
        // Terminate the program.
        return 1;
    }

    Sudoku mein_sudoku;
    mein_sudoku.import(lFileStr.c_str());
    cout << endl << mein_sudoku;
    while (mein_sudoku.magic());
    cout << endl << mein_sudoku;
}
