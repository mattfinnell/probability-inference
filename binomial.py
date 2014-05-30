from utils import nCr
from poisson import *

class Binomial:
	'implementation of the Binomial Distribution'

	def __init__(self, n, p):
		if 0.0 <= p and p <= p :
			self.p = p
		else:
			print("invalid binomial probability value");
			return 0.0

		if n >= 0:
			self.n = n
		else:
			print("invalid binomial N value")
			return 0

		if self.p <= 0.01 and self.n >= 100 :
			self.poisson = Poisson(self.p * self.n)
		else :
			self.poisson =  None

	def pmf(self, x):
		if x >= 0 and x <= self.n :
			if self.poisson is None :
				return nCr(self.n, x) * self.p**x * (1.0 - self.p)**(self.n - x)
			else :
				return self.poisson.pmf(x)

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
		if self.poisson is None :
			return self.n * self.p * (1 - self.p)
		else :
			return self.poisson.variance()
