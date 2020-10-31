from UtilityFunctions import *
from SolutionFunctions import *


def main():

    sudokuString = input("Enter the sudoku in a string format, where empty places are denoted by .")
    sudoku = createBoard(sudokuString) 
    solution = backtrackSolve(sudoku)
    if solution == True:
        printBoard(sudoku)
    else:
        print("Solution not found")


if __name__ == "__main__":
    main()

#4.....8.5.3.........7.......2.....6.....8.4......1.......6.3.7.5..2.....1.4......
