import math
from matplotlib import pyplot

def funcion(x):
    return x*(math.cos(x**2)) + 1

x = range(-math.pi()/2, math.pi()/2)

pyplot.plot(x, [funcion(i) for i in x])
pyplot.axhline(0, color="black")
pyplot.xlim(-10, 10)
pyplot.savefig("output.png")
pyplot.show()