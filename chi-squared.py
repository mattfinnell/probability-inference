from scipy import stats
import numpy

mean = 0.519

observed = [678, 227, 56, 28, 8, 14]

#Build the expected observations
expected = [stats.geom.pmf(i, mean) for i in range(1,6)]
expected.append(1 - sum(expected))
expected = [i * 1011 for i in expected]

print expected

print stats.chisquare(numpy.array(observed), numpy.array(expected))
