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
#new main fig new window, can write a lot of fig then show together
#figure parameter: facecolor, edgecolor, linewidth, frameon(True, False), layout("constrained", "compressed", "tight"), figsize(width(in), height(in)), dpi
#or fig.set_parameter =, exp fig.set_facecolor =
#layout, figsize, dpi: for main figure only
#use 'constrained' layout, or use compressed for specific aspect ratio (image, map)

"""
#SUBPLOT

fig = plt.figure(figsize=(4, 3), facecolor='lightskyblue', layout='constrained')
#figsize = (width in inches, height in inches), layout = 'contrained' means auto rescale and adjust
fig.suptitle('Figure')

ax = fig.add_subplot()  #(how many rows, how many columns, index of this graph in subplots starts from 1) of subplot, default is (1, 1, 1)
ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')   #subplot title

#plt.show()

##
fig = plt.figure(figsize=(10, 6), facecolor='lightgreen', layout='constrained')
fig.suptitle('Figure 2')

ax1 = fig.add_subplot(2, 3, 1)
ax1.set_title('Graph 1')
ax2 = fig.add_subplot(2, 3, 2)
ax2.set_title('Graph 2')
ax3 = fig.add_subplot(2, 3, 3)
ax3.set_title('Graph 3')
ax4 = fig.add_subplot(2, 3, 4)
ax4.set_title('Graph 4')
ax5 = fig.add_subplot(2, 3, 5)
ax5.set_title('Graph 5')
ax6 = fig.add_subplot(2, 3, 6)
ax6.set_title('Graph 6')

#plt.show()

#OR

fig, ax = plt.subplots(2, 3, figsize=(10, 6), facecolor='lightgreen', layout='constrained', dpi = 150)  #can use dpi when creating figure to scale everything bigger or smaller
fig.suptitle('Test')
ax[0, 0].set_title('Test 1')     #call ax from 2d list
ax[0, 1].set_title('Test 2')
ax[0, 2].set_title('Test 3')
ax[1, 0].set_title('Test 4')
ax[1, 1].set_title('Test 5')
ax[1, 2].set_title('Test 6')

#plt.show()


#OR


#pyplot.subplot_mosai (More complex grids)
fig, axs = plt.subplot_mosaic([['A', 'right'], ['B', 'right']], figsize=(4, 3), layout='constrained')
#2d array so graphs got rows and columns, since got 2 1d arrays, so got 2 rows, since got 2 elements in 1d arrays, so got 2 columns
#since the 1st row 2nd column has exact same value with 2nd row 2nd column, thus both merge together

axs['A'].set_title('Test 1')      #ax in dictionary
axs['B'].set_title('Test 2')
axs['right'].set_title('Test 3')

for ax_name, ax in axs.items():  #dictionary.items() gets key,value in pair
    ax.text(0.5, 0.5, ax_name, ha='center', va='center')

    #key is 'A', 'B', 'right'; value is the graph themselves
    #ax.text() write string directly onto that specific subplot
    #ax.text(X, Y coordinates of text, text)  ha means horizontal alignment, va means vertical alignment

#plt.show()



#SUBFIGURE
fig = plt.figure(layout='constrained', facecolor='lightskyblue')
fig.suptitle('Figure')

figL, figR = fig.subfigures(1, 2)       #list all variables only if 1 row or column, or use one variable to store all subfigure in a list (like fig[1, 0])
#can add all fig parameters here

figL.set_facecolor('yellow')
axL = figL.subplots(2, 1, sharex=True)  #sharex means both subplots share the same x-axis labeling (like 1.0, 1.5)(written once only)
axL[1].set_xlabel('x [m]')
figL.suptitle('Left subfigure')         #which figure(can be main or sub).suptitle() to give a title

figR.set_facecolor('orange')
axR = figR.subplots(1, 2, sharey=True)  #sharey means both subplots share the same y-axis labeling
axR[0].set_title('Axes 1')
figR.suptitle('Right subfigure')

#plt.show()


#if more than 1 row and more than 1 column
fig = plt.figure(figsize=(12, 6), layout='constrained')
fig.suptitle("The Main Parent Figure")

subfigs = fig.subfigures(2, 3)         #store as list(1 row or column can use also)

subfigs[0, 0].set_facecolor('lightblue')
subfigs[0, 0].suptitle("Top-Left SubFigure")

ax1 = subfigs[0, 0].subplots()
ax1.plot([1, 2, 3], [10, 20, 15])
ax1.set_title("A line plot")

subfigs[1, 2].set_facecolor('lightgreen')       
subfigs[1, 2].suptitle("Bottom-Right SubFigure")

ax2 = subfigs[1, 2].subplots()
ax2.scatter([1, 2, 3], [5, 2, 8], color='red')
ax2.set_title("A scatter plot")

#plt.show()


#or (not recommended)

fig = plt.figure(facecolor='red', figsize=(12, 6), layout='constrained', edgecolor = 'black', linewidth = 2, frameon = True, dpi = 140)
fig.suptitle("The Main Parent Figure")

fig1, fig2, fig3, fig4, fig5, fig6 = fig.subfigures(2, 3, facecolor='orange', edgecolor = 'black', linewidth = 2, frameon = True).flatten()         #Flatten squashes the 2x3 grid into a simple list of 6 items

fig1.set_facecolor('lightskyblue')
fig6.set_facecolor('yellow')

#plt.show()






'''
The Figure (The Page):
This is the physical paper itself.
It has a specific size (inches) and a specific paper quality (dpi).

The Axes (The Printed Format):
This is the grid printed onto the paper before you even pick up a pen.
Just like you can buy notebooks with standard square graph paper (rectilinear),
circular polar paper (polar), or specialized map grids (mollweide),
the Axes dictates the structure of the space you are about to draw in.

The Data (The Ink):
These are the lines, dots, and words you actually draw onto the grid.

true But in Matplotlib's mind, Everything is an Artist:
The paper (Figure) is a "Container Artist".
The printed grid (Axes) is a "Container Artist".
The ink (Lines, Text) are "Primitive Artists".
'''

"""




#add_axes
#use this instead of subplots when:
#Ignore the grid entirely. I want to place a graph right here,
#at these exact coordinates, and I want it to be exactly this size.

#parameter: rect(compulsory), projection, polar, axes_class, sharex, sharey, label, ......

#RECT is tuple of four numbers: (left, bottom, width, height)
fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_axes([0.1, 0.55, 0.8, 0.4], fc='lightblue')
#Start the graph 10% from the left edge and 55% from the bottom edge.
#Make the graph take up 80% of the figure's width and 40% of the figure's height.


#PROJECTION
import numpy as np
fig = plt.figure(figsize=(15, 8), layout='constrained')
fig.suptitle("Matplotlib Projection Types", fontsize=16)


# 1.'rectilinear': The default, standard 2D flat grid (X and Y)
ax1 = fig.add_subplot(2, 4, 1, projection='rectilinear')
ax1.set_title("1. 'rectilinear' (Default)")
ax1.plot([1, 2, 3], [1, 4, 2])


# 2.'polar': A circular coordinate system (angle and distance)
ax2 = fig.add_subplot(2, 4, 2, projection='polar')     #OR parameter polor=True (default is False)
ax2.set_title("2. 'polar'")
# Draw a simple circle on the polar plot
ax2.plot(np.linspace(0, 2*np.pi, 100), np.ones(100))




# 3. THE GEOGRAPHIC MAP PROJECTIONS (map a 3D globe onto a 2D plane
# Data is usually passed in radians (longitude/latitude)

# 3.1 'aitoff': oval map projection (NOT equal-area)
ax3 = fig.add_subplot(2, 4, 3, projection='aitoff')
ax3.set_title("3. 'aitoff'")
ax3.grid(True)

# 3.2 'hammer': equal-area oval map (continents looks more recognizable than mollweide)
ax4 = fig.add_subplot(2, 4, 4, projection='hammer')
ax4.set_title("4. 'hammer'")
ax4.grid(True)


# 3.3 'mollweide': equal-area oval map (popular in astronomy, physics)
ax6 = fig.add_subplot(2, 4, 6, projection='mollweide')
ax6.set_title("6. 'mollweide'")
ax6.grid(True)


# 3.4 'lambert': circular map projection
ax5 = fig.add_subplot(2, 4, 5, projection='lambert')
ax5.set_title("5. 'lambert'")
ax5.grid(True)


# 4. "str" (CUSTOM STRING) PROJECTION
# 'str': use string that Matplotlib recognizes as a registered custom projection. most famous is '3d'
ax7 = fig.add_subplot(2, 4, 7, projection='3d')
ax7.set_title("7. str (e.g., '3d')")
# Plotting a 3D scatter point
ax7.scatter(1, 2, 3, color='red', s=100)


#POLAR (= True means projection=polar)


#AXES_CLASS

import mpl_toolkits.axisartist as AA

fig = plt.figure(figsize=(8,6))

#axisartist Toolkit (axes_class=AA.Axes)
ax1 = fig.add_axes(rect=(0.1,0.1,0.35,0.8), axes_class = AA.Axes)
ax1.axis["right"].set_visible(False)


#Standard Matplotlib (not AA.Axes)
ax2 = fig.add_axes(rect=(0.55,0.1,0.35,0.8))
ax2.spines["right"].set_visible(False)
ax2.spines["bottom"].set_position(("data", 0))   #move the bottom axis to y=0

##  ax.spines[""].set_position()
#     ax.spines["bottom"].set_position("zero")             "zero" same as ("data", 0)
#     ax.spines["bottom"].set_position(("outward", 10))    moves the spine 10 points away from the data
#     ax.spines["bottom"].set_position(("axes", 0.5))      position based on 0 to 1.0 scale of the subplot


plt.show()





