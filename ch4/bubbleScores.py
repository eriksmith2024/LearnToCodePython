# scores = [ 60, 50, 60, 58, 54, 54, 58, 50, 53, 54 ]

# score = scores [3]
# print(' Solution #3 produced', score, 'bubbles.')

scores = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]


i = 0
length = len(scores)
print('\nTotal Bubble tests:',length,'\n')

# This solution prints the code with a space between the # and the index.  
# while i < length:
#     print('Bubble solution #', i, "scored: ", scores[i])
#     i = i + 1
# To solve the gap issue you cant concatante the i as it is a number you need to make it string first to concatanate
while i < length:
    print('Bubble solution #' + str(i), "scored: ", scores[i])
    i = i + 1



