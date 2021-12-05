def score(boards,track,b,call):
	Sum = 0
	for row in range(len(boards[b])):
		for col in range(len(boards[b][row])):
			if track[b][row][col] == 0:
				Sum = Sum + boards[b][row][col]
	return (Sum*call)


def check(track,b,r,c):
	rcount = 0
	ccount = 0
	#print(track[b])
	for row in range(len(track[b])):
		if track[b][row][c] == 1:
			rcount = rcount + 1
		if track[b][r][row] == 1:
			ccount = ccount + 1
	if ((ccount == 5) or (rcount == 5)):
		return 1
	else:
		return 0


if __name__ == '__main__':
	order = []
	boards = []
	board = []

	with open('input.txt') as f:
		line = f.readline()
		o = (line.split(","))
		o[-1] = o[-1].strip()
		order = list(int(x) for x in o)
		line = f.readline()
		#print(order)
		
		numbers = f.readlines()
		numbers = [num.strip() for num in numbers]
		numbers.append('')
		#print(numbers)
		for line in numbers:
			if line == '':
				boards.append(board)
				#print(board)
				board = []
			else:
				board.append(list(int(x) for x in line.split()))
		last = 999
		#track = [[[0]*len(boards[0][0])]*len(boards[0])]*len(boards)
		track = []
		for b in range(len(boards)):
			bor = []
			for r in range(len(boards[b])):
				row = []
				for c in range(len(boards[b][r])):
					row.append(0)
				bor.append(row)
			track.append(bor)
		#print(track)
		board_no = list(range(0,len(boards)))
		count = 0
		count1 = 0
		for call in order:
			for b in range(len(boards)):
				for r in range(len(boards[0])):
					for c in range(len(boards[0][0])):
						if (boards[b][r][c] == call):
							track[b][r][c] = 1
							if (check(track,b,r,c) == 1):
								if count == 0:
									print("Score -", score(boards,track,b, call))
									count = 1
								if (b == last and count1 == 0):
									print("Score -", score(boards,track,b, call))
									count1 = 1
								try:
									board_no.pop(board_no.index(b))
									if (len(board_no) == 1):
										print(board_no)
										last = board_no[0]
								except:
									pass

								break