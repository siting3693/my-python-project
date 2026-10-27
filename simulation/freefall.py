'''
Numerical Simulation of Free Fall Motion with and without Air Resistance using the Euler Method
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math



#graph 1: h vs t (from diff height)
g = -9.81
dt = 0.001

t = np.arange(0, 5, dt)

v1 = 0
v2 = 0
h1 = np.arange(0, 5, dt)
h1[0]=50
h2 = np.arange(0, 5, dt)
h2[0]=100



for i in range(len(t)-1):
    if h1[i]>0:
        v1 = v1 + g*dt
    else:
        v1 = 0
    h1[i+1] = h1[i] + v1*dt
    
    if h2[i]>0:
        v2 = v2 + g*dt
    else:
        v2 = 0
    h2[i+1] = h2[i] + v2*dt

    

plt.subplot(1, 2, 1)
plt.plot(t, h1)
plt.xlabel("Time, t (s)")
plt.ylabel("Height, h (m)")
plt.title(f"From {h1[0]} m")

plt.subplot(1, 2, 2)
plt.plot(t, h2)
plt.xlabel("Time, t (s)")
plt.ylabel("Height, h (m)")
plt.title(f"From {h2[0]} m")

plt.suptitle("Free Fall Motion")
plt.show()








#graph 2: Time of Fall, t (s) against Initial Height, h (m)
g = 9.81
dh = 0.001

h = np.arange(0, 100, dh)
t = np.arange(0, 100, dh)

for i in range(len(h)):
    t[i] = math.sqrt(2/g*h[i])

plt.subplot(1, 2, 1)
plt.plot(h, t)
plt.xlabel("Initial Height, h (m)")
plt.ylabel("Time of Fall, t (s)")
plt.title("Analytical Solution")




#simulation of graph 2
g = -9.81
dh = 0.1
dt = 0.01
maxHeight = 100
maxTime = 5

hInit = np.arange(0, maxHeight, dh)
tAir = np.arange(0, maxHeight, dh)

for n in range(len(hInit)):
    t = np.arange(0, maxTime, dt)
    h = np.arange(0, maxTime, dt)
    v = np.arange(0, maxTime, dt)
    h[0] = hInit[n]
    v[0] = 0

    for i in range(len(t)-1):
        if h[i] > 0:
            v[i+1] = v[i] + g*dt
            h[i+1] = h[i] + v[i+1]*dt
        else:
            tAir[n] = i * dt
            break

plt.subplot(1, 2, 2)
plt.plot(hInit, tAir)
plt.xlabel("Initial Height, h (m)")
plt.ylabel("Time of Fall, t (s)")
plt.title("Numerical Simulation (Euler Method)")

plt.suptitle("Free Fall Motion: Analytical vs Numerical Comparison")
plt.show()








#graph 4: h, v, a vs t graph (with air resistance)
g = -9.81
dt = 0.1
maxTime = 12
pi = 3.14159265
density = 1.225

class Object:
    def __init__ (self, name, mass, area, Cd):
        self.name = name
        self.mass = mass
        self.area = area
        self.Cd = Cd
        self.k = 1.0/2*Cd*density*area

o1 = Object("Basketball", 0.62, pi*0.12*0.12, 0.54)
o2 = Object("Laptop", 1.69, 0.3585*0.242, 1.2)

t = np.arange(0, maxTime, dt)
v = np.arange(0, maxTime, dt)
a = np.arange(0, maxTime, dt)
h = np.arange(0, maxTime, dt)

a[0] = -9.81
h[0] = 150

def objFall (obj):
    for i in range(len(t)-1):
        if h[i] > 0:
            v[i+1] = v[i] + a[i]*dt
            a[i+1] = (obj.k*v[i+1]*v[i+1] + obj.mass*g) / obj.mass
            h[i+1] = h[i] + v[i+1]*dt
        else:
            h[i+1] = h[i]
            v[i+1] = 0
            a[i+1] = 0
    return np.array([t, h, v, a])

def showgraph4 (obj, result):
    plt.subplot(1, 3, 1)
    plt.plot(t, result[1])
    plt.xlabel("Time, t (s)")
    plt.ylabel("Height, h (m)")
    plt.title("h vs t")

    plt.subplot(1, 3, 2)
    plt.plot(t, -result[2])
    plt.xlabel("Time, t (s)")
    plt.ylabel("Velocity, v (m/s)")
    plt.title("v vs t")

    plt.subplot(1, 3, 3)
    plt.plot(t, -result[3])
    plt.xlabel("Time, t (s)")
    plt.ylabel("Acceleration, a (m/s2)")
    plt.title("a vs t")

    plt.suptitle(f"{obj.name} Falling from {h[0]} m with Air Resistance")
    plt.show()

o1result = objFall(o1)
showgraph4(o1, o1result)

o2result = objFall(o2)
showgraph4(o2, o2result)







#graph 5: h, v vs t (with resistance) (diff k)
maxTime = 16

t = np.arange(0, maxTime, dt)
v = np.arange(0, maxTime, dt)
a = np.arange(0, maxTime, dt)
h = np.arange(0, maxTime, dt)

a[0] = -9.81
h[0] = 150

o3 = Object("k = 0.0 Object", 5, 0.5*0.5, 0)
o3.k = 0
o4 = Object("k = 0.1 Object", 5, 0.5*0.5, 0)
o4.k = 0.1
o5 = Object("k = 0.5 Object", 5, 0.5*0.5, 0)
o5.k = 0.5

def plotgraph5 (objsum, count, obj, result):
    plt.subplot(2, 3, count)
    plt.plot(t, result[1])
    plt.xlabel("Time, t (s)")
    plt.ylabel("Height, h (m)")
    plt.title(f"h vs t (k = {obj.k})")

    plt.subplot(2, 3, count + objsum)
    plt.plot(t, -result[2])
    plt.xlabel("Time, t (s)")
    plt.ylabel("Velocity, v (m/s)")
    plt.title(f"v vs t (k = {obj.k})")

o3result = objFall(o3)
o4result = objFall(o4)
o5result = objFall(o5)

plotgraph5(3, 1, o3, o3result)
plotgraph5(3, 2, o4, o4result)
plotgraph5(3, 3, o5, o5result)

plt.tight_layout()
plt.suptitle(f"Effect of Drag Coefficient (k) on Falling Motion from {h[0]} m")
plt.show()







#graph 6: h vs t (with resistance) (diff dt)
def plotgraph6 (count, dt, obj, result):
    plt.subplot(1, 3, count)
    plt.plot(t, result[1])
    plt.xlabel("Time, t (s)")
    plt.ylabel("Height, h (m)")
    plt.title(f"h vs t (dt = {dt} s)")

maxTime = 5
dt = 0.1
t = np.arange(0, maxTime, dt)
v = np.arange(0, maxTime, dt)
a = np.arange(0, maxTime, dt)
h = np.arange(0, maxTime, dt)
a[0] = -9.81
h[0] = 50

o1result = objFall(o1)
plotgraph6(1, dt, o1, o1result)

dt = 0.01
t = np.arange(0, maxTime, dt)
v = np.arange(0, maxTime, dt)
a = np.arange(0, maxTime, dt)
h = np.arange(0, maxTime, dt)
a[0] = -9.81
h[0] = 50

o1result = objFall(o1)
plotgraph6(2, dt, o1, o1result)

dt = 0.001
t = np.arange(0, maxTime, dt)
v = np.arange(0, maxTime, dt)
a = np.arange(0, maxTime, dt)
h = np.arange(0, maxTime, dt)
a[0] = -9.81
h[0] = 50

o1result = objFall(o1)
plotgraph6(3, dt, o1, o1result)


plt.suptitle(f"Effect of Time Step (dt) on Falling {o1.name} with Air Resistance (Initial Height = {h[0]} m)")
plt.show()
