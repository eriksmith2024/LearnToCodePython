import random 

height = 100                # number of rows in the grid
width = 100                 # number of columns in the grid

def randomize(grid, width, height):
    for i in range(0, height):
        for j in range (0, width):
            grid[i][j] =  random.randint(0,1)

grid_model = [0] * height   # create list with placeholders for current generation
next_grid_model = [0] * height  # create placeholders for the next generation
for i in range(height):     
    grid_model[i] = [0] * width        # fill each row with 100 zeros for current grid
    next_grid_model[i] = [0] * width   # fill each row with 100 zeros for next grid

randomize(grid_model, width, height)

def next_gen():
    global grid_model, next_grid_model   # allow modification of the two global grids

    for i in range(height):              # loop through every row
        for j in range(width):           # loop through every column in the row
            cell = 0                     # variable to hold the next state of the cell
            print('Checking cell', i, j) # debug output showing the cell being processed

            count = count_neighbours(grid_model, i, j)  # get number of live neighbours

            if grid_model[i][j] == 0:        # if the cell is currently dead
                if count == 3:               # birth rule: dead cell becomes alive with 3 neighbours
                    cell = 1                 # set cell to alive
            elif grid_model[i][j] == 1:       # if the cell is currently alive
                if count == 2 or count == 3:  # survival rule: lives with 2 or 3 neighbours
                    cell = -1                # special marker for survival (your code keeps this)

            next_grid_model[i][j] = cell     # write the new state into the next grid
            print('New value is', next_grid_model[i][j])

        temp = grid_model                    # swap grids after finishing each row
        grid_model = next_grid_model         # next generation becomes the current grid
        next_grid_model = temp               # old grid becomes the next grid (to be overwritten)
                                             # this avoids allocating new lists repeatedly

def count_neighbours(grid, row, col):
    count = 0                 # total number of living neighbours around the cell

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

    return count               # return total number of living neighbours

if __name__ == '__main__':    # only run next_gen when executed directly
    next_gen()                # run one generation update
