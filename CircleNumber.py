import math

class CircleNumber(object):
	"""docstring for ClassName"""
	def __init__(self, start,end):
		super(CircleNumber, self).__init__()
		self.start = start
		self.end = end

	def circleTime(self,num):
		time=0
		while num!=1:
			if num%2==1:
				num=num*3+1
			else:
				num/=2
			time+=1
		return time

	def findMaxTime(self):
		maxTime = 0;
		while self.start<self.end+1:
			if maxTime<self.circleTime(self.start):
				maxTime=self.circleTime(self.start)
			self.start+=1
		return maxTime

test = CircleNumber(900,1000)
print test.findMaxTime()+1