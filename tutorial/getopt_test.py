# getopt - C-style parser for command line options.

# this module helps scripts to parse the command line arguments in sys.argv.

# This module provides two functions and an exception:
# 	getopt.getopt(args, shortopts, longopts=[])

"""
args is the argument list to be parsed, without the leading reference to the runnig program.
Typically, this means sys.argv[1:]. shortopts is the string of option letters that the script wants to recognize,
with options that require an argument followed by a colon.

longopts, if specified, must be a list of strings with the names of the long options which should be supported.
The leading '--' characters should not be included in the option name. Long options which require an argument should be followed by an equal sign ('=').
Optional arguments are not supported.

The return value consists of two elements: 
	the first is a list of (option, value) pairs;
	the second is the list of program arguments left after the option list was stripped (this is a trailing slice of args).
Each option-and-value pair returned has the option as its first element,
prefixed with a hyphen for short options (e.g., '-x') or two hyphens for long options (e.g., '--long-option'),
and the option argument as its second element, or an empty string if the option has no argument.
The options occur in the list in the same order in which they were found, thus allowing multiple occurrences.
Long and short options may be mixed.00
"""

# 	getopt.gnu_getopt(args, shortopts, longopts=[])
# This function works like getopt(), except that GNU style scanning mode is used by default.

# exception:
# 	getopt.GetoptError
# 	- This is raised when an unrecognized option is found in the argument list or when an option requiring an argument is given none.
# 	getopt.error
# 	- Alias for GetoptError;

# ------------------------------------------------------------------------------------------------------------------------------------------------------

# First Error Point. Not executed.
# Because,
# You might be have getopt module in your code.
# When you refere python third party module, it try to import your module.

# this is typical usage script.
import getopt, sys

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)
	output = None
	verbose = False
	for o, a in opts:
		if o == "-v":
			verbose = True
		elif o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o in ("-o", "--output"):
			output = a
		else:
			assert False, "unhandled option"

if __name__ == "__main__":
	main()

### 한글 추가
### 옵션 문자에 :가 사용되면 옵션에 추가의 인수를 받아들인다는 의미!
### abc:de:
### 라면 a,b,d 는 단독옵션이고, c,e 는 인수를 갖는 옵션이다.

