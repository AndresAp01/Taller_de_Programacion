#Clase Jueves 6 Intro
#type(parametro)==tipo
#return si se ejecuta dentro del ciclo, rompe el ciclo
#break rompe el ciclo

#La siguiente tarea se revisa con el asistente
#Cita de revision

#----------------------------------------------------------------
"""Que es un factorial
Parametro n
Si n < 0 no esta definito, no se puede trabajar con valor absoluto
Si n = 0 por definicion, es igual al valor "1"
Si n > 0 se define n * (n-1) * (n-1) ... hasta que n = 0


#Escribir una funcion que recibe un parametro que debe ser entero y mayor
o igual para aplicar le factorial """

def factorialINC(num): #Funciona
    if num<0 or not type(num)==int:
        print("Parametro de entrada no valido")
    elif num==0:
        return 1
    else:
        #resultado  i   num
        #4          1   4
        #4          2   4
        #8          3   4
        #24         4   4
        
        resultado=num
        i=1
        while i<num: #1<4? si 2<4 si 3<4si 4<4no
            resultado=resultado*i
            #4*1=4 4*2=8 8*3=24
            i=i+1#2 3 4
        return resultado #24

def factorialDEC(num): #Funciona
    if num<0 or not type(num)==int:
        print("Parametro de entrada no valido")
    elif num==0:
        return 1
    else:
        #resultado  i   num
        #1          4   4
        #4          3   4
        #12         2   4
        #24         1   4
        #24         0   4
        
        resultado=1
        i=num
        while i>0:#4>0 si 3>0 si 2>0si 1>0 SI 0>0X
            resultado=resultado*i
            #1*4=4 4*3=12 12*2=24 24*1=24
            i=i-1#3 2 1 0
        return resultado #24
        
def SumatoriaFacto(num):
    #El numero debe empezar en 1
    if num>0 and type(num)==int:
        suma=0
        i=1
        #suma   i   num
        #0      1   4
        #0      2   4
        #3      3   4
        #9      4   4
        #33     5   4
        
        while i<=num:#1<=4 si 2<=4 si 3<=4 si 4<=4 si 5<=4 no
            suma=suma+(factorialINC(i))
            #0+(factorial(1))=0+1=1
            #1+(factorial(2))=1+2=3
            #3+(factorial(3))=3+6=9
            #9+(factorial(4))=9+24=33
            
            i=i+1 #2 3 4
        print(suma)
    else:
        print("Parametro incorrecto")

#Escribir una funciomn que recibe un numero entero uy positivo
        #para calcular la siguiente sumatoria

def SumatoriaFacto2(num): #n=1
    if num<0 or not type(num)==int:
        print("Parametro de entrada no valido")
    elif num==0:
        return
    else:
        #suma   i   num
        #0      0   1
        #1      1   1
        #3      2   1
        
        suma=0
        i=0
        while i<=num:#0<=1 si 1<=1 si 2<=1 no
            suma=suma+((i*num)+((factorialINC(i)**2)*(factorialINC(i)**3)))
            #i=0 num=1
            #0=0+((0*1)+((factorialINC(0)**2)*(factorialINC(0)**3)))
            #0=0+((0)+((1**2)*(1**3))))
            #0+((0)+(1*1))=1

            #i=1 num=1
            #1=1+((1*1)+((factorialINC(1)**2)*(factorialINC(1)**3)))
            #1=1+((1)+((1**2)*(1**3))))
            #1+((1)+(1*1))=1+(1+1) = 3
            i=i+1 #1 2
        return suma #retorna

#-------------------------------------------------------------------
#Escribir una funcion que permite saber si un numero tiene un digito par
#Recibe un numero entero y positivo, si llega a negativo, puede utilizar abs()
#Retornar True or False (booleana)
#num=23456789
#    =3579 False
#    =35769 True

def espar(num): #Funciona #57891
    if not type(num)==int:
        print("Parametro incorrecto")
    elif num==0 or num==2 or num==4 or num==6 or num==8:
        return True
    else:
        
        haypar=False #Equivale a una bandera
        #y saquemosle una copia al numero para no eliminar el original
        copia=abs(num)

        #copia  espar   num
        #57891  False   57891
        #5789   False   57891
        #578   False   57891
        
        while copia!=0: #57891si 5789 578 si
            temp=copia%10 #1 9
            if temp%2==0: #1%2 no 9%2 no 8%2si
                haypar=True #TRUE
                break #Para porque ya encontró UNO no hace falta buscar más
            copia=copia//10 #5789 578
        return haypar, copia
