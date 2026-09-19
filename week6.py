import matplotlib

print(matplotlib.__version__)



import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])     #two x values of two points (x1, x2)
ypoints = np.array([0, 250])   #two y values of two points (y1, y2)
plt.plot(xpoints, ypoints)     #normal plot syntax, draw a line from point to point
plt.show()

xpoints = np.array([1, 2, 6, 8])   #can have many points
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints)
plt.show()

ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)    #default x value is 0,1,2,3,4,5...
plt.show()





xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

#Markers (parameter: fmt, marker, markersize/ ms, markeredgecolor/ mec, markerfacecolor/ mfc)
plt.plot(xpoints, ypoints, 'o')   #with "o", plot without line
plt.show()

plt.plot(ypoints, marker = 'o')   #line with plot
plt.show()

plt.plot(ypoints, marker = '*')   #use * to mark plot (more marker in python matplotlib markers)
plt.show()

#parameter format string (fmt)(marker line color)
plt.plot(ypoints, 'o:r')   #: dotted, - solid, -- dashed, -. dashdot
plt.show()

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'y')  #can use color syntax, hexadecimal color values, or 140 supported color names
plt.show()

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = '#4CAF50')




#Line (parameter: linestyle/ ls, color/ c, linewidth/ lw)
plt.plot(ypoints, ls = '-.', c = '#4CAF50', linewidth = '7.5')
plt.show()

#multiple lines
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)    #plot all then show
plt.plot(y2)
plt.show()

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, x2, y2)   #plot together
plt.show()




#Labels and title (parameter: fontdict)(function: xlabel(), ylabel(), title())
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y, marker="o")

plt.title("Sports Watch Data")   #title
plt.xlabel("Average Pulse")      #x-axis
plt.ylabel("Calorie Burnage")    #y-axis
plt.show()

#font properties for title and labels, position the title
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1, loc = 'left')
plt.xlabel("Average Pulse", fontdict = font2, loc = 'left')
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.plot(x, y)
plt.show()




#Grid (parameter: axis, color, linestyle, linewidth)(function: grid)
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.grid()       #add grid
plt.show()

plt.plot(x, y)
plt.grid(axis = 'x')   #add x axis grid only
plt.show()

plt.plot(x, y)
plt.grid(axis = 'y')
plt.show()

plt.plot(x, y)
plt.grid(color = 'green', linestyle = '--', linewidth = 1.5)
plt.show()




#Subplot (function: subplot(), plot(), title(), suptitle())

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)         #(has 1 row, 2 columns of subplot, and this plot is the first plot)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)         #second plot
plt.plot(x,y)

plt.show()


#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1)         #2 rows 1 column
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()



#title
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")      #small title for subplot

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")     #small title for subplot

plt.suptitle("MY SHOP")  #super title for the entire figure
plt.show()




#Scatter (Showing correlation or relationship between two independent continuous variables (while line graph showing trends))
#(parameter: c/color, c, s, alpha, cmap)(function: scatter(), colorbar())
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)                 #scatter plot syntax
plt.title("relationships between the observations")   #title
plt.xlabel("age of car")      #x-axis
plt.ylabel("speed of car")
plt.show()


#day one, the age and speed of 13 cars:
plt.scatter(x, y)
#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91])
plt.scatter(x, y)

plt.show()


#color all dots (parameter: color/c)
plt.scatter(x, y, color = 'hotpink')
plt.show()


#color each dot (parameter: c)
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x, y, c=colors)   #color each dot
plt.show()

#colormap (parameter: cmap)(a list of colors, where each color has a value that ranges from 0 to 100)
#such as viridis, nipy_spectral, more in python matplotlib scatter
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis')   #name of colormap
plt.colorbar()           #optioanal, can show the colorbar
plt.show()


x = np.random.randint(100, size=(100))    #random generate values from 0 to 99, fit in 1d array with 100 columns
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')   #alpha is opacity (0 is totally transparent, 1 is fully opaque)
plt.colorbar()
plt.show()




#Bars (parameter: color, width/height(default 0.8)(vertical use width, horizontal use height))(function: bar(), barh())
x = np.array(["A", "B", "C", "D"])    #label of each bar
y = np.array([3, 8, 1, 10])           #height of each bar
plt.bar(x, y)                         #create bar syntax (label, height)
plt.show()

plt.barh(x, y)                        #horizontal bar syntax
plt.show()

plt.bar(x, y, color = "#4CAF50", width = 0.1)
plt.show()




#Histrogram (histogram: continuous range of number, bar: distinct categories (x-axis))
#(function: hist())
x = np.random.normal(170, 10, 250)    #where data collected from, using numpy normal distrbution, loc=mean, scale=standard deviation, size=size of array
print(x)
plt.hist(x)        #create histogram syntax, need 1d data only (no need x, y or label, because height is the frequency)
plt.show() 




#Pie Charts (parameter: labels, startangle, explode, shadow, colors)(function: pie(), legend(parameter: title))
#first wedge starts from the x-axis and moves counterclockwise (like what we do in math)
y = np.array([3.5, 2.5, 2.5, 1.5])     #frequency of each piece(wedge)
plt.pie(y)
plt.show() 

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]    #optional, add label for each wedge
plt.pie(y, labels = mylabels)
plt.show() 

plt.pie(y, labels = mylabels, startangle=90)     #first wedge starts from 90 degree (default is 0)
plt.show()

myexplode = [0.2, 0, 0, 0]        #in array
plt.pie(y, labels = mylabels, explode = myexplode)    #explode make certain wedge(s) to stand out
plt.show() 

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)   #shadow, add shadow to the whole pie chart
plt.show()

mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels = mylabels, colors = mycolors)   #set colors to each wedge
plt.show() 

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")          #legend function add list of label of each wedge, parameter: title (optional, title for the legend)
plt.show() 

