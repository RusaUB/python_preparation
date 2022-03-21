#Траектория тела в терминале тест SAM
#x = (speed**2*math.sin(2*angle))/9,18 #на сколько метров улетел
import math 
import matplotlib.pyplot as plt
import termplotlib as tpl
import inspect

x = []
y = []
z = []


def landed(masse,speed,angle,maxTime):
    for t in range(maxTime):
        x0 = speed*math.cos(angle)*t
        x.append(x0)
        z0 = ((-0.5*10*x0**2)/speed**2*pow(math.cos(angle),2)) + x0*math.tan(angle)
        z.append(z0)
        y0 = -0,5*10*t**2 + speed*math.sin(angle)*t
        y.append(y0)

landed(10,20,math.pi/4,10)

def Graph():
    for k in z:
        print(" "* round(k) +"#")
        print("#")

print(Graph())