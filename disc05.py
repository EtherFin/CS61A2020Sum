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
    # return min([min_elements(T-lst[x], lst) for x in range(len(lst)) if T-lst[x] >= 0]) + 1
    return min([min_elements(T-i, lst) for i in lst if T - i >= 0]) + 1


print(min_elements(12, [4, 2, 1]))

def partition_options(total, biggest):
    """
    >>> pratition_options(2, 2)
    [[2], [1, 1]]
    >>> pratition_options(3, 3)
    [[3], [2, 1], [1, 1, 1]]
    >>> pratition_options(4, 3)
    [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
    """
    if total == 0:
        return [[]]
    elif total < 0 or biggest == 0:
        return []
    else:
        with_biggest = partition_options(total-biggest, biggest)
        without_biggest = partition_options(total, biggest-1)
        with_biggest = [[biggest] + elem for elem in with_biggest] #此处应该如此使用，用 " + "
        return with_biggest + without_biggest
    
print(partition_options(2, 2))
print(partition_options(3, 3))
print(partition_options(4, 3))



def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)   #returns None
    None
    """
    # if is_leaf(tree):
    #     return [x] if label(tree) == x else []
    # else:
    #     path = [find_path(br) for br in branches(tree) if x in find_path(br)[0]]
    #     if 1:
    #         return [label(tree) + path if len(path) != 0 else None]

    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path


