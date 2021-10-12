#!/usr/bin/python3
import numpy as np
from matplotlib import pyplot as plt
  
#load data
file=open("beforeSampleValue.txt")
lines=file.readlines()
rows=len(lines)
  
datamat = np.zeros((rows, 25))
  
row=0
for line in lines:
  line=line.strip().split(', ')
  datamat[row,:]=line[::]
  row+=1

print(datamat)
print(datamat.shape)


values = np.array(datamat)
plt.plot(values)
plt.show()

