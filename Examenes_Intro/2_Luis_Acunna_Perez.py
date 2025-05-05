#Luis Andres Acunna Perez
#Segundo examen parcial

#funciones auxiliares copiadas y pegadas del archivo de la profe:
#Funcion aux suma de matrices
import copy

def sumatrices(ma1, ma2):
    if ValidaMatriz(ma1)==False or ValidaMatriz(ma2)==False or len(ma1[0])!=len(ma2[0]) or len(ma1)!=len(ma2):
        print("matrices no validas")
    else:
        filas=len(ma1)
        columnas=len(ma1[0])
        filas1=len(ma2)
        columnas1=len(ma2[0])
        matriznueva=copy.deepcopy(ma1)
        for i in range(filas):
            for j in range(columnas):
                matriznueva[i][j]=ma1[i][j]+ma2[i][j]
        return matriznueva
#Para que sumatrices funcione correctamente le cambio el nombre de ValidaMatrizSI por ValidaMatriz
#Tambien, le cambio el print por un return y le quito que me imprima ademas la ma1. No hace falta, solo quiero que me retorne la suma de matrices.

#Funcion aux validacion de matrices
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
    largo=0
    pos=0
    while largo<len(lista):
        while pos<len(lista):
            if largo!=pos:
                if lista[pos]==lista[largo]:
                    return False
                else:
                    pos=pos+1
            else:
                pos=pos+1
        pos=0
        largo=largo+1
    return True

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

#Funcion centro entregada en clase
#SE CAMBIA el nombre de largo por largofor para que FUNCIONE
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
#valor_bloque_1 y 2 son los valores numericos de 3 digitos que se extraen de nuevonum
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
            print(f"Matrices generadas: {matriz_1, matriz_2}")
            return sumatrices(matriz_1, matriz_2)

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
            print(f"Matrices generadas: {matriz_1, matriz_2}")
            return sumatrices(matriz_1, matriz_2)
        else:
            return "Algo no previsto ha pasao"

"""
Prueba 1: print(DOS(61257,89102))
Imprime:

Numeros originales: (61257, 89102)
Numeros nuevos: (69207, 25118)
matrices generadas: ([[36, 729, 4], [4, 0, 49]], [[4, 125, 1], [1, 1, 64]])
Suma de matrices:
[[40, 854, 5], [5, 1, 113]]


Prueba 2: print(DOS(133557789214365,745230987664422))
Imprime:

Numeros originales: (133557789214365, 745230987664422)
Numeros nuevos: (143250789614325, 264462789735537)
matrices generadas: ([[1, 64, 9], [4, 125, 0], [49, 512, 81], [36, 1, 16], [9, 8, 25]], [[4, 216, 16], [16, 216, 4], [49, 512, 81], [49, 27, 25], [25, 27, 49]])
Suma de matrices:
[[5, 280, 25], [20, 341, 4], [98, 1024, 162], [85, 28, 41], [34, 35, 74]]

Prueba 3:print(DOS("aaaa",12345))
Imprime: Ambos parametros deben ser numeros enteros

Prueba 4: print(DOS(1212,12345))
Imprime: Numeros originales: (1212, 12345)
         Los numeros deben tener el mismo tamanno"""

#_______________________________________________________________________________

#Comentarios de funcion TRES
#num1, num2 y num3 son los parametros que recibe la funcion
#centro1, centro2 y centro3 son los centros de los numeros
#lista es la lista donde se crearan las demas listas

def TRES(num1, num2, num3):
    num1=abs(num1)
    num2=abs(num2)
    num3=abs(num3)
    if not isinstance(num1, int) or not (num2, int) or not (num3, int):
        return "Ambos parametros deben ser numeros enteros"
    elif largofor(num1)!=largofor(num2) or largofor(num2)!=largofor(num3):
        return "Los numeros deben tener el mismo tamanno"
    elif largofor(num1 or num2 or num3)%2==0:
        return "Los numeros deben tener largo impar"
    elif largofor(num1 or num2 or num3)<3:
        return "Los numeros deben tener al menos 3 digitos"
    else:
        centro1=centronum(num1)
        centro2=centronum(num2)
        centro3=centronum(num3)
        lista=[]
        largo=largofor(num1)
        iteraciones=largo//2
        for i in range(iteraciones):
            digito_inicio_num3=(num3//(10**(largo-1-i)))%10
            digito_final_num3=(num3//(10**i))%10
            lista=lista+[[1,0,1, (digito_inicio_num3 + centro3)**2, -1,0,-1]]
            lista=lista+[[1,0,1, (digito_final_num3+centro3)**2, -1,0,-1 ]]

            digito_inicio_num2=(num2//(10**(largo-1-i)))%10
            digito_final_num2=(num2//(10**i))%10
            lista=lista+[[-2,0,-2, (digito_final_num2-centro2)**3, 2,0,2]]
            lista=lista+[[-2,0,-2, (digito_inicio_num2-centro2)**3, 2,0,2]]

            digito_inicio_num1=(num1//(10**(largo-1-i)))%10
            digito_final_num1=(num1//(10**i))%10
            lista=lista+[[3,0,3, (digito_inicio_num1*centro1)**2, -3,0,-3]]
            lista=lista+[[3,0,3, (digito_final_num1*centro1)**2, -3,0,-3]]
        print(f"Numeros originales: {num1, num2, num3}")
        return lista

"""
print(TRES(1234,3456,4567))
Primera prubea
print(TRES(61245,18973,81027))
Salida:
Numeros originales: (61245, 18973, 81027)
[[1, 0, 1, 64, -1, 0, -1], [1, 0, 1, 49, -1, 0, -1], [-2, 0, -2, -216, 2, 0, 2], [-2, 0, -2, -512, 2, 0, 2], [3, 0, 3, 144, -3, 0, -3], [3, 0, 3, 100, -3, 0, -3], [1, 0, 1, 1, -1, 0, -1], [1, 0, 1, 4, -1, 0, -1], [-2, 0, -2, -8, 2, 0, 2], [-2, 0, -2, -1, 2, 0, 2], [3, 0, 3, 4, -3, 0, -3], [3, 0, 3, 64, -3, 0, -3]]

Segunda prueba
print(TRES(123,234,345))
Numeros originales: (123, 234, 345)
[[1, 0, 1, 49, -1, 0, -1], [1, 0, 1, 81, -1, 0, -1], [-2, 0, -2, 1, 2, 0, 2], [-2, 0, -2, -1, 2, 0, 2], [3, 0, 3, 4, -3, 0, -3], [3, 0, 3, 36, -3, 0, -3]]

tercera prueba
print(TRES(12,18973,81027))
salida: Los numeros deben tener el mismo tamanno

cuarta prueba
print(TRES(1234,3456,4567))
salida: Los numeros deben tener largo impar
"""
#_______________________________________________________________________________
"""
Comentarios de funcion CUATRO
elem es el elemento a duplicar
lista es la lista de entrada
i es el indice del bucle principal
nueva es lista que vamos construyendo
item es el elemento actual de la lista pos i
nueva_sub es la sublista resultante
x es el indice del bucle de la sublista 
"""

def CUATRO1(elem, lista):
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
            print(lista)
            return nueva
        else:
            return "El segundo parametro debe ser un numero entero o una lista."
    else:
        return "El primer parametro debe ser una lista."
#_______________________________________________________________________________

"""
comentarios de variables de funciuon CUATRO
numero es el numero buscado
lista es la lista original
listas_pendientes para guardar las listas pendientes
indices_pendientes para guardar los indices o opisiciones pendientes
lista_actual es la lista que estamos proceasndo
i es el indice del bucle o posicion actual
elemento_actual es el elemento evaluado

"""

def CUATRO(numero, lista):
    if not isinstance(lista, list):
        return "El primer elemento debe ser una lista"
    elif not isinstance(numero, int):
        return "El segundo elemento debe ser un numero entero o una lista"
    print(f"Lista original: {lista}")
    listas_pendientes=[]
    indices_pendientes=[]
    lista_actual=lista
    i=0
    while True:
        while i<len(lista_actual):
            elemento_actual= lista_actual[i]
            if isinstance(elemento_actual, list):
                listas_pendientes+=[lista_actual]
                indices_pendientes+=[i+1]
                lista_actual=elemento_actual
                i=0
                continue
            else:
                if elemento_actual==numero:
                    lista_actual[i+1:i+1]=[numero]
                    i+=1
            i+=1

        if listas_pendientes:
            lista_actual=listas_pendientes[-1]
            i=indices_pendientes[-1]
            listas_pendientes=listas_pendientes[:-1]
            indices_pendientes=indices_pendientes[:-1]
        else:
            break

    return f"lista con duplicados: {lista}"

print(CUATRO(3, [1,3,[2,3,9],[3,[4,2,3,6],[8,3,3],3],3]))
#Pruebas:
"""
primera prueba:
print(CUATRO(3, [1,2,3,3,[4,3,3], 4, [3]]))
salida:
Lista original: [1, 2, 3, 3, [4, 3, 3], 4, [3]]
[1, 2, 3, 3, 3, 3, [4, 3, 3, 3, 3], 4, [3, 3]]

segunda prueba:
print(CUATRO(2, [1,[2,9],[[4,2,6],[8]],2,10]))
salida:
Lista original: [1, [2, 9], [[4, 2, 6], [8]], 2, 10]
[1, [2, 2, 9], [[4, 2, 2, 6], [8]], 2, 2, 10]

tercera prueba:
print(CUATRO(3, [1,3,[2,3,9],[3,[4,2,3,6],[8,3,3],3],3]))
salida:
Lista original: [1, 3, [2, 3, 9], [3, [4, 2, 3, 6], [8, 3, 3], 3], 3]
[1, 3, 3, [2, 3, 3, 9], [3, 3, [4, 2, 3, 3, 6], [8, 3, 3, 3, 3], 3, 3], 3, 3]

cuarta prueba:
print(CUATRO(3.4, [1,2,3,3,[4,3,3], 4, [3]]))
salida:
El segundo elemento debe ser un numero entero o una lista

quinta prueba:
print(CUATRO("a", [1,2,3,3,[4,3,3], 4, [3]]))
salida: 
El segundo elemento debe ser un numero entero o una lista
"""
