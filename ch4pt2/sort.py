from bubblesort import bubble_sort   # import just the function

scores = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]

# bubble_sort(scores)   # call the function
scores.sort()
print(scores)         # print sorted scores


smoothies = ['coconut', 'strawberry', 'banana', 'pineapple']
bubble_sort(smoothies) # uses mny custom built version from the file imported at the top
# smoothies.sort() # built in method
print(smoothies)