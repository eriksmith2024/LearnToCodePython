from tkinter import *
import model

cell_size = 5
is_running = False

# ---------------------- SETUP ----------------------
def setup():
    global root, grid_view, start_button, clear_button, choice, option

root = Tk()
root.title('The game of Life')

# canvas for grid
grid_view = Canvas(
    root,
    width=model.width * cell_size,
    height=model.height * cell_size,
    borderwidth=0,
    highlightthickness=0,
    bg='white'
)

# buttons
start_button = Button(root, text='Start', width=12)
clear_button = Button(root, text='Clear', width=12)

# option menu
choice = StringVar(root)
choice.set('Choose a Pattern')
option = OptionMenu(root, choice, 'Choose a Pattern', 'glider', 'glider gun', 'random',
                    command=lambda _: option_handler())
option.config(width=20)

# ---------------------- EVENT HANDLERS ----------------------
def start_handler(event=None):
    global is_running
    if is_running:
        is_running = False
        start_button.configure(text='Start')
    else:
        is_running = True
        start_button.configure(text='Pause')
        update()

def clear_handler(event=None):
    global is_running
    is_running = False
    for i in range(model.height):
        for j in range(model.width):
            model.grid_model[i][j] = 0
    start_button.configure(text='Start')
    update()  # redraw cleared grid

def option_handler():
    global is_running
    is_running = False
    start_button.configure(text='Start')
    selection = choice.get()
    if selection == 'glider':
        model.load_pattern(model.glider_pattern, 10, 10)
    elif selection == 'glider gun':
        model.load_pattern(model.glider_gun_pattern, 10, 10)
    elif selection == 'random':
        model.randomize(model.grid_model, model.width, model.height)
    update()

def grid_handler(event):
    x = int(event.x / cell_size)
    y = int(event.y / cell_size)
    if model.grid_model[y][x] == 1:
        model.grid_model[y][x] = 0
        draw_cell(x, y, 'white')
    else:
        model.grid_model[y][x] = 1
        draw_cell(x, y, 'black')

# ---------------------- DRAWING ----------------------
def draw_cell(row, col, color):
    x = col * cell_size
    y = row * cell_size
    outline = 'grey' if color == 'black' else 'white'
    grid_view.create_rectangle(x, y, x+cell_size, y+cell_size, fill=color, outline=outline)

def update():
    global is_running
    grid_view.delete(ALL)
    model.next_gen()
    for row in range(model.height):
        for col in range(model.width):
            if model.grid_model[row][col] == 1:
                draw_cell(row, col, 'black')
    if is_running:
        root.after(100, update)

# ---------------------- LAYOUT ----------------------
grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
grid_view.bind('<Button-1>', grid_handler)
start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
start_button.bind('<Button-1>', start_handler)
option.grid(row=1, column=1, padx=20)
clear_button.grid(row=1, column=2, sticky=E, pady=20)
clear_button.bind('<Button-1>', clear_handler)

# ---------------------- MAIN LOOP ----------------------
if __name__ == '__main__':
    setup()
    mainloop()
