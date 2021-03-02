def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    return word.lower().count(letter)

    # count = 0
    # for letter in word:
    #     if letter.lower() in word.lower():
    #         count += 1
    # return count
