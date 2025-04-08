#Clase del martes 8 abril
#------------------------------------------------------------------------------------------
#Intro
#------------------------------------------------------------------------------------------
#Recursividad

def Sumatoria_cola(n):
    if type(n)==int:
        if n==0:
            return 0
        else:
            return n + Sumatoria(n-1)

    else:
        print("Parametro Incorrecto")


def SumatoriaC(n):
    if isinstance(n, int):
        if n==0:
            return 0
        else:
            return SumatoriaC_aux(n,0)
    else:
        print("Parametro incorrecto")

def SumatoriaC_aux(n, resultado):
    if n==0:
        return resultado
    else:
        return SumatoriaC_aux(n-1, resultado+n)

def Sumatoria1(n):
    if type(n)==int:
        if n==0:
            return 0
        else:
            return Sumatoria_aux(n)
        
    else:
        print("Parametro incorrecto")

def Sumatoria_aux(n):
    if type(n)==0:
        if n==0:
            return 0
        else:
            return n+Sumatoria_aux(n-1)
        
    else:
        print("Parametro incorrecto")

resultado=SumatoriaC(3)
print(resultado)

def Largo_rec(n):
    if type(n)==int:
        if n==0:
            return 1
        else:
            return Largo_Paux(n)
    else:
        print("parametro incorrecto")

def Largo_Paux(n):
    if n==0:
        return 0
    else:
        return 1+Largo_Paux(n//10)
"""    
resultado=Largo_rec(447)
print(resultado)"""
        
def Factorial_rec(n):
    if n==0 or n==1:
        return 1
    else:
        return n*Factorial_rec(n-1)

def factorial_CFA(n):
    if n==0:
        return 1
    else:
        return FactorialCFA_aux(n)
    
def FactorialCFA_aux(n):
    if n==0:
        return 1
    else:
        return n*FactorialCFA_aux(n-1)
"""resultado=Factorial_rec(32)
print(resultado) """

def FactorialCola(n):
    if type(n)==int:
        if n==0 or n==1:
            return 1
        else:
            return FactorialC_aux(n-1)
    else:
        print("parametro incorrecto")

def FactorialC_aux(n, resultado):
    if n==0 or n==1:
        return resultado
    else:
        return FactorialC_aux(n-1, resultado*n)
    
#Escribir una funcion que recibe un numero entero y positivo+
#Construir un numero nuevo de solo los pares

def ConsNumPares(n):
    if n==0:
        return 0
    ultimo_digito=n%10
    if ultimo_digito%2==0:
        return ConsNumPares(n//10)*10+ultimo_digito
    else:
        return ConsNumPares(n//10)
    
resultado=ConsNumPares(777)
print(resultado)

def Pares(num):
    if type(num)==int:
        num=abs(num)
        if num==0:
            return 0
        else:
            return Pares_aux(abs(num), 0,0,0)
    else:
        print("parametro")

def Pares_aux(num, exponente, resultado, bandera):
    if num==0 and bandera==1:
        return resultado
    elif num==0 and bandera==0:
        return "No hay pares"
    elif (num%10)%2==0:
        return Pares_aux(num//10, exponente+1, resultado+((num%10)*10**exponente), 1)
    else:
        return Pares_aux(num//10, exponente, resultado, bandera)
    

#Escribir 4 funciones calculo del largo de una lista
#Pila destruyendo sin f auxiliar
#Pila sin destruir con f auxiliar
#cola destruyendo
#Cola sin destruir

"""def Func1(lista):
    if type(lista)==list:

    else:"""
#Pila sin destruir
def largo_lista(lista):
    print(lista)
    if lista==[]:
        return 0
    else:
        return 1+largo_lista(lista[1:])

#Pila destruyendo
def largo_lista_DES(lista):
    print(lista)
    if lista==[]:
        return 0
    else:
        return largo_lista(lista[:])
resultado=largo_lista_DES([1,2,3])
print(resultado)
    
def largoPSD(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else:
            return largoPSD_aux(lista, 0)
    else:
        print("Paremetro incorrecto")

def largoPSD_aux(lista, cont):
    if cont==len(lista):
        return 0
    else:
        return 1+largoPSD_aux(lista, cont+1)
    
def largoCD(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else:
            return largoCD_aux(lista, 0)
    else:
        print("Parametro inc")
    

def largoCD_aux(lista, resultado):
    if lista==[]:
        return resultado
    else:
        return largoCD_aux(lista[1:], resultado+1)

def largoCSD(lista):
    if type(lista)==list:
        if lista == []:
            return 0
        else:
            return largoCSD_aux(lsita, 0)
        
    else:
        print("Par incorre")

def largoCSD_aux(lista, resultado):
    if resultado==len(lista):
        return resultado
    else:
        return largoCSD_aux(lista, resultado+1)    
    
return=largoCSD([1,4,5,6,7])
print(resultado)


        
