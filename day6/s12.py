if __name__ == "__main__":
	with open('input.txt') as f:
		lanternfish = []
		lanternfish = f.readline().split(",")
		for i in range(len(lanternfish)):
			lanternfish[i] = int(lanternfish[i])
		print(lanternfish)

		tank = {x : 0 for x in range(9)}

		for fish in lanternfish:
			tank[fish] += 1
		print(tank)
		day = 0

		for day in range(256):
			new_tank = {x : 0 for x in range(9)}
			for key in tank.keys():
				new_tank[key-1] = tank[key]
			new_tank[8] = new_tank[-1]
			new_tank[6] += new_tank[-1]
			del new_tank[-1]
			tank = new_tank
			print("After Day ", day, ":", tank)
		fishes = (sum(tank[k] for k in tank.keys()))
		print(fishes)