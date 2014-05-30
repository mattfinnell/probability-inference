import math
from utils import factorial

class Poisson:
	'implementation of the Poisson Distribution'
	def __init__(self, _lambda):
		print("using poisson approximation")
		self._lambda = _lambda
	
	def pmf(self, x):
		return math.e**(-self._lambda) * ((self._lambda**x) / factorial(x))

	def mean(self):
		return self._lambda

	def variance(self):
		return self._lambda
