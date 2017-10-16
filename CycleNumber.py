import math

class Cicobject):
	"""docstring for ClassName"""
	def __init__(self, num):
		super(ClassName, self).__init__()
		self.num = num

	def isPrimeNumber(self,n):
		if n<2:
			return False;
		for i in range(2,int(math.sqrt(n))+1):
			if n%i==0:
				return False
		return True

	def number151(self):
		global sum
		sum = 367
		while self.num<150:
			sum+=186
			if self.isPrimeNumber(sum):
				self.num+=1
				continue
		return sum

test = ClassName(0)