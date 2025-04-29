"""

- Escribir una función que recibe  un número, tal qu ecuente la cantidad de pares que tiene el num
- Siempre se especifica cuando se agrega el valor absoluto
- Cuando trabajemos en multiplicacion tenemos que poner el contador en 1 si no todo va a dar

Python no es un lenguaje typificado, todo lo toma como objetos, pero cuando entra un flotante, el codigo que
tengo colapsa.

"""

def contapares(num):
    num=abs(num)
    contador=0
    while num != 0:
        if num%2==0:
            contador=contador+1
        num=num+1
        num=num//10
    print(contador)

def contafloat(num):
    if type(num)==int:
        num=abs(num)
        contador=0
        while num != 0:
            if num%2==0:
                contador=contador+1
            num=num//10
        print(contador)
    else:
        print("El parametro no es entero")

#Escribir una funcion que recibe un parametro entero y positivo, y le sacamos el promedio

def largo(num):
    if num==0:
        print(1)
    else:
        cont=0
        
        while num!=0:
            num=num//10
            cont=cont+1
        return(cont)

        
def promedio(num):
    num=abs(num)
    i=n
    suma=0
    while i>=0:
        suma=suma
        i=i-1
        if num==0:
            print(1)
        else:
            cont=0
            while num!= 0:
                num=num//10
                cont=cont+1
            print(cont)
        print("El promedio es:", num//cont)

#--------------------------------------------------------------------------------------------#
#TALLER--------------------------------------------------------------------------------------#

#Escribir una funcion que recibe dos parametros del mismo largo y positivos, reut. largo
    #Sumar los digitos pares de ambos y multiplicar los digitos impares de ambos
#tenemos suma=0, mult=1

#FUNCIONA#
def prac1(num1, num2):
    if type(num1)==int and type(num2)==int and largo(num1)==largo(num2):
        num1=abs(num1)
        num2=abs(num2)
        
        suma=0
        multi=1
        bandera=0

        while num1!=0:
            ultimo=num1%10
            if ultimo%2==0:
                suma=suma+ultimo
            else:
                multi=multi*ultimo
                bandera=1
            num1=num1//10

        while num2!=0:
            ultimo=num2%10
            if ultimo%2==0:
                suma=suma+ultimo
            else:
                multi=multi*ultimo
                bandera=1
            num2=num2//10
        if bandera==1:
            print("La suma es: ",suma," la multiplicación es: ",multi)
        else:
            print("La suma es: ",suma, "la multiplicación es: ", 0)
            

#EL MIO
def prac1luis(num1, num2):
    if type(num1)==int and type(num2)==int and largo(num1)==largo(num2):
        num1=abs(num1)
        num2=abs(num2)

        suma=0
        multi=1
        bandera=0
        
        if num1==0 and num2==0:
            print(0)
        else:
            while num1!=0 and num2!=0:
                ultimo1 = num1%10
                ultimo2 = num2%10
                if ultimo1%2==0 and ultimo2%2==0:
                    suma=suma+ultimo1+ultimo2
                
                else:
                    multi=multi+(ultimo1)*(ultimo2)
                    bandera=1
                    #suma = suma+ultimo
                num1//10
                num2//10
        if bandera==1:
            print("la operacion es", suma and multi)
        else:
            print("la operacion es", suma and 0)
