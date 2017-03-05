# Lambdas 

# Lambda expressions (sometimes called lambda forms) are used to create anonymous functions.
# The expression lambda arguments: expression yields a function object.
# The unnamed object behaves like a function object defined with:
# 	def <lambda>(arguments):
# 		return expression

# Using like this:
# 	lambda <parameter_list>: expression	

def hap(x, y):
	return x+y

print(hap(10, 20))

print((lambda x,y: x+y)(10, 20))

# map(func, list)
map(lambda x: x ** 2, range(5))
print(map(lambda x: x ** 2, range(5)))
print(list(map(lambda x: x**2, range(5))))

# reduce(func, ordered data)
# you must imort like this:
from functools import reduce
reduce(lambda x,y: x+y, [0, 1, 2, 3, 4])
print(reduce(lambda x,y: x+y, [0, 1, 2, 3, 4]))

# testing this example
# why this reduce func print 'edcba' ? explain it. 
reduce(lambda x,y: y+x, 'abcde')
print(reduce(lambda x,y: y+x, 'abcde'))

# filter(func, list)
filter(lambda x: x<5, range(10))
list(filter(lambda x: x<5, range(10)))
print(list(filter(lambda x: x<5, range(10))))

# creating func that returns odd number 
print(list(filter(lambda x: x%2, range(10))))
print(list(filter(lambda x: x%2!=0, range(10))))
print(list(filter(lambda x: x%2==0, range(10))))

