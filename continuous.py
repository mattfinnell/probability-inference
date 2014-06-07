'''
	Matt Finnell
	Thursday May 29th 2014

	Continuous Probability Package
		Contains 4 different classes of Continuous distributions

		Class Exponential
		Class Uniform
		Class StandardNormal
		Class Normal
		***Class T

'''
from math import * 

'''
Uniform Continuous Distribution
	Probably the simplest out of all distributions that are
	available. The Uniform Continuous Distribution offers the
	same probability over a range that is defined by the user.
'''
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
	
'''
Exponential continuous distribution.

	Quite a simple distribution that commonly measures decay,
	the implementation is based off of the standalone variable
	"theta" which places a weight on how skewed the distribution
	will turn out. 
'''
class Exponential :
	def __init__(self, theta) : 
		#cannot have a negative value for theta
		if not theta > 0.0 :
			print("theta value must greater than 0")
		else :
			self.theta = theta
		
	def pdf(self, x) :
		#cannot have a negative value for x
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


'''
Standard Normal Continuous Distribution
	Probably the most powerful there exists. Also known as the 
	Gaussian Distribution, this function is represented with a mean
	of zero as well as a standard deviation of 1. This is the very
	cannonicallized version of the Normal Distibution that is defined
	by the user's mean and standard deviation. 
'''
class StandardNormal : 
	Reciprocal = 1.0 / sqrt(2 * pi)

	def __init__(self) : 
		self.mean = 0
		self.variance = 1
	
	def pdf(self, z) : 
		return StandardNormal.Reciprocal * (e ** -(0.5 * z ** 2.0 ))
	
	#holy shit this function is rediculous on paper
	#...just look up Normal Distribution CDF
	def cdf(self, z) : 
		return 0.5 * (1 + erf(z / sqrt(2.0)))


'''
Normal Continuous Distribution
	The Bigger Brother of the standard normal Distribution. This 
	distribution requires custom inputs for the user's mean and 
	variance variables. These values can later on be converted over
	in terms for the Normal Standard Distribution, but on paper, it
	is nice to have the functionality to be able to select the 
	appropriate mean and variance values.
'''
class Normal :
	'implementation of the Normal Distribution'

	def __init__(self, mean, variance) :
		self.mean 		= mean
		self.variance 	= abs(variance)
	

	def cdf(self, x) :
		stdNorm = StandardNormal()
		z		= (x - self.mean) / sqrt(self.variance)
		return stdNorm.cdf(z)
		
