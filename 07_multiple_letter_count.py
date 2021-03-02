def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    dict1 = {}

    for letter in phrase:
        if letter in dict1.keys():
            dict1[letter] += 1
        else:
            dict1[letter] = 1

    return dict1
