#!/usr/bin/env python
from discrete import *

p1 = 0.75
p2 = 0.50
p3 = 0.462

_pass = 1
_fail = 0
error = 3

b1 = Bernoulli(p1)
b2 = Bernoulli(p2)
b3 = Bernoulli(p3)
print("bernoulli(%0.3f, %d)\t%0.4f" % (p1, _pass, b1.pmf(_pass)))
print("bernoulli(%0.3f, %d)\t%0.4f" % (p1, _fail, b1.pmf(_fail)))
print("bernoulli(%0.3f, %d)\t%0.4f" % (p2, _pass, b2.pmf(_pass)))
print("bernoulli(%0.3f, %d)\t%0.4f" % (p2, _fail, b2.pmf(_fail)))
print("bernoulli(%0.3f, %d)\t%0.4f" % (p3, _pass, b3.pmf(_pass)))
print("bernoulli(%0.3f, %d)\t%0.4f" % (p3, _fail, b3.pmf(_fail)))
print("bernoulli(%0.3f, %d)\t%0.4f" % (p3, error, b3.pmf(error)))
