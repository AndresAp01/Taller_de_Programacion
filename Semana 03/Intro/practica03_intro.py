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

def largo_de_num(num):
    if num==0:
        print(1)
    else:
        cont=0
        
        while num!=0:
            num=num//10
            cont=cont+1
        print(cont)

        
def promedio(num):
    num=abs(num)
    i=n
    suma=0
    while i>=0:
        suma=suma(
        i=i-1
        if num==0:
            print(1)
        else:
            cont=0
            while num!= 0:
                num=num//10
                cont=cont+1
            print(cont)
        print("El promedio es:", //cont)

         
        
        
        
