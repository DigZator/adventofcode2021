class Grid:
    def __init__(self, board):
        self.grid = board
        self.R = len(self.grid)
        self.C = len(self.grid[0])

    def is_valid_coord(self,r,c):
    	return r in range(self.R) and c in range(self.C)

    def neighbour_coord(self, r,c):
    	n = []
    	if is_valid_coord(r-1,c):
    		n.append([r-1,c])
    	if is_valid_coord(r+1,c):
    		n.append([r+1,c])
    	if is_valid_coord(r,c+1):
    		n.append([r,c]+1)
    	if is_valid_coord(r,c-1):
    		n.append([r,c-1])
    	return n

    def 
    	


if __name__ == "__main__":
	with open('input.txt') as f:
		#board = []
		#for line in f.readlines():
		#	row = []
		#	line = line.strip()
		#	for x in line:
		#		row.append(int(x))
		#	board.append(row)
		#g = Grid(board)
		#print(g.grid)
		rows = [line.strip() for line in f.readline()]
	height_map = {}
	for y, row in enumerate(rows):
		for x, height in enumerate(row):
			height_map[(x,y)] = int(height)
	print(height_map)
