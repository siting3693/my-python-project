import matplotlib.pyplot as plt
"""Matplotlib
Object-Oriented Style

                My previous style(plt.)    Object-Oriented Style(ax.)   
Draw the data	plt.plot(x, y)	           ax.plot(x, y) (Notice this stays the same!)
X-axis label	plt.xlabel("Time")	   ax.set_xlabel("Time")
Y-axis label	plt.ylabel("Height")	   ax.set_ylabel("Height")
Subplot title	plt.title("Test 1")	   ax.set_title("Test 1")
X-axis limits	plt.xlim(0, 10)	           ax.set_xlim(0, 10)
Y-axis limits	plt.ylim(0, 100)	   ax.set_ylim(0, 100)
X-axis ticks	plt.xticks([1, 2, 3])	   ax.set_xticks([1, 2, 3])
Show legend	plt.legend()	           ax.legend() (Stays the same)

"""

fig = plt.figure(figsize=(2, 2), facecolor='lightskyblue', layout='constrained')
fig.suptitle('Figure')

ax = fig.add_subplot()  #(how many rows, how many columns, index of this graph in subplots starts from 1) of subplot, default is (1, 1, 1)
ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')   #subplot title


##
fig = plt.figure(figsize=(2, 2), facecolor='lightskyblue', layout='constrained')
fig.suptitle('Figure 2')

ax = fig.add_subplot(2, 3, 1)
ax.set_title('Graph 1')
ax = fig.add_subplot(2, 3, 2)
ax.set_title('Graph 2')
ax = fig.add_subplot(2, 3, 3)
ax.set_title('Graph 3')
ax = fig.add_subplot(2, 3, 4)
ax.set_title('Graph 4')
ax = fig.add_subplot(2, 3, 5)
ax.set_title('Graph 5')
ax = fig.add_subplot(2, 3, 6)
ax.set_title('Graph 6')




