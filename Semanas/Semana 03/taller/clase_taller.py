#Clase Jueves 6 Intro
#type(parametro)==tipo
#return si se ejecuta dentro del ciclo, rompe el ciclo
#break rompe el ciclo

#La siguiente tarea se revisa con el asistente
#Cita de revision

#----------------------------------------------------------------
"""Que es un factorial
Parametro n
Si n < 0 no esta definito, no se puede trabajar con valor absoluto
Si n = 0 por definicion, es igual al valor "1"
Si n > 0 se define n * (n-1) * (n-1) ... hasta que n = 0


#Escribir una funcion que recibe un parametro que debe ser entero y mayor
o igual para aplicar le factorial """

def factorialINC(num): #Funciona
    if num<0 or not type(num)==int:
        print("Parametro de entrada no valido")
    elif num==0:
        return 1
    else:
        #resultado  i   num
        #4          1   4
        #4          2   4
        #8          3   4
        #24         4   4
        
        resultado=num
        i=1
        while i<num: #1<4? si 2<4 si 3<4si 4<4no
            resultado=resultado*i
            #4*1=4 4*2=8 8*3=24
            i=i+1#2 3 4
        return resultado #24

def factorialDEC(num): #Funciona
    if num<0 or not type(num)==int:
        print("Parametro de entrada no valido")
    elif num==0:
        return 1
    else:
        #resultado  i   num
        #1          4   4
        #4          3   4
        #12         2   4
        #24         1   4
        #24         0   4
        
        resultado=1
        i=num
        while i>0:#4>0 si 3>0 si 2>0si 1>0 SI 0>0X
            resultado=resultado*i
            #1*4=4 4*3=12 12*2=24 24*1=24
            i=i-1#3 2 1 0
        return resultado #24
        
def SumatoriaFacto(num):
    #El numero debe empezar en 1
    if num>0 and type(num)==int:
        suma=0
        i=1
        #suma   i   num
        #0      1   4
        #0      2   4
        #3      3   4
        #9      4   4
        #33     5   4
        
        while i<=num:#1<=4 si 2<=4 si 3<=4 si 4<=4 si 5<=4 no
            suma=suma+(factorialINC(i))
            #0+(factorial(1))=0+1=1
            #1+(factorial(2))=1+2=3
            #3+(factorial(3))=3+6=9
            #9+(factorial(4))=9+24=33
            
            i=i+1 #2 3 4
        print(suma)
    else:
        print("Parametro incorrecto")

#Escribir una funciomn que recibe un numero entero uy positivo
        #para calcular la siguiente sumatoria

def SumatoriaFacto2(num): #n=1
    if num<0 or not type(num)==int:
        print("Parametro de entrada no valido")
    elif num==0:
        return
    else:
        #suma   i   num
        #0      0   1
        #1      1   1
        #3      2   1
        
        suma=0
        i=0
        while i<=num:#0<=1 si 1<=1 si 2<=1 no
            suma=suma+((i*num)+((factorialINC(i)**2)*(factorialINC(i)**3)))
            #i=0 num=1
            #0=0+((0*1)+((factorialINC(0)**2)*(factorialINC(0)**3)))
            #0=0+((0)+((1**2)*(1**3))))
            #0+((0)+(1*1))=1

            #i=1 num=1
            #1=1+((1*1)+((factorialINC(1)**2)*(factorialINC(1)**3)))
            #1=1+((1)+((1**2)*(1**3))))
            #1+((1)+(1*1))=1+(1+1) = 3
            i=i+1 #1 2
        return suma #retorna

#-------------------------------------------------------------------
#Escribir una funcion que permite saber si un numero tiene un digito par
#Recibe un numero entero y positivo, si llega a negativo, puede utilizar abs()
#Retornar True or False (booleana)
#num=23456789
#    =3579 False
#    =35769 True

def espar(num): #Funciona #57891
    if not type(num)==int:
        print("Parametro incorrecto")
    elif num==0 or num==2 or num==4 or num==6 or num==8:
        return True
    else:
        
        haypar=False #Equivale a una bandera
        #y saquemosle una copia al numero para no eliminar el original
        copia=abs(num)

        #copia  espar   num
        #57891  False   57891
        #5789   False   57891
        #578   False   57891
        
        while copia!=0: #57891si 5789 578 si
            temp=copia%10 #1 9
            if temp%2==0: #1%2 no 9%2 no 8%2si
                haypar=True #TRUE
                break #Para porque ya encontró UNO no hace falta buscar más
            copia=copia//10 #5789 578
        return haypar, copia

#-----------------------------------------------------------------------------
    #TALLER
#----------------------------------------------------------------------------


def ejemploprint(num):
    cont=0
    while num!=0:
        cont=cont+1
        num=num//10
    print("cantidad de digitos contados: ", cont, num)
    #Imprimer el valor de la ultima pasada
    
def ejemploprint2(num):
    cont=0
    while num!=0:
        cont=cont+1
        num=num//10
    print("cantidad de digitos contados: ", cont, num)
    #Imprimer el valor de la ultima pasada



def ejemploreturn(num):
    cont=0
    while num!=0:
        cont=cont+1
        num=num//10
    return "cantidad de digitos contados: ", cont, num
    #Imprimer el valor de la ultima pasada

def ejemploreturn2(num):
    cont=0
    while num!=0:
        cont=cont+1
        num=num//10
    return "cantidad de digitos contados: ", cont, num
    #Imprimer el valor de la primera pasada

def ejemplobreak(num):
    cont=0
    while num!=0:
        cont=cont+1
        num=num//10
    print("cantidad de digitos contados: ", cont, num)

#colocar el valor de retorno dentro del while equivale a un print
#con un break 
    #TALLER
#----------------------------------------------------------------------------
#Que son las listas
"""
//Las listas son un conjunto de informacion y que esta incluida en []
los elementos de la lista se separan con comas ","
las listas no tienen tamaño definido, se consideran estructuras dinamicas
esto quiere decir que crecen y decrecen en tiempo de ejecución

Ejemplo:
 [2, 4, 5, 6, 1, 90, 100] los elementos estan asi: [,,,]

// Listas son indexadas
Ejemplo: El elemento 90 esta en la posición {5}
Las posiciones inician desde la {0} terminan en la cantidad de elementos -1

//Las listas son mutables, pueden cambiar en tiempo de ejecucion
La infor se encuentra secuencial,ente
"""

lista=[2,5,6,10,0,100,7,8,9]
print(lista)    #Toda la lista
print(lista[5]) #100            print lista sub 5 // mutable
lista[5]=500    #Actualiza la lista en el elemento 5 por {500}
print(lista)

print(len(lista))   #=> cantidad de elementos
num=34567           #len NO definido para números
#print(len(num)) #error porque la funcion len no esta definida para numeros
#por eso hacemos la funcion de largo" para que nos de el alrgo de un numero

#Slice permite sacar pedacitos de la lista
#sintaxis: [<opcional inicio>:<opcional final>]
#valor final siempre ccorta uno antes

Lista=[2,3,5,6,7,9,1,0]
print(Lista[1:3])   #Imprimir desde pos1 hasta pos3-1 (porque corta 1 antes, llega hasta 2)
                    #[3, 5]

print(Lista[1:])    #Imprimir desde pos1 y no indica final (por lo q no corta)
                    #[3, 5, 6, 7, 9, 1, 0]

print(Lista[:2])    #Imprimir desde {no hay pos de inicio, por lo q inicia en la 0}
                    #Hasta la pos2-1 (porque corta 1 antes, llega hasta 1)
                    #[2, 3]

print(Lista[4:7])   #Imprimir desde la pos4 hasta la 7-1 (porque corta 1 antes, llega hasta 6)
                    #uno antes hasta la 6
                    #[7, 9, 1]

print(Lista[:])     #Imprimir desde {no hay pos inicio, desde 0} hasta {no hay valor final, termina en el final de la lsita y no corta}
                    #[2, 3, 5, 6, 7, 9, 1, 0]

print(Lista[2:8])   #Imprimir desde la pos 2 hasta la pos8-1 (porque corta 1 antes, llega hasta 7)
                    #[5, 6, 7, 9, 1, 0]

#Trabajar con listas se puede trabajar destruyendo y sin destruir

#Escribir una función que recibe una lista, validar que sea lsita
#Calcular el largo e la lista destruyendo y sin destruir

#Destruyendo
def largolista(lista): #cualquier lista: [5,6,7,8,1,0]
    if type(lista)==list: #si pregunto por un int me da error
        if lista==[]: #Preguntamos si la lista es vacía
            return 0
        else:
            cont=0
            #contador   lista
            #0      [5,6,7,8,1,0]
            #1      [6,7,8,1,0]
            #2      [7,8,1,0]
            #3      [8,1,0]
            #4      [1,0]
            #5      [0]
            #6      []
            
            while lista!=[]:    #[5,6,7,8,1,0] si tiene elementos #[6,7,8,1,0] si  [7,8,1,0] si
                                #[8,1,0] si tiene, #[1,0] si [0]si []no
                cont=cont+1     #1 #2 #3 #4 #5 #6
                lista=lista[1:] #[6,7,8,1,0] #[7,8,1,0] #[8,1,0] #[1,0] #[0] #[]
            print(cont, lista)  #6, []
    else:
        print("Parametro incorrecto")

#Sin destruir
def largoSD(lista):
    if type(lista)==list: #si pregunto por un int me da error
        if lista==[]: #Preguntamos si la lista es vacía
            return 0
        else:
            cont=0
            i=0
            #contador   i   lista
            #0      0   [5, 6, 7, 8, 1, 0]
            #1      1   [5, 6, 7, 8, 1, 0]
            #2      1   [5, 6, 7, 8, 1, 0]
            #3      3   [5, 6, 7, 8, 1, 0]
            #4      4   [5, 6, 7, 8, 1, 0]
            #5      5   [5, 6, 7, 8, 1, 0]
            #6      6   [5, 6, 7, 8, 1, 0]

            
            while i<len(lista): #0<6si 1<6si 2<6si 3<6si 4<6si 5<6 si 6<6 no
                i=i+1           #1 2 3 4 5 6
                cont=cont+1     #1 2 3 4 5 6
            print(cont, lista)  #6, {En este ejercicio la variable i es para posiciones, la contador es un contador, pero justo sale que van las dos igual
            #}
    else:
        print("Parametro incorrecto")

#Escribir la siguiente funcion que recibe una lista, validar
        #contar los pares de la lista, destruyendo y sin destruir
###Tarea, numeros intro y listas d taller 

#Destruyendo
def ContarParesD(lista): #[5,6,7,8,9,1,0] 
    if type(lista)==list:
        if lista==[]:
            return 0
        else:
            cont=0
            #contador   lista
            #0      [5,6,7,8,9,1,0] P0=5
            #0      [6,7,8,9,1,0]   P0=6
            #1      [7,8,9,1,0]     P0=7
            #1      [8,9,1,0]       P0=8 ***
            #2      [9,1,0]         P0=9
            #2      [1,9]           P0=1
            
            
            while lista!=[]:        #[5,6,7,8,9,1,0] si [6,7,8,9,1,0] si [7,8,9,1,0] si
                                    #[8,9,1,0] si [9,1,0] si [1,0] si [0] si [] no
                if lista[0]%2==0:   #5%2x 6%2si 7%2no 8%2si 9%2no 1%2no 0%2si
                    cont=cont+1     #1 2 3
                lista=lista[1:]     #[6,7,8,9,1,0] [7,8,9,1,0] [8,9,1,0]
            print(cont)             #3
    else:
        print("parametro no")

#Sin destruir
def ContarParesSD(lista): #[5,6,7,8,9,1,0]
    if type(lista)==list:
        if lista==[]:
            return 0
        else:
            cont=0
            i=0
            #contador   i   lista
            #0      0   [5,6,7,8,9,1,0] i=0=>5
            #0      1   [5,6,7,8,9,1,0] i=1=>6 ****
            #1      2   [5,6,7,8,9,1,0] i=2=>7
            #1      3   [5,6,7,8,9,1,0] i=3=>8
            #2      4   [5,6,7,8,9,1,0] i=4=>9
            #2      5   [5,6,7,8,9,1,0] i=5=>1
            #3      6   [5,6,7,8,9,1,0] i=6=>0

            #si ponemos <=len porque se sale de los limites
            while i<len(lista):    #0<=7?si #1<=7?si 2<=7?si 3<=7?si 4<=7?si 5<=7?si 6<=7?si
                                    #7<=7 ya no me deja trabajar, por lo que se debe cambiar a solo <
                if lista[i]%2==0:   #5%2x 6%2si 7%2no 8%2si 9%2no 1%2no 0%2si
                    
                    cont=cont+1     #1 2 3
                i=i+1
            print(cont)
    else:
        print("Parametro incorrecto")
        
