#!/usr/bin/env python
from continuous import *

a = float(raw_input("lower bound : "))
b = float(raw_input("upper bound : "))

dist = Uniform(a, b)
for i in range(int(a) - 5 , int(b) + 5) : 
	print("%d\t%0.4f\t%0.4f" % (i, dist.pdf(i), dist.cdf(i)))	

print("\nmean\t\t%0.4f\nvariance\t%0.4f" % (dist.mean(), dist.variance()))
