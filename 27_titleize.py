def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    wordList = phrase.split(' ')

    capList = []
    for item in wordList:
        capList.append(item.capitalize())

    return ' '.join(capList)
