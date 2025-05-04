#Luis Andres Acunna Perez
#Segundo examen parcial

#funciones auxiliares copiadas y pegadas del archivo de la profe:
#validacion de matriz

def valida_matriz(matriz):
    if not isinstance(matriz, list) or len(matriz) == 0:
        return False
    primera = matriz[0]
    if not isinstance(primera, list) or len(primera) == 0:
        return False
    cols = len(primera)
    for fila in matriz:
        if not isinstance(fila, list) or len(fila) != cols:
            return False
    return True

def ValidaMatriz(matriz):
    a = 0
    b = 0
    if matriz == []:
        return False
    elif matriz[0] == [] and matriz[1] == []:
        return "La matriz no es valida"
    else:
        for i in range(len(matriz)):
            if matriz == []:
                a = 1
            elif matriz[0] == []:
                a = 1
            elif len(matriz[0]) != len(matriz[1]):
                return False
            matriz = matriz + [matriz[0]]
            matriz = matriz[1:]
    if a == b:
        return True
    else:
        return False
# validacion de conjuntos NO es conjunto
def conjunto(lista):  # [3,2,1,3]
    largo = 0  # 0
    pos = 0  # 0

    # largo      pos       lista
    while largo < len(lista):  # Afuera o Externo mas lento
        while pos < len(lista):  # Adentro o Interno, corre mas rapido
            if largo != pos:  #
                if lista[pos] == lista[largo]:
                    return (False)
                else:
                    pos = pos + 1
            else:
                pos = pos + 1
        # Antes del externo
        pos = 0
        largo = largo + 1
    return (True)

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

# _______________________________________________________________________________

#primera funcion
#Comentarios sobre las variables y que hacen las funciones

def UNO(lista):
    if isinstance(lista, list):
        if conjunto(lista)==True:
            if not lista:
                return []
            else:
                resultado=[]
                nueva_lista=[]
                desordenada=False
                for i in range(len(lista)):
                    actual=lista[i]
                    bloque=[actual-1, actual, -actual, actual+1]
                    if i==0:
                        nueva_lista=[bloque]
                    elif lista[i]>=lista[i-1]:
                        nueva_lista=nueva_lista+[bloque]
                    else:
                        if not desordenada:
                            resultado=[[1, 0, nueva_lista, 0, 1]]
                            desordenada=True
                        else:
                            resultado=resultado+[[1, 0, nueva_lista, 0, 1]]
                        nueva_lista=[bloque]
                if desordenada:
                    resultado=resultado+[[1, 0, nueva_lista, 0, 1]]
                    return f"Lista original: {lista}, Resultado: {resultado}"
                else:
                    return [lista]
        else:
            return "La lista no es un conjunto, por favor remover digitos repetidos."
    else:
        return 0


#resultado=UNO([6, -1, 2, 7, 8, 16, 100, -200])
#print(result)
#Lista original: [6, -1, 2, 7, 8, 16, 100, -200], Resultado: [[1, 0, [[5, 6, -6, 7]], 0, 1], [1, 0, [[-2, -1, 1, 0], [1, 2, -2, 3], [6, 7, -7, 8], [7, 8, -8, 9], [15, 16, -16, 17], [99, 100, -100, 101]], 0, 1], [1, 0, [[-201, -200, 200, -199]], 0, 1]]

#resultado=UNO([1,2,3,4])
#print(resultado)
#[[1, 2, 3, 4]]

#_______________________________________________________________________________

#Comentarios de las variables
#num1 y num2 son los parametros que recibe la funcion
#nuevo_num1 y 2 son los nuevos numeros generados
#digitos1 y 2 son los digitos de los numeros cuando se recorren
#digitos1inverso y 2 para recorrerlos al reves
#nuevo_largo porque los digitos cambian de largo si tien un - al final
#matriz 1 y 2 son las listas generadas a partir de los nuevos numeros
#grupos para separar en tres elementos
#desplazamiento para alinear el bloque de 3 digitos
#valor_bloque_1 y 2 son los valores numericos de 3 digitos que se extraen de nuevo num
#digito_centena1 y 2 son el digito de las centenas dentro de valor_bloque
#digito_decena1 y 2 el digito de las decenas
#digito_unidad1 y 2 el digito de las unidades
#suma es la suma de matrices 1 y2
def DOS(num1, num2):
    if not isinstance(num1, int) or not (num2, int):
        return "Ambos parametros deben ser numeros enteros"

    num1=abs(num1)
    num2=abs(num2)
    print(f"Numeros originales: {num1, num2}")
    if largofor(num1)!=largofor(num2):
        return "Los numeros deben tener el mismo tamanno"
    elif largofor(num1 or num2)%5!=0:
        return "Los numeros deben ser multiplos de 5"
    elif largofor(num1 or num2)%2==0:
        return "Los numeros deben tener largo impar"
    else:
        nuevo_num1=0
        nuevo_num2=0
        n=largofor(num1)
        for i in range(n):
            digitos1=(num1//(10**(n-i-1)))%10
            digitos2=(num2//(10**(n-i-1)))%10
            digitos1inverso=(num1//(10**i))%10
            digitos2inverso=(num2//(10**i))%10
            if i%2==0:
                nuevo_num1=nuevo_num1*10+digitos1
                nuevo_num2=nuevo_num2*10+digitos2inverso
            else:
                nuevo_num1=nuevo_num1*10+digitos2
                nuevo_num2=nuevo_num2*10+digitos1inverso
        print(f"Numeros nuevos: {nuevo_num1, nuevo_num2}")
        nuevo_largo=largofor(nuevo_num1)
        if nuevo_largo%5==0 and nuevo_largo%3==0:
            matriz_1=[]
            matriz_2=[]
            grupos=nuevo_largo//3
            for j in range(grupos):
                desplazamiento=nuevo_largo-(j+1)*3
                valor_bloque_1=(nuevo_num1//(10**desplazamiento))%1000
                valor_bloque_2=(nuevo_num2//(10**desplazamiento))%1000
                digito_centena_1=valor_bloque_1//100
                digito_decena_1=(valor_bloque_1//10)%10
                digito_unidad_1=valor_bloque_1%10

                digito_centena_2=valor_bloque_2//100
                digito_decena_2=(valor_bloque_2//10)%10
                digito_unidad_2=valor_bloque_2%10

                sub1=[digito_centena_1**2, digito_decena_1**3, digito_unidad_1**2]
                sub2=[digito_centena_2**2, digito_decena_2**3, digito_unidad_2**2]
                matriz_1=matriz_1+[sub1]
                matriz_2=matriz_2+[sub2]
            if not (ValidaMatriz(matriz_1) and ValidaMatriz(matriz_2)):
                return "Matrices inválidas"

                # 2) Sumarlas elemento a elemento
            suma=[]
            for i in range(len(matriz_1)):
                fila_suma=[]
                for j in range(len(matriz_1[i])):
                    fila_suma=fila_suma+[matriz_1[i][j] + matriz_2[i][j]]
                suma=suma+[fila_suma]
            print(f"matrices generadas: {matriz_1, matriz_2}")
            print("Suma de matrices:")
            return suma
        elif largofor(nuevo_num1)!=largofor(nuevo_num2):
            return "Los nuevos numeros quedaron de diferentes largos, no se puede construir la lista"
        elif nuevo_largo%5==0 and nuevo_largo%3!=0:
            matriz_1=[]
            matriz_2=[]
            center=nuevo_largo//2
            desplazamiento=nuevo_largo-3
            valor_bloque_1=(nuevo_num1//(10**desplazamiento))%1000
            valor_bloque_2=(nuevo_num2//(10**desplazamiento))%1000
            digito_centena_1=valor_bloque_1//100
            digito_decena_1=(valor_bloque_1//10)%10
            digito_unidad_1=valor_bloque_1%10

            digito_centena_2=valor_bloque_2//100
            digito_decena_2=(valor_bloque_2//10)%10
            digito_unidad_2=valor_bloque_2%10

            matriz_1=matriz_1+[[digito_centena_1**2, digito_decena_1**3, digito_unidad_1**2]]
            matriz_2=matriz_2+[[digito_centena_2**2, digito_decena_2**3, digito_unidad_2**2]]
            # segunda sublista
            desplazamiento_bloque2=nuevo_largo-(center+3)
            valor_bloque_1=(nuevo_num1//(10**desplazamiento_bloque2))%1000
            valor_bloque_2=(nuevo_num2//(10**desplazamiento_bloque2))%1000

            digito_centena_1=valor_bloque_1//100
            digito_decena_1=(valor_bloque_1//10)%10
            digito_unidad_1=valor_bloque_1%10

            digito_centena_2=valor_bloque_2//100
            digito_decena_2=(valor_bloque_2//10)%10
            digito_unidad_2=valor_bloque_2%10

            matriz_1=matriz_1+[[digito_centena_1**2, digito_decena_1**3, digito_unidad_1**2]]
            matriz_2=matriz_2+[[digito_centena_2**2, digito_decena_2**3, digito_unidad_2**2]]
            if not (ValidaMatriz(matriz_1) and ValidaMatriz(matriz_2)):
                return "Matrices invalidas"
            suma=[]
            for i in range(len(matriz_1)):
                fila_suma=[]
                for j in range(len(matriz_1[i])):
                    fila_suma=fila_suma+[matriz_1[i][j] + matriz_2[i][j]]
                suma=suma+[fila_suma]
            print(f"matrices generadas: {matriz_1, matriz_2}")
            print("Suma de matrices:")
            return suma
        else:
            return "Algo no previsto ha pasao"

print(DOS(1212,12345))
#Prueba 1: print(DOS(61257,89102))
#Imprime:
"""
Numeros originales: (61257, 89102)
Numeros nuevos: (69207, 25118)
matrices generadas: ([[36, 729, 4], [4, 0, 49]], [[4, 125, 1], [1, 1, 64]])
Suma de matrices:
[[40, 854, 5], [5, 1, 113]]
"""

#Prueba 2: print(DOS(133557789214365,745230987664422))
#Imprime:
"""
Numeros originales: (133557789214365, 745230987664422)
Numeros nuevos: (143250789614325, 264462789735537)
matrices generadas: ([[1, 64, 9], [4, 125, 0], [49, 512, 81], [36, 1, 16], [9, 8, 25]], [[4, 216, 16], [16, 216, 4], [49, 512, 81], [49, 27, 25], [25, 27, 49]])
Suma de matrices:
[[5, 280, 25], [20, 341, 4], [98, 1024, 162], [85, 28, 41], [34, 35, 74]]
"""

#Prueba 3:print(DOS("aaaa",12345))
#Imprime: Ambos parametros deben ser numeros enteros

#Prueba 4: print(DOS(1212,12345))
#Imprime: Numeros originales: (1212, 12345)
#         Los numeros deben tener el mismo tamanno

#_______________________________________________________________________________
def TRES():
    pass
#_______________________________________________________________________________
#Comentarios de funcion CUATRO
#elem es el elemento a duplicar
#lista es la lista de entrada
#i es el indice del bucle principal
#nueva es lista que vamos construyendo
#item es el elemento actual de la lista pos i
#nueva_sub es la sublista resultante
#x es el indice del bucle de la sublista

def CUATRO(elem, lista):
    if isinstance(lista, list):
        if isinstance(elem, (int,list)):
            i=0
            nueva=[]
            while i<len(lista):
                item=lista[i]
                if item==elem:
                    nueva=nueva+[item, item]
                elif isinstance(item, list) and elem in item:
                    nueva_sub=[]
                    x=0
                    while x<len(item):
                        nueva_sub=nueva_sub+[item[x]]
                        if item[x]==elem:
                            nueva_sub=nueva_sub+[elem]
                        x+=1
                    nueva=nueva+[nueva_sub]
                else:
                    nueva=nueva+[item]
                i+=1
            return nueva
        else:
            return "El segundo parametro debe ser un numero entero o una lista."
    else:
        return "El primer parametro debe ser una lista."

#resultado=CUATRO(3, [1,2,3,3,[4,3,3], 4, [3]])
#print(resultado)
