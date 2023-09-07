
def make_guess(n):
    """
    Let's play a guessing game! In order to do this, we'll use higher order functions.
    Write a function, make_guess, which takes in a number that we want someone to try to guess, and returns a guessing
    function.
    A guessing function is a one-argument function which takes in a number. If the number passed in is the number we
    wanted to guess, it will return the number of incorrect guesses made prior to the correct guess. Otherwise, it returns
    another guessing function, which keeps track of the fact that we've made an incorrect guess.
    Solutions which use lists, object mutation, nonlocal, or global will receive no credit.
    
    让我们来玩一个猜数字的游戏！为了实现这个目标，我们将使用高阶函数。
    编写一个名为make_guess的函数，它接受一个我们希望别人尝试猜测的数字，并返回一个猜测函数。
    猜测函数是一个接受一个数字作为参数的函数。如果传入的数字是我们想要猜测的数字，它将返回在猜中正确答案之前所猜的错误次数。
    否则，它将返回另一个猜测函数，用于追踪我们已经猜错了的事实。
    使用列表、对象变异、nonlocal或全局变量的解决方案将不会获得分数。
    
    >>> guesser = make_guess(10)
    >>> guess1 = guesser(6)
    >>> guess2 = guess1(7)
    >>> guess3 = guess2(8)
    >>> guess3(10)
    3
    >>> guess2(10)
    2
    >>> a = make_guess(5)(1)(2)(3)(4)(5)
    >>> a
    4
    """

    # def update_guess(num_incorrect):
    #     def new_guess(x):
    #         if ______:
    #             ______
    #         else:
    #             ______
    #     ______
    # return ______

    def update_guess(num_incorrect):
        def new_guess(x):
            if x == n:
                return num_incorrect
            else:
                return update_guess(num_incorrect + 1)
        return new_guess
    return update_guess(0)

# ORIGINAL SKELETON FOLLOWS

# def make_guess(n):
#     """
#     Let's play a guessing game! In order to do this, we'll use higher order functions.
#     Write a function, make_guess, which takes in a number that we want someone to try to guess, and returns a guessing
#     function.
#     A guessing function is a one-argument function which takes in a number. If the number passed in is the number we
#     wanted to guess, it will return the number of incorrect guesses made prior to the correct guess. Otherwise, it returns
#     another guessing function, which keeps track of the fact that we've made an incorrect guess.
#     Solutions which use lists, object mutation, nonlocal, or global will receive no credit.

#     >>> guesser = make_guess(10)
#     >>> guess1 = guesser(6)
#     >>> guess2 = guess1(7)
#     >>> guess3 = guess2(8)
#     >>> guess3(10)
#     3
#     >>> guess2(10)
#     2
#     >>> a = make_guess(5)(1)(2)(3)(4)(5)
#     >>> a
#     4
#     """
#     def update_guess(num_incorrect):
#         def new_guess(x):
#             if ______:
#                 ______
#             else:
#                 ______
#         ______
#     return ______
