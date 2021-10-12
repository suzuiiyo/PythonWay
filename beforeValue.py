#!/usr/bin/python3
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

xdata=pd.read_csv('./before.csv')
xdata.columns = ['采样值']

xdata_1 = xdata.loc[:, '采样值']

ydata=pd.read_csv('./before2.csv', encoding='gbk')
#ydata=pd.read_csv('./after2.csv', encoding='gbk', skiprows=52)
ydata.columns = ['采样值']

ydata_1 = ydata.loc[:, '采样值']

xdata_2 = xdata_1.describe()

ydata_2 = ydata_1.describe()

print(xdata_2)

print(ydata_2)

plt.figure(1)
#plt.scatter(ydata, s=1)
plt.plot(xdata_1, '*')
plt.plot(ydata_1, '*')
plt.show()
