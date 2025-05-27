#Luis Andres Acunna Perez
#Tarea 8

#Ejercicio 1
def UNO_RC(lista):
    if type(lista)==list:
        if lista==[]:
            return [[], []]
        return UNO_RC_Aux(lista, [], [])
    else:
        print("Error: El argumento debe ser una lista")
        return None

def UNO_RC_Aux(lista, lista_pares, lista_impares):
    if lista==[]:
        return [lista_pares, lista_impares]
    #elemento_actual=numeros[0]
    #resto_numeros=numeros[1:]
    elif lista[0]%2==0:
        #nueva_lista_pares=lista_pares+[elemento_actual]
        return UNO_RC_Aux(lista[1:], lista_pares+[lista[0]], lista_impares)
    else:
        #nueva_lista_impares=lista_impares+[elemento_actual]
        return UNO_RC_Aux(lista[1:], lista_pares, lista_impares+[lista[0]])
#print(UNO_RC([4,5,6,7,8,9,0,1,2,3]))
"""
    PRUEAS:
    print(UNO_RC([4,5,6,7,8,9,0,1,2,3]))
    [[4, 6, 8, 0, 2], [5, 7, 9, 1, 3]]
    
    print(UNO_RC([2,4,6,8]))
    [[2, 4, 6, 8], []]
    
    print(UNO_RC("a"))
    Error: El argumento debe ser una lista
    
"""

#Con recursion de pila
def UNO_PILA(numeros):
    if type(numeros)==list:
        if numeros==[]:
            return [[], []]
        return UNO_PILA_Aux(numeros, 0, [], [])
    else:
        print("Error: El argumento debe ser una lista")
        return None

def UNO_PILA_Aux(numeros, indice, lista_pares, lista_impares):
    if indice>=len(numeros):
        return [lista_pares, lista_impares]
    elemento_actual=numeros[indice]
    if elemento_actual%2==0:
        nueva_lista_pares=lista_pares+[elemento_actual]
        return UNO_PILA_Aux(numeros, indice+1, nueva_lista_pares, lista_impares)
    else:
        nueva_lista_impares=lista_impares+[elemento_actual]
        return UNO_PILA_Aux(numeros, indice+1, lista_pares, nueva_lista_impares)

"""
    PRUBEAS
    print(UNO_PILA([4,5,6,7,8,9,0,1,2,3]))
    [[4, 6, 8, 0, 2], [5, 7, 9, 1, 3]]
    
    print(UNO_PILA([2,4,6,8]))
    [[2, 4, 6, 8], []]
    
    print(UNO_PILA("a"))
    Error: El argumento debe ser una lista

"""
#________________________________________________________________________________
#Ejercicio 2
#Con recursion de cola:
def DOS_RC(lista):
    if isinstance(lista, list):
        if len(lista)!=0:
            if len(lista)%2!=0:
                print(f"Lista Original: {lista}")
                n=len(lista)
                medio=n//2
                print("Lista generada: ")
                return DOS_RC_aux(lista, 0, medio, n, [], n)
            else:
                return "El largo de la lista no es impar"
        else:
            return "La lista esta vacia"
    else:
        return "El parametro no es una lista"

def DOS_RC_aux(lista, i_actual, medio, n, resultado, potencia):
    if i_actual==medio:
        valor_medio=lista[medio]
        return resultado+[valor_medio*valor_medio]
    else:
        suma_izq=i_actual
        suma_der=(n-2)-(i_actual//2)
        sumatoria=lista[suma_izq]+lista[suma_der]
        dif_der=(n-1)-i_actual
        dif_izq=1+(i_actual//2)
        diferencia=lista[dif_der]-lista[dif_izq]

        potencia_suma=sumatoria**potencia
        potencia_diferencia=diferencia**(potencia-1)

        nueva_Lista=resultado+[potencia_suma,potencia_diferencia]
        nueva_potencia=potencia-2
        return DOS_RC_aux(lista, i_actual+1, medio, n, nueva_Lista, nueva_potencia)

"""
    PRUBEAS:
    #1
    print(DOS_RC([6,1,3,4,5]))
    Lista Original: [6, 1, 3, 4, 5]
    Lista generada: 
    [100000, 256, 125, 9, 9]
    #2
    print(DOS_RC([6,1,3,4,5,9,2]))
    Lista Original: [6, 1, 3, 4, 5, 9, 2]
    Lista generada: 
    [170859375, 1, 100000, 4096, 512, 4, 16]
    #3
    print(DOS_RC([]))
    La lista esta vacia
    #4
    print(DOS_RC([2]))
    Lista Original: [2]
    Lista generada: 
    [4]
    #5
    print(DOS_RC("aaa"))
    El parametro no es una lista
    #6
    print(DOS_RC([1,3,5,7,12]))
    Lista Original: [1, 3, 5, 7, 12]
    Lista generada: 
    [32768, 6561, 1000, 16, 25]
"""

#Con recursion de pila:

def DOS_PILA(lista):
    if isinstance(lista, list):
        if lista!=0:
            print(f"Lista original: {lista}")
            n=len(lista)
            if n%2==0:
                return "El largo de la lista no es impar"
            medio=n//2
            exponente_inicial=n
            print("Lista generada: ")
            return DOS_PILA_AUX(lista, 0, medio, n, exponente_inicial)
        else:
            return "La lista esta vacia"
    else:
        return "El parámetro no es una lista"


def DOS_PILA_AUX(lista, i_actual, medio, n, exponente):
    if i_actual==medio:
        return [(lista[medio]*lista[medio])**1]
    else:
        suma_izq=i_actual
        suma_der=(n-2)-(i_actual//2)
        sumatoria=(lista[suma_izq]+lista[suma_der])**exponente
        dif_der=(n-1)-i_actual
        dif_izq=1+(i_actual//2)
        resta=(lista[dif_der]-lista[dif_izq])**(exponente-1)

        resto=DOS_PILA_AUX(lista, i_actual+1, medio, n, exponente-2)

        return [sumatoria, resta]+resto

"""
    PRUBEAS:
    #1
    print(DOS_PILA([6,1,3,4,5]))
    Lista original: [6, 1, 3, 4, 5]
    Lista generada: 
    [100000, 256, 125, 9, 9]
    #2
    print(DOS_PILA([6, 1, 3, 4, 5, 9, 2]))
    Lista original: [6, 1, 3, 4, 5, 9, 2]
    Lista generada: 
    [170859375, 1, 100000, 4096, 512, 4, 16]
    #3
    print(DOS_PILA([1,3,5,7,12]))
    Lista original: [1, 3, 5, 7, 12]
    Lista generada: 
    [32768, 6561, 1000, 16, 25]
    
"""
