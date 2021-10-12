#!/usr/bin/python3
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
from scipy import interpolate

xdata=pd.read_csv('./after.csv', encoding='gbk')
xdata.columns = ['采样值']

xdata_1=xdata.loc[:, '采样值']

ydata=pd.read_csv('./after2.csv', encoding='gbk')
#ydata=pd.read_csv('./after2.csv', encoding='gbk', skiprows=52)
ydata.columns = ['采样值']

ydata_1=ydata.loc[:, '采样值']

xdata_2 = xdata_1.describe()

ydata_2 = ydata_1.describe()

print(xdata_2)

print(ydata_2)

#x1=np.linspace(1, 24, 24)
#x_new=np.linspace(1, 80, 80)
#tck=interpolate.splrep(x1, xdata_1)
#xdata_rep=interpolate.splev(x_new, tck)
                          
plt.figure(1)

plt.plot(xdata_1, '*')
plt.plot(ydata_1, '*')

plt.gcf().autofmt_xdate()
plt.show()
