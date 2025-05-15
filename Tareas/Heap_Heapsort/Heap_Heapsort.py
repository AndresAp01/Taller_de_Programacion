#Heap y Heapsort

#Ingresa una lsita
#Lista_original es una copia de la lista
def heap(Llave):
    print("Lista inicial: ", Llave)
    for i in range(2, len(Llave)):
        Siguiente=i
        Padre=Siguiente//2
        NuevaLlave=Llave[i]
        Llave[Siguiente]=NuevaLlave
        print("Pasada: ", Llave)
        while Siguiente!=1 and Llave[Padre]<=Llave[Siguiente]:
            Auxiliar=Llave[Padre]
            Llave[Padre]=Llave[Siguiente]
            Llave[Siguiente]=Auxiliar
            Siguiente=Padre
            Padre=Siguiente//2
    heapsort(Llave)
    return Llave[1:]

def heapsort(Llave):
    for Ultima in range(len(Llave)-1, 1,-1):
        #Mueve la llave raíz al último lugar
        Llaveanterior=Llave[Ultima]
        Llave[Ultima]=Llave[1]
        #Ajusta el árbol al tamaño menos 1
        Padre=1
        #Busca al mayor de los hijos de la raíz
        if (Ultima-1>=3) and (Llave[3]>Llave[2]):
            Hijo=3
        else:
            Hijo=2
        #Mueve las llaves hacia arriba hasta encontrar el lugar para la Llaveanterior
        while (Hijo<=Ultima-1) and (Llave[Hijo]>Llaveanterior):
            Llave[Padre]=Llave[Hijo]
            Padre=Hijo
            Hijo=Padre * 2
            #Encuentra al mayor de los hijos del padre
            if (Hijo+1<=Ultima-1) and (Llave[Hijo+1]>Llave[Hijo]):
                Hijo=Hijo+1

        Llave[Padre]=Llaveanterior


# Ejemplo de uso
#print(heap([2,4,1,70,3,4,200]))
