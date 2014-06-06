#!/usr/bin/env python
from normalDist import *

dist = Normal(3,16)
'''
neg_two = norm.pdf(-2)
minus 	= norm.pdf(-1)
zero	= norm.pdf(0)
plus	= norm.pdf(1)
pos_two = norm.pdf(2)
'''

print dist.cdfLessThan(3)
