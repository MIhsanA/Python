def decimal_to_binary(num):
	quot = int(num)
	base = 0
	counter = 0
	binary=[]
	while (quot > 0):
		rem = quot%2
		binary.append(str(rem))
		quot = quot//2
		counter +=1

	binary.reverse()
	return(int(''.join(binary)))