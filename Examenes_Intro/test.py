def largoRC(num):
    if type(num)==int:
        if num==0:
            return 0
        else:
            return largo_aux(num, 0)
    else:
        print("parametro incorrecto")

def largo_aux(num, contador):
    if num==0:
        return contador
    else:
        return largo_aux(num//10, contador+1)

#######################################################
def UNO(num1, num2):
    """
    - Toma |num1| y |num2|, valida que sean enteros de igual longitud
      y llama a UNO_aux sólo si pasan las validaciones.
    - Evita tener múltiples 'if' seguidos usando 'elif' y un único bloque final.
    """
    # Trabajar con valores absolutos
    num1, num2 = abs(num1), abs(num2)

    # Validación combinada con if/elif
    if not (isinstance(num1, int) and isinstance(num2, int)):
        mensaje_error = "num1 y num2 deben ser enteros."
    elif largoRC(num1) != largoRC(num2):
        mensaje_error = "Ambos números deben tener la misma cantidad de dígitos."
    else:
        # Sólo si pasó ambas comprobaciones
        return UNO_aux(num1, num2, largoRC(num1), 0)

    # Si hubo error, lo mostramos y salimos
    print(mensaje_error)
    return
def UNO_aux(num1, num2, largo, indice_actual):
    if indice_actual >= largo:
        return []
    cantidad_pares   = (largo + 1) // 2
    cantidad_impares = largo // 2
    odd_max  = largo - 2 + ((largo - 1) % 2)
    even_max = largo - 2 + (1 - ((largo - 1) % 2))
    posicion_primer = (
        2 * indice_actual
        if indice_actual < cantidad_pares
        else odd_max - 2 * (indice_actual - cantidad_pares)
    )
    posicion_segundo = (
        2 * indice_actual + 1
        if indice_actual < cantidad_impares
        else even_max - 2 * (indice_actual - cantidad_impares)
    )

    dig1_encontrado = (num1 // (10 ** (largo - 1 - posicion_primer))) % 10
    dig2_encontrado = (num2 // (10 ** (largo - 1 - posicion_segundo))) % 10
    sucesor1, antecesor1 = dig1_encontrado + 1, dig1_encontrado - 1
    sucesor2, antecesor2 = dig2_encontrado + 1, dig2_encontrado - 1

    digito_primer = [1, 0, 1,sucesor1,dig1_encontrado,sucesor1 + dig1_encontrado - antecesor1,antecesor1, -1, 0, -1]
    digito_segundo = [-2, 0, -2,sucesor2,dig2_encontrado,sucesor2 + dig2_encontrado - antecesor2,antecesor2, 2, 0, 2]
    return [digito_primer, digito_segundo] + UNO_aux(num1, num2, largo, indice_actual + 1)

print(UNO(123, 456))
#######################################################
def TRES(num, numincluir, cantidad, numbuscar):
    if type(num)==int and type(numincluir)==int and type(cantidad)==int and type(numbuscar)==int:
        num=abs(num)
        cantidad=abs(cantidad)
        numbuscar=abs(numbuscar)
        if num==0:
            print("Numero original:",num)
            print("Esto da error. El número buscado no se encontró")
            return "lista:",[0]
        else:
            resultado=TRES_aux(num,numincluir,cantidad,numbuscar,1)
            if resultado[1]==1:
                print("Numero original:",num)
                print("Lista:",resultado[0])
            else:
                print("Numero original:",num)
                print("Esto da error. El número buscado no se encontró")
    return True

def TRES_aux(num,numincluir,cantidad,numbuscar,cont):
    if num==0:
        return [[],0,cont]
    else:
        resto=TRES_aux(num//10,numincluir,cantidad,numbuscar,cont)
        resto_lista=resto[0]
        encontrado=resto[1]
        cont=resto[2]
        digito=num%10
        if digito==numbuscar:
            sublista=[numbuscar-1]+[1, 0, 1]+[numincluir]*cantidad+[digito**cont,-digito]+[numincluir]*cantidad+[0,-1,0]+[numbuscar+1]
            return [resto_lista+[sublista],1,cont+1]
        else:
            return [resto_lista+[digito],encontrado,cont]

print(TRES(123456, 789123, 3, 4))

def TRES(num, numincluir, cantidad, numbuscar):
    if type(num)==int and type(numincluir)==int and type(cantidad)==int and type(numbuscar)==int: #verifica que los tipos sean enteros
        num=abs(num) #valor absoluto a los parametros
        cantidad=abs(cantidad) #valor absoluto a los parametros
        numbuscar=abs(numbuscar) #valor absoluto a los parametros
        print("Numero original:",num) #imprime el numero original
        if num==0 and  numbuscar==0: #verifica si el numero es 0
            central=[numincluir]*cantidad #saca la cantidad del numero a insertar
            lista=[[-1]+[1]+[0]+[1]+central+[0,0]+central+[0]+[1]+[0]+[1]] #saca la lista con cierto patron
            return lista #retorna la lista
        else:
            print("Lista:",TRES_aux(num,numincluir,cantidad,numbuscar,1,[])) #imprime la lista rescursiva
    return True

def TRES_aux(num,numincluir,cantidad,numbuscar,cont,lista):
    if num<=0: #verifica si el numero es menor o igual a 0
        return lista #retorna la lista
    digito=(num//(10**(largoRC(num)-1)))%10 #saca el digito de la posicion
    if digito==numbuscar: #verifica si el digito es igual al buscado
        inicio=[numbuscar-1]+[1,0,1] #saca el inicio
        central1=[numincluir]*cantidad #saca la cantidad del numero a insertar
        potencia=[digito**cont] #saca la potencia del digito
        negativo=[-1*numbuscar] #saca el negativo del digito
        central2=[numincluir]*cantidad #saca la cantidad del numero a insertar
        fin=[0,-1,0]+[numbuscar+1] #saca el fin
        cuerpo=inicio+central1+potencia+negativo+central2+fin #saca el cuerpo final de lista
        num=num%(10**(largoRC(num)-1)) #quita el primer digito del numero
        cont+=1 #suma 1 al contador
        lista+=[cuerpo] #agrega a la lista con cierto patron
        return TRES_aux(num,numincluir,cantidad,numbuscar,cont,lista) #retorna la funcion auxiliar con los nuevos parametros
    else:
        lista+=[digito] #agrega a la lista si no es igual al buscado
        num=num%(10**(largoRC(num)-1)) #quita el primer digito del numero
        return TRES_aux(num,numincluir,cantidad,numbuscar,cont,lista) #retorna
