#!/usr/bin/env python
from poisson import *

_lambda = float(raw_input("error mean : "))
i = int(raw_input("error count : "))

dist = Poisson(_lambda)
print(dist.pmf(i))
