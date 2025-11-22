import random

height = 100  # number of rows
width = 100   # number of columns

# create two grids: current and next generation
grid_model = [[0] * width for _ in range(height)]
next_grid_model = [[0] * width for _ in range(height)]

# randomize grid
def randomize(grid, width, height):
    for i in range(height):
        for j in range(width):
            grid[i][j] = random.randint(0, 1)

# count live neighbors of a cell
def count_neighbours(grid, row, col):
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if (0 <= i < height) and (0 <= j < width):
                if (i, j) != (row, col):
                    count += grid[i][j]
    return count

# compute next generation
def next_gen():
    global grid_model, next_grid_model
    for i in range(height):
        for j in range(width):
            count = count_neighbours(grid_model, i, j)
            if grid_model[i][j] == 1:
                next_grid_model[i][j] = 1 if count in (2, 3) else 0
            else:
                next_grid_model[i][j] = 1 if count == 3 else 0
    # swap grids
    grid_model, next_grid_model = next_grid_model, grid_model

# patterns
glider_pattern = [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
]

glider_gun_pattern = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


# load pattern into grid
def load_pattern(pattern, x_offset=0, y_offset=0):
    global grid_model
    # clear grid
    for i in range(height):
        for j in range(width):
            grid_model[i][j] = 0
    # copy pattern
    for j, row in enumerate(pattern):
        for i, val in enumerate(row):
            if 0 <= x_offset+i < height and 0 <= y_offset+j < width:
                grid_model[x_offset+i][y_offset+j] = val

if __name__ == '__main__':
    randomize(grid_model, width, height)
    next_gen()
