def getSum(num):
	count = 0;
	for x in range(len(num)):
		for y in range(len(num) - x):
			if num[x]+num[y]>10:
				count+=1;
	return count

a=[1,4,8,10,10]
print getSum(a)
