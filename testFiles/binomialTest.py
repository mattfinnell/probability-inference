#!/usr/bin/env python
from binomial import *

n1 = 10
p1 = 0.5
x1 = 6

b1 = Binomial(n1, p1)


for n in range(0, n1 + 1):
	print("b(%d, %0.3f)\tf(%d)\t%0.4f" % (n1, p1, n, b1.pmf(n)))

print("cdf\t\t%0.4f" % (b1.cdf(5)))
print("mean\t\t%0.4f\nvariance\t%0.4f" % (b1.mean(), b1.variance())) 
