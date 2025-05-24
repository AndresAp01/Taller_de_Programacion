#Luis Andres Acunna Perez
#
#MENU
ans=True
while ans:
    print ("""
    1.Ordenamientos
    2.Busquedas
    3.Salir
    """)
    ans=input("Que le gustaria hacer? ")
    if ans=="1":
        print("""
        Opciones de ordenamiento:
        1. Burbuja
        2. Seleccion
        3. Insercion
        4. Shell
        5. Quicksort
        """)
        op=input("\n Escoga la opcion:")

        if op=="1":
          print("""
            primer ordenamiento
            """)
        elif op=="2":
            print("Segundo ordenamiento")

    elif ans=="2":
      print("\n Opciones de Busquedas:")
    elif ans=="3":
      print("\n Adios!")
      break
    elif ans !="":
      print("\n No es una opcion valida.")


#CODIGOS
#AUXILIARES
def largo(num):
    if num==0:
        print(1)
    else:
        cont=0
        while num!=0:
            num=num//10
            cont=cont+1
        return cont
#BURBUJA
def ordenamientoBurbuja(lista):
    for i in range(1, len(lista)):
        for j in range(0, len(lista) - i):
            if (lista[j] > lista[j + 1]):
                k = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = k
        print(lista)
#SELECCION
def selectionsort(lista):
    for i in range(0, len(lista) - 1):
        minimo = i
        for j in range(i + 1, len(lista)):
            if lista[minimo] > lista[j]:
                minimo = j
            aux = lista[minimo]
        lista[minimo] = lista[i]
        lista[i] = aux
        print(lista)

#INSERCION
def insercionDirecta(lista):
    for i in range(1, len(lista)):
        v=lista[i]
        j=i-1
        while j>=0 and lista[j]>v:
            lista[j+1]=lista[j]
            j=j-1
        lista[j+1]=v
    print(lista)
"""    todas
    las
    pasadas"""

#SHELL
def  ordenShell(lista):
     inc=int(len(lista)/2 )
     while  inc>0:
          for  i in range(inc,len(lista)):
               j=i
               temp=lista[i]
               while j>=inc and lista[j-inc]>temp:
                    lista[j]=lista[j-inc]
                    j=j-inc
               lista[j]=temp
          if (inc==2) :
               inc=1
          else :
               inc=int(inc/2.5)
     print(lista) #todas las pasadas

#QUICKSORT
def quicksort(lista):
    if len(lista)==1 or len(lista)==0:
        return lista
    else:
        pivot=lista[0]
        print(pivot)
        i=0
        for j in range(len(lista)-1):
            if lista[j+1]<pivot:
                lista[j+1],lista[i+1]=lista[i+1], lista[j+1]
                i+=1
        lista[0],lista[i] = lista[i],lista[0]
        primera=quicksort(lista[:i])
        segunda=quicksort(lista[i+1:])
        primera.append(lista[i])
        print(primera + segunda)
    return (primera+segunda)  #todas las pasadas
#RAIDX
def Radix(lista):
    print(lista)
    max_num=lista[0]
    for num in lista:
        if num>max_num:
            max_num=num
    largo_mayor=largo(max_num)
    print(max_num, largo_mayor)
    for _ in range(largo_mayor):
        lista_temp=[]
        for i in range(10):
            lista_temp=lista_temp+[[]]
        for i in range(len(lista)):
            digito=(lista[i]//(10**_))%10
            lista_temp[digito]=lista_temp[digito]+[lista[i]]
            print(lista_temp)
        lista_completa=[]
        for i in range(10):
            lista_temp_ordenada=insercionDirecta(lista_temp[i])
            lista_completa=lista_completa+lista_temp_ordenada
        lista=lista_completa
    print(lista)


#BUSQUEDAS
#BINARIA
def busquedaBinaria(lista,item):
    primero=0
    ultimo=len(lista)-1
    encontrado=False
    while primero <=ultimo and not encontrado:
        puntoMedio=(primero+ultimo)//2
        if lista[puntoMedio]==item:
            encontrado=True
        else:
            if item<lista[puntoMedio]:
                ultimo=puntoMedio-1
            else:
                primero=puntoMedio+1
    print (encontrado) #todas las pasadas

#SECUENCIAL
def busquedaSecuencial(lista,nume):
    posicion=0
    encontrado=False
    while posicion < len(lista) and not encontrado:
        if lista[posicion]== nume:
            encontrado = True
        else:
            posicion = posicion+1
    print (encontrado) #todas las pasadas

#SHAKE COCKTAIL
def cocktailSort(lista):
    n=len(lista)
    intercambiado=True
    inicio=0
    final=n-1
    while intercambiado:
        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        intercambiado=False

        # loop from left to right same as the bubble
        # sort
        for i in range(inicio, final):
            if (lista[i]>lista[i + 1]):
                lista[i], lista[i+1]=lista[i+1], lista[i]
                intercambiado = True

        # if nothing moved, then array is sorted.
        if not intercambiado:
            break
        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        intercambiado=False
        # move the end point back by one, because
        # item at the end is in its rightful spot
        final=final-1
        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(final-1, inicio-1, -1):
            if (lista[i]>lista[i+1]):
                lista[i], lista[i+1]=lista[i+1], lista[i]
                swapped=True
        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start=start+1
