class DataSet :
	# accept data as size 2 tuples
	def __init__(self, Data) :
		self.data = Data
		self.dataLen = len(Data)
		self._Sxy = None
		self._Sxx = None
		self._Bintercept = None
		self._Bslope = None

	def Sxy(Self) :
		if not Self._Sxy :
			prodSum = 0.0
			xSum = 0.0
			ySum = 0.0

			for i in range(0, Self.dataLen) :
				prodSum += float(Self.data(i, 0)) * float(Self.data(i, 1))
				xSum    += float(Self.data(i, 0))
				ySum    += float(Self.data(i, 1))

			Self._Sxy = prodSum - (1.0 / float(Self.dataLen)) * xSum * ySum

		return Self._Sxy

	def Sxx(Self) : 
		if not Self._Sxx :
			squareSum = 0.0
			normalSum = 0.0

			for i in range(0, Self.dataLen) :
				x = float(Self.data(i, 0))
				squareSum += x ** 2.0
				normalSum += x

			Self._Sxx = squareSum - (1.0 / float(Self.dataLen)) * (normalSum ** 2.0)

		return Self._Sxx
	
	def Bslope(Self) :
		if not Self._Bslope :
			Self._Bslope = Self.Sxy() / Self.Sxx()

		return Self._Bslope
	
	def Bintercept(Self) :
		if not Self._Bintercept :
			Self._Bintercept = Self.dataYAvg() + Self.Bslope() * Self.XAvg()
