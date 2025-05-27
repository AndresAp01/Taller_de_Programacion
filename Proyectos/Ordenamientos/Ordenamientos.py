#Luis Andres Acunna Perez
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
        for j in range(0, len(lista)-i):
            if (lista[j]>lista[j+1]):
                k=lista[j+1]
                lista[j+1]=lista[j]
                lista[j]=k
    print(lista)
#SELECCION
def selectionsort(lista):
    for i in range(0, len(lista)-1):
        minimo=i
        for j in range(i+1, len(lista)):
            if lista[minimo]>lista[j]:
                minimo=j
            aux=lista[minimo]
        lista[minimo]=lista[i]
        lista[i]=aux
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
#MERGE
def merge_sort(my_list):  # merge sort sacado de data camp
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1
    print(my_list)  # todas las pasadas

#SHAKE
def shake(lista):
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i]>lista[j]:
                lista[i],lista[j]=lista[j],lista[i]
    print(lista)
print(shake([4,2,1,6,8]))
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
    #Para imprimir todas las pasadas:
    return (primera+segunda)
#RADIX
def Radix(lista):
    if not isinstance(lista, list):
        return "Dato invalido"
    elif lista==[]:
        return []
    else:
        for i in range(len(lista)):
            if lista[i] < 0:
                return 'Hay elementos negativos en la lista'

        mayor=0
        for i in range(len(lista)):
            if i==0:
                mayor=lista[i]
            else:
                if lista[i] > mayor:
                    mayor = lista[i]

        cont = 0
        for i in range(largo(mayor)):
            l0=[]
            l1=[]
            l2=[]
            l3=[]
            l4=[]
            l5=[]
            l6=[]
            l7=[]
            l8=[]
            l9=[]
            while lista != []:
                if (lista[0]//(10**cont))%10==0:
                    l0+=[lista[0]]
                elif (lista[0] // (10 ** cont)) % 10 == 1:
                    l1+=[lista[0]]
                elif (lista[0] // (10 ** cont)) % 10 == 2:
                    l2+=[lista[0]]
                elif (lista[0] // (10 ** cont)) % 10 == 3:
                    l3+=[lista[0]]
                elif (lista[0] // (10 ** cont)) % 10 == 4:
                    l4+=[lista[0]]
                elif (lista[0] // (10 ** cont)) % 10 == 5:
                    l5+=[lista[0]]
                elif (lista[0] // (10 ** cont)) % 10 == 6:
                    l6+=[lista[0]]
                elif (lista[0] // (10 ** cont)) % 10 == 7:
                    l7+=[lista[0]]
                elif (lista[0] // (10 ** cont)) % 10 == 8:
                    l8+=[lista[0]]
                elif (lista[0] // (10 ** cont)) % 10 == 9:
                    l9+=[lista[0]]
                lista=lista[1:]
            print(l0, l1, l2, l3, l4, l5, l6, l7, l8, l9)
            lista=lista+l0+l1+l2+l3+l4+l5+l6+l7+l8+l9
            print(lista)
            cont+=1
        return lista

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

def largo(n):
    if not isinstance(n, int):
     return 'Error'
    elif n==0:
     return 1
    cont=0
    for i in range(n):
     cont+=1
     n//=10
     if n==0:
         return cont

#MENU_______________________
def input_lista(mensaje):
    while True:
        entrada=input(mensaje).strip()
        if entrada.startswith('[') and entrada.endswith(']'):
            entrada=entrada[1:-1].strip()
        if "," in entrada:
            elementos=entrada.split(",")
        else:
            elementos=entrada.split()
        try:
            lista=[]
            for num_str in elementos:
                num_str=num_str.strip()
                if not num_str:
                    continue
                if '.' in num_str or not num_str.lstrip('-').isdigit():
                    raise ValueError
                lista.append(int(num_str))
            return lista
        except ValueError:
            print("¡Error! Ingresa solo enteros. Ejemplo: [6,1,3] o 6 1 3")

def menu():
    principal=(
                "1.Ordenamientos\n"
                "2.Busquedas\n"
                "3.Salir\n"
    )
    ordenamientos=(
                    "1.Burbuja\n"
                    "2.Seleccion\n"
                    "3.Insercion\n"
                    "4.Shell\n"
                    "5.Quicksort\n"
                    "6.Radix\n"
                    "7.Merge\n"
                    "8.Shake\n"
                    "9. Ingresar nueva lista\n"
                    "10.Salir\n"
    )
    busquedas=(
                "Ingrese una opcion\n"
                "1.Secuencial\n"
                "2.Binaria\n"
                "3.Salir\n"
    )

    lista_actual=None
    while True:
        print(principal)
        opcion=input("Ingrese una opcion(1-3): ")
        if opcion=="1": #Ordenamientos
            if lista_actual is None:
                lista_actual=input_lista("Ingrese la lista: ")
            while True:
                print(ordenamientos)
                y=input("Ingrese una opcion(1-9): ")
                if y=="1": ordenamientoBurbuja(lista_actual.copy())
                elif y=="2": selectionsort(lista_actual.copy())
                elif y=="3": insercionDirecta(lista_actual.copy())
                elif y=="4": ordenShell(lista_actual.copy())
                elif y=="5": quicksort(lista_actual.copy())
                elif y=="6": Radix(lista_actual.copy())
                elif y=="7": pass
                elif y=="8": pass
                elif y=="9":
                    lista_actual=input_lista("Ingrese la nueva lista: ")
                elif y=="10":
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opcion invalida")
        elif opcion=="2":
            if lista_actual is None:
                lista_actual=input_lista("Ingrese la lista: ")
            while True:
                print(busquedas)
                y=input("Ingrese una opcion(1-4): ")
                if y=="1":
                    lista=input_lista("Ingrese la lista: ")
                    num=int(input("Ingrese el numero a buscar: "))
                    busquedaSecuencial(lista_actual, num)
                if y=="2":
                    lista=input_lista("Ingrese la lista: ")
                    num=int(input("Ingrese el numero a buscar: "))
                    busquedaBinaria(lista_actual, num)
                elif y=="3":
                    lista_actual=input_lista("Ingrese la nueva lista: ")
                elif y=="4":
                    break
                else:
                    print("Opcion invalida")
        elif opcion=="3":
            print("Hasta luego!")
            break
        else:
            print("Opcion incorrecta")
menu()