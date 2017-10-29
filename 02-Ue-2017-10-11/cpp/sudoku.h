#include <iostream>
using namespace std;

#ifndef SUDOKU_H
#define SUDOKU_H
 
class Sudoku {
    public:
        Sudoku();
        int import();
        int show();
        int magic();
        friend std::ostream& operator<< (std::ostream &out, const Sudoku &sudoku);

    private:
        bool grid[9][9][10];
        int checkElement(int x, int y);
        int setOthers(int i, int entry);
};
 
#endif
