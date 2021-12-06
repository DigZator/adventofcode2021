import numpy as np

if __name__ == "__main__":
	with open('input.txt') as f:
		Wires = []
		large = 0

		for line in f.readlines():
			line = line.strip()
			#print(line)
			nums = line.split(" -> ")
			#print(nums)
			ends = []
			for points in nums:
				coord = []
				coord.append(int(points.split(",")[0]))
				coord.append(int(points.split(",")[1]))
				ends.append(coord)
				for dis in coord:
					if dis > large:
						large = dis
			Wires.append(ends)
		
		board = np.zeros([large+1,large+1], dtype = int)
		#print(board)

		for wire in Wires:
			x1,y1,x2,y2 = wire[0][0], wire[0][1], wire[1][0], wire[1][1]
			if (x1 == x2):
				if (y1 > y2):
					for y in range(y2, y1 + 1):
						board[x1][y] = board[x1][y] + 1
						#print(board[x1][y], y)
				else:
					for y in range(y1, y2 + 1):
						board[x1][y] = board[x1][y] + 1
			elif (y1 == y2):
				if (x1 > x2):
					for x in range(x2, x1 + 1):
						board[x][y1] = board[x][y1] + 1
				else:
					for x in range(x1, x2 + 1):
						board[x][y1] = board[x][y1] + 1
			elif (abs(x1-x2) == abs(y1-y2)):
				if ((x1 > x2) and (y1 > y2)):
					for offset in range(x1 - x2):
						board[x2+offset][y2+offset] +=  1
					#board[x1][y1] = board[x1][y1] + 1
				elif ((x1 > x2) and (y1 < y2)):
					for offset in range(x1 - x2):
						board[x2+offset][y2-offset] +=  1
					#board[x1][y2] = board[x1][y2] + 1
				elif ((x1 < x2) and (y1 < y2)):
					for offset in range(x2 - x1):
						board[x2-offset][y2-offset] +=  1
					#board[x2][y2] = board[x2][y2] + 1
				elif ((x1 < x2) and (y1 > y2)):
					for offset in range(x2 - x1):
						board[x2-offset][y2+offset] +=  1
					#board[x2][y1] = board[x2][y1] + 1
				#xdiff,ydiff = 0,0
				#if (x1 > x2):
				#	xdiff = 1
				#elif (x1 < x2):
				#	xdiff = -1
				#if (y1 > y2):
				#	ydiff = 1
				#elif (y1 < y2):
				#	ydiff = -1
#
				#y = y2
				#x = x2
#
				#while ((y != y1) and (x != x1)):
				#	board[x][y] = board[x][y] + 1
				#	x = x + xdiff
				#	y = y + ydiff
				#board[y1][x1] += 1
		count = 0
		for x in board:
			for y in x:
				if y >= 2:
					count = count + 1
		print(count)