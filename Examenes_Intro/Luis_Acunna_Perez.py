#Luis Andres Acunna Perez
#Codigo Auxiliar___________________________________________________________________________________________
def largo(num):
    if num == 0:
        print(1)
    else:
        cont = 0
        while num != 0:
            num = num // 10
            cont = cont + 1
        return cont
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
            print("Tamaño incorrecto, debe tener una cantidad impar de digitos.")
    else:
        print("Parametro incorrecto, debe ser un numero entero. ")
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
    if isinstance(num1, int) and isinstance(num2, int) and largo(num1)==largo(num2):
        #45672 #98371
        lista = [] #Empiezo una lista vacia donde iran todas las sublistas
        #No hay listas intermedias, se suma ' lista ' consigo misma y se actualiza en cada iteracion o vuelta
        len1 = largo(num1) #Variable len1 para obtener el largo del num1
        len2 = largo(num2) #Variable len2 para obtener le largo del num2
        patron_izq = [1, 0, 1]  # Es el patron que va al principio de la lista al procesar el num1
        patron_der = [-1, 0, -1]  # Es el que va al final de la lista al procesar el num1
        patron_izq2 = [2, 0, 2]  # Patron al principio al analizar el num2
        patron_der2 = [-2, 0, -2]  # Patron al final al analizar el num2

        i1_izq = 0 #indice del num1 de izquierda a derecha
        i2_izq = 0 #indice del num2 de izquierda a derecha
        i1_der = 0 #indice del num1 de derecha a izquierda
        i2_der = 0 #indice del num2 de derecha a izquierda
        i_centro = 0 #indice del centro innecesario pero para seguir la misma logica

        while i1_izq < len1 // 2 and i1_der < len1 // 2:
            #Mientras el indice num 1 de izq a derecha // 2 y indice num 1 de der a izq // 2 Para que se detenga al llegar al cetnro

            if i_centro < len1: #Si el centro es menor que el largo del num
                centro1 = centronum(num1)  # Obtener el dígito central de num1
                #La lista se suma con otra lista adentro, que va: [patron, centro+antecesor, centro, negativo, centro - sucesor, patron]
                lista += [patron_izq + [centro1 + (centro1 - 1)] + [centro1, -centro1] + [centro1 - (centro1 + 1)] + patron_der]

            if i2_der < len2: #Si el indice es menor al largo del num2
                # i2_der = 0
                # i2_der = 1
                derecha_izquierda2 = (num2 // (10 ** i2_der)) % 10
                #digito = 98361 // 10**(0) %10 = 1
                # digito = 98361 // 10**(1) %10 = 6
                sucesor = derecha_izquierda2 + 1 #Defino sucesor como el digito + 1 (porque es en la recta numerica)
                #sucesor = 2
                antecesor = derecha_izquierda2 - 1 #Antecesor como el digito - 1
                #antecesor = 0
                lista += [patron_izq + [derecha_izquierda2 + antecesor] + [derecha_izquierda2, -derecha_izquierda2] + [derecha_izquierda2 - sucesor] + patron_der]
                i2_der += 1  # Avanzar al siguiente dígito de num2

            if i2_izq < len2:
                #Para encontrar el digito de izquierda a derecha
                izquierda_derecha2 = (num2 // (10 ** (len2 - i2_izq - 1))) % 10
                #digito = 98361 // 10 ** (5 - 0 - 1) %10
                #digito = 9
                # digito = 98361 // 10 ** (5 - 1 - 1) %10
                #digito = 8
                print(izquierda_derecha2)
                sucesor = izquierda_derecha2 + 1
                antecesor = izquierda_derecha2 - 1
                lista += [patron_izq + [izquierda_derecha2 + antecesor] + [izquierda_derecha2, -izquierda_derecha2] + [izquierda_derecha2 - sucesor] + patron_der]
                i2_izq += 1

            if i_centro < len2:
                centro2 = centronum(num2)  # Defino el dígito central de num2
                lista += [patron_izq2 + [centro2 + (centro2 - 1)] + [centro2, -centro2] + [centro2 - (centro2 + 1)] + patron_der2]
                i_centro += 1

            # Se invierte el proceso para que ahora sea primero de izquierda a derecha y leugo de der a izq
            if i1_izq < len1:
                izquierda_derecha1 = (num1 // (10 ** (len1 - i1_izq - 1))) % 10
                #digito = ()
                sucesor = izquierda_derecha1 + 1
                antecesor = izquierda_derecha1 - 1

                lista += [patron_izq2 + [izquierda_derecha1 + antecesor] + [izquierda_derecha1, -izquierda_derecha1] + [izquierda_derecha1 - sucesor] + patron_der2]
                i1_izq += 1  # Avanzar al siguiente dígito de num1

            # Procesar el primer dígito de derecha a izquierda de num1 (si existe)
            if i1_der < len1:
                derecha_izquierda1 = (num1 // (10 ** i1_der)) % 10 # int(str(num1)[len1 - i1_der - 1])  #(num1 // (10**i1_der)) % 10  # Obtener el dígito de derecha a izquierda
                sucesor = derecha_izquierda1 + 1
                antecesor = derecha_izquierda1 - 1
                lista += [patron_izq2 + [derecha_izquierda1 + antecesor] + [derecha_izquierda1, -derecha_izquierda1] + [derecha_izquierda1 - sucesor] + patron_der2]
                i1_der += 1  # Avanzar al siguiente dígito de num1

        return lista  # Devolver la lista de resultados
    else:
        print("Parametros incorrectos, deben ser numeros enteros, debe tener una cantidad impar de digitos y ambos del mismo largo. \n Por ejemplo, num1: 123 y num2: 456")
        return 0
resultados = UNO(45672, 98361)
print(resultados)
i = 0
while i < len(resultados):
    print(resultados[i])
    i += 1

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
def TRES(num1, num2):
    #45672 #98371
    if isinstance(num1, int) and isinstance(num2, int):

        lista = []
        len1 = largo(num1)
        len2 = largo(num2)
        patron_izq = [-1, 0, -1]  # Es el patron que va al principio de la lista
        patron_der = [0, 1, 0]  # Es el que va al final de la lista
        patron_izq2 = [2, 0, 2]  # Patron al principio al analizar el num2
        patron_der2 = [0, -2, 0]  # Patron al final al analizar el num2
        patron_centro_izq = [3 ,0 , 3]
        patron_centro_der = [0, -3, 0]

        centro1 = centronum(num1)
        centro2 = centronum(num2)
        #Les doy nombres mas complejos a los indices para que sea facil de entender
        indice_num1_izq_a_der = 0 #
        indice_num1_der_a_izq = 0 #
        indice_num2_centro_a_derecha = (len2 // 2) - 1 #1 #0
        indice_num2_centro_a_izq = (len2 // 2) + 1 #3 #4 #5

        # Mientras haya dígitos por procesar en alguno de los números
        while indice_num2_centro_a_izq > len2 or indice_num2_centro_a_derecha>=0:
        #while indice1_izqader <= indice1_deraizq and indice_num2_centro_a_derecha <= indice2_deraizq:
            if indice_num2_centro_a_izq < len2:  # Si hay dígitos restantes en num2 1>0 si #FUNCIONA
                #3 < 5 si
                #4 < 5 si
                #5 < 5 no
                digito_izq_num2 = (num2 // (10 ** indice_num2_centro_a_izq)) % 10
                #dig = 98361 // 10 ** 3 %10
                #dig = 8
                #dig = 98361 // 10 ** 4 %10
                #dig = 9
                lista += [patron_izq + [(centro1 + digito_izq_num2) ** 2] + patron_der]
                indice_num2_centro_a_izq += 1

            if indice_num2_centro_a_derecha >= 0: #FUNCIONA
                #1 >= 0 si
                #0 >= 0 si
                #-1 >= 0 no
                digito_izq_num2 = (num2 // (10 ** indice_num2_centro_a_derecha)) % 10
                #dig = 98361 // 10 ** 1 %10
                #dig = 6
                # dig = 98361 // 10 ** 0 %10
                # dig = 1
                lista += [patron_izq + [(centro1 + digito_izq_num2)**2] + patron_der]
                indice_num2_centro_a_derecha -= 1

            if indice_num1_der_a_izq >= 0:
                digito = (num1 // (10 ** indice_num1_der_a_izq)) % 10
                lista += [patron_izq2 + [(centro2 * digito)**3] + patron_der2]
                indice_num1_der_a_izq += 1

            if indice_num1_izq_a_der >= 0:
                digito = (num1 // (10 ** (len1 - indice_num1_izq_a_der - 1))) % 10
                print(digito)
                lista += [patron_izq2 + [(centro2 * digito)**3] + patron_der2]
                indice_num1_izq_a_der += 1

            # Al final, agregar una última lista con la suma de los centros de ambos números
        lista = lista + [[patron_centro_izq + [(centro1 + centro2)**(len1 - 2)] + patron_centro_der]]

        return lista  # Devolver la lista de listas
    else:
        print("Parametros incorrecto, ambos deben ser numeros enteros, del mismo largo y cantidad de digitos impar \n Por ejemplo: 123, 456")
'''(45672, 98361)
resultados = TRES(1456725, 6983617)
print(resultados)
i = 0
while i < len(resultados):
    print(resultados[i])
    i += 1'''
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