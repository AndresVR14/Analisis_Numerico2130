def Horner(res, polinomio, x):
    conM=0
    conS=0
    n=len(polinomio)
    for i in range(n):
        if i==0:
            res=polinomio[i]
        else:
            res= res * x 
            conM=conM+1
            if polinomio[i]!=0:
                res += polinomio[i]
                conS=conS+1
        
    print('Sumas: '+str(conS))
    print('Multiplicaciones: '+str(conM))
    print('Resultado: '+str(res))


polinomio = [1, 8/27]
pol = [100, 0]
x=4
res=0
Horner(res, polinomio, x)