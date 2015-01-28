from scipy import stats
import math

class DataSet :
	# accept data as size 2 tuples
	def __init__(self, Data) :
		self.data = Data
		self.dataLen = len(Data)

		# Data attributes that require series calculations
		self._dataXSum = None
		self._dataYSum = None
		self._XSumSquare = None
		self._Sxy = None
		self._Sxx = None
		self._Syy = None
	
	def dataXSum(self) :
		if not self._dataXSum :
			total = 0.0
			for i in range(0, self.dataLen) :
				total += self.data[i][0]

			self._dataXSum = total

		return self._dataXSum
	
	def dataYSum(self) : 
		if not self._dataYSum :
			total = 0.0
			for i in range(0, self.dataLen) :
				total += self.data[i][1]

			self._dataYSum = total

		return self._dataYSum
	
	def dataXAvg(self) : 
		return (1.0 / float(self.dataLen)) * self.dataXSum()

	def dataYAvg(self) : 
		return (1.0 / float(self.dataLen)) * self.dataYSum()
				
	def Sxy(self) :
		prodSum = 0.0

		for i in range(0, self.dataLen) :
			prodSum += float(self.data[i][0]) * float(self.data[i][1])

		return  prodSum - (1.0 / float(self.dataLen)) * self.dataXSum() * self.dataYSum()


	def Sxx(Self) : 
		if not Self._Sxx :
			squareSum = 0.0
			normalSum = 0.0

			for i in range(0, Self.dataLen) :
				x = float(Self.data[i][0])
				squareSum += x ** 2.0
				normalSum += x

			Self._Sxx = squareSum - (1.0 / float(Self.dataLen)) * (normalSum ** 2.0)

		return Self._Sxx

	def Syy(self) : 
		if not self._Syy :
			squareSum = 0.0

			for i in range(0, self.dataLen) :
				x = float(self.data[i][1])
				squareSum += x ** 2.0

			self._Syy = squareSum - (1.0 / float(self.dataLen)) * (self.dataYSum()** 2.0)

		return self._Syy
	
	def SST(self) :
		return self.Syy()
	
	def SSR(self) :
		return (self.Bslope() ** 2.0) * self.Sxx()
	
	def SSE(self) :
		return self.SST() - self.SSR()
	
	def Bslope(Self) :
		return Self.Sxy() / Self.Sxx()

	
	def Bintercept(Self) :
			return  Self.dataYAvg() - Self.Bslope() * Self.dataXAvg()

	def Regression(Self) :
		return "Y_hat = %f + %fx" % (Self.Bintercept(), Self.Bslope())
	
	def Expected(Self, x_hat) :
		return Self.Bintercept() + Self.Bslope() * float(x_hat)
	
	def detCoefficient(self) :
		return (self.Sxy() ** 2.0) / (self.Sxx() * self.Syy())
	
	def Correlation(self) :
		correlation = math.sqrt(self.detCoefficient())

		if self.Bslope() < 0.0 :
			self._correlation = -1.0 * correlation

		return self._correlation
	
	def regressionDeviation(self) :
		df = float(self.dataLen - 2)
		return math.sqrt(self.SSE() / df)
	
	def dataXSumSquare(self) :
		if not self._XSumSquare :
			total = 0.0

			for i in range(0, self.dataLen) :
				total += self.data[i][0] ** 2

			self._XSumSquare = total
		return self._XSumSquare

	def BinterceptStdError(self) :
		return self.regressionDeviation() * math.sqrt(self.dataXSumSquare() / (float(self.dataLen) * self.Sxx()))

	def BslopeStdError(self) :
		return self.regressionDeviation() / math.sqrt(self.Sxx())
	
	def TwoTailCI_slope(self, alpha) :
		error = stats.t.ppf(1.0 - float(alpha) / 2.0, self.dataLen - 2) * self.BslopeStdError()
		slope = self.Bslope()

		return (slope - error, slope + error)
	
	# Return True to reject the null hypothesis
	def TwoTailTest_slope(self, nullEstimate,  alpha) :
		t = (self.Bslope() - float(nullEstimate)) / self.BslopeStdError()
		t_test = stats.t.ppf(1.0 - float(alpha) / 2.0, self.dataLen - 2) * self.BslopeStdError()

		if abs(t) > t_test :
			return True
		return False
	
	def OneTailTest_slope(self, nullEstimate, alpha) :
		t = (abs(self.Bslope()) - float(nullEstimate)) / self.BslopeStdError()
		t_value = stats.t.ppf(1.0 - float(alpha) / 2.0, self.dataLen - 2) * self.BslopeStdError()

		if t >= t_value : 
			return True 
		return False 

	def MSR(self) :
		return self.SSR()

	def MSE(self) :
		return self.SSE() / float(self.dataLen - 2)

	def predictionInterval(self, x, alpha) :
		x        = float(x)
		x_diff   = ((x - self.dataXAvg()) ** 2.0) / self.Sxx()
		t_value  = stats.t.ppf(1.0 - float(alpha) / 2.0, self.dataLen - 2)
		error    = self.regressionDeviation() * math.sqrt(1 + (1.0 / float(self.dataLen)) + x_diff)
		expected = self.Expected(x)

		return (expected - t_value * error, expected + t_value * error)
	
	def outliers(self) :
		outliers = []
		s = self.regressionDeviation()
		a = 1
		b = 1.0 / float(self.dataLen)

		for i in range(0, self.dataLen) :
			e = self.data[i][1] - self.Expected(i)

			c = (self.data[i][0] - self.dataXAvg()) ** 2.0
			c /= self.Sxx()

			e_star = e / (s * math.sqrt(a - b - c))

			print abs(e_star)

			if abs(e_star) > 2.0 :
				outliers.append(i)

		return outliers

testData = [(0, 394.33),(4, 329.50),(8, 291.00),(12,255.17),(16,229.33),(20,204.83),(24,179.0),(28,163.83),(32,150.33)]
test = DataSet(testData)
print test.OneTailTest_slope(8, 0.05)
print test.predictionInterval(25, 0.05)
print test.outliers()
