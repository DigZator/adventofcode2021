if __name__ == "__main__":
	with open('input.txt') as f:
		crab_loc = []
		crab_loc = [int(x) for x in f.readline().split(",")]
		#print(crab_loc)
		most = max(crab_loc)
		least = min(crab_loc)
		#print(most,least)
		dis = 99999999999
		for i in range(least, most):
			dist = sum(((abs(i-d)*(abs(i-d)+1))/2) for d in crab_loc)
			if dis > dist:
				dis = dist

		print(dis)