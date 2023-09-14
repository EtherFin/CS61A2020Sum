class A:
	z = -1
	def f(self, x):
		return B(x-1)

class B(A):
	n = 4
	def __init__(self, y):
		if y:
			self.z = self.f(y)
		else:
			self.z = C(y+1)

class C(B):
	def f(self, x):
		return x

a = A()
b = B(1)
b.n = 5

C(2).n


a.z == C.z


a.z == b.z


# Which evaluates to an integer?
# b.z
# b.z.z
print(b.z.z.z)
# b.z.z.z.z
# None of these

print('hello?')

def generate_subsets():
	"""
	>>> subsets = generate_subsets()
	>>> for _ in range(3):
	... print(next(subsets))
	...
	[[]]
	[[], [1]]
	[[], [1], [2], [1, 2]]
	"""
	def helper(n):
		if n == 0:
			return [[]]
		else:
			return [[n] + elem for elem in helper(n-1)] + helper(n-1)
	i = 0
	while 1:
		yield helper(i)
		i+=1

# print('hello!?')
# subsets = generate_subsets()
# for _ in range(3):
# 	print(next(subsets))


def sum_paths_gen(t):
	"""
	>>> t1 = tree(5)
	>>> next(sum_paths_gen(t1))
	5
	>>> t2 = tree(1, [tree(2, [tree(3), tree(4)]), tree(9)])
	>>> sorted(sum_paths_gen(t2))
	[6, 7, 10]
	"""
	# if ___________________________:
	# 	yield ____________________
	# for __________________________:
	# 	for __________________________:
	# 		yield ____________________
	if is_leaf(t):
		yield label(t)
	for branch in branches(t):
		for s in sum_paths_gen(branch):
			yield label(t) + s

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

# t1 = tree(5)
# print(next(sum_paths_gen(t1)))
# t2 = tree(1, [tree(2, [tree(3), tree(4)]), tree(9)])
# print(sorted(sum_paths_gen(t2)))