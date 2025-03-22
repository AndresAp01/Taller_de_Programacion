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
            print("Tamaño incorrecto")
    else:
        print("Parametro incorrecto")

def sucesor_central(num):
    if isinstance(num, int):  # Verificar que el parámetro sea un entero
        num = abs(num)  # Convertir a positivo
        centro = centronum(num)  # Obtener el dígito central usando la función centronum
        sucesor = None  # Variable para almacenar el sucesor

        while num != 0:
            digito = num % 10  # Extraer el último dígito
            num = num // 10  # Eliminar el último dígito
            if digito == centro:  # Si encontramos el dígito central
                sucesor = num % 10  # El sucesor es el siguiente dígito
                break  # Salir del bucle

        return sucesor  # Devolver el sucesor
    else:
        print("El parámetro debe ser un número entero.")

print(sucesor_central(13456))

def antecesor_central(num):
    if isinstance(num, int):  # Verificar que el parámetro sea un entero
        num = abs(num)  # Convertir a positivo
        centro = centronum(num)  # Obtener el dígito central usando la función centronum
        antecesor = None  # Variable para almacenar el antecesor

        while num != 0:
            digito = num % 10  # Extraer el último dígito
            num = num // 10  # Eliminar el último dígito
            if num % 10 == centro:  # Si el siguiente dígito es el central
                antecesor = digito  # El antecesor es el dígito actual
                break  # Salir del bucle

        return antecesor  # Devolver el antecesor
    else:
        print("El parámetro debe ser un número entero.")
print(antecesor_central(13456))