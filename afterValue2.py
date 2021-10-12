#!/usr/bin/python3
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

data=pd.read_csv('./after2.csv', encoding='gbk')
data.columns = ['采样值']

ydata=data.loc[:, '采样值']

#columns = data.columns
#columns_value = columns.values

#rows = data.index
#rows_value = rows.values

#print(type(columns), columns)
#print(type(columns_value), columns_value)
#print(type(rows), rows)
#print(type(rows_value), rows_value)

plt.figure(1)
plt.plot(ydata, '*')
plt.show()
