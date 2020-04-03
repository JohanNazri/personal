def sudoku_print(grid):
    for i in range(0,len(grid[0])):
        print(grid[i])

def viable(n,grid,y,x):
    """Checks if an int n is a viable answer for grid[x][y]"""
    # Check to the left and right of answer
    for i in range(0,9): 
        if n == grid[i][x]:
            return False
    # Check above and below answer
    for j in range(0,9):
        if n == grid[y][j]: 
            return False

    # Get the coord of the top right of the 3X3 box for given x and y
    x_box = x //3 *3 
    y_box = y //3 *3
    # Check the values in the same 3X3 box
    for i in range(0,3): # x-coord
        for j in range(0,3): # y-coord
            if n == grid[y_box+j][x_box+i]:
                return False
    return True

def sudoku_solver(grid):
    """Solves Sudoku Puzzles using recursion"""
    for i in range(0,9): # x-coord
        for j in range(0,9): # y-coord
            # Check if there is a blank value
            if grid[j][i] == 0:
                # Try all possible answers
                for n in range(1,10):
                    # Check if the answer is viable
                    if viable(n,grid,j,i):
                        # Replace blank with an initial guess
                        grid[j][i] = n
                        # Perform the same operation on the next blank value
                        sudoku_solver(grid)
                        # Remove initial guess if it cannot be completed
                        grid[j][i] = 0
                # Return if there are no possible solutions for the blank value
                return
    # Print the grid in the desired format
    sudoku_print(grid)            

grid = [[7,4,0,1,0,0,0,0,0],[0,0,2,8,9,3,0,0,0],[0,0,0,5,0,0,0,0,6],[0,0,8,0,4,0,0,3,0],[0,3,5,7,8,0,6,0,4],[0,9,0,0,0,0,8,0,0],[8,0,0,0,5,0,0,0,7],[0,0,0,0,0,0,4,0,0],[0,0,0,6,0,0,0,0,3]]

print("----ORIGINAL----")
sudoku_print(grid)

print("\n-----SOLUTION-----")
sudoku_solver(grid)