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

# C(2).n


# a.z == C.z


# a.z == b.z


# Which evaluates to an integer?
# b.z
# b.z.z
print(b.z.z.z)
# b.z.z.z.z
# None of these