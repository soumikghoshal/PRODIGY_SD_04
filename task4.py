# Function to check if placing num in grid[row][col] is valid
def is_valid(grid, row, col, num):
    # Check if the number exists in the current row
    for x in range(9):
        if grid[row][x] == num:
            return False
    
    # Check if the number exists in the current column
    for x in range(9):
        if grid[x][col] == num:
            return False
    
    # Check if the number exists in the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    
    return True

# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(grid):
    empty_cell = find_empty_location(grid)
    
    # If there are no empty cells, the puzzle is solved
    if not empty_cell:
        return True
    
    row, col = empty_cell
    
    # Try placing numbers 1 to 9 in the empty cell
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            # Assign num to the current empty cell
            grid[row][col] = num
            
            # Recursively solve the rest of the puzzle
            if solve_sudoku(grid):
                return True
            
            # Backtrack if no valid number can be placed
            grid[row][col] = 0
    
    return False

# Function to find an empty location in the grid
def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None

# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Example unsolved Sudoku puzzle (0 represents empty cells)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the puzzle and print the result
if solve_sudoku(grid):
    print("Solved Sudoku Grid:")
    print_grid(grid)
else:
    print("No solution exists for the given Sudoku puzzle.")
