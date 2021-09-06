def print_upper_words(words, starting_letters):
    """ 
        words: list of word strings
        starting_letters: set of letter strings

        - Prints only words that begin with a letter from starting_letters
        - Prints words in upper-case
        - Prints each word on a separate line
    """

    for word in words:
        if word[0] in starting_letters:
            print(word.upper())