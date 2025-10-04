import os

# Get the folder where crazy.py is
folder = os.path.dirname(__file__)
file_path = os.path.join(folder, 'lib.txt')

with open(file_path, 'r') as my_file:
    my_text = my_file.read()

line1 = my_file.readline()
print(line1)
line2 = my_file.readline()
print(line2)

print(my_text)
my_file.close()