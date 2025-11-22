my_grid = [[0, 1, 2, 3],
           [4, 5, 6, 7],
           [8, 9, 10, 11]
           ]

value = my_grid[2][3]
print(value)

height = 100
width = 100

grid_model = [0] * height

for i in range(height):
    grid_model[i] = [0] * width