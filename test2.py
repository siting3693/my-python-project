import numpy as np
from numpy import random
import matplotlib.pyplot as plt

#set width (bins)
x = np.random.normal(170, 10, 250)

#1. auto
plt.hist(x, bins="auto")
plt.show()

#2. set total number of bins
plt.hist(x, bins=10)
plt.show()

#3. custom bin edges (data type of parameter is list, range, np.ndarray)
step = 5
bins = np.arange(min(x), max(x)+step, step)   #stop not included, so add 1 step
plt.hist(x, bins=bins, edgecolor="black", color="green")
plt.show()

bins = range(140, 205, 5)
plt.hist(x, bins=bins, edgecolor="black", color="green")
plt.show()
