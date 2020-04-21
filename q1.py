for i in range(0,2):
	for j in range(1,6):
		if i == 0:
			print("*"*(j-i))
		if i != 0 and (6-j-i) != 0:
			print("*"*(6-j-i))

