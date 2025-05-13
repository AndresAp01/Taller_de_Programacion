#Luis Andres Acunna Perez

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
def sumatoria_pila(n):
    if n<0 or type(n)!=int:
        return "Parámetro incorrecto"
    return sumatoria_pila_aux(n, 0, n)

def sumatoria_pila_aux(i, tope, original):
    if i>tope:
        return 0
    f = factorial_CFA(i)
    termino = (f + original**2 * f) ** 3
    return termino + sumatoria_pila_aux(i + 1, tope, original)

#CON COLA
def sumatoria_cola(n):
    if n < 0 or type(n) != int:
        return "Parámetro incorrecto"
    return sumatoria_cola_aux(0, n, n, 0)

def sumatoria_cola_aux(i, tope, original, acumulador):
    if i > tope:
        return acumulador
    f = factorialCola(i)
    termino = (f + original**2 * f) ** 3
    return sumatoria_cola_aux(i + 1, tope, original, acumulador + termino)


print(sumatoria_pila(1))
print(funcion4_Cola(1))
