def wears_jacket(temp,raining):
    """
    >>>wears_jacket(90,False)
    False
    >>>wears_jacket(40,False)
    True
    >>>wears_jacket(100,True)
    True
    """
    return temp<60 or raining

def square(x):
    print("here!")
    return x*x
 
def so_slow(num):
    x = num
    while x>0:
        x = x+1
    return x / 0

#square(so_slow(5))得到nothing

def is_prime(n):
    """
    >>>is_prime(10)
    False
    >>>is_Prime(7)
    True
    """
    m = n - 1
    while m > 1:
        if n % m == 0:
            return False
        else:
            m -= 1
    return True

#print(is_prime(1))

# x = 3
# def p(rint):
#     print(rint)
# def g(x, y):
#     if x:
#         print("one")
#     elif x:
#         print(True, x) # Does x being truth-y affect the printed value?
#     if y:
#         print(True, y) # Does y being truth-y affect the printed value?
#     else:
#         print(False, y) # Does y being false-y affect the printed value?
#     return print(p(y))+x
# print(g(3,2)) 


#The Recursion
grow = lambda n:f_then_g(grow,print,n//10)

shrink = lambda n:f_then_g(print,shrink,n//10)
    
    
def inverse_casecade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)
    

inverse_casecade(123456)

y = "y"
h = y
def y(y):
    h = "h"
    if y == h:
        print(y)
        return y + "i"
    y = lambda y: y(h)
    print(y)
    return lambda h: y(h)
print(y)
y = y(y)(y)
print(y)