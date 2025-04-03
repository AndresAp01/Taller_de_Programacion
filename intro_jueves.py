#Escribir una funcion que recibe una lista
#INvertir la lista
#For range e item

def Invetir_Range():
    if type(lista)==list:
        if lsita==[]:
            return []
        else:
            Linvertida=[]
            for i in range(len(lista)):
                Linvertida=[lista[i]]+Linvertida
            return Linvertida
    else:
        print("Parametro incorrecto")

#Escribir una funcion que recibe dos numeros enteros positivos del mismo largo
#Sumar y multiplicar por posicion. Los num trabajados desde pos[0]
#Quiz realizado y agregar el quiz con un solo while
def largo(num):
    if num==0:
        print(1)
    else:
        cont=0
        while num!=0:
            num=num//10
            cont=cont+1
        return cont

def InvertirlistaFI(lista):
    if isisntance(lista,list):
        if lista==[]:
            return []
        else:
            Linvertida=[]
            for item in lista:
                Linvertida=[item]+Linvertida
            return Linvertida
    else:
        print("Parametro incorrecto")

def ManejoNumporlargo(num1, num2):#123 456
    if type(num1)==int and type(num2)==int and laego(num1)==largo(num2):
        num=abs(num1)
        num2=abs(num2)
        larg1=largo(num1)-1
        larg2=largo(num2)-1
        suma=0
        mult=1

        #larg1  larg2   suma    mult    num1    num2
        #2      2       0       1       123     456
        #1      2       3       1       12      456
        #0      2       3       2       1       456
        #-1     2       4       1       0
        #-1     1       4
        #-1     0       0
        #-1     -1      9
        while num1!=0:#123 si
            temp=num1%10 #3 2 1
            if larg1%2==0: #2%2SI 1%2NO 0%2SI
                suma=suma+temp
                #0+3=3
                #3+1=4
            else:
                mult=mult*temp
            num1=num1//10 #12 1 0
            larg1=larg-1 #1 0 1
        print(suma,mult) #4, 2

        while num2!=0: #456si 45si 4si
            temp=num2%10 #6 5 4
            if larg2%2==0: #2%2x 1%2si 0%2no
                suma=suma+temp
                #4+5=9
            else:
                mult=mult*temp
                #2*6=12
                #12*4=48
            num2=num2//10#45 4 0
            larg2=larg2-1
        print(suma,mult)
    else:
        prit("Error incorrecto")

#MAtrices
"""x=5
y=x
print(x,y)
x=x+1
print(x,y)

matriz=[[4,5],[4,1]]
matriz1=matriz
print(matriz, matriz1)
matriz=[[6,10],[4,1]]"""

"""def crammer():
    with open("ecuaciones.txt", "r") as archivo:
        lineas=[archivos.readlines()]"""
def crammer():
    with open("ecuaciones.txt", "r") as archivo:
        datos = [int(line.strip()) for line in archivo if line.strip() != ""]
    # Agrupamos los números en sublistas de 3 elementos
    ecuaciones = [datos[i:i+3] for i in range(0, len(datos), 3)]

    print(ecuaciones)
    F0C0=ecuaciones[0][0]
    F0C1=ecuaciones[0][1]
    F1C0=ecuaciones[1][0]
    F1C1=ecuaciones[1][1]
    F0C2=ecuaciones[0][2]
    F1C2=ecuaciones[1][2]

    determinante=F0C0*F1C1 - F1C0*F0C1
    print(determinante)
    determinantey=(F0C0*F1C2)-(F1C0*F0C2)
    print(determinantey)
    determinantex=F0C2*F1C1 - F1C2*F0C1
    print(determinantex)

    difx=determinantex/determinante
    dify=determinantey/determinante
    print(difx)
    print(dify)

    par_ordenado=(difx, dify)
    print(par_ordenado)
print(crammer())

#Determinante x
#matriz se sustituye los valores de igualdad por la columna de las x 0 2 y mantengo las y
#(0*1)-(2*1)