def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    # for (let i = 0; i < nums.length: i++){
    #     for (let j = 0; )
    # }

    # for num in range(len(nums)):
    #     for i in range(len(nums) - 1):
    #         if nums[num] + nums[i]
    # |
    # [5, 1, 4, 8, 3, 2] 3
    # |

    # using value of current index
    # minus that value from goal (7 - 5 = 2)
    # search rest of list for that value
    # if found return current index val and matching index/val
    # otherwise continue

    for i in range(len(nums)):
        goalDiff = goal - nums[i]
        nextItem = i + 1
        for nextItem in range(len(nums)):
            if nums[nextItem] == goalDiff:
                return (nums[i], nums[nextItem])

    return ()
