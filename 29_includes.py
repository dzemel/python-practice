def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if start is not None:
        for i in range(len(collection), start):
            # print(f"i is {start}, collection[i] is {collection[start]}")
            if sought == collection[i]:
                return True
        return False

    # dict
    if isinstance(collection, dict):
        for item in collection.values():
            if item == sought:
                return True
        return False

    # for item in range(len(collection)):
    #     if sought == item:
    #         return True

    if sought in collection:
        return True
    return False
