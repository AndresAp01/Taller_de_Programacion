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
    opciones_principales = ["Insercion", "Buscar", "Salir"]
    subopciones = ["Pais", "Ciudad", "Restaurante", "Menu", "Productos", "Clientes", "Regresar al mantenimiento"] #Para poder ingresar a otro ciclo y muestre un segundo menu

    while True:
        mostrar_menu(opciones_principales)
        print("\n Ingrese que quiere hacer: ")
        x = int(input())
        # verificando que este dentro de las opciones

        if type(x)==int:
            if x == 1:
                pass
            elif x == 2:
                print("Has seleccionado Buscar.")
                while True:
                    # Mostrar submenú
                    mostrar_menu(subopciones)
                    y = int(input("Selecciona una subopción (1-7) para buscar: "))

                    if y == 1:
                        print("\n Has seleccionado buscar Pais.")
                        print("\n El Pais buscado existe .... bla bla bla")
                    elif y == 2:
                        print("Has seleccionado buscar Ciudad.")
                    elif y == 3:
                        print("Has seleccionado buscar Restaurante.")
                    elif y == 4:
                        print("Has seleccionado buscar Menu.")
                    elif y == 5:
                        print("Has seleccionado buscar Productos.")
                    elif y == 6:
                        print("Has seleccionado buscar Clientes.")
                    elif y == 7:
                        print("Volviendo al menú principal...")
                        break  # Salir del submenú y volver al menú principal
                    else:
                        print("Opción no válida. Por favor, selecciona una subopción del 1 al 7.")
            elif x == 3:
                break #Sale del programa por completo
            else:
                print("\n\n Atencion!! \n Ingresa una opcion del 1 al 3.")
                continue #Para que el usuario no tenga que reiniciar el programa

MainMenu()

#----------------------------------------------------------------------------------------------------------------------
