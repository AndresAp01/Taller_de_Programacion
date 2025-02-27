#Sumatoria
   #final=n(parametro de trabajo)
    #Sumatoria operacion ((((ielevado2)*(nelevado3))+((ielevadon)+(nelevadoi)))elevado2)
    #inicio i=0
    #Trabajar n=3=> Incremento y decremento

#Si n=0 i=0 ((((0**2)*(0**3))+((0**0)+(0**0)))**2)
            # =  (((0*0)+(1+1))**2) => (0+2)**2 =4
def SumatoriaGrande(n):
    if n==0:
        print(4)
    else:
        i=0
        suma=0
        while i<=n:
            suma=suma+((((i**2)*(n**3))+((i**n)+(n**i)))**2)
            i=i+1
        print(suma)
        
