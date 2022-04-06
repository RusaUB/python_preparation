import os
from turtle import color 
import matplotlib.pyplot as plt

print(os.curdir) # "."
print(os.path.basename(os.curdir))
print(os.listdir()) #All files in this derectory ['index.py', 'main.py']
print(os.path.isfile(os.curdir)) #If it's fille (with out other files) This is flase
print(os.path.isdir(os.curdir)) #If it's folder This is true 

print("Répertoire courant: ", os.path.abspath('.')) #/Users/rustam/Documents/Python
print("Répertoire courant: ", os.curdir) #only .
print("Changement de répertoire")
print("Répertoire courant: ", os.path.basename(os.path.abspath(os.curdir))) #Python 

ob = open("main.py", "w")
ob.write("test")
ob.close

ob = open("main.py" , "r")
print(ob.readline())
ob.close

a = "a , b , c , d , e , f , g"
l = a.split(",")

txt = ''
print(txt.join(l)) #a b c d e f g


def f(x):
    return x*x

lx = []

for k in range(-10,10):
    lx.append(k)
ly = []
for i in lx:
    ly.append(f(i))

#plt.plot(lx, ly, color = "b" , label = "toto")
#plt.legend()
#plt.imread("anime.jpg")
#plt.show()

k = ["random", "shit"]
txt = ' '
print(txt.join(k))