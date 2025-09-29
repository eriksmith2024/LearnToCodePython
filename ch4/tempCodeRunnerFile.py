# scores = [ 60, 50, 60, 58, 54, 54, 58, 50, 53, 54 ]

# score = scores [3]
# print(' Solution #3 produced', score, 'bubbles.')

scores = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .25,
         .33, .31, .25, .29, .27, .22,
         .31, .25, .25, .33, .21, .25,
         .25, .25, .28, .25, .24, .22,
         .20, .25, .30, .25, .24, .25,
         .25, .25, .27, .25, .26, .29]

high_score = 0 

# i = 0 #  NEED TO INITIALISE WITH THE WHILE LOOP OPTION - NOT NEEDED IN THE FOR IN LOOP 
length = len(scores)

# This solution prints the code with a space between the # and the index.  
# while i < length:
#     print('Bubble solution #', i, "scored: ", scores[i])
#     i = i + 1
# To solve the gap issue you cant concatante the i as it is a number you need to make it string first to concatanate
for i in range(length):
# while i < length: #THIS IS AN ALTERNATE LOOP OPTION WITH WHILE
    print('Bubble solution #' + str(i), "scored: ", scores[i])
    # i = i + 1. # ONLY REQUIED IN THE WHILE LOOP NOT NEEDED IN THE FOR IN LOOP
    if scores[i] > high_score:
        high_score =  scores[i]

print('\nTotal Bubble tests:',length,'\n')
print('Highest Bubble score:', high_score, '\n')

best_solutions = [ ]
for i in range(length):
    if high_score == scores[i]:
        best_solutions.append(i)

print('The solutions with the highest score are: ', best_solutions, '\n')


cost = 100.0
most_effectice = 0

for i in range(length):
    if scores[i] == high_score and cost[i] < cost:
        most_effectice = i
        cost = costs[i]
print('Solution ', most_effectice, ' is the most effective with a cost of ', costs[most_effectice])
