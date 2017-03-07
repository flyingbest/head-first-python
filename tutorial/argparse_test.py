import argparse

""" The basics
parser = argparse.ArgumentParser()
parser.parse_args()
"""
# The --help option, which can also be shortened to -h, is the only option we get for free.

""" Introducing Positional arguments
parser = argparse.ArgumentParser()
parser.add_argument("echo") 
args = parser.parse_args()
print(args.echo)
"""
# add_argument() method, which is what we use to specify which command-line options the program is willing to accept.
# The parse_args() method actually returns some data from the options specified, in this case, echo.
# The variable is some form of ‘magic’ that argparse performs for free (i.e. no need to specify which variable that value is stored in).
# You will also notice that its name matches the string argument given to the method, echo.

""" make it a bit more useful
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)
"""

""" doing something even more useful
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number")
args = parser.parse_args()
print(args.square**2)
"""
# It didn't go so well.
# That's because argparse treats the options we give it as strings, unless we tell it otherwise.
# So, let's tell argparse to treat that input as an integer.

"""
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()
print(args.square**2)
"""

""" Introducing Optional Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
	print("Verbosity turned on")
"""
# To show that the option is actually optional, there is no error when running the program without it.
# Note that by default, if an optional argument isn’t used, the relevant variable, in this case args.verbosity, is given None as a value,
# which is the reason it fails the truth test of the if statement.

"""
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbose:
	print("Verbosity turned on")
"""
# The option is now more of a flag than something that requires a value.
# We even changed the name of the option to match that idea.
# Note that we now specify a new keyword, action, and give it the value "store_true".
# This means that, if the option is specified, assign the value True to args.verbose. Not specifying it implies False.

""" Short options
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbose:
	print("Verbosity turned on")
"""

""" Combining Positional ans Optional arguments
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
	print("The square of {} equals {}".format(args.square, answer))
else:
	print(answer)
"""
# Note that the order does not matter.

"""
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbose", help="increase output verbosity", type=int)
args = parser.parse_args()
answer = args.square**2
if args.verbose == 2:
	print("The square of {} equals {}".format(args.square, answer))
elif args.verbose == 1:
	print("{}^2 = {}".format(args.square, answer))
else:
	print(answer)
"""
# Let's fix it by restricting the values the --verbosity option can accept.

"""
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbose", help="increase output verbosity", type=int, choices=[0,1,2])
args = parser.parse_args()
answer = args.square**2
if args.verbose == 2:
	print("The square of {} equals {}".format(args.square, answer))
elif args.verbose == 1:
	print("{}^2 = {}".format(args.square, answer))
else:
	print(answer)
"""
# let’s use a different approach of playing with verbosity, which is pretty common.
# It also matches the way the CPython executable handles its own verbosity argument.

"""
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="count")
args = parser.parse_args()
answer = args.square**2
if args.verbose == 2:
	print("The square of {} equals {}".format(args.square, answer))
elif args.verbose == 1:
	print("{}^2 = {}".format(args.square, answer))
else:
	print(answer)
"""
# Now here’s a demonstration of what the “count” action gives. You’ve probably seen this sort of usage before.
# And if you don’t specify the -v flag, that flag is considered to have None value.

"""
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="count")
args = parser.parse_args()
answer = args.square**2
# bug fix: replace == with >=
if args.verbose >= 2:
	print("The square of {} equals {}".format(args.square, answer))
elif args.verbose >= 1:
	print("{}^2 = {}".format(args.square, answer))
else:
	print(answer)
"""
# Third output not so good. add defualt keyword.

"""
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.square**2
if args.verbose >= 2:
	print("The square of {} equals {}".format(args.square, answer))
elif args.verbose >= 1:
	print("{}^2 = {}".format(args.square, answer))
else:
	print(answer)
"""
# Remember that by default, if an optional argument isn't specified, it gets the None value, and that cannot be compared to an int value.
# (hence the TypeError exception.)

""" Getting a little more advanced
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbose", action="count", default=0)
args = parser.parse_args()
answer = args.x**args.y
if args.verbose >= 2:
	print("{} to the power {} equals {}".format(args.x, args.y, answer))
elif args.verbose >= 1:
	print("{}^{} = {}".format(args.x, args.y, answer))
else:
	print(answer)
"""
# Notice that so far we’ve been using verbosity level to change the text that gets displayed.
# The following example instead uses verbosity level to display more text instead.

"""
parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbose", action="count", default=0)
args = parser.parse_args()
answer = args.x**args.y
if args.verbose >= 2:
	print("Running '{}".format(__file__))
if args.verbose >= 1:
	print("{}^{} == ".format(args.x, args.y), end="")
print(answer)
"""

# So far, we have been working with two methods of an argparse.ArgumentParser instance.
# Let’s introduce a third one, add_mutually_exclusive_group(). It allows for us to specify options that conflict with each other.
# Let’s also change the rest of the program so that the new functionality makes more sense:
# we’ll introduce the --quiet option, which will be the opposite of the --verbose one:
""" Conflicting options
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y
if args.quiet:
	print(answer)
elif args.verbose:
	print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
	print("{}^{} == {}".format(args.x, args.y, answer))
"""
# Before we conclude, you probably want to tell your users the main purpose of your program, just in case they don’t know.

parser = argparse.ArgumentParser(description="Calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y
if args.quiet:
	print(answer)
elif args.verbose:
	print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
	print("{}^{} == {}".format(args.x, args.y, answer))

# Conclusion
# The argparse module offers a lot more than shown here.
# its docs are quite detailed and thorough, and full of examples.

