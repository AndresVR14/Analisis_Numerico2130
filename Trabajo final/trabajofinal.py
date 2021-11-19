import numpy as np
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt
import sympy as sp

x,y,z = sp.symbols('x,y,z')

def factorial( n ):
    if n == 0:
        return 1
    fact = 1
    for i in range( 1, n+1 ):
        fact *= i
    return fact
 
def taylor_mthd( f, a, b, N, IV ):
    h = (b-a)/float(N)                 
    t = np.arange( a, b+h, h )        
    w = np.zeros((N+1,))               
    t[0], w[0] = IV                     
    for i in range(1,N+1):              
        T = 0
        for j in range(len(f)):
            h_factor = h**(j)/float(factorial(j+1))
            T += h_factor * f[j]( t[i-1], w[i-1] )
        w[i] = w[i-1] + h * T
    return w,t

# Modelo SIR 
def ecuaciones(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * C * I/N
    dIdt = beta * S * C* I/N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


#Impresion de las gráficas
def plot(S, I, R, t, divide_by=1):
    fig, ax = plt.subplots()
    ax.plot(t, S / divide_by, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.plot(t, I / divide_by, 'r', alpha=0.5, lw=2, label='Infectado')
    ax.plot(t, R / divide_by, 'g', alpha=0.5, lw=2, label='Recuperado con inmunidad')
    ax.set_xlabel('Tiempo /días')
    ax.set_ylabel('Porcentaje')
    legend = ax.legend()
    # fig.show()
    
def plot_with_death_rate(S, I, R, t, divide_by=1, death_rate=0.05):
    # Dibujamos los datos de S(t), I(t) y R(t)
    fig, ax = plt.subplots()
    ax.plot(t, S / divide_by, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.plot(t, I / divide_by, 'r', alpha=0.5, lw=2, label='Infectado')
    RR = R * (1 - death_rate)
    DD = R - RR
    ax.plot(t, RR / divide_by, 'g', alpha=0.5, lw=2, label='Recuperado con inmunidad')
    ax.plot(t, DD / divide_by, 'k', alpha=0.5, lw=2, label='Muertos')
    ax.set_xlabel('Tiempo /días')
    ax.set_ylabel('Porcentaje')
    legend = ax.legend()
    # fig.show()
    
# Población inicial, N.
N = 4500 
 
# Condiciones iniciales
I0 = 10/N
R0 = 0
S0 = N - I0
 
# Parámetros
C = 4
beta = 0.06 
gamma = 0.021 

 
# Pasos temporales (en días)
t = np.linspace(0, 365, 365)
 
# condiciones iniciales
y0 = S0, I0, R0

# Integrate the SIR equations over the time grid, t.
ret = odeint(ecuaciones, y0, t, args=(N, beta, gamma))

S, I, R = ret.T

plot_with_death_rate(S, I, R, t, divide_by=N, death_rate=0.05)
plt.show()

m = max(I)
i = np.where(I==m)

#punto 3
print('Cantidad maxima:', max(I))
print('Dia cantidad maxima:', max(i[0]))

#punto 4
print(f'Porcentaje maximo infectados: {max(I)/N*100}%')
print(f'Porcentaje maximo recuperados: {max(R)/N*100}%')


k = gamma/(beta*C)

controlados = []

for i in range(len(S)):
    if k > S[i]/N:
        controlados.append(t[i])
        
#punto 5
print('Dias controlados',len(controlados))
print('Primer dia', round(controlados[0],0))

#punto 8
 
f   = lambda t,I: gamma**I
df  = lambda t,I: I*gamma
ddf = lambda t,I: I

IV = (1.5, 3 )
 
w3,tt = taylor_mthd( [ f, df, ddf ], 1.5, 0.5, N, IV )

print(w3)

plt.plot(w3, tt, label = "Recuperados")
 
# naming the x axis
plt.xlabel('tiempo/ dias')
# naming the y axis
plt.ylabel('porcentaje de recuperados')
# giving a title to my graph
plt.title('Solución sistema de ecuaciones')
 
# show a legend on the plot
plt.legend()
 
# function to show the plot
plt.show()