#Luis Andres Acunna Perez - Luis Andrés Acuña Pérez
#Codigo Auxiliar___________________________________________________________________________________________
#Funcion largo() que obtiene el largo de un numero
def largo(num):
    if num == 0:
        print(1)
    else:
        cont = 0
        while num != 0:
            num = num // 10
            cont = cont + 1
        return cont
#Funcion centronum() que consigue el centro de un numero impar
def centronum(num): #Funciona
    if isinstance(num, int):
        num = abs(num)
        if largo(num) % 2 != 0:
            pos_centro = (largo(num) - 1) // 2
            cont = largo(num) - 1
            digito_central = 0

            while num != 0:
                ultimo_digito = num % 10
                if cont == pos_centro:
                    digito_central = ultimo_digito
                    break
                num = num // 10
                cont = cont - 1
            return digito_central
        else:
            print("Tamaño incorrecto, debe tener una cantidad impar de digitos.")
    else:
        print("Parametro incorrecto, debe ser un numero entero. ")
#Funcion pasalista() que pasa un numero a una lista
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
#Funcion factorialDEC() que obtiene el factorial de un numero decreciendo
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
'''Variables utilizadas:
    lista : Empiezo una lista vacia donde iran todas las sublistas (solo se usa una lista, no hay intermedias)
    len1 : Variable len1 para obtener el largo del num1 
    len2 : Variable len2 para obtener le largo del num2
    patron_izq : Es el patron que va al principio de la lista al procesar el num1
    patron_der : Es el que va al final de la lista al procesar el num1
    patron_izq2 : Patron al principio al analizar el num2
    patron_der2 : Patron al final al analizar el num2
    i1_izq : indice del num1 de izquierda a derecha
    i2_izq : indice del num2 de izquierda a derecha
    i1_der : indice del num1 de derecha a izquierda
    i2_der : indice del num2 de derecha a izquierda
    i_centro : indice del centro innecesario pero para seguir la misma logica
    
    centro1 : obtiene el centro del num1
    centro2 : obtiene el centro del num2
    sucesor = (digito) + 1 : Defino sucesor como el digito + 1 (porque es en la recta numerica)
    antecesor = (digito) - 1 #Antecesor como el digito - 1
        (digito) son las siguientes variables;
    derecha_izquierda2 : es el digito de derecha a izquierda del num2
    izquierda_derecha2 : es el digito de izquierda a derecha del num2
    izquierda_derecha1 : es el digito de izquierda a derecha del num1
    derecha_izquierda1 : es el digito de derecha a izquierda del num1
    '''
def UNO(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int) and largo(num1)==largo(num2):
        #45672 #98371
        lista=[]
        len1=largo(num1)
        len2=largo(num2)
        patron_izq=[1, 0, 1]
        patron_der=[-1, 0, -1]
        patron_izq2=[2, 0, 2]
        patron_der2=[-2, 0, -2]

        i1_izq=0
        i2_izq=0
        i1_der=0
        i2_der=0
        i_centro=0

        while i1_izq<len1//2 and i1_der<len1//2:
            if i_centro<len1:
                centro1=centronum(num1)
                lista += [patron_izq+[centro1+(centro1-1)]+[centro1, -centro1]+[centro1-(centro1+1)]+patron_der]

            if i2_der<len2:
                derecha_izquierda2=(num2//(10**i2_der))%10
                sucesor=derecha_izquierda2+1
                antecesor=derecha_izquierda2-1
                lista += [patron_izq+[derecha_izquierda2+antecesor]+[derecha_izquierda2,-derecha_izquierda2]+[derecha_izquierda2-sucesor]+patron_der]
                i2_der += 1

            if i2_izq<len2:
                izquierda_derecha2=(num2//(10**(len2-i2_izq-1)))%10
                print(izquierda_derecha2)
                sucesor=izquierda_derecha2+1
                antecesor=izquierda_derecha2-1
                lista += [patron_izq+[izquierda_derecha2+antecesor]+[izquierda_derecha2,-izquierda_derecha2]+[izquierda_derecha2-sucesor]+patron_der]
                i2_izq += 1

            if i_centro<len2:
                centro2=centronum(num2)
                lista += [patron_izq2 + [centro2 + (centro2 - 1)] + [centro2, -centro2] + [centro2 - (centro2 + 1)] + patron_der2]
                i_centro += 1

            if i1_izq<len1:
                izquierda_derecha1=(num1//(10**(len1-i1_izq-1)))%10
                sucesor=izquierda_derecha1+1
                antecesor=izquierda_derecha1-1
                lista += [patron_izq2+[izquierda_derecha1+antecesor]+[izquierda_derecha1, -izquierda_derecha1]+[izquierda_derecha1-sucesor]+patron_der2]
                i1_izq += 1

            if i1_der<len1:
                derecha_izquierda1=(num1//(10**i1_der))%10
                sucesor=derecha_izquierda1+1
                antecesor=derecha_izquierda1-1
                lista += [patron_izq2+[derecha_izquierda1+antecesor]+[derecha_izquierda1, -derecha_izquierda1]+[derecha_izquierda1-sucesor]+patron_der2]
                i1_der += 1

        return lista
    else:
        print("Parametros incorrectos, deben ser numeros enteros, debe tener una cantidad impar de digitos y ambos del mismo largo. \n Por ejemplo, num1: 123 y num2: 456")
        return 0

print(UNO(33445, 21345))
#_________________________________________________________________________________________________________________
#Funcion 2
''' 
lista : Convierto el número a una lista usando la función "pasalista".
lista_2 : Inicio una lista vacia donde ira cada iteracion de la sublista
contador_ceros : Para llevar la cuenta de cuantos ceros aparecen.
i : Para recorrer la lista del num usando un indice "i"
sublista : una lista con el patron y el contador de 0s
'''
def DOS(num): #Funciona
    if isinstance(num, int):
        lista=pasalista(num)
        contador_ceros=1
        lista_2=[]
        i=0
        while i<len(lista):
            if lista[i]==0:
                sublista=[1, 0, 1, contador_ceros, 0, 1, 0]
                lista_2=lista_2+[sublista]
                contador_ceros += 1
            else:
                lista_2=lista_2+[lista[i]]
            i += 1
        return lista_2
    else:
        print("Parametro incorrecto, debe ser un numero entero")
#_________________________________________________________________________________________________________________
#Funcion 3

''' que
lista : inicio una lsita vacia
len1 : llama a la funcion aux largo y obtiene el alrgo del num1
len2 : llama a largo y obtiene el largo del num2
patron_izq : patron a la izquierda del num1
patron_der : patron a la derecha del num1
patron_izq2 : patron a la izquierda del num2
patron_der2 : patron a la derecha del num2
patron_centro_izq : patron del centro izq
patron_centro_der : patron del centro der

centro1 : llama a centronum() y obtiene el centro del numero1
centro2 : llama a centronum() y obtiene el centro del numero2
digito : variable del digito que se esta buscando en cada if

indice_num1_izq_a_der : indice del num1 de izquierda a derecha
indice_num1_der_a_izq : indice del num1 de derecha a izquierda

indice_num2_centro_a_derecha : indice del num2 del centro a la derecha
indice_num2_centro_a_izq : indice del num2 del centro a la izquierda

#Hice la siguiente prueba corta en dos ifs para probar que funcionaran
            if indice_num2_centro_a_izq<len2:
                #3 < 5 si
                #4 < 5 si
                #5 < 5 no
                digito_izq_num2=(num2//(10**indice_num2_centro_a_izq))%10
                #dig = 98361 // 10 ** 3 %10
                #dig = 8
                #dig = 98361 // 10 ** 4 %10
                #dig = 9
                lista += [patron_izq+[(centro1+digito_izq_num2)**2]+patron_der]
                indice_num2_centro_a_izq += 1

            if indice_num2_centro_a_derecha>=0: #FUNCIONA
                #1 >= 0 si
                #0 >= 0 si
                #-1 >= 0 no
                digito_izq_num2=(num2//(10**indice_num2_centro_a_derecha))%10
                #dig = 98361 // 10 ** 1 %10
                #dig = 6
                # dig = 98361 // 10 ** 0 %10
                # dig = 1
                lista+=[patron_izq+[(centro1+digito_izq_num2)**2]+patron_der]
                indice_num2_centro_a_derecha -= 1       
'''

def TRES(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        lista=[]
        len1=largo(num1)
        len2=largo(num2)
        patron_izq=[-1, 0, -1]
        patron_der=[0, 1, 0]
        patron_izq2=[2, 0, 2]
        patron_der2=[0, -2, 0]
        patron_centro_izq=[3 ,0 , 3]
        patron_centro_der=[0, -3, 0]

        centro1=centronum(num1)
        centro2=centronum(num2)

        indice_num1_izq_a_der=0
        indice_num1_der_a_izq=0
        indice_num2_centro_a_derecha=(len2//2)-1
        indice_num2_centro_a_izq=(len2//2)+1

        while indice_num2_centro_a_izq>len2 or indice_num2_centro_a_derecha>=0:
            if indice_num2_centro_a_izq<len2:
                digito=(num2//(10**indice_num2_centro_a_izq))%10
                lista += [patron_izq+[(centro1+digito)**2]+patron_der]
                indice_num2_centro_a_izq += 1

            if indice_num2_centro_a_derecha>=0:
                digito=(num2//(10**indice_num2_centro_a_derecha))%10
                lista+=[patron_izq+[(centro1+digito)**2]+patron_der]
                indice_num2_centro_a_derecha -= 1

            if indice_num1_der_a_izq>=0:
                digito=(num1//(10**indice_num1_der_a_izq))%10
                lista+=[patron_izq2+[(centro2*digito)**3]+patron_der2]
                indice_num1_der_a_izq +=1

            if indice_num1_izq_a_der>=0:
                digito=(num1//(10**(len1-indice_num1_izq_a_der-1)))%10
                lista+=[patron_izq2+[(centro2*digito)**3]+patron_der2]
                indice_num1_izq_a_der+=1
        lista = lista + [[patron_centro_izq + [(centro1 + centro2)**(len1 - 2)] + patron_centro_der]]
        return lista
    else:
        print("Parametros incorrecto, ambos deben ser numeros enteros, del mismo largo y cantidad de digitos impar \n Por ejemplo: 123, 456")

#_________________________________________________________________________________________________________________
#Funcion 4
'''
i : indice para recorrer 
suma : almacena los valores de la variable operacion
par1 : nombro variable par1 para simplificar la 'parte1' de la operacion: que es el factorial del indice^2
        llamo a la funcion auxiliar factorialDEC()
par2 : es el n que le otorgamos cuando llamamos la funcion, el numero que queremos hacer
numerador : es el numerador de la operacion
denominador : es el denominador de la operacion
        #Lo hice de esta manera para separar eel codigo y que fuera mas facil comprenderla de mi parte
operacion : es el resultado de dividir el numerador entre el denominador (todo el termino de la suma)
'''
def CUATRO(n):
    if isinstance(n, int) and n > 0:
        i=1
        suma=0
        while i<=n:
            par1=i**2
            par1=factorialDEC(par1)
            par2=n
            par2=factorialDEC(par2)  # lo mismo con par2
            numerador=(((par1)**3)**2) * (((n**2)+1)**(n-1)) * (((n-1)+3)**2)
            denominador=((((3**n) * ((n*(i**2))**i)) + ((par2)**2))**4)
            operacion=(numerador/denominador)
            suma+=operacion
            i=i+1
        print(suma**3)
    else:
        print("Parametro incorrecto, debe ser un numero entero y positivo y diferente de 0")