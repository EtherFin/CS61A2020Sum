def min_elements(T, lst):
    if T == 0:
        return 0
    return min([min_elements(T-lst[x], lst[x:]) for x in range(len(lst)) if T-lst[x] >= 0]) + 1

print(min_elements(12, [4, 2, 1])) # 4 + 4 + 4 so should print 3
print(min_elements(10, [4, 2, 1])) # 4 + 4 + 2 so should print 3
print(min_elements(0, [3, 2, 1])) # should print 0