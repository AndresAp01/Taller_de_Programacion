#Conjunto es una lista
#No hay elementos repetidos (validar)
#No importa el orden de los elementos

# validacion de conjuntos NO es conjunto
def conjuntoNO(lista):#[3,2,1,8]
    largo=0 #0
    pos=0 #0
    #largo      pos       lista
    #0          0         [3,2,1,8]
    #0          1         [3,2,1,8]
    #0          2         [3,2,1,8]
    #0          3         [3,2,1,8]
    #0          4         [3,2,1,8]
    #1          0         [3,2,1,8]
    #1          1         [3,2,1,8]
    #1          2         [3,2,1,8]
    #1          3          [3,2,1,8]
    #1          4           [3,2,1,8]
    #2          0           [3,2,1,8]
    #2          1           [3,2,1,8]


    while largo<len(lista):# Afuera o Externo mas lento
        #largo<len(lista)
        #0<4 si 1<4si 2<4si 3<4si 4<4no

        while pos<len(lista):#Adentro o Interno, corre mas rapido
              #0<4si 1<4si 2<4si 3<4si 4<4no #1ra pasada
              #0<4si 1<4si 2<4si 3<4si 4<4no #2da pasada
              #0<4si 1<4si 2<4si 3<4si 4<4no  3ra pasada
            if largo!=pos:#
                #0!=0 no 0!=1 si 0!=2si 0!=3 0!=1si 1ra pasada
                #1!=0si 1!=1no 1!=2si 1!=3si 1!=4si 2da pasada
                #2!=0si 2!=1no 2!=2no 2!=3si 2!=4si 3ra psada
                if lista[pos]==lista[largo]:
                    #2=3x 1-3x 8=3x

                    return False

                else:
                    pos=pos+1#0 1 2 3
            else:
                pos=pos+1#
        #Antes del externo
        pos=0
        largo=largo+1
    return( True)

def conjuntoSI(lista):#[3,2,1,8]
    largo=0 #0
    pos=0 #0
    #largo      pos       lista
    #0          0         [3,2,1,8]
    while largo<len(lista):# Afuera o Externo mas lento
        #largo<len(lista)
        while pos<len(lista):#Adentro o Interno, corre mas rapido
            if largo!=pos:#
                if lista[pos]==lista[largo]:#
                    return(False)
                else:
                    pos=pos+1#
            else:
                pos=pos+1#
        #Antes del externo
        pos=0
        largo=largo+1
    return( True)

#union de conjuntos         T       T
def union(lista1,lista2):#[2,3,4,8],[5,3,6]=[2,3,4,8,5,6]
    if conjuntoSI(lista1)==True and conjuntoSI(lista2)==True:
        while lista2!=[]:#

            if lista2[0] in lista1:
                lista2=lista2[1:]#[6]
            else:
                lista1=lista1+[lista2[0]]#
                #[2,3,4,8]+[5]=[2,3,4,8,5]
                lista2=lista1[1:] #[3,6][]

        return lista1 #[2,3,4,8,5,6]
    else:
        return "debe ingresar conjuntos"

#intersección                      T      T
def interseccion(lista1,lista2):#[2,3,4],[5,3,6]=[3]
    if conjuntoSI(lista1)==True and conjuntoSI(lista2)==True:
        listanueva=[]
        #listanueva    lista1   lista2
        #[]            [2,3,4]  [5,3,6]


        while lista2!=[]:#
            if lista2[0] in lista1:

                if lista2[0] not in listanueva:#
                    listanueva=listanueva+[lista2[0]]

            lista2=lista2[1:]#
        return listanueva #
    else:
        return "debe ser conjuntos"


#Funcion que diferencia simetrica (A union B)-(A inter B)
# [2,3,4,5],[3,7,8,9,2,0]
#Union=[2,3,4,5,7,8,9,0]
#Interseccion=[3,2]
#Diferencia=[4,5,7,8,9,0]


def diferencia (lista1,lista2):# [2,3,4,5],[3,7,8,9,2,0]
    if conjunto(lista1)==True and conjunto(lista2)==True:
        LUnion=union(lista1,lista2)#[2,3,4,5,7,8,9,0]
        LInter=interseccion(lista1,lista2)#[2,3]

        #print(LUnion,LInter)
        LNueva=[]
        #LNueva       lista1      lista2        LUnion            LInterseccion
        #[]           [2,3,4,5]   [3,7,8,9,2,0] [2,3,4,5,7,8,9,0] [2,3]


        while LUnion!=[]:#

            if LUnion[0] not in LInter:

                LNueva=LNueva+[LUnion[0]]
            LUnion=LUnion[1:]#
        return LNueva#
    else:
        print("No son conjuntos")
#Matrices Es una lista de listas

#Matrices
#[[2,3,4],[5,6,7]] valida No cuadrada 2x3
#[[1,2,4,5],[3,4,5,6],[12,34,5,67],[6,7,0,9]] Valida cuadrada 4x4
#[[3,7,9,0],[6,7]]NO es una matriz valida
#len(matriz) len2
#len F0=4 lenF1=2


#Ejemplo para una matriz no valida. Es la misma diferente corrida
#Validacion de matriz. NO funciona [[3,4],[6,8],[5]]
def ValidaMatrizNO(matriz):
    a=0
    b=0
    # a  b     matriz
    # 0  0    [[3,4],[6,8],[5]]

    if matriz==[]:
        return False
    elif matriz[0]==[] and matriz[1]==[]:
        return "La matriz no es valida"
    else:
        for i in range(len(matriz)):#i=0 1 2 3x
            if matriz==[]:
                a=1
            elif matriz[0]==[]:
                a=1
            elif len(matriz[0])!=len(matriz[1]):#
                #2!=2no 2!=1si
                #a=1
               return False
            matriz=matriz+[matriz[0]]#[[3,4],[6,8],[5],[3,4]]
            matriz=matriz[1:]#[[6,8],[5],[3,4]]
    if a==b:
        return True
    else:
        return False

def ValidaMatrizSI(matriz): #[[3,4],[5,6]]
    a=0
    b=0
    # a  b     matriz
    # 0  0      [[3,4],[5,6]]

    if matriz==[]:
        return False
    elif matriz[0]==[] and matriz[1]==[]:
        return "La matriz no es valida"
    else:
        for i in range(len(matriz)):#1=0si 1si 2no
            if matriz==[]:
                a=1
            elif matriz[0]==[]:
                a=1
            elif len(matriz[0])!=len(matriz[1]):#
                #2!=2no 2!=2no
               return False
            matriz=matriz+[matriz[0]]#[[3,4],[5,6],[3,4]]
            matriz=matriz[1:]#[[5,6],[3,4]]

    if a==b:
        return True
    else:
        return False

#Escribir una funcion que recibe dos matrices, deben ser validas y del mismo tamaño
#Sumar ambas matrices

import copy

def sumatrices(ma1,ma2):#[2,3],[4,6]]  [[4,6],[7,8]]=[[6,9],[11,14]]
    if ValidaMatrizSI(ma1)==False or ValidaMatrizSI(ma2)==False or len(ma1[0])!=len(ma2[0])or len(ma1)!=len(ma2):
        print("matrices no validas")
    else:
        filas=len(ma1)#2
        columnas=len(ma1[0])#2
        filas1=len(ma2)#2
        columnas1=len(ma2[0])#2
        matriznueva=copy.deepcopy(ma1)
        for i in range(filas):#i=0 1 2x
            for j in range(columnas):#
               matriznueva[i][j]=ma1[i][j]+ma2[i][j]

        print(matriznueva,ma1)

#Escribir una multiplicacion de numero(escalar) por una matriz

def Multiplicanummatriz(matriz,num):#
    if ValidaMatrizSI(matriz) and type(num)==int:
        MatrizNueva=copy.deepcopy(matriz)#
        print(MatrizNueva)
        for i in range(len(MatrizNueva)):#
            for j in range (len(MatrizNueva[0])):#
                MatrizNueva[i][j]=matriz[i][j]*num
                #MatrizNueva[0][0]=matriz[0][0]*2=>3*2
        print(MatrizNueva,matriz)#
    else:
        print("Parametro incorrecto")

def MatrizTraspuesta(matriz):#[[1,2,3,10],[5,6,7,4],[10,8,9,11]] 3x4  4x3
    if ValidaMatrizSI(matriz)==True:
        largoFila=len(matriz)#
        largoColumnas=len(matriz[0])#
        matrizTraspuesta=[0]*largoColumnas#
        print(matrizTraspuesta)
        for i in range (largoColumnas):#i=
            matrizTraspuesta[i]=[0]*largoFila


            print(matrizTraspuesta) #

            for j in range(largoFila):#j=0 1 2 3x


                matrizTraspuesta[i][j]=matriz[j][i]


        print(matrizTraspuesta)#
    else:
        print("Parametro incorrecto")

