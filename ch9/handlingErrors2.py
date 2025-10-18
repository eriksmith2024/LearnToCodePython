try:
    filename = 'notthere.txt'
    file = open(filename, 'r')
except FileNotFoundError:
    print('Sorry,', filename, ' could not be found.')
except IsADirectoryError:
    print("That's a directory not a file!")
else:
    print("It's a good thing we could open that file.")
    file.close()
finally:
    print("I'm running now no matter what happens")