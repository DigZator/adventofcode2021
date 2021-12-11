if __name__ == "__main__":
	with open('input.txt') as f:
		board = []
		for line in f.readlines():
			row = []
			line = line.strip()
			for x in line:
				row.append(int(x))
			board.append(row)
		risk_sum = 0
		R = len(board)
		C = len(board[R-1])
		for r in range(len(board)):
			for c in range(len(board[r])):
				small = True
				#TOP
				if (((r-1 >= 0) and (board[r-1][c] <= board[r][c])) or
					((r+1 < R) and (board[r+1][c] <= board[r][c])) or
					((c-1 >= 0) and (board[r][c-1] <= board[r][c])) or
					((c+1 < C) and (board[r][c+1] <= board[r][c]))):
					small = False
				if small:
					risk_sum += board[r][c]+1
		print(risk_sum)
