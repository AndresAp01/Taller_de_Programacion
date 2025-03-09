#Luis Andres Acunna Perez
#Tarea #3

def funcion1(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else:
            suma=0
            multi=1
            ultimo=lista[0]
            while lista!=[]:
                
                if lista[0]%2==0:
                    multi=multi*(ultimo**3)
                
                else:
                    suma=suma+(ultimo**2)
                
                lista=lista[1:]
            print("la suma de los impares es: ", suma, "la multiplicacion de los pares: ", multi)

#Suma todos los valores impares y ^2
#Multiplica todos los valores impares y ^3
