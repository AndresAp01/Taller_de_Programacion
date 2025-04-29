#ciclos
#cilo while: Un ciclo repite un proceso hasta que la ocndicion sea falsa
## el numero 0 para python es par

"""
Syntax:

while <condicion> (sea verdadera)
    |acciones
    |acciones

Escribir una funcion que va a contar que cuente los pares desde el 0 hasta el 10, sin recibir parámetros."""

#Ejemplo profe:
def cuentapares():
    contador=0
    num=0
    while num<11:
        if num%2==0:
            contador=contador+1
        num=num+1
    print(contador)

#Ejemplo mio xd

