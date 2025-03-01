#Luis Andres Acunna Perez

def multiplicadorimpares(num):
    #Prueba 1: 33
    #Prueba 2: 59874563214587
    #Prueba 3: 12345678
    #Prueba 4: 123
    contador = 1

    if num == 0:
        print(0)
    else:
        while num!=0:
            ultimo = num % 10 #para obtener el ultimo digito

            if ultimo % 2 !=0: #si es impar
                contador = contador * (ultimo ** 3) #Eleva a la 3 y mult. por el almacenado

            num  = num // 10 #Divide entre 10 para pasar al siguiente digito

    print("El resultado de los digitos impares elevados a la 3 es: ",contador)
    #Resultado 1: 729
    #Resultado 2: 4522822787109375
    #Resultado 3: 1157625
    #Resultado 4: 27


