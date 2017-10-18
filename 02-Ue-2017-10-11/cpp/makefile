# https://stackoverflow.com/questions/2481269/how-to-make-a-simple-c-makefile
# https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html#zz-2.

CXX=g++
CPPFLAGS=-g -Wall
LDFLAGS=-g

all: blub

blub: runrun.o sudoku.o
	g++ $(LDFLAGS) -o blub runrun.o sudoku.o

runrun.o: runrun.cpp sudoku.o
	g++ $(CPPFLAGS) -c runrun.cpp

sudoku.o: sudoku.cpp
	g++ $(CPPFLAGS) -c sudoku.cpp

clean:
	rm blub runrun.o sudoku.o
