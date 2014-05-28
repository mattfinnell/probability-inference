class Bernoulli:
	'implementation of the Bernoulli distribution'

	def __init__(self, myP):
		if 0.0 <= myP and myP <= 1.0 :
			self.p = myP
		else 
			print("invalid bernoulli value")

	def pmf(self, x):
		if x == 0 or x == 1:
			return self.p**x * (1.0 - self.p)**(1 - x)
		print("x value is not contained within bernoulli range of {0,1}")
		return 0.0
	
	def mean(self):
		return self.p
	
	def variance(self):
		return self.p * (1.0 - self.p)
