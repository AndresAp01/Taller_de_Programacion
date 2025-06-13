#Factirual de Cola

def FactorialCola(n):
    if type(n)==int:
        if n==0 or n==1:
            return 1
        else:
            return FactorialC_aux(n-1, 1)
    else:
        print("parametro incorrecto")

def FactorialC_aux(n, resultado):
    if n==0 or n==1:
        return resultado
    else:
        return FactorialC_aux(n-1, resultado*n)

#Factorial de Pila

def Factorial_Pila(n):
    if isinstance(n, int):
        if n==0 or n==1:
            return 1
        else:
            return n*Factorial_Pila(n-1)
    else:
        print("parametro incorrecto")