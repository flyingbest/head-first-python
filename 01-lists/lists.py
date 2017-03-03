# This is python practicing code.

## Add more data in the list.
cast = ["Cleese", "Palin", "Jones", "Idle"]	# cast is variable.
print(cast)
print(len(cast))	# len = length
print(cast[1])	# cast[0] = Cleese, cast[1] = Palin, like this, python starts counting from ZERO.

cast.append("Gilliam")	# add a single data item to the end of your list.
print(cast)

cast.pop()	# remove data from the end of your list.
print(cast)

cast.extend(["Gilliam", "Chapman"])	# add a collection of data items to the end of your list.
print(cast)

cast.remove("Chapman")	# remove a specific data item from your list.
print(cast)

cast.insert(0, "Chapman")	# add a data item before a specific slot location.
print(cast)

movies = ["The Holy Grail", "The Life of Brain", "The Meaning of Life"]
print(movies)

movies.insert(1, 1975)
movies.insert(3, 1979)
movies.insert(5, 1983)

print(movies)


## iterate with the list data.
fav_movies = ["Holy Grail", "Life of Brain"]

for each_flick in fav_movies:	# each_flick is a target identifier
	print(each_flick)

# for <target identifier> in <list>:
#		<list-processing code...>

count = 0
while count < len(fav_movies):
	print(fav_movies[count])
	count = count + 1
# these while and for statements do the same thing.


## handle many levels of nested lists.
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
						["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

print(movies)

# first step
for each_item in movies:
	print(each_item)

# second step
for each_item in movies:
	if isinstance(each_item, list):
		for nested_item in each_item:
			print(nested_item)
	else:
		print(each_item)

# third step
for each_item in movies:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item, list):
				for deeper_item in nested_item:
					print(deeper_item)
			else:
				print(nested_item)
	else:
		print(each_item)


## Don't repeat code: create a function
def print_lol(the_list):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)
# this called Recursion.
# this is recursive function.

print_lol(movies)
