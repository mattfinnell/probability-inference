import ch11datasets as ds
import numpy as np

class DataSet :
	def __init__(self, Xtable, Y) :
		self.X = Xtable
		self.Y      = Y
	
	def fn(self, function, *args) :
		return function(self.X, self.Y, *args)

	
def beta_values(X, y) :
	values = (X.transpose() * X).I * X.transpose() * y
	return [values.item((i,0)) for i in range(0, values.size)]

def expected(X, y, x) :
	betas = beta_values(X, y)
	x = np.float64(x)

	return betas[0] + sum([betas[i] * x ** np.float64(i) for i in range(1, len(betas))])

def error(X, y, i) :
	return y.item((i, 0)) - expected(X, y, X.item((i, 1)))

def SSE(X, y) :
	return sum([error(X,y,i)**2.0 for i in range(0, X.shape[0])])

	
d = DataSet(ds.X, ds.y)
print d.fn(SSE)
