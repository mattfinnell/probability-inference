from linearRegression import *
from datasets import *

ch10 = DataSet(Mileage, GrooveDepth)
ex12 = DataSet(x, y)
hw6 = DataSet(Pressure, BoilingPt)
hw7 = DataSet(Year, Time)

OldFaithful = DataSet(LAST, NEXT)
IMR = DataSet(IMR_Year, IMR_rate)
retention = DataSet(MEM_p, [math.log(datum) for datum in MEM_t])
