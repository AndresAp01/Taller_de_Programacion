#Luis Andres Acuña Perez
#Tarea 7
#1

def esPrimo(n):
    if isinstance(n, int):
        i=1
        divisores=0
        while i<=n:
            if n%i==0:
                divisores+=1
            i+=1
        return divisores==2
    else:
        print("El parámetro ingresado no es un número entero.")

def UNO(n):
    listaPrimos=""
    n=abs(n)
    if isinstance(n, int):
        for i in range(2, n+1):
            if esPrimo(i):
                listaPrimos=listaPrimos+"-"+str(i)
        if listaPrimos!= "":
            print(listaPrimos[1:])
        else:
            print("No hay primos en el rango")
    else:
        print("El parámetro ingresado no es valido")

#2
def DOS(dato):
    if isinstance(dato, str) and dato.isdigit():
        total=0
        for caracter in dato:
            if caracter in "2357":
                total+=1
        print("En la cadena hay:", total, "digitos primos.")
    else:
        print("Parametro incorrecto, ingrese cadena de numeros")

#3
def TRES(cadena):
    if isinstance(cadena, str) and cadena.isdigit():
        primos="2357"
        for digito in primos:
            if digito in cadena:
                cadena=cadena.replace(digito, "p")
        print(cadena)
    else:
        print("Parámetro incorrecto")
