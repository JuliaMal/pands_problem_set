
# ref: https://www.digitalocean.com/community/tutorials/how-to-plot-data-in-python-3-using-matplotlib
# adding matplotlib library
import matplotlib.pyplot as plt

x = range(5)
y = x


plt.subplot(221)
plt.plot(x,y)
# naming the graph
plt.title("Plot of the function y = f(x) in the range [0, 4]")

plt.subplot(222)
plt.plot(x,y)
# naming the graph
plt.title("Plot of the function y = f(x^x) in the range [0, 4]")

plt.subplot(223)
plt.plot(x,y)
# naming the graph
plt.title("Plot of the function y = f(2^x) in the range [0, 4]")

# setting a range for X and Y axes
plt.xlim(0,4)
plt.ylim(0,4)

# adding the name for X and Y axes
plt.xlabel("X")
plt.ylabel("Y")

#saving a graph as png file
plt.savefig("plot_of_functions.png")

# show results in the graph
plt.show()

