if __name__ == "__main__":
	with open('input.txt') as f:
		add = 0

		for line in f.readlines():
			#print(line)
			top, mid, bot = '', '', ''
			topright, topleft = '', ''
			botright, botleft = '', ''
			data, num = line.split(" | ")
			num = num.strip().split()
			data = data.split()
			#print(data, num)
			topright = [dig for dig in data if len(dig) == 2][0]
			botright = topright
			#print(topright,botright)
			hold = [dig for dig in data if len(dig) == 3][0]
			hold = hold.replace(topright[0],'')
			top = hold.replace(topright[1],'')
			#print(top)
			hold = [dig for dig in data if len(dig) == 4][0]
			hold = hold.replace(topright[0],'')
			hold = hold.replace(topright[1],'')
			topleft = hold
			mid = hold
			hold = [dig for dig in data if len(dig) == 5]
			#print(hold)
			for i in range(len(hold)):
				rm_let = [top, topleft[0], topleft[1]]
				for let in rm_let:
					hold[i] = hold[i].replace(let,'')
			hold = [hol for hol in hold if len(hol) == 2][0]
			#0print(hold)
			if hold.find(topright[0]) != -1:
				botright = topright[0]
				topright = topright[1]
			else:
				botright = topright[1]
				topright = topright[0]
			#print(topright,botright)
			bot = hold.replace(botright,'')
			#print(bot)
			hold = [dig for dig in data if len(dig) == 7][0]
			rm_let = [top, topright, botright, bot, topleft[0], topleft[1]]
			for let in rm_let:
				hold = hold.replace(let, '')
			botleft = hold
			hold = [dig for dig in data if len(dig) == 5]
			for i in range(len(hold)):
				rm_let = [top, bot, topright, botright, botleft]
				#print(rm_let)
				for let in rm_let:
					hold[i] = hold[i].replace(let,'')
			mid = [let for let in hold if len(let) == 1][0]
			#print(mid)
			for i in range(len(hold)):
				hold[i] = hold[i].replace(mid, '')
			topleft = [let for let in hold if len(let) == 1][0]
			#print(topleft)
			decode = 0
			for dig in num:
				if len(dig) == 2:
					decode = decode*10 + 1
				if len(dig) == 3:
					decode = decode*10 + 7
				if len(dig) == 4:
					decode = decode*10 + 4
				if len(dig) == 7:
					decode = decode*10 + 8
				if len(dig) == 5:
					if ((dig.find(botright) != -1) and (dig.find(topright) != -1)):
						decode = decode*10 + 3
					elif ((dig.find(botright) != -1) and (not (dig.find(topright) != -1))):
						decode = decode*10 + 5
					elif ((not (dig.find(botright) != -1)) and (dig.find(topright) != -1)):
						decode = decode*10 + 2
				if len(dig) == 6:
					if (dig.find(topright) == -1):
						decode = decode*10 + 6
					elif (dig.find(mid) == -1):
						decode = decode*10 + 0
					elif (dig.find(botleft) == -1):
						decode = decode*10 + 9
			#print(num, decode)
			add = add + decode
		print(add)