if __name__ == '__main__':
	order = []
	boards = []
	board = []

	with open('input.txt') as f:
		line = f.readline()
		order = (line.split(","))
		order[-1] = order[-1].strip()
		line = f.readline()
		
		numbers = f.readlines()
		numbers = [num.strip() for num in numbers]
		print(numbers)

	#print(order)
