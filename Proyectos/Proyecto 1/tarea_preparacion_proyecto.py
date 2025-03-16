#Luis Andres Acunna Perez y Patrick :p

#Cita revision Jueves 19 de marzo en hora consulta de 5 a 7
#Tener inserciones y listas

#----------------------------------------------------------------------------------
#Menu:
""" Se requiere una funcion a parte de la del menu para que se pueda hacer un ciclo infinito
Se usa for, enumerate, start
por cada indice para cada opcion en la enumeracion de las opciones y que empiece en 1
se imprime
"""
def mostrar_menu(opciones):
    print("\n=== Bienvenido al mantenimiento de la base de datos ===")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

def MainMenu():
    opciones = ["Insercion", "Buscar", "Salir"]
    subopciones = [] #Para poder ingresar a otro ciclo y muestre un segundo menu

    while True:
        mostrar_menu(subopciones)


        x = int(input())
        if x == 1:
            pass
        elif x == 2:
            while True:
                print("1 para verificar Pais")
                print("2 para buscar Ciudad")
                print("3 para buscar restaurante")
                print("4 para buscar menu")
                print("5 para buscar productos")
                print("6 para buscar cliente")
                break
            continue
        elif x == 3:
            break
MainMenu()
