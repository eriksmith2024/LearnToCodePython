import tkinter as tk
import random

height = 100
width = 100

# Create grid with sample values 0–100 (for heatmap colours)
grid_model = [[random.randint(0, 100) for _ in range(width)] for _ in range(height)]

# Function to convert value → colour (blue low, red high)
def value_to_colour(val):
    # val expected 0–100
    r = int((val / 100) * 255)        # red increases with value
    b = int(255 - (val / 100) * 255)  # blue decreases with value
    return f"#{r:02x}00{b:02x}"

window = tk.Tk()
window.title("Heatmap 100 x 100")

canvas_size = 500
canvas = tk.Canvas(window, width=canvas_size, height=canvas_size)
canvas.pack()

cell_size = canvas_size // width   # size of each square

# Draw heatmap
for row in range(height):
    for col in range(width):
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size

        colour = value_to_colour(grid_model[row][col])

        canvas.create_rectangle(x1, y1, x2, y2, fill=colour, outline="")

window.mainloop()
