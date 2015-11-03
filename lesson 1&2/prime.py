def isPrime(num):
	for a in range(num - 1,1,-1):
		if num%a == 0:
			return 0
	return 1

print isPrime(3)
print isPrime(5)
print isPrime(6)
print isPrime(17)