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

	Standard_Reciprocal = 1 / sqrt(2 * pi)

	def __init__(self) : 
		self.mean = 0
		self.variance = 1
	
	def pdf(self, z) : 
		return StandardNormal.Standard_Reciprocal * (e ** -( (1.0 / 2.0) * z ** 2.0 ))
	
	def cdfLessThan(self, z) :
		hits = 0

		for i in range(0, AREA_DETAIL) :
			x = uniform(-6, 6)
			y = uniform(0, StandardNormal.Standard_Reciprocal)
			if x < z and y < self.pdf(z) :
				hits += 1

		return float(hits)/ float(AREA_DETAIL)

class Normal :
	'implementation of the Normal Distribution'

	def __init__(self, mean, variance) :
		self.mean 		= mean
		self.variance 	= abs(variance)
	
	def cdfLessThan(self, x) :
		stdNorm = StandardNormal()
		z 		= (x - self.mean) / sqrt(self.variance)
		return stdNorm.cdfLessThan(z)
