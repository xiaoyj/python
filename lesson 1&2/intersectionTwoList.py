def intersection(a,b):
	c=[]
	for i in a:
		for j in b:
			if i == j :
				c.append(i)
				continue
	return c

a=[1,4,8,3]
b=[3,9,1,0,12]
print intersection(a,b)