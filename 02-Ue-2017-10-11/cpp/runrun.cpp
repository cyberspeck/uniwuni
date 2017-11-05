#include <iostream>
#include <stdio.h>
#include "sudoku.h"

using namespace std;


int main() {

    Sudoku mein_sudoku;
    cout << endl << mein_sudoku << endl;
    mein_sudoku.import();
    cout << endl << mein_sudoku;
//    mein_sudoku.magic();
}
