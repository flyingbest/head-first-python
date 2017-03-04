# Bundling code with data

def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)

	(mins, secs) = time_string.split(splitter)
	return(mins + '.' + secs)

"""
def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		return(data.strip().split(','))
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)
"""

"""
sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest time are: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
"""

# this code is for loop for print.
sample = ['james2.txt', 'julie2.txt', 'mikey2.txt', 'sarah2.txt']

"""
for each_item in sample:
	arr = get_coach_data(each_item)
	(arr_name, arr_dob) = arr.pop(0), arr.pop(0)
	print(arr_name + "'s fastest time are: " + str(sorted(set([sanitize(t) for t in arr]))[0:3]))
"""


# Use a dictionary to associate data
"""
Dictionary A built-in data structure (included with Python) that allows you to associate data with keys, as opposed to numbers.
This lets your in-memory data closely match the structure of your actual data.
"""

"""
cleese = {}
palin = dict()
print(type(cleese))
print(type(palin))

cleese['Name'] = 'John Cleese'
cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']
palin = {'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writer', 'tv']}

print(palin['Name'])
print(palin['Occupations'][-1])		# tv
print(cleese['Occupations'][-1])	# film producer

# provide the data asociated with the new key.
palin['Birthplace'] = "Broomhill, Sheffield, England"
cleese['Birthplace'] = "Weston-super-Mare, North Somerset, England"

print(palin)
print(cleese)
"""

# Unlike lists, a Python dictionary does not maintain insertion order, which can result in some unexpected behavior.
# The key point is that the dictionary maintains the associations, not the ordering.

"""
for each_item in sample:
	arr = get_coach_data(each_item)
	arr_data = {}
	arr_data['Name'] = arr.pop(0)
	arr_data['DOB'] = arr.pop(0)
	arr_data['Times'] = arr
	print(arr_data['Name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in arr_data['Times']]))[0:3]))
"""

# improve get_coach_data function

"""
def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		templ = data.strip().split(',')
		return({'Name'	:	templ.pop(0),
						'DOB'		: templ.pop(0),
						'Times'	: str(sorted(set([sanitize(t) for t in templ]))[0:3])})
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)

for each_item in sample:
	arr = get_coach_data(each_item)
	print(arr['Name'] + "'s fastest times are: " + arr['Times'])
"""


# Bundle your code and its data in a class
"""
Like the majority of other modern programming languages, Python lets you create and define an object-oriented class
that can be used to asscociate code with the data that it operates on.

Using a class helps reduce complexity.
Reduced complexity means fewer bugs.
Fewer bugs means more maintainable code.
"""

# Define a class
"""
Once this definition is in place, you can use it to create (or instantiate) data objects, which inherit their characteristics from your class.
Within the object-oriented world, your code is often referred to as the class's methods, and your data is often referred to as its attributes.
Instantiated data objects are often referred to as instance.
"""

# Use class to define classes
"""
Python uses class to create objects. Every defined class has a special method called __init__(), which allows you to control how objects are initialized.
Here's the basic form:
"""
# class Athlete:
# 	def __init__(self):
#			# The code to initialize an "Athlete" object.
#				...

# Creating object instances
# a = Athlete()
# b = Athlete()

# The importance of self
"""
To confirm: when you define a class you are, in effect, defining a custom factory function that you can then use in your code to create instance:
# a = Athlete()

When Python processes this line of code, it turns the factory function call into the following call, which identifies the class, the method
( which is automatically set to __init__() ) and the object instance being operated on:
# Athlete.__init__(a) //a is the target identifier of the object instance.

Now take another look at how the __init__() method was defined in the class:
# def __init__(self):
#		# The code initialize an "Athlete" object.
#			...
"""
# The target identifier is assigned to the self argument.
"""
This is a very important argument assignment. Without it, the Python interpreter can't work out which object instance to apply the method invocation to.
Note that the class code is designed to be shared among all of the object instances:
the methods are shared, the attributes are NOT. The self argument helps identify which object instance's data to work on.
"""

# Every method's first argument is self
"""
class Athlete:
	def __init__(self, value=0):
		self.thing = value
	def how_big(self):
		return(len(self.thing))

d = Athlete("Holy Grail.")
print(d.how_big())

a = Athlete("")
print(a.how_big())
"""

"""
class Athlete:
	def __init__(self, a_name, a_dob=None, a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times

sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = Athlete('James Jones')

print(type(sarah))
print(type(james))

print(sarah)
print(james)

print(sarah.name)
print(james.name)
print(sarah.dob)
print(james.dob)
print(sarah.times)
print(james.times)
"""

# improve get_coach_data function

"""
class Athlete:
	def __init__(self, a_name, a_dob=None, a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times

	def top3(self):
		return(sorted(set([sanitize(t) for t in self.times]))[0:3])

# add Athlete class def
	def add_time(self, time_value):
		self.times.append(time_value)

	def add_times(self, list_of_times):
		self.times.extend(list_of_times)

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		templ = data.strip().split(',')
		return Athlete(templ.pop(0), templ.pop(0), templ)
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)

for each_item in sample:
	arr = get_coach_data(each_item)
	print(arr.name + "'s fastest times are: " + str(arr.top3()))
"""

# create a new object instance for Vera.

"""
vera = Athlete('Vera Vi')
vera.add_time('1.31')
print(vera.top3())
vera.add_times(['2.22', "1-21", '2:22'])
print(vera.top3())
"""


# Inherit from Python's built-in list

"""
class NamedList(list):
	def __init__(self, a_name):
		list.__init__([])
		self.name = a_name

johnny = NamedList("John Paul Jones")
print(type(johnny))
print(dir(johnny))

johnny.append("Bass Player")
print(johnny)
johnny.extend(['Composer', "Arranger", "Musician"])
print(johnny)

print(johnny.name)

for attr in johnny:
	print(johnny.name + " is a " + attr + ".")
"""

# improve Athlete class

class AthleteList(list):
	def __init__(self, a_name, a_dob=None, a_times=[]):
		list.__init__([])
		self.name = a_name
		self.dob = a_dob
		self.extend(a_times)

	def top3(self):
		return(sorted(set([sanitize(t) for t in self]))[0:3])

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		templ = data.strip().split(',')
		return(AthleteList(templ.pop(0), templ.pop(0), templ))	# Athlete -> AthleteList change
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)

vera = AthleteList('Vera Vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22', "1-21", '2:22'])
print(vera.top3())

for each_item in sample:
	arr = get_coach_data(each_item)
	print(arr.name + "'s fastest times are: " + str(arr.top3()))

# 'self' - a method argument that always refers to the current object instance.

