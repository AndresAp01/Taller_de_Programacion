#Luis Andres Acunna Perez

"""cadena="pepe"
print(cadena.capitalize())
print(cadena)
cadena=cadena.capitalize()
print(cadena)
#Convertiro a mayusculas
cadena="pablo"
cadena=cadena.upper()
print(cadena)
#Convertiro a minusculas
cadena="PABLO"
print(cadena.lower())
print(cadena)

cadena='esto es una prueba y es solo eso'
print(len(cadena))
Cadena tiene posibilidad de usar len y tambien es indexada
pos=0
mayuscula y minuscula son diferentes
Buscar un caracter es -1, no esta

find sintaxis ("cadena", <opcional inicio>, <opcional fin>)
en que posicion esta dentro de cadena
pos=cadena.find("es", 15)
print(pos)

cadena=cadena.replace("es", "ES", 2)
print(cadena)"""

#Escribir una funcion que recibe una cadena de numeros. Analiza cada digito, y si es par, lo cambia por 1.
def cambiar_par(cadena): #"345678" visualmente los str numericos se ven 345678
    if type(cadena)==str:
        for i in range(len(cadena)): #i=0si 1si 2si 3si 4si 5 6
            temp=''.join(cadena[i]) #Toma un caracter 3 internamente "3" "4" '5' '6' '7' '8'
            print("digito utilizado: ", temp) #'3' '4' '5' '6' '7' '8'
            temp=int(temp) #3 4 5 6 7 8
            if temp%2==0: #3%2no 4%2si  5%2no 6%2si 7%2no 8%2si
                cadena=cadena.replace(cadena[i], "1")
                #'345678'=>'315678'
                #'315678'=>'315178'
                #'315178'=>'315171'

        print(cadena)
    else:
        print("Debe escribir una cadena")

#print(cambiar_par("345678"))

#Escribir una funcion para contar la cantidad de digitos numericos
#'ty3s2rt3'

def cuentanumeros1(cadena):
    if type(cadena)==str:
        cont=0
        for i in range(len(cadena)): #i=0si 1si 2si 3si 4si 5 6 7 8no
            if cadena[i].isdigit():
                #'t'x 'y'x '3'si 's'x '2'si 'r'x 't'x '3'si'
                cont=cont+1 #1 2 3
        print(cont) #3
    else:
        print("Debe escribir una cadena")

#print(cuentanumeros1("ty3s2rt3"))

#Hasta aqui quiz

def cuentranumeros2(cadena): #'3sto 3s un 3j3mplo 123 p4r4 num3r0s 56'
    if type(cadena)==str:
        cont=0
        lista=[]
        lista=cadena.split(" ")
        #print(lista)
        #lista=['3sto', '3s', 'un', '3j3mplo', '123', 'p4r4', 'num3r0s', '56'']
        for i in range(len(lista)):#i=0 1 2 3 4 5 6 7 8x
            if lista[i].isdigit():
                #'3sto' x '3s' x 'un' x '3j3mplo' x '123'si 'p4r4' x 'num3r0s' x '56'si
                cont=cont+1 #1 2
        print(cont) #2
    else:
        print("Parametro incorrectp")

#print(cuentranumeros2("3sto 3s un 3j3mplo 123 p4r4 num3r0s 56"))

def largoSD(num): # 23456
    if num==0:
        return 1
    else:
        cont=0 #
        temp=num#Copia
        while temp!=0:  #23456 2345 234 23 2 0
            temp=temp//10 #2345  234  23  2 0
            cont=cont+1  #0 1 2 3 4 5
         #
        return cont #5

def PasalistaFor(num): #234  [2,3,4] 0 [0]

    if isinstance (num,int):
        num=abs(num)#234
        if num==0:
            return [0]
        else:
            listaNueva=[]#definiendo un lista vacia,almacenar los elementos
            for i in range(0,num):#234 23 2 0   i=0 1 2 3   233
                if num==0:
                    return listaNueva
                else:
                    listaNueva= [num%10]+listaNueva
                                #[4]+[]=[4]
                                #[3]+[]=[3,4]
                                #[2]+[3,4]=[2,3,4]
                    num=num//10#234 23 2 0

    else:
         print(" No es entero")

#Escribir una funcion que recibe dos numeros enteros positivos del mismo largo, validar, negativo con abs, se inserttan
#en dos listas
#Se intercalan las listas, se convierten a str y se imprimen como numero nuevo

def Intercalar(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int) and largoSD(num1)==largoSD(num2):
        num1=abs(num1)
        num2=abs(num2)
        lista1=PasalistaFor(num1)
        lista2=PasalistaFor(num2)
        print(lista1, lista2)
        lista3=[]
        #intercalar:
        i=0
        while i<len(lista1):
            lista3=lista3+[lista1[i]]+[lista2[i]]
            i=i+1
        print(lista3)
        for i in range(len(lista3)):
            lista3[i]=str(lista3[i])
        print(lista3)
        cadena=''.join(lista3)
        print(cadena)
    else:
        print("Parametros incorrectos")

#print(Intercalar(234, 567))

#Clase jueves
#Escribir una funcion que recibe un numero entero positivo
#pasa a lista y los elementos pares se cambian por un 1
#regresa un numero

def CambiaPares(num): #234567
    if type(num)==int:
        num=abs(num)
        lista=PasalistaFor(num) #[2,3,4,5,6,7]
        print( lista)
        for i in range(len(lista)):
            if lista[i]%2==0:
                lista[i]=1
        print(lista)
        for i in range(len(lista)):
            lista[i]=str(lista[i])
        print(lista)
        cadena=''.join(lista)
        print(cadena)
    else:
        print("Parametro incorrecto")

print(CambiaPares(234567))

#Escribir una funcion que recibe un string(cadena de caracteres)
#contar la cantidad de vocales que existen
#Se reemplaza por vocales mayusculas

def vocales(cadena): #'Ana va para la EscuelA ana va FelIz'
    if type(cadena)==str:
        cadena=cadena.lower()
        print(cadena)
        cont=0
        for i in range(len(cadena)):
            if cadena[i]=="a" or cadena[i]=="e" or cadena[i]=="i" or cadena[i]=="o" or cadena[i]=="u":
                cont=cont+1
        for i in range(len(cadena)):
            if cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u":
                c=''.join(cadena[i])
                c=c.upper()
                print(c)
                cadena=cadena.replace(cadena[i], c)
        print(cadena, "cantidad de vocales: ", cont)
    else:
        print("Parametro incorrecto")

print(vocales("Ana va para la EscuelA ana va FelIz"))

#escribir una funcion que recbe una cadena (validar), buscar una palabra
#se reemplaza por otra palabra una cantidad de veces

def ReemplazarPalabra(cadena, buscar, reemplazar, cantidad):
    if type(cadena)==str and type(buscar)==str and type(reemplazar)==str and type(cantidad)==int:
        cadena=cadena.lower()
        cont=0
        for i in range(len(cadena)):
            if cadena[i].find(buscar) and cont<cantidad:
                cadena=cadena.replace(buscar, reemplazar, cantidad)
                cont=cont+cantidad
        print(cadena)
    else:
        print("Parametros incorrectos")

print(ReemplazarPalabra("Ana va para la Escuela ana va muy Feliz ana ama la EscuEla y la playa bien por ana", "ana", "palangana", 2))

def cuentaletra():
    cantidad=int(input("Cuantos nombres quiere ingresar? : "))
    lista=[]
    for i in range(cantidad):
        nombre=input("Ingrese nombre: ")
        lista=lista+nombre
    print(lista)
    letrainicial=input('Digite la letra inicial a buscar: ')
    cont=0
    for i in lista:
        if i[0]==letrainicial.lower() or i[0]==letrainicial.upper():
            cont=cont+1
    print(cont)
    print("Cantidad de nombres que empiezan por la letra ", letrainicial, "es: ", cont)