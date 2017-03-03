# Dealing with errors

# It's all lines of text
"""
The basic input mechanism in Python is line based:
when read into your program from a text file, data arrives one line at a time.

Python's open() BIF lives to interact with files. When combined with a for statement, reading files is straightforward.
"""

the_file = open('sketch.txt')
# Do something with the data
# in "the_file".

"""
for each_line in the_file:
	(role, line_spoken) = each_line.split(':')
	print(role, end='')
	print(' said: ', end='')
	print(line_spoken, end='')
"""

# error : too many values to unpack
# Know your methods and ask for help
"""
It might be useful to see if the split() method includes any functionality that might help here.
You can ask the IDLE shell to tell you more about the spilt() method by using the help() BIF.
"""

"""
for each_line in the_file:
	(role, line_spoken) = each_line.split(':', 1)
	print(role, end='')
	print(' said: ', end='')
	print(line_spoken, end='')
"""

# Add extra logic

data = "I tell you, there's no such thing as a flying circus."
print(data.find(':'))
# the string does NOT contain a colon, so find() returns -1 for NOT FOUND.

"""
for each_line in the_file:
	if not each_line.find(':') == -1:
		(role, line_spoken) = each_line.split(':', 1)
		print(role, end='')
		print(' said: ', end='')
		print(line_spoken, end='')
"""


# Handle exceptions
"""
The traceback is Python's way of telling you that something unexpected has occurred during runtime.
In the Python world, runtime errors are called exceptions.
"""

# The try/except mechanism
"""
Python includes the try statement, which exist to provide you with a way to systematically handle exceptions and errors at runtime.
The general form of the try statement looks like this:
"""

# try :
#				your code (which might cause a runtime error)
# except:
# 			your error-recovery code

"""
for each_line in the_file:
	try:
		(role, line_spoken) = each_line.split(':', 1)
		print(role, end='')
		print(' said: ', end='')
		print(line_spoken, end='')
	except:
		pass	# if a runtime error occurs, this code is executed.
"""

# Which is better? Extra code, Exception handler


# What about other errors?
# Handling missing files

"""
#import os
#if os.path.exist('/sketch.txt'):
#	the_file = open('sketch.txt')

	for each_line in the_file:
		if not each_line.find(':') == -1:
			(role, line_spoken) = each_line.split(':', 1)
			print(role, end='')
			print(' said: ', end='')
			print(line_spoken, end='')
	
#	the_file.close()
#else:
#	print('The data file is missing!')
"""

"""
#try:
#	the_file = open('sketch.txt')

	for each_line in the_file:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			print(role, end='')
			print(' said: ', end='')
			print(line_spoken, end='')
		except:
			pass

#	the_file.close()
#except:
#	print('The data file is missing!')
"""

# So, which approach is best? fiist one or second one?

# Complexity is rarely a good thing
"""
By using Python's exception-handling mechanism, you get to concentrate on what your code needs to do,
as opposed to worrying about what can go wrong and writing extra code to avoid runtime errors.
"""

# Last, You need to somehow use except in a less generic way.

"""
#try:
#	the_file = open('sketch.txt')

	for each_line in the_file:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			print(role, end='')
			print(' said: ', end='')
			print(line_spoken, end='')
		except ValueError:
			pass

#	the_file.close()
#except IOError:
#	print('The data file is missing!')
"""
# Be specific with your exceptions
# If your exception-handling code is designed to deal with a specific type of error,
# be sure to specific the error type on the except line.

the_file.close()

