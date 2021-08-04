import math
def algoritmo(x,n,E):
    y=1/2*(x+n/x)
    print(y)
    while(abs(x-y)>E):
        x=y
        y=1/2*(x+n/x)
        print(y)
    if math.sqrt(7)==y:
        print('El valor de y es verdadero')


n=7
x = 7
E = 10**(-8)
algoritmo(x,n,E)