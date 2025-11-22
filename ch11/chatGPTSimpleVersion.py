import tkinter as tk

# Grid size
height = 5
width = 5
cell_size = 50  # pixels

# Create the two grids: current and next generation
grid_model = [[0 for _ in range(width)] for _ in range(height)]
next_grid_model = [[0 for _ in range(width)] for _ in range(height)]

# Initialize some live cells for demo
grid_model[1][2] = 1
grid_model[2][2] = 1
grid_model[3][2] = 1  # This forms a vertical "blinker" pattern

# Function to count alive neighbours
def count_neighbours(grid, row, col):
    count = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue  # skip the cell itself
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
            # Apply Game of Life rules
            if grid_model[i][j] == 1:
                if count == 2 or count == 3:
                    next_grid_model[i][j] = 1  # survives
                else:
                    next_grid_model[i][j] = 0  # dies
            else:
                if count == 3:
                    next_grid_model[i][j] = 1  # becomes alive
                else:
                    next_grid_model[i][j] = 0  # stays dead
    # Swap grids
    grid_model, next_grid_model = next_grid_model, grid_model
    draw_grid()  # update the GUI

# Function to draw the grid in the canvas
def draw_grid():
    canvas.delete("all")  # clear previous drawing
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
window.title("5x5 Game of Life")

canvas = tk.Canvas(window, width=width*cell_size, height=height*cell_size)
canvas.pack()

# Button to go to next generation
button = tk.Button(window, text="Next Generation", command=next_gen)
button.pack()

# Initial draw
draw_grid()

window.mainloop()
