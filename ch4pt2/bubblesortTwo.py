def bubble_sort(scores, numbers):
    swapped = True  # Start with swapped = True to enter the while loop

    while swapped:  # Keep looping as long as a swap was made in the last pass
        swapped = False  # Reset swapped at the start of each pass
        for i in range(0, len(scores)-1):  # Go through each index except the last
            if scores[i] < scores[i + 1]:  # If current score is less than the next, swap
                # Swap scores
                temp = scores[i]  
                scores[i] = scores[i + 1]  
                scores[i + 1] = temp  
                
                # Swap corresponding numbers to match the new order
                temp = numbers[i]  
                numbers[i] = numbers[i + 1]  
                numbers[i + 1] = temp  
                
                swapped = True  # Set swapped to True so the loop continues

# List of scores to sort
scores = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]

number_of_scores = len(scores)  # Count how many scores there are
solution_numbers = list(range(number_of_scores))  # Create a list of numbers [0, 1, 2,...]

bubble_sort(scores, solution_numbers)  # Sort the scores (and numbers) in descending order


print(scores,'\n\n', solution_numbers)

print('\n\n','Top Bubble Solutions')
for i in range(0,3):
    print(str(i + 1) + ')','Bubble solution #' + str(solution_numbers[i]),'score:', scores[i], '\n\n')

