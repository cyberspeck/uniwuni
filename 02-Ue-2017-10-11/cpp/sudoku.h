#ifndef SUDOKU_H
#define SUDOKU_H
 
class Sudoku {
    public:
        Sudoku();
        int magic();
        int import();
    private:
        bool grid[9][9][10];
};
 
#endif
