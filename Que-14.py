
import numpy as np
import matplotlib.pyplot as plt

def fuzzy(gamma):
  arr=np.linspace(0, 20, 100)
  list_x=[]
  for i in arr:
    factor=gamma*abs((10/max(i,10)-(i/max(i,10)))) 
    # print(factor)
    if factor ==0:
      x=1
    if factor>0 and factor<=1:
      x=1-factor
    if factor >1:
      x=0
    list_x.append(x)
  return arr, list_x

for i in range(1, 6):
  arr, list_x=fuzzy(i)
  plt.plot(arr, list_x)
  plt.show()