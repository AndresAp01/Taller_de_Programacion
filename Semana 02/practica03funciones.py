#Funciones
"""def Nombre():
        acciones"""

#ejemplo sin parametros:
def saludo():
    print("Hola a todos")

def EjemploCondicionales(x):
#probar con 24, 25, 26, 27, 27.5     
    if (x%4)==0:
        print(x*x)
    elif (x%4)==1:
        print(x/6)
    elif (x%4)==2:
        print(((x**2)*(x**3))**2)
    elif (x%4)==3:
        print(x**3+5)
    else:
        print("No hay nada que hacer")




"""Si el numero es par mult por 3, si es impar suma 2
"""

def parimpar(x):
    if (x%2)==0:
        print(x*3)
    else:
        print(x+2)

#Escribir una funcion que recibe 3 parametros (x, y, z)
        #Si x es mayoe que z = (x^2 + y^5 + z^4)^6
        #Si x es menor que y (x + y + z)*(z**3)
        #Si no, (z**3 * x**2) + y

x=10
y=2
z=1
def funcxyz(x,y,z):
    if(x>z):
        print(((x**2)+(y**5)+(z**4))**6)
    elif(x<y):
        print((x+y+z)*(z**3))
    else:
        print(((z**3)*(x**2))+y)

print(((1**3)*(1**2))+1)




