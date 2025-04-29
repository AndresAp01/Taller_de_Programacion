#Clase Martes Semana 4 // intro
#Escribir una funcion que recibe una lista,
#suma los elementos impares de la lista ** 2 destruyendo y sin destr.

#Destruyendo
def funcion1(lista):
    if type(lista)==list:
        #if isinstance(lista, list)
        if lista==[]:
            return 0

        suma = 0
        multi = 1

        lista_copia = lista[:]
        while lista_copia:
            ultimo = lista_copia[0]
            if ultimo%2==0:
                multi = multi*(ultimo)
                #multi=multi*lista_copia[0]**2
            else:
                suma = suma+(ultimo**2)

            lista_copia = lista_copia[1:]
            
        print("La suma de los impares es: ",suma)
        nuev_valor= multi * suma
        return nuev_valor

    else:
        print("Debe escribir una lista")

#Sin destruir

def funcion2(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else:
            suma=0
            multi=1
            i=0

            while i<len(lista):
                if lista[i]%2==0:
                    multi*=lista[i]
                else:
                    suma+=lista[i]**2
                    
                i=i+1
            nuevo_valor = multi*suma
            print("El valor de la suma: ", suma,"El valor req es:", nuevo_valor)
            return nuevo_valor
            
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Numeros de derecha a izq

num = 123406
temp = num%10
print(temp)
num=num//10
print(num)

#De izq a der
num = 123406
temp = num%10
temp = num//(10**(6-1)) #El **6-1 es porque no tenemos la funcion len
#temp = num//10**(largo(num)-1)
print(temp)
num = num%10**(6-1)
print(num)

#------------ Largo ------------------------

def largo(num):
    if num==0:
        print(1)
    else:
        cont=0
        
        while num!=0:
            num=num//10
            cont=cont+1
        return(cont)
        
#------------ Largo ------------------------

#------------ Suma sin ceros ---------------
    #------------ Quiz ---------------
        
#Escribir una funcion que recibe dos num de cualq largo igual tamaño
def sumasinceros(num1, num2):
    #num1 = abs(num1)
    #num2 = abs(num2)
    if type(num1)==int and isinstance(num2, int) and largo(num1)==largo(num2):
        num1 = abs(num1)
        num2 = abs(num2)
        exp1=0
        exp2=0
        nuevo_num_1=0
        nuevo_num_2=0

        while num1!=0:
            if num1%10==0:
                num1=num1//10
            
            else:
                nuevo_num_1=nuevo_num_1 + ((num1%10)*(10**exp1))
                num1=num1//10
                exp1=exp1+1

        print(nuevo_num_1)

        while num2!=0:
            if num2%10==0:
                num2=num2//10
            
            else:
                nuevo_num_2=nuevo_num_2 + ((num2%10)*(10**exp2))
                num2=num2//10
                exp2=exp2+1

        print(nuevo_num_2)
        print("La suma total es: ",nuevo_num_1 + nuevo_num_2)
    else:
        print("Algun parametro es incorrecto.")
        

#Eliminar los 0 y contruir dos numeros nuevos
    #------------ Quiz ---------------
#------------ Suma sin ceros ---------------

#Escribir una funcion que recibe un numero positivo y uno negativo
        
lista=[2,3]
lista=lista+[100]
print(lista)
lista=[200]+lista
print(lista)

def numalista1(n):
    if n>0 and isinstance(n, int):
        num=abs(num)
        lista=[]
        while n>0:
            lista=[n%10]+lista
            n//=10
        print(lista)


#---------------Promedio lista------------------
        #-------Destruyendo---------------------

        
def promedio_lista_SD(lista):
    if type(lista)==list:
        i=0
        promedio=0
        
        while i<len(lista):
            promedio=promedio+lista[1]
            i+=1
        promedio/=len(lista)
        print(promedio)
        
def promedio_lista_D(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else:
            i=0
            promedio=0
            while len(lista)>0:
                promedio+=lista[0]
                lista=lista[1:]
                i+=1
            promedio/=i
            print(promedio)
            
