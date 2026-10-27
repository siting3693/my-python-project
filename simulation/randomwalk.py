import numpy as np
from numpy import random
import matplotlib.pyplot as plt


'''
#1D Random Walk

#Graph 1: Particle Position vs Step Number (Trajectory of a Particle)
numofstep = 1000

position = np.zeros(numofstep+1)
steps = random.choice([-1, 1], size=(numofstep))

for i in range(numofstep):
    position[i+1] = position[i] + steps[i]

plt.plot(range(numofstep+1), position, marker = ".")
plt.xlabel("Time Step, t")
plt.ylabel("Displacement, x")
plt.title("Trajectory of a Particle Under 1D Random Walk")
plt.show()





#Graph 2: Probability Distribution of Particle Displacement Following a 1D Random Walk
def _1drandomwalks (stepsize, numofstep, numofsample):
    finalposition = np.zeros(numofsample)
    for j in range(numofsample):
        position = 0
        steps = random.choice([-stepsize, stepsize], size=(numofstep))

        for i in steps:
            position = position + i

        finalposition[j] = position

    return finalposition


def calcmean (finalposition, numofsample):
    totalstep = 0
    for i in finalposition:
        totalstep = totalstep + i
    mean = totalstep / numofsample
    return mean

def calcvar (finalposition, mean, numofsample):
    var = 0
    for i in finalposition:
        var = var + (i - mean)**2
    var = var/numofsample
    return var
#Var(X)=E(X2)−[E(X)]2, so 1 step got eachsmallstep square de variance, total var is each step de var * numofstep


def plot (finalposition, stepsize, title, mean, var):
    bins = np.arange(min(finalposition), max(finalposition)+stepsize*4, stepsize*4)

    plt.hist(finalposition, bins = bins, edgecolor = "black")
    plt.xlabel("Displacement, x")
    plt.ylabel("Frequency / Probability Density")
    plt.text(0.05, 0.9, f"μ = {mean:.2f}\nσ² = {var:.2f}", transform=plt.gca().transAxes)
    plt.title(title)



def graph2 (stepsize, numofstep, numofsample, title):
    finalposition = _1drandomwalks(stepsize, numofstep, numofsample)
    mean = calcmean(finalposition, numofsample)
    var = calcvar(finalposition, mean, numofsample)
    plot(finalposition, stepsize, title, mean, var)


stepsize = 2
numofstep = 1000
numofsample = 10000
graph2(stepsize, numofstep, numofsample, f"Gaussian Distribution of Particle Displacement in 1D Random Walk")
plt.show()

#gaussian distribution = normal distribution




#Graph 3: compare diff numofstep
stepsize = 1
numofsample = 10000

plt.subplot(1, 3, 1)
numofstep = 10
graph2(stepsize, numofstep, numofsample, f"n = {numofstep}")

plt.subplot(1, 3, 2)
numofstep = 100
graph2(stepsize, numofstep, numofsample, f"n = {numofstep}")

plt.subplot(1, 3, 3)
numofstep = 1000
graph2(stepsize, numofstep, numofsample, f"n = {numofstep}")

plt.suptitle("Effect of Number of Steps, n, on Particle Displacement Distribution")

plt.show()



#Graph 4: compare diff numofsample
stepsize = 1
numofstep = 1000

plt.subplot(1, 3, 1)
numofsample = 100
graph2(stepsize, numofstep, numofsample, f"N = {numofsample}")

plt.subplot(1, 3, 2)
numofsample = 1000
graph2(stepsize, numofstep, numofsample, f"N = {numofsample}")

plt.subplot(1, 3, 3)
numofsample = 10000
graph2(stepsize, numofstep, numofsample, f"N = {numofsample}")

plt.suptitle("Effect of Sample Size, N, on Estimated Displacement Distribution")

plt.show()



#Graph 5: compare diff step size
numofsample = 10000
numofstep = 1000

plt.subplot(1, 3, 1)
stepsize = 1
graph2(stepsize, numofstep, numofsample, f"s = {stepsize}")

plt.subplot(1, 3, 2)
stepsize = 2
graph2(stepsize, numofstep, numofsample, f"s = {stepsize}")

plt.subplot(1, 3, 3)
stepsize = 3
graph2(stepsize, numofstep, numofsample, f"s = {stepsize}")

plt.suptitle("Effect of Step Size, s, on Particle Displacement Distribution")

plt.show()


'''



endtime = 0.000001
timestep = 0.01e-9
time = np.arange(0, endtime, timestep)
avgtimestep = 0.13e-9
numofparticle = 1000
rmove = complex(real = 0.005e-9)
imove = complex(imag = 0.005e-9)
directions = {-rmove, rmove, -imove, imove}

position = np.zeros(numofparticle, dtype=complex)
lastmove = np.zeros(numofparticle, dtype=complex)

for i in range(len(time + 1)):
    for j in range(numofparticle):
        collision = random.choice([1,0], p = [timestep/avgtimestep, 1 - timestep/avgtimestep])
        if collision:
            valid_directions = list(directions - {lastmove[j]})
            lastmove[j] = random.choice(valid_directions)
            position[j] += lastmove[j]



plt.scatter(np.real(position), np.imag(position))
plt.show()












