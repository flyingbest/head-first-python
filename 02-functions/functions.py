# Modules of functions

# Modules let you organize your code for optimal sharing.
# The distribution utilities let you share your modules with the world.

# Modulea are everywhere.
# A module is simply z text file that contains Python code.

""" (triple quote) for multiple-line comments.
This is the standard way to include a multiple-line comment in your code.
"""


# Prepare your distribution
"""
1. begin by creating a folder for your module.
2. create a file called "setup.py" in your new folder.
"""

# Build your distribution
"""
3. build a distribution file.
	open a terminal window within your nester folder and type a single command: $ python3 setup.py sdist
4. install your distribution into your lacal copy of Python.
	type this command: $ sudo python3 setup.py install
5. then, your distribution is ready.
"""

# A quick review of your distribution
"""
After setup, These files and folders are all created for you by the distribution utilities.
"""

# Import a module to use it
"""
Now that your module is built, packaged as a distribution, and installed, let's see what's involved in using it.
To use a module, simply import it into your programs or import it into the IDLE shell:
	import nester
The import statement tells Python to include the nester.py module in your program.

import nester
cast = ['Palin', 'Cleese','Idle', 'Jones', 'Gilliam', 'Chapman']
print_lol(cast)
"""

# But it didn't Work!

# Python's modules implement namespaces
"""
All code in Python is associated with a namespace.
So, instead of invoking the function as print_lol(cast) you need to qualify the name as nester.print_lol(cast).

nester.print_lol(cast)
"""

# Register with the PyPI website
# Upload your code to PyPI
# Welcome to the PyPI community
# With success comes responsibility

# Before your write new code, think BIFs.

# range() : Returns an iterator that generates numbers in a specified range on demand and as needed.

import pdb

for num in range(4):
	print(num)

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
						["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print(movies)

#pdb.set_trace()
"""
def print_lol(the_list, level):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, level+1)
		else:
			for tab_stop in range(level):
				print("\t", end='')
			print(each_item)

print_lol(movies, 0)
"""

# trace your code
# Python Debugger - pdb
# import pdb
# pdb.set_trace() : this point is when trace is started.
# n : step next (executed current line)
# s : step in (move inside of current line of function)
# run : if next set_trace() doesn't exist, finished debugging.

# This url is pdb doc.
# https://docs.python.org/3/library/pdb.html


# Use optional arguments

"""
To turn a required argument to a function into an optional argument, provide the argument with a default value.
When no argument value is provided, the default value is used.
When an argument value is provided, it is used instead of the default.

def print_lol(the_list, level=0):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, level+1)
		else:
			for tab_stop in range(level):
				print("\t", end='')
			print(each_item)

print_lol(movies, 0)
print_lol(movies)
print_lol(movies, 5)
"""


# But, your API is still not right
# Amend your module one last time to add a third argument to your function.

def print_lol(the_list, indent=False, level=0):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, indent, level+1)
		else:
			if indent:
				for tab_stop in range(level):
					print("\t", end='')
			print(each_item)

print_lol(movies)
print_lol(movies, True)
print_lol(movies, True, 5)

