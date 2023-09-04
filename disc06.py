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

# f = memory(100)
# print(f(lambda x: x * 2))
# print(f(lambda x: x > 5)) #True等价于数字 1， 导致下面的语句值为 2
# print(f(lambda x: x * 2))

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
            return f(i-1)
    return prepend, lambda x: get(x)  #用lambda改变get的绑定 ！！！


# prepend, get = nonlocalist()
# prepend(2)
# prepend(3)
# prepend(4)
# print(get(0)) #4
# print(get(1)) #3
# print(get(2)) #2
# prepend(8)
# print(get(2)) #t3


def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)


# f = lambda x: [print(i + 1) for i in range(x)]
# f = f(10)
# print(f)
# f


square = lambda x: x * x
double = lambda x: 2 * x
def memory(x, f):
    """Return a higher-order function that prints its
    memories.
    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    """
    def g(h):
        print(f(x))
        return memory(x, h)
    return g

# f = memory(3, lambda x: x)
# f = f(square)
# f = f(double)
# f = f(print)
# f = f(square)


def announce_losses(who, last_score=0):
    """
    >>> f = announce_losses(0)
    >>> f1 = f(10, 0)
    >>> f2 = f1(1, 10) # Player 0 loses points due to swine swap
    Oh no! Player 0 just lost 9 point(s).
    >>> f3 = f2(7, 10)
    >>> f4 = f3(7, 11) # Should not announce when player 0's score does not change
    >>> f5 = f4(11, 12)
    """
    # assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # def say(score0, score1):
    #     if who == 0:
    #         score = ________________________
    #     elif who == 1:
    #         score = ________________________
    #     if ________________________:
    #         ________________________________________________
    #     return ________________________
    # return say

    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    def say(score0, score1):
        if who == 0:
            score = score0
        elif who == 1:
            score = score1
        if score < last_score:
            print("Oh no! Player" , who , "just lost" , (last_score - score) , "point(s).")
        return announce_losses(who, score)
    return say 


# f = announce_losses(0)
# f1 = f(10, 0)
# f2 = f1(1, 10) # Player 0 loses points due to swine swap
# f3 = f2(7, 10)
# f4 = f3(7, 11) # Should not announce when player 0's score does not change
# f5 = f4(11, 12)

    # (Fall 2013) The CS 61A staff has developed a formula for determining what a fox
    # might say. Given three strings—a start, a middle, and an end—a fox will say the
    # start string, followed by the middle string repeated a number of times, followed by
    # the end string. These parts are all separated by single hyphens.
    # Complete the definition of fox says, which takes the three string parts of the fox’s
    # statement (start, middle, and end) and a positive integer num indicating how many
    # times to repeat middle. It returns a string. You cannot use any for or while
    # statements. Use recursion in repeat. Moreover, you cannot use string operations
    # other than the + operator to concatenate strings together.
def fox_says(start, middle, end, num):
    """
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """
    def repeat(k):
        if k == 1:
            return middle
        return middle + '-' + repeat(k-1)
    return start + '-' + repeat(num) + '-' + end

# print(fox_says('wa', 'pa', 'pow', 10))


# Constructor
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

# Selector
def label(tree):
    """Return the label value of a tree."""
    return tree[0]

# Selector
def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
# For convenience
def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise."""
    return not branches(tree)

def primary_stress(t):
    """
    >>> word = tree("", [
    tree("w", [tree("s", [tree("min")]), tree("w", [tree("ne")])]),
    tree("s", [tree("s", [tree("so")]), tree("w", [tree("ta")])])])
    >>> primary_stress(word)
    'so'
    >>> phrase = tree("", [
    tree("s", [tree("s", [tree("law")]), tree("w", [tree("degree")])]),
    tree("w", [tree("requirement")])])
    >>> primary_stress(phrase)
    'law'
    """
    def helper(t, num_s):
        if is_leaf(t):
            return [label(t), num_s]
        if label(t) == "s":
            num_s = num_s + 1
        return max([helper(br, num_s) for br in branches(t)], key = lambda x: x[1]) # 递归的抽象 ！！！
    return helper(t, 0)[0]


# word = tree("", [
#     tree("w", [tree("s", [tree("min")]), tree("w", [tree("ne")])]),
#     tree("s", [tree("s", [tree("so")]), tree("w", [tree("ta")])])])
# print(primary_stress(word))

def subset_sum(seq, k):
    if k in seq:
        return True 
    elif not seq:
        return False
    else:
        # return subset_sum(seq[1:], k - seq[0]) or subset_num(seq[1:], k)
        return any([subset_sum(seq[1:], k - x) for x in seq])


# print(subset_sum([2, 4, 7, 3], 5))
# print(subset_sum([1, 9, 5, 7, 3], 2))