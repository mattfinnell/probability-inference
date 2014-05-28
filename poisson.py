from math import e

class Poisson(Binomial):
	'implementation of the Poisson Distribution'
	def __init__(self):
		if Parent.n >= 100 and Parent.p <= 0.01 and Parent.p >= 0.0:
			_lambda = Parent.n * Parent.p
		else:
			_lambda = None
	
	def pmf(self, x):
		if self._lambda is not None and x > 0:
			return math.e**(-self._lambda) * ((self._lambda**x) / factorial(x))
		elif self._lambda is not None and not x > 0:
			print("cannot have a negative pmf input x for poisson processes")
			return 0
		else:
			return Parent.pmf(x)

	def mean(self):
		return self._lambda

	def variance(self):
		return self._lambda
