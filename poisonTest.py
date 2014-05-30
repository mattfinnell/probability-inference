#!/usr/bin/env python
from poisson import *

n = 200
p = 0.01

dist = Poisson(n*p)
print(dist.pdf(1))
