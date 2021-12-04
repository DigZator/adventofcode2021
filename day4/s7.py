if __name__ == '__main__':
	order = []
	boards = []
	board = []

	with open('input.txt') as f:
		line = f.readline()
		order = (line.split(","))
		order[-1] = order[-1].strip()
		print(f.readline())

	print(order)