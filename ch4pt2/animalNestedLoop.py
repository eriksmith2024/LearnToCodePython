for word in ['ox', 'cat', 'lion', 'tiger', 'bobcat']:
    for i in range(2, 7):
        letters = len(word)
        if(letters % i) == 0:
            print(i, word)


# Basically goes the loop of words 
# and then an inner loop for each word loops through index of 2 to 7
# it assigns the word length of the word i.e. ox is 2
# it then divides the number against each of the index, 2,3,4,5,6
# if the length divided by the index number = 0 it gets printed