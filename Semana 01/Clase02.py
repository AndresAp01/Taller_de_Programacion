#Comentario de una linea
""" Bloque
de
comentario"""
#print palabra reservada
#Python es un lenguaje interpretado, no compilado
#C++ es un lenguaje compilado

#definicion de un variable en la memoria con valor de 2
x=2
#x=x+4 Modificanbdo la memoria

print(x+2)
print(x)

#+
#-
#*
#/ decimales #// entera
#% residuo

#Potencia: **
x=3
#primera forma
x=x**2
print(x)

#segunda forma
x**=3
print(x)

#funcion pow(parametros1, parametro2)
#parametro 1 base y parametro2 es el exponmente
#parametros valores que la funcion espera para trabahjar

print(pow(2,3))

#practica

x=2
y=3
z=5

print(((x+y)**4)*((y+z)**5))
print((pow(x+y,4)) * (pow(y+z,5)))

#Segunda forma profe
uno=(x+y)
dos=uno**4
tres=y+z
cuatro=tres**5
cinco=dos*cuatro
print(cinco)

#Caracteristicas de python
"""1. Sensible a las mayusculas

2. Lenguaje interpretado

3. Identado

4. Tres tipos de errores
    1. Errores de sintaxis (syntax) Algo que esta mal escrito
    Ejemplo: print("Hola!"
    
    4.2 Error de link, al utilizar libreria no se indica de donde viene la funcion
    Ejemplo: print(sqrt(4))
    tendria que tener: import.math
    
    4.3 Error de logica.
    Ejemplo= 2+2=5 :(

    """

#practica
#definir las siguientes variables
#(x**3) + ('y'**2)*('y'**5) dividido por z-x
x=1
y=2
z=3

primer=(x**3)
segundo=y**2
tercer=y**5
cuarto=z-x

print((((x**3)+(y**2))*(y**5))/(z-x)) 

#Mismos valores de variables
#(x elev a la 3, mas, y elev a la 2) * ((z+z)*(y*5)) todo divid entre z-y

print(((x**3 + y**2)*((z+z)*(y*5)))/(z-y))
