num3 = 0
for num1 in range(1000000,0,-1):
	origin = num1
	palidrome  = 0
	while origin != 0:
		palidrome = palidrome * 10 + origin % 10
		origin /= 10
	if palidrome == num1:
		for num2 in range(999,0,-1):
			if num1%num2 == 0:
				num3 = num1/num2
				if num3<1000:
					print 'the max palidrome is ',num1,'=',num2,'*',num3
					break
	if num3 != 0 and num3 < 1000:
		break