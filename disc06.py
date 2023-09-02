def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    """
    def memory_helper(func):
        nonlocal n
        n = func(n)
        return n
    return memory_helper

f = memory(100)
print(f(lambda x: x * 2))
print(f(lambda x: x > 5)) #True等价于数字 1， 导致下面的语句值为 2
print(f(lambda x: x * 2))

def nonlocalist():
    """
    >>> prepend, get = nonlocalist()
    >>> prepend(2)
    >>> prepend(3)
    >>> prepend(4)
    >>> get(0)
    4
    >>> get(1)
    3
    >>> get(2)
    2
    >>> prepend(8)
    >>> get(2)
    3
    """
    # get = lambda x: "Index out of range!"
    # def prepend(value):
    #     nonlocal get
    #     f = get
    #     def get(i):
    #         if i == 0:
    #             return value
    #         return f(i-1)
    #     return value
    # return prepend, get

    get = lambda x: "Index out of range!"
    def prepend(value):
        nonlocal get
        f = get
        def get(i):
            if i == 0:
                return value
        return value
    return prepend, get
            return f(i-1)


prepend, get = nonlocalist()
prepend(2)
prepend(3)
prepend(4)
print(get(0)) #4
print(get(1)) #3
print(get(2)) #2
prepend(8)
print(get(2)) #t3


def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)