# Work that data

with open('james.txt') as jaf:
	data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
	data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
	data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
	data = saf.readline()
sarah = data.strip().split(',')

"""
print(james)
print(julie)
print(mikey)
print(sarah)
"""


# Sort in one of two ways
"""
In-place sorting takes your data, arranges it in the order you specify, and then replaces your original data with the sorted version.
The original ordering is lost. With lists, the sort() method provides in-place sorting:

Copied sorting takes your data, arranges it in the order you specify, and then returns a sorted copy of your original data.
Your original data's ordering is maintained and only the copy is sorted. In Python, the sorted() BIF supports copied sorting.
"""

"""
data = [6,3,1,2,4,5]
print(data)

data.sort()
print(data)

data1 = [6,3,1,2,4,5]
print(data1)

data2 = sorted(data1)
print(data1)
print(data2)
"""

"""
print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))
"""

# Nonuniformity in the coach's data is causing the sort to fail.

def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins, secs) = time_string.split(splitter)

	return(mins + '.' + secs)

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:
	clean_james.append(sanitize(each_t))

for each_t in julie:
	clean_julie.append(sanitize(each_t))

for each_t in mikey:
	clean_mikey.append(sanitize(each_t))

for each_t in sarah:
	clean_sarah.append(sanitize(each_t))

"""
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
"""

# By default, both the sort() method and the sorted() BIF order your data in ascending order.
# To order your data in descending order, pass the reverse=True argument to either sort() or sorted() and Python will take care of things for you.

# Duplicated code is problem. -> better way to write code (list comprehension)

# Comprehending lists
"""
Consider what you need to do when you transform one list into another. Four things have to happen. You need to:
	1. create a new list to hold the transformed data.
	2. iterate each data item in the original list.
	3. with each iteration, perform the transformation.
	4. append the transformed data to the new list.

Here's the same functionality as a list comprehension, which involves creating a new list by specifying the transformation that is to be applied to each
of the data items within an existing list.

clean_mikey = [sanitize(each_t) for each_t in mikey]

what's interesting is that the transformation has been reduced to a single line of code.
Additionally, there's no need to specify the use of the append() method as this action is implied within the list comprehension.
"""

mins = [1,2,3]
secs = [m*60 for m in mins]
print(secs)

meter = [1,10,3]
feet = [m*3.281 for m in meter]
print(feet)

lower = ["I", "don't", "like", "spam"]
upper = [s.upper() for s in lower]
print(upper)

dirty = ['2-22', '2:22', '2.22']
clean = [sanitize(t) for t in dirty]
print(clean)

clean = [float(s) for s in clean]
print(clean)

clean = [float(sanitize(t)) for t in ['2-22', '3:33', '4.44']]
print(clean)

"""
print(sorted([sanitize(t) for t in james]))
print(sorted([sanitize(t) for t in julie]))
print(sorted([sanitize(t) for t in mikey]))
print(sorted([sanitize(t) for t in sarah]))
"""

# Iterate to remove duplicates
# list slice:

"""
james = sorted([sanitize(t) for t in james])
julie = sorted([sanitize(t) for t in julie])
mikey = sorted([sanitize(t) for t in mikey])
sarah = sorted([sanitize(t) for t in sarah])

unique_james = []
for each_t in james:
	if each_t not in unique_james:
		unique_james.append(each_t)

print(unique_james[0:3])

unique_julie = []
for each_t in julie:
	if each_t not in unique_julie:
		unique_julie.append(each_t)

print(unique_julie[0:3])

unique_mikey = []
for each_t in mikey:
	if each_t not in unique_mikey:
		unique_mikey.append(each_t)

print(unique_mikey[0:3])

unique_sarah = []
for each_t in sarah:
	if each_t not in unique_sarah:
		unique_sarah.append(each_t)

print(unique_sarah[0:3])
"""


# Remove duplicates with sets
"""
In addition to lists, Python also comes with the set data structure, which behaves like the sets you learned all about in math class.
The overriding characteristics of sets in Python are that the data items in a set are unordered and duplicates are not allowed.
If you try to add a data item to a set that already contains the data item, Python simply ignores it.
Create an empty set using the set() BIF, which is an example of a factory function:
	distances = set()
It is also possible to create and populate a set in one step. You can provide a list of data values between curly braces or specify an existing list
as an argument to the set() BIF, which is the factory function:
	distances = {10.6, 11, 8, 10.6, "two", 7}
	distances = set(james)

"""

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		return(data.strip().split(','))
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)

sarah = get_coach_data('sarah.txt')

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])


# Python Lingo
"""
Method Chaining - reading from left to right, applies a collection of methods to data.
Function Chaining - reading from right to left, applies a collection of functions to data.
A 'slice' - access more than one item from a list.
A 'set' - a collection of unordered data items that contains no duplicates.
"""

