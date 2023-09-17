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

class Email:
	"""Every email object has 3 instance attributes: the
	message, the sender name, and the recipient name.
	"""
	def __init__(self, msg, sender_name, recipient_name):
		self.msg = msg 
		self.sender_name = sender_name
		self.recipient_name = recipient_name



class Server:
	"""Each Server has an instance attribute clients, which
	is a dictionary that associates client names with
	client objects.
	"""
	def __init__(self):
		self.clients = {}


	def send(self, email):
		"""Take an email and put it in the inbox of the client
		it is addressed to.
		"""
		self.clients[email.recipient_name].receive(email)


	def register_client(self, client, client_name):
		"""Takes a client object and client_name and adds them
		to the clients instance attribute.
		"""
		# Note: This worksheet is a problem bank—most TAs will not cover all the problems in discussion section.
		# 10 Iterators, Generators, Object-Oriented Programming
		self.clients[client_name] = client 



class Client:
	"""Every Client has instance attributes name (which is
	used for addressing emails to the client), server
	(which is used to send emails out to other clients), and
	inbox (a list of all emails the client has received).
	"""
	def __init__(self, server, name):
		self.inbox = []
		self.server = server 
		self.name = name 


	def compose(self, msg, recipient_name):
		"""Send an email with the given message msg to the
		given recipient client.
		"""
		self.server.send(Email(msg, self.name, recipient_name))


	def receive(self, email):
		"""Take an email and add it to the inbox of this
		client.
		"""
		# Note: This worksheet is a problem bank—most TAs will not cover all the problems in discussion section.
		# Iterators, Generators, Object-Oriented Progra
		self.inbox += email


class Pet():
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner
    
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
        
    def talk(self):
        print(self.name)

class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super.__init__(self, name , owner)
        self.lives = lives
    
    def talk(self):
        """ Print out a cat's greeting.
        
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + ' says meow!')
    
    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        self.lives -= 1
        if self.lives == 0:
            super.is_alive = False
        
        
class NoisyCat(Cat):
    
    """A Cat that repeats thins twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        # Not necessary ,because it is the same with the Cat class
        super.__init__(self, name, owner, lives=9)
        
    def talk(self):
        """Talks twice as much as a regular cat.
        
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        super.talk
        super.talk
        
        
lst = [6, 1, 'a']
# TypeError: 'list' object is not an iterator
# print('next(lst):', next(lst))

lst_iter = iter(lst)
print('next(lst_iter):', next(lst_iter))
print('next(lst_iter):', next(lst_iter))
print('next(iter(lst)):', next(iter(lst)))
print('[x for x in lst_iter]:', [x for x in lst_iter])


def gen_naturals():
    current = 0
    while True:
        yield current
        current += 1


gen = gen_naturals()
print('next(gen):', next(gen))
print('next(gen):', next(gen))


# def generate_subsets():
#     """Return all subsets from 1 to n."""
#     pass
#
#
# subsets = generate_subsets()
# for _ in range(3):
#     print(next(subsets))


# [[]]
# [[], [1]]
# [[], [1], [2], [1, 2]]

# • class: a template for creating objects
# • instance: a single object created from a class
# • instance attribute: a property of an object, specific to an instance
# • class attribute: a property of an object, shared by all instances of a class
# • method: an action (function) that all instances of a class may perform
class Student:
    students = 0

    def __init__(self, name, ta):
        self.name = name
        self.understanding = 0
        Student.students += 1
        print('There are now', Student.students, 'students')
        ta.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print('Thanks, ' + staff.name)


class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1


# what would Python display:
# callahan = Professor('Callahan')
# elle = Student('Elle', callahan)
# elle.visit_office_hours(callahan)
# elle.visit_office_hours(Professor("Paulette"))
# elle.understanding
# [name for name in callahan.students]
# x = Student("Vivian", Professor("Stromwell")).name
# x
# [name for name in callahan.students]

class Email:
    """Every email object has 3 instance attributes: the message,
    the sender name, and recipient name.
    """

    def __init__(self, msg, sender_name, recipient_name):
        self.message = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associated client names with client objects.
    """

    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        client = self.clients[email.recipient_name]
        client.receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them to
        the clients instance attribute.
        """
        self.clients[client_name] = client


class Client:
    """Every Client has instance attributes name (which is used for
    addressing emails to the client), server (which is used to send emails
    out to other clients), and inbox (a list of all emails the client has received).
    """

    def __init__(self, server, name):
        self.inbox = []
        self.name = name
        self.server = server

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this client."""
        self.inbox.append(email)


# Inheritance
class Pet():
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.is_alive = True

    def eat(self, thing):
        print(self.name + ' ate a ' + str(thing) + '!')

    def talk(self):
        print(self.name)


class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        print(self.name + ' says meow!')

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive' becomes
        False. If this is called after lives has reached zero, print out that
        the cat has no more lives to lose.
        """
        if self.lives > 0:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False
        else:
            print('the cat has no more lives to lose.')


class NoisyCat(Cat):
    def talk(self):
        """Talks twice as much as a regylar cat."""
        Cat.talk(self)
        Cat.talk(self)


# what would Python display:
class A:
    def f(self):
        return 2

    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)


class B(A):
    def f(self):
        return 4


# x, y = A(), B()
# x.f()
# print(B.f()) # Error
# x.g(x, 1)
# y.g(x, 2)

