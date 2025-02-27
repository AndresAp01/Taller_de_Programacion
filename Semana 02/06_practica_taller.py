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


#TALLER*************************************************************************#
        
def SumatoriaGrandeDec(n):
    if n==0:
        print(4)
    else:
        i=n
        suma=0
        #i      suma    n
        #2      0       2
        #1      1600    2
        #0      1721    2
        #-1     1722    2
        
        while i>=0:
            suma=suma+((((i**2)*(n**3))+((i**n)+(n**i)))**2)
            #Primera pasada i=2 n=2
            #0+((((2**2)*(2**3))+((2**2)+(2**2)))**2)
            #0+((((4*8)+(4+4))**2)
            #0+((32+8)**2)=0+(40**2)=1600

            #Segunda Pasada i=1 = n=2
            #1600 + ((((1**2)*(2**3))+((1**2)+(2**1)))**2)
            #1600+((1*8)+(1+2))**2)
            #1600+((8+3)**2)=1600+(11**2)=1600+121=1721

            #Tercera pasada i=0 n=2
            #1721+((((0**2)*(2**3))+((0**2)+(2**0)))**2)
            #1721+(((0*3)+(0+1))**2)=1721+1=1722
            
            i=i-1 #1 0 -1
        print(suma) #1722


num=4567890
temp=4567890%10
print(temp)
num=num//10
print(num)

#Escribir una funcion que calcula la cantidad de digitos de un numero
#4567890 tiene 7 digitos

def largo_de_num(num):
    if num==0:
        print(1)
    else:
        cont=0
        #cont   num
        #0      4567890
        #1      456789
        #2
        #3
        #4
        #5
        #6
        #7
        
        while num!=0: #4567890si
            num=num//10
            cont=cont+1
        print(cont)

#Escribir una funcion que recibe un numero de parametro
        #contar la cantidad de digitos pares del numero

def CuentaPares(num):
    if num==0:
        print(1)
    else:
        cont=0
        #cont   num*
        #0      4567890
        #1      456789
        #1      45678
        #2      4567
        #2      456
        #3      45
        #3      4
        
        while num!=0:#4567890si 456789si 45678si 4567 si 456si 45si 4si
            ultimo=num%10#0 9 8 7 6 5 4
            if ultimo%2==0:#0%2si 9%2no 8%2si 7%2no 6%2si 5%2no 4%2si
                cont=cont+1#1 2 3 4
                num=num//10#456789, 4567, 45, 0
            else:
                num=num//10#45678 456 4
        print(cont)#4


#QUIZQUIZ
        #Modificacion para mejora

def CuentaParesMod(num):
    if num==0:
        print(1)
    else:
        cont=0
        #cont   num*
        #0      4567890
        #1      456789
        #1      45678
        #2      4567
        #2      456
        #3      45
        #3      4
        
        while num!=0:#4567890si 456789si 45678si 4567 si 456si 45si 4si
            ultimo=num%10#0 9 8 7 6 5 4
            if ultimo%2==0:#0%2si 9%2no 8%2si 7%2no 6%2si 5%2no 4%2si
                cont=cont+1#1 2 3 4
            num=num//10#456789, 4567, 45, 0
        print(cont)#4

        
#Escribir una funcion que recibe un numero de cualquier tamaño
#Todos los digitos pares del numero van para una variable, elevados a la 3
#Todos los digitos impares del numero van para una variable, elevados a la 2
#Todo se suma

#Igual que este pasado con la corrida

        
"""def SumaParImpar(num):
    if num==0:
        print()
    else:"""
    
