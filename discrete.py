'''
	Matt Finnell
	Thursday May 29th 2014

	Discrete Probablility Package
		Contains 3 different classes of Discrete distributions
	
		Class Bernoulli
		Class Binomial
		Class Poisson
'''

import math
from utils import *

'''
Bernoulli Discrete Distribution
	A very simple and slightly impractical distribution that just measures
	the probability of one event turning out to be true or false...
'''
class Bernoulli:

	def __init__(self, myP):
		if 0.0 <= myP and myP <= 1.0 :
			self.p = myP
		else :  
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

'''
Binomial Discrete Distribution
	Simple but powerful distribution that measures the probability of 
	sequences of "success / fail" events. all the user has to do is 
	input the probability of "success" and the number of trials to be 
	calculated from the set. 

	The CDF of this function measures out the probability of x successes
	from n trials with a probability of p

	The awesome part of this function, is that I have it triggered so that
	as the number of trials increases beyond 100 and the probability is
	less than 1% it will transfer over to a poisson approximation model.
	Which does a much faster and better job of estimating the situation
	because it factors in one input variable "theta" that considers
	a convergence of trial_count*probability. 
'''
class Binomial:
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
		
		#Trigger Poisson given the conditions that p <= 0.01 and n >= 100
		if self.p <= 0.01 and self.n >= 100 :
			self.poisson = Poisson(self.p * self.n)
		else :
			self.poisson =  None
	
	def pmf(self, x):
		if x >= 0 and x <= self.n :
			if self.poisson is None :
				return nCr(self.n, x) * self.p**x * (1.0 - self.p)**(self.n - x)

			#poisson trigger
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

'''
Poisson Discrete Approximation
	Simple Distribution that Approximates the Binomial Distribution.
'''
class Poisson:
	def __init__(self, _lambda):
		self._lambda = _lambda
	
	def pmf(self, x):
		return math.e**(-self._lambda) * ((self._lambda**x) / float(factorial(x)))
	
	def cdf(self, x):
		ret = 0.0
		for i in range(0, x + 1) :
			ret += self.pmf(i)

		return ret

	def mean(self):
		return self._lambda

	def variance(self):
		return self._lambda

def negativeBinomialPDF(x,r,p) :
	x = float(x)
	r = float(r)
	p = float(p)

	return nCr(x + r - 1, x) * (1.0 / ((p ** -1.0 ) ** (x + r)))

def negativeBinomialCDF(r,p,n) :
	val = 0.0

	for i in range(0, n + 1) :
		val += negativeBinomialPDF(i,r,p)
	
	return val

for i in range(0, 6) :
	print "pdf(%d)" % (i), "-->", negativeBinomialPDF(i, 3, 0.5)

print 1 - negativeBinomialCDF(3, 0.5, 5)


		
