"""
The analyze module uses the Flesch-Kincaid readability test to analyse 
text and produce a readability score. This score is then converted into 
a grade-based readability category.
"""

def count_sentences(text):
    """Count the number of sentences in a string of text.

    A sentence is considered to end when it contains one of the 
    following terminal characters: period (.), semicolon (;), 
    question mark (?) or exclamation mark (!).
    """
    count = 0
    terminals = '.;?!'
    for char in text:
        if char in terminals:
            count += 1
    return count


def count_syllables(words):
    """Count the total number of syllables in a list of words.

    Args:
        words (list): List of word strings.

    Returns:
        int: Total number of syllables across all words.
    """
    count = 0
    for word in words:
        count += count_syllables_in_word(word)
    return count


def count_syllables_in_word(word):
    """Estimate the number of syllables in a single word.

    This is a heuristic algorithm and may not be 100% accurate.
    """
    count = 0
    endings = '.,;!?:'
    last_char = word[-1]

    # Strip punctuation at the end
    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word

    # Very short words are assumed to have one syllable
    if len(processed_word) <= 3:
        return 1

    # Remove a trailing 'e' or 'E'
    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]

    vowels = "aeiouAEIOU"
    prev_char_was_vowel = False

    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count += 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False

    # Add one syllable if word ends with 'y'
    if processed_word[-1] in 'yY':
        count += 1

    return count


def output_results(score):
    """Print the corresponding reading level for a Flesch-Kincaid score."""
    if score >= 90:
        print('Reading level at 5th grade \n')
    elif score >= 80:
        print('Reading level at 6th grade \n')
    elif score >= 70:
        print('Reading level at 7th grade \n')
    elif score >= 60:
        print('Reading level at 8-9th grade \n')
    elif score >= 50:
        print('Reading level at 10th-12th grade \n')
    elif score >= 30:
        print('Reading level of college student \n')
    else:
        print('Reading level at college graduate \n')


def compute_readability(text):
    """Compute and print a Flesch-Kincaid readability score for a text string."""
    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)

    score = (206.835
             - 1.015 * (total_words / total_sentences)
             - 84.6 * (total_syllables / total_words))

    print('\n', total_words, 'words')
    print('\n', total_sentences, 'sentences')
    print('\n', total_syllables, 'syllables \n')
    print('\n', score, 'reading ease score \n')
    output_results(score)


if __name__ == "__main__":
    import ch1text
    print('Chapter1 Text:')
    compute_readability(ch1text.text)
