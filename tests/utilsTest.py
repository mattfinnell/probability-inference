#!/usr/bin/env python
from utils import *

print("n\tn!\t  nCr(10,n) nPr(10,n)")
for i in range(0, 10 + 1) :
	print("%d\t%d\t  %d\t    %d" % (i, factorial(i), nCr(10,i), nPr(10,i)))
