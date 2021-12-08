if __name__ == "__main__":
	with open('input.txt') as f:
		lanternfish = []
		lanternfish = f.readline().split(",")
		for i in range(len(lanternfish)):
			lanternfish[i] = int(lanternfish[i])
		print(lanternfish)

		day = 0
		for day in range(80):
			#day += 1
			for i in range(len(lanternfish)):
				lanternfish[i] -= 1
				if (lanternfish[i] < 0):
					lanternfish[i] = 6
					lanternfish.append(8)
			print("After Day ", day, ":", lanternfish)
		print(len(lanternfish))