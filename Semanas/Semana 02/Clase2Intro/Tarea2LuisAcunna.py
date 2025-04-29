#Tarea #2 Luis Andrés Acuña Pérez

def Contadorespares1(x): #se le asigna una función con un nombre que denota lo que hace con un parámetro "x"
    #La variable que contará los numeros pares empieza en el numero 0
    contador=0
    #Revisa que cada numero del parámetro sea >= 0 
    while x>=0: 
        if x%2==0:
            #Entra al ciclo, verifica si el residuo de el numero a contar es igual a 0
            #Se suma si es igual a 0:
            contador=contador+1 
        x=x-1 #Se le resta en uno en cada iteración, se va acercando al cero.

    print("La cantidad de números pares que hay del 0 al 10 son: ",contador) #Se imprime el mensaje que indica la cantidad de números



#Primera prueba x=10, respuesta: {6}

    
#Ejercicio 2

def cuentaPares(num):
    #Se verifica si el parámetro es igual a 0
    if num==0:
        #Si el parámetro es igual a 0 solo se imprime 1. Porque python cuenta el 0 como par.
        print(1)
    #Si el parám. no es igual a 0, entra al ciclo else
    else:
        #El contador empieza en 0
        cont=0
        #La variable empieza en 0 que se usa en el while
        i=0

        #Se ejecuta el while mientras i sea<=0
        while i<=num:
            #Dentro del ciclo while, se verifica que el residuo sea 0 para que sea par y lo cuente
            if i%2==0:
                #Si i es par, se suma el contador cont en 1.
                cont=cont+1
            #Se incrementa en 1 por cada vez que lo pasa
            i=i+1 #lleva: 2, 3, 4, 5, 6, etc...
        print(cont) #imprime {6}

#Mismos resultados

                
