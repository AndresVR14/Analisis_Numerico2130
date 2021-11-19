
library(rgl) 

# Punto 1 y 2

SIR.model <- function(t, b, g){ 
  require(deSolve) 
  N = 4500
  init <- c(S=1-(2/779853),I=2/779853,R=0)
  parameters <- c(beta=b,gamma=g)
  time <- seq(0,t,by=t/(2*length(1:t))) 
  eqn <- function(time,state,parameters){
    with(as.list(c(state,parameters)),{ 
      dS <- -beta*C/N 
      dR <- gamma*I 
      dI <- beta*C*S/N-gamma*I 
      return(list(c(dS,dI,dR)))}) 
  }
  out<-ode(y=init,times=time,eqn,parms=parameters, method = "rk4") 
}
SIR.model(365,0.06,0.021)

# Parametros
Beta<-0.06
c <-4
gama<- 0.021
N1<-4500

# Condiciones iniciales 
I0<-10/N1
S0<-N1-I0
R0<-0

paso<-1

# Numero de pasos (dias)
dias<-365

S<-function(x,y,z,t) -Beta*x*y
I<-function(x,y,z,t) Beta*x*y-gama*y
R<-function(x,y,z,t) gama*y

vS<-replicate(dias+1,0)
vI<-replicate(dias+1,0)
vR<-replicate(dias+1,0)

vS[1]<-S0
vI[1]<-I0
vR[1]<-R0



vS2<-replicate(dias+1,0)
vI2<-replicate(dias+1,0)
vR2<-replicate(dias+1,0)

vS2[1]<-1
vI2[1]<-14/N1
vR2[1]<-7/N1


p<-2
while(p<=dias+1){
  xi<-vS[p-1]
  yi<-vI[p-1]
  zi<-vR[p-1]
  
  k1<-paso*S(xi,yi,zi,ti)
  l1<-paso*I(xi,yi,zi,ti)
  m1<-paso*R(xi,yi,zi,ti)
  
  k2<-paso*S(xi+(1/2)*k1,yi+(1/2)*l1,zi+(1/2)*m1,ti+paso/2)
  l2<-paso*I(xi+(1/2)*k1,yi+(1/2)*l1,zi+(1/2)*m1,ti+paso/2)
  m2<-paso*R(xi+(1/2)*k1,yi+(1/2)*l1,zi+(1/2)*m1,ti+paso/2)
  
  k3<-paso*S(xi+(1/2)*k2,yi+(1/2)*l2,zi+(1/2)*m2,ti+paso/2)
  l3<-paso*I(xi+(1/2)*k2,yi+(1/2)*l2,zi+(1/2)*m2,ti+paso/2)
  m3<-paso*R(xi+(1/2)*k2,yi+(1/2)*l2,zi+(1/2)*m2,ti+paso/2)
  
  k4<-paso*S(xi+k3,yi+l3,zi+m3,ti+paso)
  l4<-paso*I(xi+k3,yi+l3,zi+m3,ti+paso)
  m4<-paso*R(xi+k3,yi+l3,zi+m3,ti+paso)
  
  vS2[p]<-xi+(1/6)*(k1+2*k2+2*k3+k4)
  vI2[p]<-yi+(1/6)*(l1+2*l2+2*l3+l4)
  vR2[p]<-zi+(1/6)*(m1+2*m2+2*m3+m4)
  
  p<-p+1
}

MatrizError<-matrix(0:0, nrow=10, ncol=2)
MatrizError<-data.frame(MatrizError)
colnames(MatrizError)<-c( "ErrorrRelativo","ErrorAbsolutoI")
          


for (i in 1:10){ 
 
  MatrizError$ErrorAbsolutoI[i]<-abs(vI[i]-vI2[i])
  MatrizError$ErrorRelativoI[i]<-MatrizError$ErrorrelativoI[i]/vI[i]
 
}

View(MatrizError)