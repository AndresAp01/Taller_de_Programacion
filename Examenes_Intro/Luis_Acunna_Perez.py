#Luis Andres Acunna Perez
#Codigo Auxiliar___________________________________________________________________________________________
#Largo de un Numero
def largo(num):
    if num == 0:
        print(1)
    else:
        cont = 0
        while num != 0:
            num = num // 10
            cont = cont + 1
        return cont
#Funcion de centro de un numero
def centronum(num): #Funciona
    if isinstance(num, int):
        num = abs(num)
        if largo(num) % 2 != 0:
            pos_centro = (largo(num) - 1) // 2 #porque es impar, se le resta uno para que sea par y se divide entre dos
            cont = largo(num) - 1 #Inicia en la posicion del ultimo digito
            digito_central = 0

            while num != 0:
                ultimo_digito = num % 10
                if cont == pos_centro:
                    digito_central = ultimo_digito
                    break
                num = num // 10
                cont = cont - 1 #Decrece la posicion del ultimo digito
            return digito_central
        else:
            print("Tamaño incorrecto")
    else:
        print("Parametro incorrecto")
#Funcion para pasar numero a lista

def pasalista(num):
    if isinstance(num, int):
        num = abs(num)
        if num >= 0 and num <= 9:
            return [num]
        else:
            listaNueva = []
            while num != 0:
                listaNueva = [num % 10] + listaNueva
                num = num // 10
            return listaNueva
    else:
        print("Parametro incorrecto")

#Funciones para Examen____________________________________________________________________________________
def UNO(num1, num2): #Funcion UNO recibe dos parametros num1 y num2
    if isinstance(num1, int) and isinstance(num2, int):
        #Esto verifica que el num1 y el num2 sean enteros
        num1 = abs(num1)  # Para hacerlos positivos siempre
        num2 = abs(num2)
        #Doy valores a las variables
        patron_izq = [1, 0, 1]  # Es el patron que va al principio de la lista
        patron_der = [-1, 0, -1]  # Es el que va al final de la lista
        patron_izq_2 = [2, 0, 2]  # Patron al principio al analizar el num2
        patron_der_2 = [-2, 0, -2]  # Patron al final al analizar el num2
        #Para que sean del mismo tamanno:
        if largo(num1) >= 3 and largo(num2) >= 3 and largo(num1) == largo(num2):

            #Procesando el num1
            antecesor = 0
            sucesor = 0
            centro_num1 = centronum(num1)  # Para encontrar el centro del num1
            while num1 != 0:
                ultimo_digito_num1 = num1 % 10  # Extraer el último dígito
                num1 = num1 // 10  # Eliminar el último dígito

                if num1 % 10 == centro_num1:  # Si el siguiente dígito es el central
                    sucesor = ultimo_digito_num1  # El sucesor es el dígito actual
                if ultimo_digito_num1 == centro_num1:  # Si el dígito actual es el central
                    antecesor = num1 % 10  # El antecesor es el siguiente dígito
            print(antecesor, sucesor)

            lista_nueva_num1 = patron_izq + [centro_num1 + antecesor] + [centro_num1, -centro_num1] + [centro_num1 - sucesor] + patron_der
            print(lista_nueva_num1)

            #Procesando el Num2
            antecesor_2 = None
            sucesor_2 = None
            centro_num2 = centronum(num2)  # para encontrar el centro del num2
            while num2 != 0:
                ultimo_digito_num2 = num2 % 10  # Extraer el último dígito
                num2 = num2 // 10  # Eliminar el último dígito

                if num2 % 10 == centro_num2:  # Si el siguiente dígito es el central
                    sucesor_2 = ultimo_digito_num2  # El sucesor es el dígito actual
                if ultimo_digito_num2 == centro_num2:  # Si el dígito actual es el central
                    antecesor_2 = num2 % 10  # El antecesor es el siguiente dígito
            print(antecesor_2, sucesor_2)
            lista_nueva_num2 = patron_izq_2 + [centro_num2 + antecesor_2] + [centro_num2, -centro_num2] + [
                centro_num2 - sucesor_2] + patron_der_2
            print(lista_nueva_num2)

            #despues = pass_none
        else:
            print("Ambos numeros deben tener mas de 3 digitos")
    else:
        print("El numero debe ser entero y tener mas de 3 digitos")

#UNO(45672,98361)

#_________________________________________________________________________________________________________________
#Funcion 2
def DOS(num): #Funciona
    if isinstance(num, int):
        lista = pasalista(num) # Convierto el número a una lista usando la función "pasalista".
        contador_ceros = 1 #Para llevar la cuenta de cuantos ceros aparecen.
        nueva_lista = []
        i = 0  # Para recorrer la lista usando un indice "i"
        while i < len(lista): #Mientras el indice sea menor al largo de la lista
            if lista[i] == 0:  # Si encontramos un 0 en el indice "i":
                sublista = [1, 0, 1, contador_ceros, 0, 1, 0]  # Inicializo una variable Sublista
                nueva_lista = nueva_lista + [sublista] #A la nueva lista le concateno la sublista
                contador_ceros += 1  # Incrementar el contador de ceros
            else:
                nueva_lista = nueva_lista + [lista[i]] #Usando concatenacion, le agrego el digito actual
            i += 1  # Avanzar al siguiente elemento

        return nueva_lista  # Devolver la lista modificada
    else:
        print("Parametro incorrecto, debe ser un numero entero")

#_________________________________________________________________________________________________________________
#Funcion 3



