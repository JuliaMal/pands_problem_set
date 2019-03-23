# ref: 
# https://www.digitalocean.com/community/tutorials/how-to-plot-data-in-python-3-using-matplotlib
# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.arange.html
# https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

# adding matplotlib library
import matplotlib.pyplot as plt
import numpy as np

# Creating functions and setting the range for x
# Used numpy arange function (start, stop, step)(Return evenly spaced values within a given interval)
x = np.arange(0.0, 4.0, 0.01)
y = x
y2 = x * x
y3 = 2 ** x

# Plot functions
plt.plot(x,y, color = "dodgerblue")
plt.plot(x,y2, color = "orangered")
plt.plot(x,y3, color = "green")

# naming the graph
plt.title("Plot of the functions y = f(x), y = f(x^2), y = f(2^x) in the range [0, 4]")

# adding names as text for each plot
plt.text(2, 1, "y = f(x)", color = "dodgerblue")
plt.text(2.3, 10, "y = f(x^2)", color = "orangered")
plt.text(3, 7, "y = f(2^x)", color = "green")

# adding the name for X and Y axes
plt.xlabel("X")
plt.ylabel("Y")

#saving a graph as png file
plt.savefig("plot_of_functions.png")

# show results in the graph
plt.show()


