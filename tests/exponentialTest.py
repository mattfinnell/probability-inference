#!/usr/bin/env python
from continuous import *

theta = float(raw_input("theta value : "))
n = float(raw_input("point of interest : "))
dist = Exponential(theta)
print(dist.cdf(n))
