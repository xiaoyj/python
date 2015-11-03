def judgeSum(a):
	sum = 0
	for i in a:
		for j in range (len(a)-i,len(a),1):
			if i+j==10:
				sum += 1
	return sum

print judgeSum([2,9,3,1,4,7])