#!/usr/bin/env python
from poisson import *

n = 500
p = 0.0034

dist = binomial(n,p)
for i in range(0, 10) :
	print("%d\t%d" % (i * 50, )
