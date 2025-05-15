#Luis Andres Acunna Perez
#auxiliar de factorial
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
#CON PILA
def suma_pila(n):
    return (suma_pila_aux(n, 0))**3

def suma_pila_aux(n, i):
    if i>n:
        return 0
    f=factorial_CFA(i)*(1+n**2)
    return f+suma_pila_aux(n, i+1)

#CON COLA
def suma_cola(n):
    return (suma_cola_aux(n, 0, 0))**3

def suma_cola_aux(n, i, acumulado):
    if i>n:
        return acumulado
    f=factorial_CFA(i)*(1+n**2)
    return suma_cola_aux(n, i+1, acumulado+f)

"""
Prueba
n=1
print("Pila:", suma_pila(n))
print("Cola:", suma_cola(n))
Pila: 8000
Cola: 8000

n=2
print("Pila:", suma_pila(n))
print("Cola:", suma_cola(n))
Pila: 8000
Cola: 8000
"""
