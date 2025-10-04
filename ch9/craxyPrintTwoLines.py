import os

folder = os.path.dirname(__file__)
file_path = os.path.join(folder, 'lib.txt')

with open(file_path, 'r') as my_file:
    line1 = my_file.readline()  # read first line
    line2 = my_file.readline()  # read second line
print('')
print(line1)
print(line2)
