print(list(range(0,6,1)))
print(list(range(5,1))) #inicio en 5 y termina en 1, no puede generar la lista
print(list(range(5)))   #
print(list(range(1,5))) #inicie en 1, termine en 5
print(list(range(1,5,-1))) #porque le estamos diciendo que vaya decrementando
print(list(range(0,20,5))) #
print(list(range(0,30)))

#___________________________________________________________________
#Codigo auxiliar
def largo(num):
    if isinstance(num, int):
        num=abs(num)
        if num==0:
            return 1
        else:
            cont=0
            
            for i in range(num):
                if num == 0:
                    return cont
                    # o con break
                cont=cont+1
                num=num//10
            print(cont)
    else:
          print("Parámetro incorrecto")

#__________________________________________________________________
def Sumatoria(n):
	suma = 0
	i = 0
	while i <= n:
		suma = suma + i
		i = i + 1
	print(suma)
	
def SumatoriaF(n):
	suma = 0
	for i in range (0, n+1, 1):
		suma=suma+i
	print(suma)
        
def Factorial(n):
    if isinstance(n, int):
        n=abs(n)
        if n==0 or n==1:
            return 1
        else:
            resultado=n
            for i in range(1,n):
                resultado=resultado*i
            return resultado
    else:
         print("Parametro incorrecto")

def sumatoria1(n):
    if type(n) == int and n>=0:
        n=abs(n)
        if n==0:
            return 1
        else:
            suma=0
            for i in range(0,n+1,1):
                suma=suma+(Factorial((Factorial(i))+((n+i)**2)))
            return suma
    else:
         print("Parametro incorrecto")


def largoSD(lista):
    if type(lista) == list:
        if lista==[]:
            return 0
        else:
            cont = 0
            for i in range (0, len(lista), 1): #(len(lista))
                cont = cont + 1
            return cont
    else:
        print("Parametro incorrecto")

def SumarElementosLista(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else:
            suma=0
            for i in range(len(lista)):
                suma=suma+lista[i]
            return suma
    else:
        print("Parametro incorrecto")

#Escribir dos funciones
        #Contar los pares de una lista D y SD

def conta_pares_SD(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else:
            for i in range(len(lista)):
                if lista[0]%2==0:
                    cont=cont+1
                lista=lista[1:]
            return cont
    else:
        print("Parametro incorrecto")

def Contar_pares_D(lista):
    if isinstance(lista, list):
        if lista==[]:
            return 0
        else:
            cont=0
            for i in range(len(lista)):
                if lista[0]%2==0:
                    cont=cont+1
            return cont
    else:
        print("Parametro incorrecto")

def prueba(lista):
    if lista==[]:
        return 0
    else:
        cont=0
        for item in lista:
            cont=cont+item
        print(cont)

def num_a_lista(n):
    lista=[]
    for i in range(n):
        if n!=0:
            lista=[n%10]+lista
            n//=10
        else:
            return lista
            break
    return lista
"""
Escribir una funcion que recibe dos parametros digito entero y positivo
num entero y positivo
pasa a lista
contar las apariciones del digito dentro del numero
WhileSD
WhileD
For range
For item
"""

def contar_digito(digito, n):
    if isinstance(digito, int) and isinstance(n, int):
        digito=abs(digito)
        n=abs(n)
        if digito > 9:
            return "El dígito debe estar entre 0 y 9"
        lista_digitos = num_a_lista(n)
        contador = 0
        for i in range(len(lista_digitos)):
            if lista_digitos[i] == digito:
                contador += 1
        
        return contador
    else:
        print("Los parametros deben ser enteros positivos")
    
def EncontrarNumSD(busq, num):
    lista=[]
    num=abs(num)
    busq=abs(busq)
    if isinstance(num, int) and  isinstance(busq, int):
        lista=num_a_lista(num)
        cont=0
        contapariciones = 0
        while len(lista)>cont:
            if lista[cont]==busq:
                contapariciones += 1
            cont += 1
        print(contapariciones)
    else:
        print("Parametros incorrectos")

#While Des
def whileD(digito, num):
    if isinstance(digito, int) and isinstance(num, int):
        digito = abs(digito)
        num = abs(num)
        num=pasalistafor(num)
        cont=0
        while num!=[]:
            if digito = num[0]:
                cont += 1
            num=num[1:]
        return cont
    else:
        print("Parametro incorrecto")


