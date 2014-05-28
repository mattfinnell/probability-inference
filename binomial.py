from utils import nCr

class Binomial:
	'implementation of the Binomial Distribution'

	def __init__(self, myN, myP):
		if 0.0 <= myP and myP <= 1.0 :
			self.p = myP
		else:
			print("invalid binomial probability value");
			return 0.0

		if myN >= 0:
			self.n = myN
		else:
			print("invalid binomial N value")
			return 0;

	def pmf(self, x):
		if x >= 0 and x <= self.n :
			return nCr(self.n, x) * self.p**x * (1.0 - self.p)**(self.n - x)
		print("invalid value for x. 0 <= x <= n")
		return 0

	def cdf(self, x):
		if x >= 0 and x <= self.n :
			ret = 0.0
			for i in range(0, x + 1) :
				ret += self.pmf(i)

			return ret
		print("invalid value for x. 0 <= x <= n")
		return 0;

	def mean(self):
		return self.n * self.p
	
	def variance(self):
		return self.n * self.p * (1 - self.p)
