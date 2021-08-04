import math
x=0.3
e= math.exp(x)
E=10**-10
sum=0
i=0
while abs(e-sum)>E:
    sum+= e*(x**i)/math.factorial(i)
    i+=1
    print(sum)

