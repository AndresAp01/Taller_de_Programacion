#Tarea #2 Introduccion a la Progr.
#Luis Andres Acunna Perez

def funcion1(num1, num2):
    if type(num1)==int and type(num2)==int:
        num1=abs(num1)
        num2=abs(num2)
        
        suma=0
        multi=1
        sumadenum=num1+num2
        
        if sumadenum%2==0:
            suma=((num1*num2)**2)
            return suma
        else:
            multi=((num1*num2)**3)
            return multi
        
    
    #Si la suma de los numeros es par, se hace: suma = (num1*num2)**2
    #Si la suma de los numeros es impar, se hace: multi = (num1*num2)**3


def sumatoria(n):
    if n<=1 or not type(n)==int:
        print ("Error, el numero debe ser mayor que 1 y un numero entero")
    suma=0
    i=1    
    while i<=n:
        temp = (i**n)+(n**i)
        suma=suma+((factorialINC(temp)*(2**n))//(n-1))
        i=i+1
    return suma
#--------------
        #Funcion de factorial tomada de la lista auxiliar.

def factorialINC(num): #Funciona
    if num<0 or not type(num)==int:
        print("Parametro de entrada no valido")
    elif num==0:
        return 1
    else:
        resultado=num
        i=1
        while i<num:
            resultado=resultado*i
            i=i+1
        return resultado    
