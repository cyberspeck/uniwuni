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
