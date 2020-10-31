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

