import numpy
import talib
from numpy import genfromtxt

my_data = genfromtxt('15minutes.csv', delimiter=',')
close = my_data[:,4]





moving_average = talib.SMA(close,timeperiod=10)

rsi = talib.RSI(close)

print(rsi)
