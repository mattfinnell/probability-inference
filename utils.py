def factorial(x):
	if x > 1 :
		return x * factorial(x - 1)
	else :
		return 1

def nCr(n, r):
	return factorial(n) / (factorial(r) * factorial(n - r))

def nPr(n, r):
	return factorial(n) / factorial(n-r)
