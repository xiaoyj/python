def findString(a):
	x = {}
	for i in range(0,len(a)):
		x.setdefault(a[i],0)
		x[a[i]] += 1
	maxC = 0
	maxLetter = a[0]
	for k in x.keys():
		if(maxC <= x[k]):
			maxC = x[k]
			maxLetter = k
	return maxC,maxLetter

print findString("abdueubxuuq82jxnHuu") 