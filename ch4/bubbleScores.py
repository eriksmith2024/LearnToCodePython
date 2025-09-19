# scores = [ 60, 50, 60, 58, 54, 54, 58, 50, 53, 54 ]

# score = scores [3]
# print(' Solution #3 produced', score, 'bubbles.')

scores = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]


# i = 0 #  NEED TO INITIALISE WITH THE WHILE LOOP OPTION - NOT NEEDED IN THE FOR IN LOOP 
length = len(scores)
print('\nTotal Bubble tests:',length,'\n')

# This solution prints the code with a space between the # and the index.  
# while i < length:
#     print('Bubble solution #', i, "scored: ", scores[i])
#     i = i + 1
# To solve the gap issue you cant concatante the i as it is a number you need to make it string first to concatanate
for i in range(length):
# while i < length: #THIS IS AN ALTERNATE LOOP OPTION WITH WHILE
    print('Bubble solution #' + str(i), "scored: ", scores[i])
    # i = i + 1. # ONLY REQUIED IN THE WHILE LOOP NOT NEEDED IN THE FOR IN LOOP


# CHAT GPT NOTES BELOW ON DIFFERENCE OF WHILE AND FOR .. IN LOOP
# 🔹 Why the for loop is better in this case:

# No manual index management

# In the while loop, you have to initialise i = 0 before the loop, and then remember to increment it with i = i + 1 inside the loop.

# If you forget to increment, you get an infinite loop.

# The for i in range(length): version automatically takes care of index progression.

# ✅ Less chance of mistakes.
# ✅ Cleaner and shorter code.

# Clearer intent

# for i in range(length): immediately tells the reader:
# “Loop from 0 up to length - 1”.

# With while, you have to read multiple lines (i = 0, condition, increment) to figure out the loop’s purpose.

# ✅ More readable and Pythonic.

# No need to touch i yourself

# In the while version, you mistakenly still have i = i + 1 inside your for loop — but it does nothing because the for loop ignores your manual increment.

# With for, you let Python manage i so you don’t risk breaking the loop logic.

# 🔹 When a while loop is better

# Use a while loop when:

# You don’t know in advance how many times you need to loop.
# (e.g., keep looping until the user types "quit", or until a sensor gives a certain reading).

# Use a for loop when:

# You do know the number of iterations (like looping through a list, or range(n)).

# 👉 In this exact case (looping through all the scores by index), the for loop is more Pythonic, safer, and simpler.