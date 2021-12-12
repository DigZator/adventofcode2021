with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

height_map = {}

for y, row in enumerate(lines):
	for x, height in enumerate(row):
		height_map[(x,y)] = int(height)

#print(height_map)
#print(height_map.items())
low = []

for coord, height in height_map.items():
	x,y = coord
	near = ((x+1,y),(x-1,y),(x,y+1),(x,y-1))
	small = True
	for adj in near:
		if height_map.get(adj, 10) <= height:
			small = False
			break
	if small:
		low.append(coord)

#print(low)

basin_sizes = []

for point in low:
	part = set([point])
	check = [point]
	while check:
		x, y = check.pop()
		near = ((x+1,y),(x-1,y),(x,y+1),(x,y-1))
		for adj in near:
			adj_height = height_map.get(adj, 0)
			if adj_height > height_map[(x,y)] and adj_height != 9:
				part.add(adj)
				check.append(adj)

	basin_sizes.append(len(part))

basin_sizes.sort(reverse = True)
#print(basin_sizes)
#print(basin_sizes[0],basin_sizes[1],basin_sizes[2])
print(basin_sizes[0]*basin_sizes[1]*basin_sizes[2])

