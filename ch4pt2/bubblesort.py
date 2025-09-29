def bubble_sort(scores):
    # Define a function called bubble_sort that takes a list called scores

    swapped = True
    # Start with swapped = True to enter the while loop at least once

    while swapped:
        # Keep looping until no swaps are made in a full pass
        swapped = False
        # Assume no swaps will happen this pass, will change if we do swap
        for i in range(0, len(scores)-1):
            # Go through each index from 0 up to the second-last element
            if scores[i] < scores[i+1]:
                # Check if current element is bigger than the next element
                temp = scores[i]
                # Store the current element in a temporary variable
                scores[i] = scores[i+1]
                # Move the next element into the current position
                scores[i+1] = temp
                # Put the stored element into the next position (swap done)
                swapped = True
                # Mark that a swap happened, so we will check again in next pass

