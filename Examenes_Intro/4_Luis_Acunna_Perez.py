#4to Examen Luis Acunna Perez
#_______________________________________________________________________________________________________________________
#FUNCIONES AUXILIARES
#FACTORIAL COLA
"""
Valida que n es un entero
Si n es 0 i 1 retorna 1
Si n>1 llama a factorialC_aux con n-1 y 1 para iniciar el resultado
"""
def FactorialCola(n):
    if type(n)==int:
        if n==0 or n==1:
            return 1
        else:
            return FactorialC_aux(n, 1)
    else:
        print("parametro incorrecto")
"""
Si n es 0 o 1 returna el resultado
Paso recursivo: 
    Actualiza resultado multiplicandolo por n 
    Reduce n en 1 (n-1)
    La llamada recursiva es lo ultimo que hace (condiciion de finalizacion)
"""
def FactorialC_aux(n, resultado):
    if n==0 or n==1:
        return resultado
    else:
        return FactorialC_aux(n-1, resultado*n)

#FACTORIAL DE PILA
"""
Valida que n es un entero
Si n es 0 o 1 retorna 1
Paso recursivo: 
CALCULA n * factorial_Pila(n-1)
"""
def Factorial_Pila(n):
    if isinstance(n, int):
        if n==0 or n==1:
            return 1
        else:
            return n*Factorial_Pila(n-1)
    else:
        print("parametro incorrecto")

#Largo recursivo de Pila
def Largo_Rec_Pila(n):
    if type(n)==int:
        if n==0:
            return 1
        else:
            return Largo_Rec_Pila_Aux(n)
    else:
        print("parametro incorrecto")

def Largo_Rec_Pila_Aux(n):
    if n==0:
        return 0
    else:
        return 1+Largo_Rec_Pila_Aux(n//10)

#Calcula el centro de un numero usando ciclo while, hasta que se alcance un numero que larg=cont
def centronum(num): #81027
    if isinstance(num, int):
        num=abs(num)
        if Largo_Rec_Pila(num)%2!=0:
            larg=(Largo_Rec_Pila(num)-1)//2
            cont=Largo_Rec_Pila(num)-1
            while num!=0:
                temp=num%10
                if cont==larg:
                    centro=temp
                    break
                num=num//10
                cont=cont-1
            return centro
        else:
            print("Tamaño incorrecto")
    else:
        print("Parametro incorrecto")
#_______________________________________________________________________________________________________________________

#UNO
"""
Explicacion del codigo:
    Funcion principal que cuenta cuantas veces aparece cada elemento en la lista
    Retorna una lista de [antecesor, numero, cantidad, opuesto, sucesor]
"""
def UNO(lista):
    if type(lista)==list:
        print(f"Lista inicial: {lista}")
        return UNO_AUX(lista, [], 0, 0, [], "inicio")

    else:
        print("Parametro incorrecto")
"""
    lista: la lista original o residual
    resultado: acumula los resultados parciales
    conteo: lleva la cuenta de las ocurrencias del primer elemento
    indice: posicion actual en la lista
    nueva_lista: acumula los elementos que no son iguales al primer elemento durante la fase de "filtrar"
    bandera: controla el flujo ("inicio", "contar", "filtrar")
"""
def UNO_AUX(lista, resultado, conteo, indice, nueva_lista, bandera):
    if bandera=="inicio":
        if lista==[]:
            return resultado
        else:
            return UNO_AUX(lista, resultado, 0, 0, [], "contar")
    elif bandera=="contar": #Cuenta cuantas veces aparece el elemento
        if indice==len(lista):
            return UNO_AUX(lista, resultado, conteo, 0, [], "filtrar")
        elif lista[indice]==lista[0]:
            return UNO_AUX(lista, resultado, conteo+1, indice+1, [], "contar")
        else:
            return UNO_AUX(lista, resultado, conteo, indice+1, [], "contar")
    elif bandera=="filtrar": #Crea la sublista de los elementos ya contados ademas de crear una nueva lista para empoezar a contar los elementos restantes
        if indice==len(lista):
            return UNO_AUX(nueva_lista, resultado+[[1, 0, 1, [lista[0]-1, lista[0], conteo, lista[0]*(-1), lista[0]+1], 0, 1, 0]], 0, 0, [], "inicio")
        elif lista[indice]!=lista[0]:
            return UNO_AUX(lista, resultado, conteo, indice+1, nueva_lista+[lista[indice]], "filtrar")
        else:
            return UNO_AUX(lista, resultado, conteo, indice+1, nueva_lista, "filtrar")
    else:
        return "Parametro incorrecto"
#_______________________________________________________________________________________________________________________
#DOS UNO
"""
Entra un numero se valida que es entero y mayor a 0
llama a la auxiliar calcula nominador y denominador de manera separada
y devuelve el resultado total
"""
def DOS1(n):
    if type(n)!=int:
        print("Parametro incorrecto, debe ser un numero entero.")
    elif n<=0:#n<=0 no
        print("Error. El n debe ser mayor a 0")
    else:
        return DOS1_AUX(n, ((n-2)**n)**3*(n-1)**4, 2*(n*4), 1, 0)

#Llama a FactorialCola() para calcular el factorial de el indice

def DOS1_AUX(n, numerador, denominador, i, suma):
    if i>n:
        return suma
    return DOS1_AUX(n, numerador, denominador, i+1,
                    suma+(FactorialCola(i)*numerador
                    /
                    (((denominador)**i)**2+n)))

#FUNCION DOS DOS
"""
Entra un numero se valida que es entero y mayor a 0
llama a la auxiliar y devuelve el resultado total ^2
"""
def DOS2(n): #2
    if type(n)!=int:
        print("Parametro incorrecto, debe ser un numero entero.")
    elif n<=0: #2>0
        print("Error. El n debe ser mayor a 0")
    else:
        return DOS2_AUX(n, 1)**2

"""
Entra n, i
Condicion de finalizacion cuando i sea mayor a cero
Calcula la suma y le suma la anterior (pila)
retorna cuando i sea mayor
"""
def DOS2_AUX(n, i):
    if i>n:
        return 0
    else:
        return (
                ((((i**2)*(n+1)*n*(n-1))**n)/
                (((2*((n*3)**(i+1)))**2)+n))
                +DOS2_AUX(n, i+1)
                )
#_______________________________________________________________________________________________________________________
"""
    Función principal que procesa lista de longitud impar
    Genera [[primer elemento + x - y], [segundo elemento + x - y], ...]
    donde x = elemento siguiente saltándose uno
    y = elemento siguiente a x saltándose uno
"""
def TRES(lista):
    if type(lista)!=list:
        return "Parametro incorrecto, debe ser una lista"
    elif len(lista)%2!=1:
        return "Parametro incorrecto, debe ser longitud impar"
    elif len(lista)<3:
        return "Parametro incorrecto, debe tener mas de 3 elementos"
    return TRES_AUX(lista, 0)

def TRES_AUX(lista, indice):
    if indice>=len(lista):
        return []
    else:
        return [[
            (-1)**indice*(indice+1), 0, (-1)**indice*(indice+1), #Patron
            ((lista[indice]+ #Digito
            lista[(indice+2)%len(lista)]- #Se salta 2
            lista[(indice+4)%len(lista)])* #Se salta 4
            (lista[indice]-1)+(lista[indice]*-1))**(indice+1), #Calcula antecesor,
            (-1)**(indice+1)*(indice+1), 0, (-1)**(indice+1)*(indice+1) #Patron
        ]]+TRES_AUX(lista, indice+1)

#_______________________________________________________________________________________________________________________
#Funcion CUATRO
"""
Verifica si los numeros son enteros, los pasa por abs y calcula el largo con Largo_Rec_Pila
Si los largos son iguales, trabaja
#Si el largo es impar, trabaja
Llama a la funcion auxiliar para crear la lista de listas
Procesa pares de digitos simetricos desde los extremos hacia el centro, hasta llegar al centro, genera sublistas
con valores segun las reglas de la potencia que va alternando
"""
def CUATRO(num1, num2, num3):
    print(f"numeros originales: {num1, num2, num3}")
    print("Lista generada: \n")
    if not (type(num1)==int and type(num2)==int and type(num3)==int):
        print("Parametros incorrectos, deben ser numeros enteros")
    else:
        num1=abs(num1)
        num2=abs(num2)
        num3=abs(num3)
        if Largo_Rec_Pila(num1)!=Largo_Rec_Pila(num2) or Largo_Rec_Pila(num1)!=Largo_Rec_Pila(num3):
            print("Los numeros deben tener el mismo largo")
        elif Largo_Rec_Pila(num1)%2==0:
            print("Los numeros deben tener largo impar")
        else:
            return CUATRO_AUX(num1, num2, num3, 0, 0, True)

def CUATRO_AUX(num1, num2, num3, par, desplazamiento, bandera):
    if par>=Largo_Rec_Pila(num1)//2:
        return [] #Condicion de finalizacion, devuelve la lista vacia para comenzar a construir el resultado final
    if bandera: #true si
        potencias=[2, 3]
    else: #false
        potencias=[3, 2]

    return [
        [1, 0, 1, #Patron
         ((num3//(10**(Largo_Rec_Pila(num3)-1-desplazamiento)))%10+centronum(num3))**potencias[0],
            #num3//(10**Elemento+centro)**potencias[0] dependiendo de la pasada
         -1, 0, -1], #Patron
        [1, 0, 1,
         ((num3//(10**desplazamiento))%10+centronum(num3))**potencias[0],
         -1, 0, -1],
        [-2, 0, -2,
         ((num2//(10**desplazamiento))%10-centronum(num2))**potencias[1],
         2, 0, 2],
        [-2, 0, -2,
         ((num2//(10**(Largo_Rec_Pila(num2)-1-desplazamiento)))%10-centronum(num2))**potencias[1],
         2, 0, 2],
        [3, 0, 3,
         ((num1//(10**(Largo_Rec_Pila(num1)-1-desplazamiento)))%10*centronum(num1))**potencias[0],
         -3, 0, -3],
        [3, 0, 3,
         ((num1//(10**desplazamiento))%10*centronum(num1))**potencias[0],
         -3, 0, -3],
    ]+CUATRO_AUX(num1, num2, num3, par+1, desplazamiento+1, not bandera)
    #Actualiza el par de sublistas, el desplazamiento y el bool de la bandera
