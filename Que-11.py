
import numpy as np

array=[[0.5,-1.1,0.24,-0.22,-1.8], [0.15,-1.4,0.11,-0.28,-0.3], [0.1,-1.4,0.11,0.6,-1.11]]
desired=[1,-1,1]
x = np.array(array)
weight=[0.1, 0.17,0.2,-1.1, -0.4]
output = []
c = 2.5
p = 0 #epochs

for p in range(10):
    output=[]
    print(p)
    for i in range(3): #3 times train
        y = 0
        for j in range(len(x[i])):
            y = y + x[i][j]*weight[j]
        if(y>0):
            y=1
        elif(y<0):
            y=-1
        output.append(y)
        weight = weight + c*(desired[i]-y)*x[i]
        print("List Output",weight,output)
    error_arr=np.absolute(np.array(output)- np.array(desired))
    err=np.mean(error_arr)
    print(err)