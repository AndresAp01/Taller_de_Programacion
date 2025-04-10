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

def seleccion(lista):
    if type(lista)==list:
        for i in range(0, len(lista)-1):
            minimo=i
            for j in range(i+1, len(lista)):
                if lista[minimo]>lista[j]:
                    minimo=j
                aux=lista[minimo]
            lista[minimo]=lista[i]
            lista[i]=aux
            print(lista)
    else:
        print("Parametro incorrecto")

def Problema2_1(num1, num2):
    lista1=pasalista(num1)
    lista2=pasalista(num2)
    if len(lista1)!=len(lista2):
        print("Los numeros deben tener el mismo largo")
    n=len(lista1)

    lista=[]
    izquierda=range(0, n, 1)
    derecha=range(n-1, -1, -1)
    for i in range(n):
        if i%2==0:
            lista+=[lista1[izquierda[i//2]]+lista2[derecha[i//2]]]

        else:
            lista+=[lista1[derecha[i//2]]+lista2[izquierda[i//2]]]

    return lista

# ordenamientos
# desde el menos eficiente pero mas sencillo burbuja iterativo
#... al mas eficiente pero mas complicado de programar quicksort recursivo
#ascendentes o descendentes

#ordenamiento burbuja
#cantidad de la informacion, realiza n pasadas por la información
# len de la informacion -1

def ordenamientoBurbuja(lista):#[9,1,0,10,2]
    #lista 1era pasada#[9,1,0,10,2] [1,9,0,10,2] [1,0,9,10,2] [1,0,9,2,10] 
    #Lista 2da pasada [1,0,9,2,10][0,1,9,2,10][0,1,2,9,10]
    #lista 3era pasada [0,1,2,9,10]
    #lista 4ta pasada
     for i in range(1,len(lista)):#i= 1si 2si 3si 4si 5x
         #Primera pasada i=1si
         #Segunda pasada i=2si
         #Tercera pasada i=3si
         #Cuarta pasada i=4si
         
          for j in range(0,len(lista)-i):#j
              #  i=1 1era Pasada j=0si 1si 2si 3si 4x 5-1=4x
              # 2da pasada  j=0si  1si 2si 3x         5-2=3x
              # 3era pasada j=0si j=1si 2x            5-3=2x
              #4ta pasada j=0 1x                      5-4=1x
             
               if(lista[j] > lista[j+1]):
                   #1era pasada i=1 j=0si 1si 2si 3 [0,1,2,9,10]
                   #9>1si 9>0si 9>10x 10>2si
                   #2da pasada i=2 j=0si 1si 2si
                   #1>0si 1>9x 9>2x
                   #3era pasada
                   #0>1x 1>2x
                   #4ta pasada
                   #0>1x
                    temporal = lista[j+1]
                    #Primera pasada 1 0 2
                    #0 2
                    
                    lista[j+1] = lista[j]
                    #[9,9,0,10,2] [1,9,9,10,2] [1,0,9,10,10]
                    #[1,0,9,2,10] [1,1,9,9,2][0,1,9,9,10]
                    lista[j] = temporal
                    #[1,9,0,10,2] [1,0,9,10,2] [1,0,9,2,10] 
                    #[0,1,2,9,10]
               print(lista)#[0,1,2,9,10]


#Ordenamiento de Seleccion
def seleccion(lista):
    #[4,20,1,10,3]
    #[1,20,4,10,3]
    #[1,3,4,10,20]
    #[1,3,4,10,20]
    #[1,3,4,10,20]
    
    for i in range(0,len(lista)-1):#i=0si 1si 2si 3 4x(len(lista)-1) 5x
        minimo=i#0 1 2 3
        for j in range(i+1,len(lista)):
            #j=1si 2si 3si 4si 5x
            #i=0 j=1 j=2 j=3 j=4 1era pasada
            #i=1 j=2 j=3 j=4 5x
            #i=2 j=3 4 5x
            #i=3 j=4 5x
            if lista[minimo]>lista[j]:
           
                
                minimo=j#2 2 4
            aux=lista[minimo]#4 1 1 1 4 4 3 4 4 10
        lista[minimo]=lista[i]#[4,20,4,10,3] [1,20,4,10,20] [1,3,4,10,20][1,3,4,10,20]
        lista[i]=aux#[1,20,4,10,3][1,3,4,10,20] [1,3,4,10,20][1,3,4,10,20]
        print(lista)


#Ordenamiento
def insercion(lista):#[4,20,1,10,3]
    for i in range (1,len(lista)):#i=1,2,3,4,5x
        v=lista[i]#
        j=i-1#
        while j>=0 and lista[j]>v:
            
            lista[j+1]=lista[j]
            j=j-1#
        lista[j+1]=v #
        print(lista)


# Escribir una funcion que una busqueda en una lista. Secuencial, de uno en uno comparando
# el elemento
#[3,6,1,9,0],9
#Validar la lista, numero entero

def Busquedasecuencial(lista,num):#
    if type(lista)==list and type(num)==int:
        posicion=0#
        encontrado=False#
        while posicion < len(lista) and not encontrado:
            print(posicion)
              
              
            if lista[posicion]==num:
                
                encontrado=True #
                #break
            else:
                posicion=posicion+1
        return encontrado
    else:
        print("Parametro incorrecto")

Busquedasecuencial([0,1,3,6,9], 0)

#Escribir una funcion que trabaja buscando un elemento dentro de una lista con
#busqueda binaria
# La lista debe estar ordenada, puede ser ascendente o descendente
            
   #REQUISITO
   #los datos tienen que estar ordenados

def BusquedaBinaria(lista,num):#
    
    if isinstance(lista,list) and isinstance(num,int):
        primero=0
        ultimo=len(lista)-1
        encontrado=False
        #primero     ultimo    encontrado      lista              num
       
        
        while primero<=ultimo and not encontrado:
            
            puntomedio=(primero+ultimo)//2#
            if lista[puntomedio]==num:#
                encontrado=True
            else:
                if num<lista[puntomedio]:#
                    ultimo=puntomedio-1#
                else:
                    primero=puntomedio+1#
        print(encontrado)#F
                
    else:
        print ("Parametro incorrecto")

BusquedaBinaria([1,4,5,8,9,12,15],4)