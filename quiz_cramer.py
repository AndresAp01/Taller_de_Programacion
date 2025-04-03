#Quiz Luis Acunna Perez
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
    with open("ecuaciones.txt", "r") as archivo: #abre
        #line.strip para eliminar saltos 
        datos=[int(line.strip()) for line in archivo if line.strip()!=""]
        #range(0, len, 3) para tener indices de 0 hasta la longitud de datos, incremento de 3 en 3
        #datos[i:i+3] para cada indice i se extrae una sublista de 3
        #[x, y, soluc]
    ecuaciones=[datos[i:i+3] for i in range(0, len(datos), 3)]

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