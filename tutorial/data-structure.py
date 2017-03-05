# Python Data Structure

# What's the differences between Tuples and Lists?
"""
Tuples are fixed size in nature whereas lists are dynamic.
In other words, a tuple is immutable whereas a list is mutable.
	1. You can't add elements to a tuple. Tuples have no append or extend method.
	2. You can't remove elements from a tuple. Tuples have no remove or pop method.
	3. You can find elements in a tuple, since this doesn’t change the tuple.
	4. You can also use the in operator to check if an element exists in the tuple.
"""

# So what are tuples good for?
"""
Tuples are faster than lists.
If you’re defining a constant set of values and all you’re ever going to do with it is iterate through it, use a tuple instead of a list.

It makes your code safer if you “write-protect” data that doesn’t need to be changed.
Using a tuple instead of a list is like having an implied assert statement that shows this data is constant,
and that special thought (and a specific function) is required to override that.

Some tuples can be used as dictionary keys (specifically, tuples that contain immutable values like strings, numbers, and other tuples).
Lists can never be used as dictionary keys, because lists are not immutable.
"""

