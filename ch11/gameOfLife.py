# my_grid = [[0, 1, 2, 3],
#            [4, 5, 6, 7],
#            [8, 9, 10, 11]
#            ]

# value = my_grid[2][3]
# print(value)

height = 100               # number of rows in the grid
width = 100                # number of columns in the grid

grid_model = [0] * height  # create a list with 100 zeros (temporary placeholder rows)
for i in range(height):    
    grid_model[i] = [0] * width   # replace each placeholder with a row of 100 zeros

def next_gen():
    global grid_model           # allow the function to modify the global grid_model

    for i in range(height):     # loop over every row index
        for j in range(width):  # loop over every column index inside each row
            cell = 0            # temporary variable to store next state for this cell
            print('Checking cell', i, j)  # debugging output showing current cell
            count = count_neighbours(grid_model, i, j)  # count live neighbours around this cell

            if grid_model[i][j] == 0:     # if the current cell is dead
                if count == 3:            # dead cell becomes alive if exactly 3 neighbours
                    cell = 1              # mark as newly alive
            elif grid_model[i][j] == 1:   # if the current cell is alive
                if count == 2 or count == 3:  # survives if 2 or 3 neighbours
                    cell = -1             # mark as surviving (special flag in your version)
    
def count_neighbours(grid, row, col):
    count = 0                # store running total of live neighbours

    # top
    if row > 0:
        count += grid[row - 1][col]

    # top-left
    if row > 0 and col > 0:
        count += grid[row - 1][col - 1]

    # top-right
    if row > 0 and col < width - 1:
        count += grid[row - 1][col + 1]

    # left
    if col > 0:
        count += grid[row][col - 1]

    # right
    if col < width - 1:
        count += grid[row][col + 1]

    # bottom
    if row < height - 1:
        count += grid[row + 1][col]

    # bottom-left
    if row < height - 1 and col > 0:
        count += grid[row + 1][col - 1]

    # bottom-right
    if row < height - 1 and col < width - 1:
        count += grid[row + 1][col + 1]

    return count             # return total number of live neighbours

if __name__ == '__main__':   # only run next_gen if this file is executed directly
    next_gen()               # call the function to compute next generation
