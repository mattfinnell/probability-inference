'''
	Matt Finnell
	Thursday May 29th 2014

	Continuous Probability Package
		Contains 2 different classes of Continuous distributions

		Class Exponential
		Class Uniform
'''

import math

class Exponential :
	def __init__(self, theta) : 
		if not theta > 0.0 :
			print("theta value must greater than 0")
		else :
			self.theta = theta
	
	def pdf(self, x) :
		if float(x) > 0.0 :
			return (1.0 / self.theta) * math.e**(-x / self.theta)
		else :
			return 0.0
	
	def cdf(self, x) :
		if float(x) > 0.0 :
			return 1.0 - math.e**(-x / self.theta)
		else : 
			return 0.0
	
	def mean(self) :
		return self.theta
	
	def variance(self) :
		return self.theta**2.0


class Uniform :
	def __init__(self, a, b) :
		if a < b :
			self.a = float(a)
			self.b = float(b)
		else : 
			self.a = float(b)
			self.b = float(a)
	
	def pdf(self, x) :
		if self.a <= x and x <= self.b :
			return 1 / (self.b - self.a)
		else :
			return 0
	
	def cdf(self, x) :
		if x < self.a :
			return 0
		elif self.a <= x and x < self.b :
			return (x - self.a) / (self.b - self.a)
		else :
			return 1
	
	def mean(self) :
		return (self.b + self.a) / 2
	
	def variance(self) :
		return (self.b - self.a)**2 / 12
		
