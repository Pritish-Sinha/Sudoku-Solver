def createBoard(string):
   
    w, h = 9, 9;
    board = [[0 for x in range(w)] for y in range(h)] 
    counter = 0

    for i in range(9):
        for j in range(9):
            if string[counter] != ".":
                 board[i][j] = int(string[counter])
            counter+=1

    return board

def printBoard(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -"
                                           
        
        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j !=0: 
                print("| ", end="")

            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="") 

def findEmptySpot(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j) 

    

def isValid(sudoku, value, position):
   
    for i in range(len(sudoku[0])):
        if sudoku[position[0]][i] == value and position[1] != i:
            return False

   
    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == value and position[0] != i:
            return False

    
    mini_grid_x = position[1] // 3
    mini_grid_y = position[0] // 3

    for i in range(mini_grid_y*3, mini_grid_y*3 + 3):
        for j in range(mini_grid_x * 3, mini_grid_x*3 + 3):
            if sudoku[i][j] == value and (i,j) != position:
                return False

    return True
