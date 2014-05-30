#!/usr/bin/env python
from discrete import *


n = int(raw_input("enter population size: "))
p = float(raw_input("enter probability val: "))
binom = Binomial(n, p)

max_loop = 25
if n > max_loop :
	n = max_loop

print("i\tpmf\tcdf")
for i in range(n + 1) :
	print("%d\t%0.4f\t%0.4f" % (i, binom.pmf(i), binom.cdf(i)))
