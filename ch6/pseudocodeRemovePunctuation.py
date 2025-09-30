import ch1text
import string  # needed for string.punctuation

def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    # split text into words
    words = text.split()
    total_words = len(words)
    
    print(words)
    print('\n', total_words, 'words')

    # CLEAN THE WORDS INSIDE THE FUNCTION
    cleaned_words = []
    for word in words:
        cleaned_word = ""
        for char in word:
            if char not in string.punctuation:  # keep only non-punctuation
                cleaned_word += char
        cleaned_words.append(cleaned_word)

    # show cleaned words and their count
    print(cleaned_words)
    print('\n', len(cleaned_words), 'cleaned words')

    # return cleaned words in case we want to use them outside
    return cleaned_words

# call the function and save cleaned words
words = compute_readability(ch1text.text)

# print Python's built-in punctuation string
print('\n',string.punctuation ,'\n')


# MY SOLUTION

# loop through words
#     for each character in word
#         if character in list_of_punctuation
#             remove character

#  CHAT GPT SOLUTION
# loop through each word in words
#     create an empty string cleaned_word
#     loop through each character in word
#         if character is not in list_of_punctuation
#             add character to cleaned_word
#     replace original word with cleaned_word

# CHAT GPT ACTUAL CODE
# now handled inside compute_readability; no need for duplicate loop
