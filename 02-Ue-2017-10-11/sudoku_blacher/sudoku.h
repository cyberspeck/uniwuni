#include <iostream>
using namespace std;

#ifndef SUDOKU_H
#define SUDOKU_H
 
class Sudoku {
    public:
        Sudoku();
        int import(const char* lFile);
        int show();
        int magic();
        int force();
        int clone(int mother[][10], int daughter[][10]);
        friend std::ostream& operator<< (std::ostream &out, const Sudoku &sudoku);

    private:
        int magicApplied;
        int grid[81][10];
        int setElement(int i, int e);
        int checkElement(int i);
        int setOthers(int i);
};
 
#endif
