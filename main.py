#!/usr/bin/env python
from binomial import *


#n = int(raw_input("enter population size: "))
#p = float(raw_input("enter probability val: "))

n = 4800
p = 0.0008333

binom = Binomial(n, p)
print("i\tpmf\tcdf")
#for i in range(n + 1) :
#	print("%d\t%0.4f\t%0.4f" % (i, binom.pmf(i), binom.cdf(i)))

print("4\t%0.4f\t0.04f" % (binom.pmf(4), binom.cdf(4)))

print("\nmean\t\t%0.4f\nvariance\t%0.4f" % (binom.mean(), binom.variance()))
