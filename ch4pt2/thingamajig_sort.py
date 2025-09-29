characters = 'amanaplanac'  # Original string we want to process

output = ''  # Start with an empty string to build the output
length = len(characters)  # Get the length of the string
i = 0  # Start index for the first loop

# Loop to add characters in original order
while i < length:
    output = output + characters[i]  # Add current character to output
    i = i + 1  # Move to the next character to avoid infinite loop

# Prepare for second loop to add characters in reverse order (excluding last char)
i = -2  # Start from second-to-last character (negative indexing)

# Loop to add characters in reverse order
while i >= -length:
    output = output + characters[i]  # Add character from the end
    i = i - 1  # Move backwards through the string

print(output)  # Print the final result, which is a palindrome
