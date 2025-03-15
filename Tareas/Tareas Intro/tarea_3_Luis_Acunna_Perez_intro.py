#Luis Andres Acunna Perez
#Funcion que recibe dos listas del mismo tamanno, validar
#Sumar los elementos de ambas, una destruyendo y una sin destruir

#Funcion 1 Sin Destruir ----------------------------------------------------------------------------------------------

def recibe_listas(lista1,lista2):
    if isinstance(lista1, list) and isinstance(lista2,list) and len(lista1) == len(lista2):
    #Validar que sea lista # Validar mismo tamanno
        longitud = len(lista1)
        resultado = [1] * longitud
        i = 0
        
        while i < longitud:
            resultado[i] = lista1[i] + lista2[i]
            i = i + 1
        return resultado
    else:
        print("Ambos parámetros deben ser listas y deben tener el mismo tamaño")

#Funcion 1 Destruyendo -----------------------------------------------------------------------------------------------

def recibe_lista_D(lista1,lista2):
    if isinstance(lista1, list) and isinstance(lista2,list) and len(lista1) == len(lista2):
        longitud = len(lista1)
        resultado = [1] * longitud

        i = 0

        while i < longitud:
            resultado[i] = lista1[0] + lista2[0]
            lista1 = lista1[1:]
            lista2 = lista2[1:]
            i = i + 1

        return resultado
    else:
        print("Error, las listas deben ser del mismo tamaño. ")

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Funcion 2 Sin Destruir -----------------------------------------------------------------------------------------------

def recibe_numero(num): #123
    if isinstance(num, int): #validar que sea entero
        num=abs(num)         #Transforma a positivo
        #Para determiar si es impar
        temp = num #123, 12, 1, 0
        contador = 0 #0, 1, 2, 3

        #determinar la cantidad de digitos
        while temp > 0: #123si, 12si, 1si
            temp = temp // 10 #12, 1, 0
            contador = contador + 1 #0+1=1, 1+1=2, 2+1
            
        #Si la cantidad es par da error
        if contador%2 == 0: 
            print("Error, el numero debe tener una cantidad impar de digitos")
            return "Ninguno"
            
        pos_medio = contador // 2 #3//2=1, 
        num = num // (10 ** pos_medio) #123//(10**1) = 12
        digito_medio = num % 10 #2 
        #para calcular la posicion del digito
        return digito_medio #2

    else:
        print("Error, debe ser un numero entero")
        return "Ninguno"

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def contar(num):
    temp = num%10
    print(temp) #El que quita
    num=num//10
    print(num) #Lo que sobra
