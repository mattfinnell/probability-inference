from scipy import stats
import numpy
import math

class DataSet :
	def __init__(self, X, Y) :
		self.X = X
		self.Y = Y
	
	def fn(self, function, *args) :
		return function(self.X, self.Y, *args)

def Sss(X, Y) :
	return numpy.float64(sum([X[i] * Y[i] - mean(X) * mean(Y) for i in range(0, len(X))]))

def Sxx(X, Y) :
	return Sss(X,X)

def Syy(X, Y) :
	return Sss(Y, Y)

def Sxy(X, Y) :
	return Sss(X, Y)

def mean(X) :
	return (numpy.float64(1.0) / numpy.float64(len(X))) * numpy.float64(sum(X))

def slope(X, Y) :
	return Sss(X, Y) / Sss(X, X)

def intercept(X, Y) :
	return mean(Y) - slope(X,Y) * mean(X)

def expected(X, Y, x) :
	return intercept(X, Y) + slope(X, Y) * x 

def residuals(X, Y) :
	return [Y[i] - expected(X, Y, X[i]) for i in range(0, len(Y))]

def SST(X, Y) :
	return Sss(Y, Y)

def SSR(X, Y) :
	return (slope(X, Y) ** 2.0) * Sss(X, X)

def SSE(X, Y) :
	return SST(X, Y) - SSR(X, Y)

def rsquared(X, Y) :
	return 1 - SSE(X, Y) / SST(X, Y)

def r(X, Y) :
	rVal = math.sqrt(rsquared(X, Y))
	if slope(X, Y) < 0.0 :
		rVal *= -1.0
	
	return rVal

def variance(X, Y) :
	return SSE(X, Y) / numpy.float64(len(X) - 2)

def interceptError(X, Y) :
	dev = numpy.float64(math.sqrt(variance(X, Y)))
	a   = sum(X[i] * X[i] for i in range(0, len(X)))
	b   = len(X) * Sss(X,X)

	return dev * numpy.float64(math.sqrt(a / b))

def slopeError(X, Y) :
	dev = numpy.float64(math.sqrt(variance(X, Y)))
	return dev / numpy.float64(math.sqrt(Sss(X, X)))

def slopeCI(X, Y, alpha) :
	s = slope(X, Y)
	diff = abs(stats.t.ppf(alpha / 2.0, len(X) - 2)) * slopeError(X, Y)
	return (s - diff, s + diff)

def interceptCI(X, Y, alpha) :
	i = intercept(X, Y)
	diff = abs(stats.t.ppf(alpha / 2.0, len(X) - 2)) * interceptError(X, Y)
	return (i - diff, i + diff)

def slopeHypothesis(X, Y, null, alpha) :
	diff = abs((slope(X, Y) - numpy.float64(null))) / slopeError(X, Y)
	test = abs(stats.t.ppf(alpha / 2.0, len(X) - 2))

	if diff > test :
		return True
	
	return False

def MSR(X, Y) :
	return SSR(X, Y)

def MSE(X, Y) :
	return SSE(X, Y) / numpy.float64(len(X) - 2)

def ANOVA(X, Y) :
	print "(Source, SS, df, MS, F)"
	print "Regression", SSR(X, Y), " ", 1, " ", MSR(X, Y), " ", MSR(X,Y) / MSE(X,Y)
	print "Error     ", SSE(X, Y), " ", len(X) - 2, " ", MSE(X,Y)
	print "Total     ", SST(X, Y), " ", len(X) - 1

def predictionInterval(X, Y, x, alpha) :
	expect = expected(X, Y, numpy.float64(x))
	tstat  = abs(stats.t.ppf(alpha / 2.0, len(X) - 2))
	dev    = numpy.float64(math.sqrt(variance(X, Y)))
	a      = 1.0 / numpy.float64(len(X))
	b      = ((numpy.float64(x) - mean(X)) ** 2.0) / Sss(X,X)
	diff   = tstat * dev * math.sqrt(1 + a + b)

	return (expect - diff, expect + diff)

def standardResiduals(X, Y) :
	dev = math.sqrt(variance(X,Y))
	return [residuals(X, Y)[i] / (dev * math.sqrt(1 - leverage(X, Y, i))) for i in range(0, len(X))]

def outliers(X, Y) :
	return [i for i in range(0, len(X)) if standardResiduals(X,Y)[i] > 2.0]

def leverage(X, Y, i) :
	return (1.0 / numpy.float64(len(X))) + ((X[i] - mean(X)) ** 2.0) / Sss(X, X)

def influentials(X, Y) :
	threshold = 2.0 * (2.0) / float(len(X))
	return [i for i in range(0, len(X)) if leverage(X,Y,i) > threshold]
