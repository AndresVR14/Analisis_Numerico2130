import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import warnings
warnings.simplefilter("ignore")


#Metodo Runge Kutta
def rungeKutta(v, lorenz):
    
    h= 1
    lista_t = np.arange(1,50,0.002)   
    X,Y=[],[]
    
    def fun(v):   
        x,y = (v[0], v[1])
        fx, fy = lorenz(x,y)
        return np.array([fx,fy],float)
      
    for t in range(4500):   
        k1=h*fun(v)
        k2=h*fun(v+(0.5*k1))
        k3=h*fun(v+(0.5*k2))
        k4=h*fun(v+k3)
        
        v += (k1+2*k2+2*k3+k4)/float(6)
        
        X.append(v[0])
        Y.append(v[1])
    return np.array([X,Y])


#Sistema de lorenz
def lorenz(x,y):
    
    f1 = -0.06 * x * 4 * y/4500
    f2 = 0.06 * x * 4* y/4500 - 0.021 * y
    f3 = 0.021 * y
    
    #f1 = (a*x) + (y*z)
    #f2 = b*(y-z)
    #f3 = (-x*y) + ((c*y)-z)
    return f1, f2

a = 10/4500
b = 4500-a
c = 0
v=[1,1] #variables x,y,z

#FUNCION
x,y = rungeKutta(v, lorenz)

print(x)
print(y)

#GRAFICAR
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x,y)
plt.show()
