#-----Ejercicio 1-----

"""
Crea una función llamada calcular_imc() que reciba como parámetros el peso en 
kg y la altura en metros de una persona. La función debe calcular el Índice 
de Masa Corporal (IMC) con la fórmula:𝐼𝑀𝐶=peso/altura2
"""

def calcular_imc(kg, m):
    imc = 0
    imc = kg/(m**2)
    return imc

print(calcular_imc)


#-----Ejercicio 2------

""" Crea una función llamada convertir_temperatura() que reciba un número (temperatura) 
y una cadena ("C" o "F") indicando si la conversión es de Celsius a Fahrenheit o viceversa.
Si la entrada es en Celsius, usa la fórmula:𝐹=𝐶×9/5+32 la entrada es en Fahrenheit, usa 
la fórmula:𝐶=(𝐹−32)×5/9

"""

def convertir_temperatura(temp, escala):
    temperatura = 0
    if escala == "C":
        temperatura = (temp*(9/5))+32
    elif escala == "F":
        temperatura = (temp-32)*(5/9)
    else:
        return "ERROR. Datos ingresados son incorrectos."

    return temperatura

print(convertir_temperatura(0, "C"))
#-----ejercicio 3-----
"""
Crea una función es_bisiesto(anio) que reciba un año como parámetro y determine si es
 bisiesto. Un año es bisiesto si:Es divisible por 4 y no es divisible por 100 y es 
 divisible por 400.

"""

def es_bisiesto(y):
    if (y%4 == 0) and (y%100 != 0) and (y%400 == 0):
        return "El año es bisiesto."
    else:
        return "El año no es bisiesto."
    
print(es_bisiesto(2024))

#-----Ejercicio 4----
"""
Crea una función llamada par_o_impar() que reciba un número entero. 
La función debe determinar si el número es par o impar y luego verificar 
si es mayor o menor a 50.

"""

def par_o_impar(num):
    if num % 2 == 0:
        if num < 50:
            return "El numero es par y menor a 50"
        elif num == 50:
            return "El numero es par e igual a 50"
        else:
            return "El numero es par y menor a 50"
    else:
        if num < 50:
            return "El numero es par y menor a 50"
        elif num == 50:
            return "El numero es par e igual a 50"
        else:
            return "El numero es par y menor a 50"
        
print(par_o_impar(200))
   
