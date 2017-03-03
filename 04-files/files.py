# Saving data to files

"""
man = []
other = []

try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError:
	print('The datafile is missing!')

print(man)
print(other)
"""

# Open your file in write mode

out = open("data.out", "w")
print("Norwegian Blues stun easily.", file=out)
out.close()

man = []
other = []

try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError:
	print('The datafile is missing!')

"""
try:
	man_data = open('man_data.txt', 'w')
	other_data = open('other_data.txt', 'w')

	print(man, file=man_data)
	print(other, file=other_data)
	
	# If Crash here!
	# blow two lines of code DON'T get to run.	
	man_data.close()
	other_data.close()

except IOError:
	print('File Error!')
"""

# Files are left open after an exception!

# Extend try with finally
# when you have a situation where code must always run no matter what errors occurs,
# add that code to your try statement's finally suite:

"""
try:
	man_data = open('man_data.txt', 'w')
	other_data = open('other_data.txt', 'w')

	print(man, file=man_data)
	print(other, file=other_data)

except IOError:
	print('File Error!')

finally:
	if 'man_file' in locals():
		man_data.close()
	if 'other_file' in locals():
		other_data.close()
"""


# Knowing the type of error is not enough

"""
try:
	data = open('missing.txt')
	print(data.readline(), end='')
except IOError as err:
	print('File error: ' + str(err))
finally:
	if 'data' in locals():
		data.close()
"""


# Use with to work with files

try:
	with open('its.txt', "w") as data:
		print("It's...", file=data)
except IOError as err:
	print('File error: ' + str(err))

# The with statement takes advantage of a Python technology called the context management protocol.

try:
	with open('man_data.txt', 'w') as man_data:
		print(man, file=man_data)
	
	with open('other_data.txt', 'w') as other_data:
		print(other, file=other_data)

except IOError as err:
	print('File Error: ' + str(err))


# Defualt formats are unsuitable for files

"""
with open('man_data.txt') as mdf:
	print(mdf.readline())
"""
# no need to close your file, because 'with' does that for you.


# Why not modify print_lol()?

val = ["ansxodbs", "rlawltn", ["mom", "dad", ["you", "and", "i"]]]

import sys
def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, indent, level+1, fh)
		else:
			if indent:
				for tab_stop in range(level):
					print("\t", end='', file=fh)
			print(each_item, file=fh)

#print_lol(val, True, 0)


# Pickle your data
# Python ships with a standard library called pickle, which can save and load almost any Python data object, including lists.

# Save with dump and restore with load
"""
using pickle is straightforward: import the required module, then use dump() to save your data and, some time later,
load() to restore it. The only requirement when working with pickled files is that they have to be opened in binary access mode:
"""

import pickle

try:
	with open('man_data.txt', 'wb') as man_file:
		pickle.dump(man, man_file)
	with open('other_data.txt', 'wb') as other_file:
		pickle.dump(other, other_file)
except IOError as err:
	print('File error: ' + str(err))
except pickle.PickleError as perr:
	print('Pickling error: ' + str(perr))

new_man = []
new_other = []

try:
	with open('man_data.txt', 'rb') as man_file:
		new_man = pickle.load(man_file)
	with open('other_data.txt', 'rb') as other_file:
		new_other = pickle.load(other_file)
except IOError as err:
	print('File error: ' + str(err))
except pickle.PickleError as perr:
	print('Pickling error: ' + str(perr))

#print_lol(new_man)
#print_lol(new_other)

# pickle really shines when you load some previously pickled data into another program.
# And, of course, there's nothing to stop you from using pickle with nester.
# After all, each module is designed to serve different purposes.

