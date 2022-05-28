# Created by Michał Śliwiński Warsaw 27.05.2022

from matplotlib import pyplot
from numpy import loadtxt
import numpy as np


data = loadtxt('data.txt', dtype='int')

final = np.zeros((2, len(data)))

print("Linear function determination by two points")

for i in range(len(data)):
    x=data[0,i-1]
    y=data[i-1,0]
    at=(data[i,0]-data[i-1,0])/(data[0,i]-data[0,i-1])
    bt=data[i-1,0]-at*data[0,i-1]
    at=final[i-1,0]
    bt=final[i-1,1]
    

x1=int(input("Input x1:"))
y1=int(input("Input y1:"))
x2=int(input("Input x2:"))
y2=int(input("Input y2:"))

print("Point one(",x1,",",y1,") Point two(",x2,",",y2,")")

# y=ax+b

a=(y2-y1)/(x2-x1)
b=y1-a*x1

print("y=",a,"x+",b)

x = [x1,x2] 
 
y = [y1,y2] 
 
 
pyplot.plot(x,y) 
pyplot.title('Linear function')
 
 
pyplot.show()