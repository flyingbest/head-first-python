import sys

print('Program started!')
print('Number of arguments: ', len(sys.argv), ' arguments.')
print('Argument List: ', str(sys.argv))
print('')

if sys.argv[1] == 'bfs':
	print("Breadth-First Search Algorithm working here...")
	list = sys.argv[2].split(',')
	print("This is comma-separated list of integers : " + str(list))
	print("example: ")
	print("list[0] : " + list[0])
	print("list[1] : " + list[1])

elif sys.argv[1] == 'dfs':
	print("Depth-First Search Algorithm working here...")
	list = sys.argv[2].split(',')
	print("This is comma-separated list of integers : " + str(list))
	print("example: ")
	print("list[0] : " + list[0])
	print("list[1] : " + list[1])

elif sys.argv[1] == 'ast':
	print("A-Star Search Algorithm working here...")
	list = sys.argv[2].split(',')
	print("This is comma-separated list of integers : " + str(list))
	print("example: ")
	print("list[0] : " + list[0])
	print("list[1] : " + list[1])

elif sys.argv[1] == 'ida':
	print("IDA-Star Search Algorithm working here...")
	list = sys.argv[2].split(',')
	print("This is comma-separated list of integers : " + str(list))
	print("example: ")
	print("list[0] : " + list[0])
	print("list[1] : " + list[1])

print('')
print("Program Finished!")
