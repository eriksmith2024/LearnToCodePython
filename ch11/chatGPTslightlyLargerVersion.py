import tkinter as tk

# Grid size
height = 10
width = 10

# Maximum canvas size in pixels
canvas_width = 500
canvas_height = 500

# Calculate cell size to fit the canvas proportionally
cell_size_x = canvas_width // width
cell_size_y = canvas_height // height
cell_size = min(cell_size_x, cell_size_y)

# Create the two grids: current and next generation
grid_model = [[0 for _ in range(width)] for _ in range(height)]
next_grid_model = [[0 for _ in range(width)] for _ in range(height)]

# Initialize some live cells for a more interesting pattern
# Vertical blinker in the middle
grid_model[2][4] = 1
grid_model[3][4] = 1
grid_model[4][4] = 1

# Small block in top-left corner (still life)
grid_model[0][0] = 1
grid_model[0][1] = 1
grid_model[1][0] = 1
grid_model[1][1] = 1

# Glider pattern in bottom-right
grid_model[6][7] = 1
grid_model[7][8] = 1
grid_model[8][6] = 1
grid_model[8][7] = 1
grid_model[8][8] = 1

# Function to count alive neighbours
def count_neighbours(grid, row, col):
    count = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            r = row + dr
            c = col + dc
            if 0 <= r < height and 0 <= c < width:
                count += grid[r][c]
    return count

# Function to calculate next generation
def next_gen():
    global grid_model, next_grid_model
    for i in range(height):
        for j in range(width):
            count = count_neighbours(grid_model, i, j)
            if grid_model[i][j] == 1:
                if count == 2 or count == 3:
                    next_grid_model[i][j] = 1
                else:
                    next_grid_model[i][j] = 0
            else:
                if count == 3:
                    next_grid_model[i][j] = 1
                else:
                    next_grid_model[i][j] = 0
    grid_model, next_grid_model = next_grid_model, grid_model
    draw_grid()

# Function to draw the grid in the canvas
def draw_grid():
    canvas.delete("all")
    for i in range(height):
        for j in range(width):
            x1 = j * cell_size
            y1 = i * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            color = "black" if grid_model[i][j] == 1 else "white"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

# GUI setup
window = tk.Tk()
window.title(f"{width}x{height} Game of Life")

canvas = tk.Canvas(window, width=width*cell_size, height=height*cell_size)
canvas.pack()

button = tk.Button(window, text="Next Generation", command=next_gen)
button.pack()

draw_grid()
window.mainloop()
