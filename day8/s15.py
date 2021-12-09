if __name__ == "__main__":
	with open('input.txt') as f:
		count = 0
		for line in f.readlines():
			data, num = line.split(" | ")
			num = num.strip().split()
			for dig in num:
				if ((len(dig) == 2) or (len(dig) == 3) or (len(dig) == 4) or (len(dig) == 7)):
					count += 1
		print(count)
