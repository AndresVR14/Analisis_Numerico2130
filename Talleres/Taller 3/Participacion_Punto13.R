#Participaci�n, punto 13
#Interpolaci�n lineal


#matriz con la base imponible de la forma y=ax^2+bx+c
matriz_incog <- matrix(c(4410000^2, 4410000, 1,
                         4830000^2, 4830000, 1,
                         5250000^2, 5250000, 1), 3, 3, byrow = TRUE)

#arreglo con la cuota integra es decir la y de la funci�n interpolaci�n
cuotasIntegras <- c(1165978, 1329190, 1501474)

#eliminaci�n gaussiana para obtener la matriz soluci�n 
m2_gauss <- gaussianElimination(matriz_incog, cuotasIntegras)
gaussianElimination(matriz_incog, cuotasIntegras)

#funci�n interpolaci�n
cat(m2_gauss[1,4], "x^2 + ", m2_gauss[2,4], "x + ", m2_gauss[3,4])

#gr�fica con cojunto de puntos
par(mar=c(1,1,1,1))
x<-c(4410000, 4830000, 5000000, 5250000, 5670000)#Base imponible
y<-c(1165978, 1329190, 1397831, 1501474, 1682830)#cuota integra

windows()
plot(x,y,main = "Gr�fica con conjunto de puntos", pch = 18, bg= "dark green", col="dark green", cex = 1, lwd = 1, 
     xlab = "Base imponible", ylab = "Cuota �ntegra", axes = TRUE)
lines(x,y, lwd =1, col = "dark green")


par(mar=c(1,1,1,1))
windows()
#gr�fica a partir de la cuadratica obtenida en la interpolaci�n
curve(m2_gauss[1,4]*x^2+m2_gauss[2,4]*x+m2_gauss[3,4], main = "Gr�fica funci�n cuadratica", from = 4410000, to= 5670000,
      type = "l", col ="blue", xlab = "Base Imponible", ylab ="Cuota �ntegra", axes = TRUE, 
      xlim = c(4400000,5700000), ylim = c(1200000, 1900000))

################################
#interpolaci�n de tercer grado
#matriz con la base imponible de la forma y=ax^3+bx^2+cx+d
matriz_incog2 <- matrix(c(4410000^3, 4410000^2, 4410000, 1,
                         4830000^3, 4830000^2, 4830000, 1,
                         5250000^3, 5250000^2, 5250000, 1), 4, 4, byrow = TRUE)

#arreglo con la cuota integra es decir la y de la funci�n interpolaci�n
cuotasIntegras2 <- c(1165978, 1329190, 1501474, 1682830)

#eliminaci�n gaussiana para obtener la matriz soluci�n 
m3_gauss <- gaussianElimination(matriz_incog2, cuotasIntegras2)
gaussianElimination(matriz_incog2, cuotasIntegras2)

#funci�n interpolaci�n
cat(m3_gauss[1,5],"x^3 + ",m3_gauss[2,5], "x^2 + ", m3_gauss[3,5], "x + ", m3_gauss[4,5])

#Gr�fica a partir de la cubica obtenida
par(mar=c(1,1,1,1))
windows()
curve(m3_gauss[1,5]*x^3+m3_gauss[2,5]*x^2+m3_gauss[3,5]*x+m3_gauss[4,5], main = "Gr�fica funci�n cubica", from = 4410000, to= 5670000,
      type = "l", col ="purple", xlab = "Base Imponible", ylab ="Cuota �ntegra", axes = TRUE, 
      xlim = c(4400000,5700000), ylim = c(1700000, 2400000))

