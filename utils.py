'''
	Matt Finnell
	Thursday May 29th 2014

	Utility package
		Contains multiple functions that primarily work off of discrete
		values. All elemementary enumeration functions 

		function	factorial
		function	nCr
		function	nPr
'''
#  simple factorial function. Not recursive due to stack overflows =P
def factorial(x):
	if x > 1 :
		return x * factorial(x - 1)
	else :
		return 1

#  n Choose r Function. n items, select 4. Order doesn't matter (set), 
#   no replacement
def nCr(n, r):
	return factorial(n) / (factorial(r) * factorial(n - r))

#  n Permutate r Function. n items, select 4. Order Matters (tuple),
#   no replacement
def nPr(n, r):
	return factorial(n) / factorial(n-r)
