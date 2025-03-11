#Luis Andres Acunna Perez
#Tarea #3

def funcion1(lista):
    if type(lista)==list:
        if lista==[]:
            return 0, 1

        suma = 0
        multi = 1

        lista_copia = lista[:]
        while lista_copia:
            ultimo = lista_copia[0]
            if ultimo%2==0:
                multi = multi*(ultimo**3)
            else:
                suma = suma+(ultimo**2)

            lista_copia = lista_copia[1:]

        print("La suma de los impares es: ",suma, "y la multipllicacion de lois pares es:", multi)
        return suma, multi

    else:
        print("Debe escribir una lista")
#Suma todos los valores impares y ^2
#Multiplica todos los valores impares y ^3
    
