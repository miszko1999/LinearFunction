# Created by Michał Śliwiński Warsaw 26.05.2022

from matplotlib import pyplot

print("Linear function determination by two points")
    
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
 
 
pyplot.show()