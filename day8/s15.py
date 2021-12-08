if __name__ == "__main__":
	with open('input.txt') as f:
		seg_dig = {'a':[0,2,3,5,6,7,8,9],
				   'b':[0,4,5,6,8,9],
				   'c':[0,1,2,3,4,7,8,9],
				   'd':[2,3,4,5,6,8,9],
				   'e':[0,2,6,8],
				   'f':[0,1,3,4,5,6,7,8,9],
				   'g':[0,2,3,5,6,8,9]}
		dig_seg = {0:['a', 'b', 'c', 'e', 'f', 'g'], #6
				   1:['c', 'f'], #2
				   2:['a', 'c', 'd', 'e', 'g'], #5
				   3:['a', 'c', 'd', 'f', 'g'], #5
				   4:['b', 'c', 'd', 'f'], #4
				   5:['a', 'b', 'd', 'f', 'g'], #5
				   6:['a', 'b', 'd', 'e', 'f', 'g'], #6
				   7:['a', 'c', 'f'], #3
				   8:['a', 'b', 'c', 'd', 'e', 'f', 'g'], #7
				   9:['a', 'b', 'c', 'd', 'f', 'g']} #6

		count = 0
		for line in f.readlines():
			#print(line)
			data, num = line.split(" | ")
			num = num.strip().split()
			#print(num)
			for dig in num:
				if ((len(dig) == 2) or (len(dig) == 3) or (len(dig) == 4) or (len(dig) == 7)):
					count += 1
					#print(dig)
		print(count)
