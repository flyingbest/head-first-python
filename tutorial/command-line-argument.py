
# Python provides a getopt module that helps you parse command-line options and arguments.
# $ python test.py arg1 arg2 arg3

# The Python sys module provides access to any command-line arguments via the sys.argv. This serves two purposes:
# 		1. sys.argv is the list of command-line arguments.
#			2. len(sys.argv) is the number of command-line arguments.

import sys

print('Number of arguments: ', len(sys.argv), ' arguments.')
print('Argument List: ', str(sys.argv))

# type into shell command like this:
# $ python3 command-line-argument.py arg1 arg2 arg3

# Note: As mentioned above, first argument is always script name and it is also being counted in number of arguments.


# -------------------------------------------------------------------------------------------------------------------

# These arguments are stored in the sys module's argv attribute as a list.
# The getopt module processes sys.argv using the conventions of the Unix getopt() function.
# More powerful and flexible command line processing is provided by the argparse module.

# create getopt.py, argparse.py files.
