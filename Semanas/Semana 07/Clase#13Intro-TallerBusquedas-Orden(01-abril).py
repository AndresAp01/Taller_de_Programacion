#Introduccion a ciclos anidados
#un ciclo dentro de otro ciclo
        #for       for       while     while    ciclo externo
          #for       while    while      for    ciclo interno

#el ciclo interno corre mas que el externo
for i in range(0,3):#i=0si 1si 2si 3x
    for j in range (0,4):
        print(i,j,"Hola")#j=0si 1si 2si 3si 4x

            #1era pasada i=0  j=0   0 0 Hola
                        #i=0  j=1   0 1 Hola
                        #i=0  j=2   0 2 Hola
                        #i=0  j=3   0 3 Hola

            #2da  asada i=1   j=0   1 0 Hola
                        #i=1  j=1   1 1 Hola
                        #i=1  j=2   1 2 Hola
                        #i=1  j=3   1 3 Hola

            #3era pasada i=2  j=0   2 0 Hola
                        #i=2  j=1   2 1 Hola
                        #i=2  j=2   2 2 Hola
                        #i=2  j=3   2 3 Hola


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
               
#Ordenamiento
def insercion(lista):#[4,20,1,10,3]
    #lista
    #P0 1  2  3 4
    #[4,20,1,10,3]
    #[4,20,1,10,3]
    #[4,20,20,10,3]2da pasada
    #[4,4,20,10,3]
    #[1,4,20,10,3]
    #[1,4,20,20,3]3ra pasada
    #[1,4,10,20,3]4ta pasada
    #[1,4,10,20,20]
    #[1,4,10,10,20]
    #[1,4,4,10,20]
    
    for i in range (1,len(lista)):#i=1,2,3,4,5x
        # i=1si  2si 3si 4si 5x
        #1era pasada i=1
        #2da pasada  i=2
        #3era pasada i=3
        #4ta pasada  i=4
        
        v=lista[i]#20 1 10 3
        j=i-1#0 1 2 1 3 2 1
        while j>=0 and lista[j]>v:
            #1era pasada 0>=0si 4>20x
            #2da pasada 
              #1>=0 and 20>1si
              #0>=0 and 4>1si
              #-1>=0x
            #3ra pasada
              #2>=0 and 20>10si
              #1>=0 and 4>10x
            #4ta pasada
              #3>=0 and 20>3si
              #2>=0 and 10>3si
              #1>=0 and 4>3si
              #0>=0 and 1>3x
            lista[j+1]=lista[j]
            j=j-1#0 -1 1 2 1 0
        lista[j+1]=v #[4,20,1,10,3][1,4,20,10,3][1,4,10,20,3][1,3,4,10,20]
        print(lista)


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

# Escribir una funcion que una busqueda en una lista. Secuencial, de uno en uno comparando
# el elemento
#[3,6,1,9,0],9
#Validar la lista, numero entero

def Busquedasecuencial(lista,num):#[3,6,1,9,0],9
    if type(lista)==list and type(num)==int:
        posicion=0#0 1 2 3
        encontrado=False#F
        while posicion < len(lista) and not encontrado:
            print(posicion)
              
              #0<5 and Fsi 1<5 and Fsi 2<% and Fsi 3<5 and Fsi
            if lista[posicion]==num:
                #3==9x 6==9x 1==9x 9==9si
                encontrado=True #T
                #break
            else:
                posicion=posicion+1
        return encontrado
    else:
        print("Parametro incorrecto")

#Escribir una funcion que trabaja buscando un elemento dentro de una lista con
#busqueda binaria
# La lista debe estar ordenada, puede ser ascendente o descendente
            
   
def BusquedaBinaria(lista,num):#[1,4,5,8,9,12,15],10
    
    if isinstance(lista,list) and isinstance(num,int):
        primero=0
        ultimo=len(lista)-1
        encontrado=False
        #primero     ultimo    encontrado      lista              num
        #0           7-1=6     F               #[1,4,5,8,9,12,15] 10
        #4           7-1=6     F               #[1,4,5,8,9,12,15] 10
        #4           7-1=4     F               #[1,4,5,8,9,12,15] 10
        #5           7-1=4     F               #[1,4,5,8,9,12,15] 10
        
        while primero<=ultimo and not encontrado:
            #0<=6 and F si 4<=6 and F si 4<=4 and Fsi 5<=4x
            puntomedio=(primero+ultimo)//2#(0+6)//2=3 (4+6)//2=5 (4+4)//2=4
            if lista[puntomedio]==num:#8==10x 12==10x 9==10x
                encontrado=True
            else:
                if num<lista[puntomedio]:#10<8x  10<12si 10<9x
                    ultimo=puntomedio-1#4
                else:
                    primero=puntomedio+1#3+1=4 4+1=5
        print(encontrado)#F
                
    else:
        print ("Parametro incorrecto")



