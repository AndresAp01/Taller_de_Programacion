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
def factorialDEC(num):  # Funciona
    if num < 0 or not type(num) == int:
        print("Parametro de entrada no valido")
    elif num == 0:
        return 1
    else:
        resultado = 1
        i = num
        while i > 0:
            resultado = resultado * i
            i = i - 1
        return resultado


#Funciones para Examen____________________________________________________________________________________
def UNO(num1, num2):
    #45672 #98371
    lista = []
    len1 = largo(num1)
    len2 = largo(num2)
    patron_izq = [1, 0, 1]  # Es el patron que va al principio de la lista
    patron_der = [-1, 0, -1]  # Es el que va al final de la lista
    patron_izq2 = [2, 0, 2]  # Patron al principio al analizar el num2
    patron_der2 = [-2, 0, -2]  # Patron al final al analizar el num2
    centro1 = centronum(num1)
    centro2 = centronum(num2) #innecesario pero lo pongo para no complicarme
    i1_izq = 0
    i2_izq = 0
    i1_der = 0
    i2_der = 0
    # Mientras haya dígitos por procesar en alguno de los números
    while (i1_izq < len1 // 2 and i1_der < len1 // 2):
        # Procesar el centro de num1 (si existe)
        if centro1 != 0:
            lista += [patron_izq + [centro1 + (centro1 - 1)] + [centro1, -centro1] + [centro1 - (centro1 + 1)] + patron_der]
        '''if i_centro < len1:
            centro1 = centronum(num1)  # Obtener el dígito central de num1
            lista += [patron_izq + [centro1 + (centro1 - 1)] + [centro1, -centro1] + [centro1 - (centro1 + 1)] + patron_der]
            i_centro += 1'''

        # Procesar el primer dígito de derecha a izquierda de num2 (si existe)
        if i2_der < len2:
            # Obtener el dígito de derecha a izquierda
            derecha_izquierda2 = (num2 // (10 ** i2_der)) % 10
            sucesor = derecha_izquierda2 + 1
            antecesor = derecha_izquierda2 - 1
            lista += [patron_izq + [derecha_izquierda2 + antecesor] + [derecha_izquierda2, -derecha_izquierda2] + [
                derecha_izquierda2 - sucesor] + patron_der]
            i2_der += 1  # Avanzar al siguiente dígito de num2

        # Procesar el primer dígito de izquierda a derecha de num2 (si existe)
        if i2_izq < len2:
            izquierda_derecha2 = int(str(num2)[i2_izq]) #((num2 // (10 ** (len2 - i2_izq))) % 10)
            sucesor = izquierda_derecha2 + 1
            antecesor = izquierda_derecha2 - 1
            lista += [patron_izq + [izquierda_derecha2 + antecesor] + [izquierda_derecha2, -izquierda_derecha2] + [
                izquierda_derecha2 - sucesor] + patron_der]
            i2_izq += 1

        # Procesar el centro de num2 (si existe)
        if centro2 != 0:
            lista += [patron_izq2 + [centro2 + (centro2 - 1)] + [centro2, -centro2] + [
                centro2 - (centro2 + 1)] + patron_der2]
        ''' if i_centro < len2:
            centro2 = centronum(num2)  # Obtener el dígito central de num2
            lista += [patron_izq2 + [centro2 + (centro2 - 1)] + [centro2, -centro2] + [centro2 - (centro2 + 1)] + patron_der2]
            i_centro += 1 '''


        # Procesar el primer dígito de izquierda a derecha de num1 (si existe)
        if i1_izq < len1:
            izquierda_derecha1 = int(str(num1)[i1_izq]) #(num1 // (10**(len1 - i1_izq))) % 10  # Obtener el dígito de izquierda a derecha
            sucesor = izquierda_derecha1 + 1
            antecesor = izquierda_derecha1 - 1

            lista += [patron_izq2 + [izquierda_derecha1 + antecesor] + [izquierda_derecha1, -izquierda_derecha1] + [izquierda_derecha1 - sucesor] + patron_der2]
            i1_izq += 1  # Avanzar al siguiente dígito de num1

        # Procesar el primer dígito de derecha a izquierda de num1 (si existe)
        if i1_der < len1:
            derecha_izquierda1 = int(str(num1)[len1 - i1_der - 1])  #(num1 // (10**i1_der)) % 10  # Obtener el dígito de derecha a izquierda
            sucesor = derecha_izquierda1 + 1
            antecesor = derecha_izquierda1 - 1
            lista += [patron_izq2 + [derecha_izquierda1 + antecesor] + [derecha_izquierda1, -derecha_izquierda1] + [derecha_izquierda1 - sucesor] + patron_der2]
            i1_der += 1  # Avanzar al siguiente dígito de num1

    return lista  # Devolver la lista de resultados
resultados = UNO(45672, 98361)
print(resultados)
'''i = 0
while i < len(resultados):
    print(resultados[i])
    i += 1'''

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
def TRES():
    pass #MA:ANANNAAAAA

#_________________________________________________________________________________________________________________
#Funcion 4
def CUATRO(n): #SUpongo que funciona
    if isinstance(n, int) and n > 0:
        i = 1
        suma = 0 #inicio variable de suma que almacenara los valores calculados de la variable operacion
        while i <= n: #mintras el indice sea mayor que 1, hago la operacion
            par1 = i ** 2  # nombro variable par1 para simplificar
            par1 = factorialDEC(par1)  # par1 le calculo factorial llanando a la funcion auixiliar de factorial
            par2 = n
            par2 = factorialDEC(par2)  # lo mismo con par2
            numerador = (((par1)**3)**2) * (((n**2)+1)**(n-1)) * (((n-1)+3)**2)
            denominador = ((((3**n) * ((n*(i**2))**i)) + ((par2)**2)) ** 4)
            operacion = (numerador/denominador)
            suma += operacion
            i = i + 1
        print(suma**3)
    else:
        print("Parametro incorrecto, debe ser un numero entero y positivo y diferente de 0")