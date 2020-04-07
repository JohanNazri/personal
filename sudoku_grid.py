class SudokuGrid:
    def __init__(self,*grid):
        self.grid = grid

    def sudoku_print(self):
        for i in range(0,9):
            print(self.grid[i])

    def viable(self,n,y,x):
        """Checks if an int n is a viable answer for grid[x][y]"""
        # Check to the left and right of answer
        for i in range(0,9): 
            if n == self.grid[i][x]:
                return False
        # Check above and below answer
        for j in range(0,9):
            if n == self.grid[y][j]: 
                return False

        # Get the coord of the top right of the 3X3 box for given x and y
        x_box = x //3 *3 
        y_box = y //3 *3
        # Check the values in the same 3X3 box
        for i in range(0,3): # x-coord
            for j in range(0,3): # y-coord
                if n == self.grid[y_box+j][x_box+i]:
                    return False
        return True

    def sudoku_solver(self):
        """Solves Sudoku Puzzles using recursion"""
        for i in range(0,9): # x-coord
            for j in range(0,9): # y-coord
                # Check if there is a blank value
                if self.grid[j][i] == 0:
                    # Try all possible answers
                    for n in range(1,10):
                        # Check if the answer is viable
                        if self.viable(n,j,i):
                            # Replace blank with an initial guess
                            self.grid[j][i] = n
                            # Perform the same operation on the next blank value
                            self.sudoku_solver()
                            # Remove initial guess if it cannot be completed
                            self.grid[j][i] = 0
                    # Return if there are no possible solutions for the blank value
                    return
        # Print the grid in the desired format
        self.sudoku_print()            