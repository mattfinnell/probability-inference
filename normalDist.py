'''
	Matt Finnell
	Friday June 6th 2014

	Normal Distribution Package
		Contains two classes regarding the Normal Distribution

		Class StandardNormal		--standard normal distribution
		Class Normal				--Normal dist with custom mean
										and variance.
'''

from math import *
from random import *

AREA_DETAIL = 10000000

class StandardNormal : 
	'implementation of the Standard Normal Distribution'

	Standard_Reciprocal = 1.0 / sqrt(2 * pi)

	def __init__(self) : 
		self.mean = 0
		self.variance = 1
	
	def pdf(self, z) : 
		return StandardNormal.Standard_Reciprocal * (e ** -(0.5 * z ** 2.0 ))
	
	def cdf(self, z) : 
		return 0.5 * (1 + erf(z / sqrt(2.0)))

class Normal :
	'implementation of the Normal Distribution'

	def __init__(self, mean, variance) :
		self.mean 		= mean
		self.variance 	= abs(variance)
	

	def cdf(self, x) :
		stdNorm = StandardNormal()
		z		= (x - self.mean) / sqrt(self.variance)
		return stdNorm.cdf(z)
