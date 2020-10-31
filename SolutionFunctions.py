from UtilityFunctions import *

def backtrackSolve(sudoku):
    find = findEmptySpot(sudoku)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if isValid(sudoku, i, (row, col)):
            sudoku[row][col] = i

            if backtrackSolve(sudoku):
                return True

            sudoku[row][col] = 0

    return False
