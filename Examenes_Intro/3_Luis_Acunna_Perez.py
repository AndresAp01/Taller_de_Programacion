#Luis Andres Acunna Perez
#Tercer examen parcial
#____________________________________________________________________________________________________#
#FUNCIONES AUXILIARES
#funcion aux para LARGO RECURSIVO
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
#funcion aux para largo con FOR
def largofor(num):
    if isinstance(num,int):
        num=abs(num)
        if num==1:
            return 1
        else:
            cont=0
            for i in range(0,num,1):
                if num==0:
                    break
                cont=cont+1
                num=num//10
            return cont
    else:
        print("Parametro incorrecto")

#Funcion centronum() copiado de auxiliares
def centronum(num):
    if isinstance(num, int):
        num=abs(num)
        if largofor(num)%2!=0:
            larg=(largofor(num)-1)//2
            cont=largofor(num)-1
            while num!=0:
                temp=num%10
                if cont==larg:
                    centro=temp
                    break
                num=num//10
                cont=cont-1
            return centro
        else:
            print("Tamaño incorrecto")
    else:
        print("Parametro incorrecto")

#____________________________________________________________________________________________________#
"""
    FUNCION UNO()
    funcion de entrada prepara los dos numeros para que UNO_aux() los procese
    num1 y num2 los numeros originales
    largo es numero de digitos
"""
def UNO(num1, num2):
    num1, num2=abs(num1), abs(num2)
    print(f"primer numero: {num1}, segundo numero: {num2}")
    largo=largoRC(num1)
    if not (isinstance(num1, int) and isinstance(num2, int)):
        print("num1 y num2 deben ser enteros.")
    elif largoRC(num2)!=largo:
        print("Ambos números deben tener la misma cantidad de dígitos.")
    else:
        return UNO_aux(num1, num2, largo, 0)
"""
    Funcion UNO auxiliar recursiva
    num1 y num2 los numeros originales
    largo es numero de digitos
    indice_actual es el paso de la recursión (0 hasta largo-1)
    cantidad_pares es cuantos indices pares hay al iterar hacia adelante
    indice_impar_maximo es el mayor indice impar valido
    posicion_primer es la posicion del primer digito
    pos2 es la posicion del segundo digito
"""
def UNO_aux(num1, num2, largo, indice_actual):
    if indice_actual>=largo:
        return []
    cantidad_pares=(largo+1)//2
    cantidad_impares=largo//2
    if indice_actual<cantidad_pares:
        posicion_primer=2*indice_actual
    else:
        if (largo-1)%2==1:
            indice_impar_maximo=largo-1
        else:
            indice_impar_maximo=largo-2
        paso_extra=indice_actual-cantidad_pares
        posicion_primer=indice_impar_maximo-2*paso_extra
    if indice_actual<cantidad_impares:
        posicion_segundo=2*indice_actual+1
    else:
        if (largo-1)%2==0:
            indice_par_maximo=largo-1
        else:
            indice_par_maximo=largo-2
        paso_extra2=indice_actual-cantidad_impares
        posicion_segundo=indice_par_maximo-2*paso_extra2
    dig1_encontrado=(num1//(10**(largo-1-posicion_primer)))%10
    dig2_encontrado=(num2//(10**(largo-1-posicion_segundo)))%10
    sucesor1=dig1_encontrado+1
    antecesor1=dig1_encontrado-1
    sucesor2=dig2_encontrado+1
    antecesor2=dig2_encontrado-1

    digito_primer=[1,0,1, sucesor1, dig1_encontrado, sucesor1+dig1_encontrado-antecesor1, antecesor1,-1,0,-1]
    digito_segundo=[-2,0,-2, sucesor2, dig2_encontrado, sucesor2+dig2_encontrado-antecesor2, antecesor2, 2,0,2]

    return [digito_primer, digito_segundo]+UNO_aux(num1, num2, largo, indice_actual+1)

""" PRUEBAS de UNO()
    print(UNO(0,0))
    []
    
    print(UNO(10,5))
    primer numero: 10, segundo numero: 5
    Ambos números deben tener la misma cantidad de dígitos.
    
    print(UNO(1,5))
    primer numero: 1, segundo numero: 5
    [[1, 0, 1, 2, 1, 3, 0, -1, 0, -1], [-2, 0, -2, 6, 5, 7, 4, 2, 0, 2]]
    
    print(UNO(123, 456))
    primer numero: 123, segundo numero: 456
    [[1, 0, 1, 2, 1, 3, 0, -1, 0, -1], [-2, 0, -2, 6, 5, 7, 4, 2, 0, 2], [1, 0, 1, 4, 3, 5, 2, -1, 0, -1], [-2, 0, -2, 7, 6, 8, 5, 2, 0, 2], [1, 0, 1, 3, 2, 4, 1, -1, 0, -1], [-2, 0, -2, 5, 4, 6, 3, 2, 0, 2]]

    print(UNO(612345, 107895))
    primer numero: 612345, segundo nuemro: 107895
    [[1, 0, 1, 7, 6, 8, 5, -1, 0, -1], [-2, 0, -2, 1, 0, 2, -1, 2, 0, 2], [1, 0, 1, 3, 2, 4, 1, -1, 0, -1], [-2, 0, -2, 9, 8, 10, 7, 2, 0, 2], [1, 0, 1, 5, 4, 6, 3, -1, 0, -1], [-2, 0, -2, 6, 5, 7, 4, 2, 0, 2], [1, 0, 1, 6, 5, 7, 4, -1, 0, -1], [-2, 0, -2, 10, 9, 11, 8, 2, 0, 2], [1, 0, 1, 4, 3, 5, 2, -1, 0, -1], [-2, 0, -2, 8, 7, 9, 6, 2, 0, 2], [1, 0, 1, 2, 1, 3, 0, -1, 0, -1], [-2, 0, -2, 2, 1, 3, 0, 2, 0, 2]]

    print(UNO(12345, 67893))
    primer numero: 12345, segundo numero: 67893
    [[1, 0, 1, 2, 1, 3, 0, -1, 0, -1], [-2, 0, -2, 8, 7, 9, 6, 2, 0, 2], [1, 0, 1, 4, 3, 5, 2, -1, 0, -1], [-2, 0, -2, 10, 9, 11, 8, 2, 0, 2], [1, 0, 1, 6, 5, 7, 4, -1, 0, -1], [-2, 0, -2, 4, 3, 5, 2, 2, 0, 2], [1, 0, 1, 5, 4, 6, 3, -1, 0, -1], [-2, 0, -2, 9, 8, 10, 7, 2, 0, 2], [1, 0, 1, 3, 2, 4, 1, -1, 0, -1], [-2, 0, -2, 7, 6, 8, 5, 2, 0, 2]]

"""
#____________________________________________________________________________________________________#
#FUNCION DOS
"""
    FUNCION DOS()
    # VARIABLES #
    L1, L2, L3 son los largos de los numeros
    centro1, centro2, centro3 son los centros de los numeros
    resultado es la lista final con los resultados
    principio_d3, final_d3 son los primeros y ultimos digitos de num3
    principio_d2, final_d2 son los primeros y ultimos digitos de num2
    principio_d1, final_d1 son los primeros y ultimos digitos de num1
    
"""
def DOS(num1, num2, num3):
    if num1!=0 or num2!=0 or num3!=0:
        if isinstance(num1, int) and isinstance(num2, int) and isinstance(num3, int):
            L1=largofor(num1)
            L2=largofor(num2)
            L3=largofor(num3)
            if L1==L2==L3:
                if L1%2!=0:
                    largo=L1
                    centro1=centronum(num1)
                    centro2=centronum(num2)
                    centro3=centronum(num3)
                    resultado=[]
                    for i in range((largo-1)//2):
                        principio_d3=(num3//(10**(largo-1-i)))%10
                        final_d3=(num3//(10**i))%10
                        resultado=resultado+[[centro1, principio_d3, final_d3]]
                        principio_d1=(num1//(10**(largo-1-i)))%10
                        final_d1=(num1//(10**i))%10
                        resultado=resultado+[[centro3, principio_d1, final_d1]]
                        principio_d2=(num2//(10**(largo-1-i)))%10
                        resultado=resultado+[[centro1, principio_d2, centro2]]
                        final_d2=(num2//(10**i))%10
                        resultado=resultado+[[centro3, final_d2, centro2]]
                    return f"Lista generada: {resultado}"
                else:
                    return "El largo de los numeros debe ser impar"
            else:
                return "Los tres numeros deben tener el mismo largo."
        else:
            return "Los numeros deben ser enteros."
    else:
        return "Los numeros deben ser distintos de cero."
"""
    Pruebas de DOS():
    {1}
    DOS(12113, 456, 789)
    Los tres numeros deben tener el mismo largo.
    
    {2}
    print(DOS(121, 456, "na"))
    Los numeros deben ser enteros.
    
    {3}
    print(DOS(31235,89012,43576))
    Lista generada: [[2, 4, 6], [5, 3, 5], [2, 8, 0], [5, 2, 0], [2, 3, 7], [5, 1, 3], [2, 9, 0], [5, 1, 0]]
    
    {4}
    print(DOS(3123567,8901249,4357620))
    Lista generada: [[3, 4, 0], [7, 3, 7], [3, 8, 1], [7, 9, 1], [3, 3, 2], [7, 1, 6], [3, 9, 1], [7, 4, 1], [3, 5, 6], [7, 2, 5], [3, 0, 1], [7, 2, 1]]

    {5}
    print(DOS(0, 0, 0))
    Los numeros deben ser distintos de cero.
"""
#____________________________________________________________________________________________________#
#FUNCION TRES
"""
    TRES():
    Funcion principal que procesa un numero entero:
    Valida los parametros
    Convierte los valores a positivos
    si num y numbuscar no son 0, imprime el resultado de la funciOn recursiva auxiliar
    # VARIABLES #
        num numero original a procesar
        cantidad cuiantas veces a repetir el numincluit
        numbuscar es el digito a detectar
        bloque central la lista de repeticiones de numincluit
        lista_inicial la lista inicial con los bloques de numincluit y bloque central
        
    Comentarios TRES_aux():
    Función recursiva auxiliar
    Extrae digitos del parAmetro num de uno en uno
    Si el digito coincide, construye
    Si no coincide añade el dígito a resultados
    Repite el proceso con el resto de los dígitos hasta que num <= 0
    # VARIABLES #
        largofor(num) numero de digitos
        divisor aisla el primer digito
        bloque1 bloque anters de la potencia
        inverso negativo del digito a buscar
        bloque2 bloque despues del inverso
        fin secuencia de cierre
        contador_nivel avanza al siguiente nivel
        
"""
def TRES(num, numincluir, cantidad, numbuscar):
    if isinstance(num, int):
        if isinstance(numincluir, int):
            if isinstance(cantidad, int):
                if isinstance(numbuscar, int):
                    num=abs(num)
                    cantidad=abs(cantidad)
                    numbuscar=abs(numbuscar)
                    print("Numero original:", num)
                    if num==0 and numbuscar==0:
                        bloque_central=[numincluir]*cantidad
                        lista_inicial=[[-1, 1, 0, 1]+bloque_central+[0, 0]+bloque_central+[0, 1, 0, 1]]
                        return lista_inicial
                    else:
                        print("Lista:", TRES_aux(num, numincluir, cantidad, numbuscar, 1, []))
                else:
                    print("num a buscar debe ser entero")
            else:
                print("cantidad debe ser entero")
        else:
            print("el num a incluir debe ser entero")
    else:
        print("num debe ser entero")

def TRES_aux(num, numincluir, cantidad, numbuscar, contador_nivel, resultados):
    if num<=0:
        return resultados
    longitud=largofor(num)
    divisor=10**(longitud-1)
    digito_actual=(num//divisor)%10
    resto_num=num%divisor

    if digito_actual==numbuscar:
        inicio=[numbuscar - 1, 1, 0, 1]
        bloque1=[numincluir]*cantidad
        potencia=[digito_actual**contador_nivel]
        inverso=[-numbuscar]
        bloque2=[numincluir]*cantidad
        fin=[0, -1, 0, numbuscar+1]
        cuerpo = inicio + bloque1 + potencia + inverso + bloque2 + fin
        resultados += [cuerpo]
        contador_nivel += 1
    else:
        resultados+=[digito_actual]

    return TRES_aux(resto_num, numincluir, cantidad, numbuscar, contador_nivel, resultados)

"""
    PRUEBAS de TRES():
    {1}
    print(TRES(13439, 8, 5, 3))
    Numero original: 13439
    Lista: [1, [2, 1, 0, 1, 8, 8, 8, 8, 8, 3, -3, 8, 8, 8, 8, 8, 0, -1, 0, 4], 4, [2, 1, 0, 1, 8, 8, 8, 8, 8, 9, -3, 8, 8, 8, 8, 8, 0, -1, 0, 4], 9]
    {2}
    print(TRES(1229, 5, 2, 1))
    Numero original: 1229
    Lista: [[0, 1, 0, 1, 5, 5, 1, -1, 5, 5, 0, -1, 0, 2], 2, 2, 9]
    {3}
    print(TRES(0, 5, 2, 1))
    Numero original: 0
    Lista: []
"""
#____________________________________________________________________________________________________#
#FUNCION CUATRO
"""
    CUATRO()
    Duplica todas las apariciones del elemento 'objetivo' en una lista, incluyendo elementos dentro de sublistas anidadas
    objetivo el elemento que se desea duplicar en la lista
    lista_principal La lista donde se buscara el objetivo
    La lista original modificada con los elementos objetivo duplicados
    
    # VARIABLES #
        pila es la lista que funciona como pila para recorrer las sublistas pendientes de procesar
        visitadas la lista que lleva registro de las sublistas ya procesadas para evitar repeticiones
        nuevos_elementos es la lista temporal para almacenar sublistas encontradas durante el procesamiento
        lista_actual es sublista que se está procesando en cada iteración
        indice es la posicion actual dentro de la lista_actual que se esta evaluando
        elemento es el individual que se esta evaluando en cada posicion
"""
def CUATRO(objetivo, lista_principal):
    if isinstance(objetivo, int):
        if isinstance(lista_principal, list):
            print("Lista original:", lista_principal)
            pila=[lista_principal]
            visitadas=[]
            for lista_actual in pila:
                nuevos_elementos=[]
                indice=0
                for digito in range(len(lista_actual)):
                    if indice>=len(lista_actual):
                        break
                    elemento=lista_actual[indice]
                    if elemento==objetivo:
                        lista_actual[indice:indice+1]=[[1,0,1,elemento, elemento, -elemento, elemento+1,0,1,0]]
                        indice+=2
                    else:
                        if isinstance(elemento, list) and elemento not in visitadas:
                            nuevos_elementos+=[elemento]
                            visitadas+=[elemento]
                        indice+=1
                pila+=nuevos_elementos
            return f"Lista generada: {lista_principal}"
        else:
            print("La lista principal debe ser una lista")
    else:
        print("El objetivo debe ser entero")

"""
    PRUEBAS DE CUATRO()
    {1}
    print(CUATRO(2, [1,[2,9],[[4,2,6],[8,2]],2,10]))
    Lista original: [1, [2, 9], [[4, 2, 6], [8, 2]], 2, 10]
    [1, [[1, 0, 1, 2, 2, -2, 3, 0, 1, 0], 9], [[4, [1, 0, 1, 2, 2, -2, 3, 0, 1, 0], 6], [8, [1, 0, 1, 2, 2, -2, 3, 0, 1, 0]]], [1, 0, 1, 2, 2, -2, 3, 0, 1, 0], 10]
    
    {2}
    print(CUATRO(1, [1]))
    Lista original: [1]
    [[1, 0, 1, 1, 1, -1, 2, 0, 1, 0]]
    
    {3}
    print(CUATRO(1, []))
    Lista original: []
    []
"""