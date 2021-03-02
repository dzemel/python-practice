def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newStr = ""
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            letter = letter.swapcase()
        newStr += letter
        # newStr += letter.upper()

    return newStr
