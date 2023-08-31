def min_elements(T, lst):
    """
    >>> min_elements(12, [4, 2, 1]) # 4 + 4 + 4 so should print 3
    3
    >>> min_elements(10, [4, 2, 1]) # 4 + 4 + 2 so should print 3
    3
    >>> min_elements(0, [3, 2, 1]) # should print 0
    0
    """
    if T == 0:
        return 0
    return min([min_elements(T-lst[x], lst[x:]) for x in range(len(lst)) if T-lst[x] >= 0]) + 1


def partition_options(total, biggest):
    """
    >>> pratition_options(2, 2)
    [[2], [1, 1]]
    >>> pratition_options(3, 3)
    [[3], [2, 1], [1, 1, 1]]
    >>> pratition_options(4, 3)
    [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
    """
    if ?:
        return ?
    elif ?:
        return ?
    else:
        with_biggest = ?
        without_biggest = ?
        ? = [[?]?]
        return with_biggest + without_biggest
