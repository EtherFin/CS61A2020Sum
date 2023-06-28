def is_prime(n):
    def p_h(n,m):
        if n==1 or (m < n and n % m == 0): 
            return False
        elif m == n:
            return True
        else:
            return p_h(n,m+1)
    return p_h(n,2)


def count_k(n, k):
    """
    >>> count_k(3, 3) #3,2+1,1+2,1+1+1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) #Only one step at a time
    1
    """
    if n == 1:
        return 1
    if n <= k:
        return 1 + count_k(n,n-1)
    else:
        return sum([count_k(n-x, k) for x in range(1, k+1)])
    
def max_product(s):
    """
    Return the maximum product that can be formed using non-consecutive elements of s.
    
    >>> max_product([10,3,1,9,2]) #10 * 9
    90
    >>> max_product([5,10,5,10,5]) #5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    print(s)
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return s[0]
    elif len(s) == 2:
        return s[1]
    else:
        return max(s[1]*max_product(s[3:]),s[0]*max_product(s[2:]))
    
    
def check_hole_number(n):
    tmp = list(str(n))
    if len(tmp)==3:
        return tmp[1]<tmp[0] and tmp[1]<tmp[2]
    else:
        tmp2 = tmp[:3]
        tmp1 = tmp[2:]
        return check_hole_number(sum([int(x)*pow(10,tmp1[::-1].index(x)) for x in tmp1[::-1]])) and check_hole_number(int(tmp2[0])*100+int(tmp2[1])*10+int(tmp2[2]))
    

def check_hole_number_1(n):
    if n<1000:
        return (n%100-n%10)/10<n/100 and (n%100-n%10)/10<n%10
    return check_hole_number_1(n/100) and check_hole_number_1(n%1000)
    
    
# def check_mountain_number(n):
#     def helper(number):
#         if check_hole_number_1(number):
#             return False
#         if number<1000:
#             return (number%100-number%10)/10!=number/100 and (number%100-number%10)/10!=number%10
#         return check_mountain_number(number/100) and check_mountain_number(number%1000)
#     return helper(n)


def check_mountain_number(n):
    def helper(number,turn_counts=0):
        print(number,turn_counts)
        if number<100 and int(number/10)!=number%10 and turn_counts<=1:
            return True
        if number>=100:
            return helper(int(number/10),turn_counts+1) if (number/10%10-number/100%10) * (number%10-number/10%10) < 0 else helper(int(number/10),turn_counts)
        return False
    return helper(n)