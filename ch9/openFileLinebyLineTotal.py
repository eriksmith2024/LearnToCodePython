my_file = open('lib.txt', 'r')
# while True:
#     line = my_file.readline()
#     if line != '':
#         print(line)
#     else:
#         break

for line in my_file:
    print(line)

my_file.close()