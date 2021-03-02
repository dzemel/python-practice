def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_str = ""
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            letter = letter.swapcase()
        new_str += letter
        # new_str += letter.upper()

    return new_str
