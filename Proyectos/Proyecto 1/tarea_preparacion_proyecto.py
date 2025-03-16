#Luis Andres Acunna Perez y Patrick :p

#Cita revision Jueves 19 de marzo en hora consulta de 5 a 7
#Tener inserciones y listas

#----------------------------------------------------------------------------------
#Menu:
""" Se requiere una función aparte de la del menu para que se pueda hacer un ciclo infinito
Se usa for, enumerate, start
por cada índice para cada opcion en la enumeración de las opciones y que empiece en 1
se imprime
"""

paises = []
ciudades = []
restaurantes = []
menus = []
productos = []
clientes = []


def cargar_paises():
    with open("Archivos/Paises.txt", "r") as archivo:
        for linea in archivo:
            cod_pais, nombre = linea.strip().split(";")
            if not any(p[0] == cod_pais for p in paises):  # Validar que no haya duplicados
                paises.append((cod_pais, nombre))

def mostrar_menu(opciones):
    print(f"\n=== Bienvenido al menu de Mantenimiento de Bases de Datos ===")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

#--------------------------------------------------------------------------------------------------
#INSERCIONES_--------------------------------------------------------------------------------------
def insertar_pais(cod_pais, nombre):
    if any(p[0] == cod_pais for p in paises):
        print("❌ Código de país ya existe.")
    else:
        paises.append((cod_pais, nombre))
        print("✅ País agregado correctamente.")

#--------------------------------------------------------------------------------------------------
#BUSQUEDAS_----------------------------------------------------------------------------------------

def buscar_pais(nombre_archivo,buscar):
    """
    input ("Ingrese el nombre del pais")
        abre archivo
        separe elementos y los ponga en una lista
        valide si elemento buscado esta en la lista
        print(valdio)
    else
    """
    try:
        # Abrimos el archivo específico
        with open(nombre_archivo, "r") as archivo:
            # Leemos el archivo línea por línea
            for linea in archivo:
                # Eliminamos espacios en blanco y saltos de línea
                linea = linea.strip()

                # Ignoramos líneas vacías
                if not linea:
                    continue

                # Separamos por punto y coma
                elementos = linea.split(";")

                # Verificamos que tengamos al menos 3 elementos y que el tercer elemento
                # sea igual a la ciudad buscada (sin importar mayúsculas/minúsculas)
                if len(elementos) >= 2 and elementos[1].lower() == buscar.lower():
                    print(f"¡El pais '{buscar}' fue encontrado! Código: {elementos[0]}")

                    return True
            print(f"El pais '{buscar}' no existe en el archivo.")
            return False

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        return False

def buscar_ciudad():
    nombre_archivo = "Archivos/Ciudades.txt"
    buscar = input("Ingrese el nombre de la ciudad a buscar: ")
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                elementos = linea.split(";")
                if len(elementos) >= 3 and elementos[2].lower() == buscar.lower():
                    print(f"¡La ciudad '{buscar}' fue encontrada! Código: {elementos[1]}")

                    return True

                print(f"La ciudad '{buscar}' no existe en el archivo.")
                return False

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        return False

def buscar_rest():
    nombre_archivo = "Archivos/Restaurantes.txt"
    buscar = input("Ingrese el nombre del restaurante a buscar: ")
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                elementos = linea.split(";")
                if len(elementos) >= 4 and elementos[3].lower() == buscar.lower():
                    print(f"¡La ciudad '{buscar}' fue encontrada! Código: {elementos[2]}")
                    return True
            print(f"El restaurante '{buscar}' no existe en el archivo.")
            return False

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        print("Asegúrate de que el archivo exista en la ruta correcta.")
        return False

def buscar_menu():
    nombre_archivo = "Archivos/Menu.txt"
    buscar = input("Ingrese el nombre del Menu a buscar: ")
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                elementos = linea.split(";")
                if len(elementos) >= 5 and elementos[4].lower() == buscar.lower():
                    print(f"¡El Menu '{buscar}' fue encontrado! Código: {elementos[3]}")

                    return True
            print(f"El Menu '{buscar}' no existe en el archivo.")
            return False

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        return False

def buscar_produ():
    nombre_archivo = "Archivos/Productos.txt"
    buscar = input("Ingrese el nombre del producto a buscar: ")
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                elementos = linea.split(";")
                if len(elementos) >= 8 and elementos[5].lower() == buscar.lower():
                    print(f"¡El producto '{buscar}' fue encontrado! Código: {elementos[4]}, Calorías: {elementos[6]} y Precio: {elementos[7]}")
                    return True
            print(f"El producto '{buscar}' no existe en el archivo.")
            return False

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        return False

def buscar_cli():
    # Especificamos la ruta exacta del archivo
    nombre_archivo = "Archivos/Clientes.txt"

    # Pedimos al usuario que ingrese la ciudad a buscar
    buscar = input("Ingrese el nombre del cliente a buscar: ")

    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                elementos = linea.split(";")
                if len(elementos) >= 2 and elementos[1].lower() == buscar.lower():
                    print(f"¡El cliente '{buscar}' fue encontrado! Numero de cliente: {elementos[0]}")
                    return True
            print(f"El cliente '{buscar}' no existe en el archivo.")
            return False

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        print("Asegúrate de que el archivo exista en la ruta correcta.")
        return False

#_________________________________#
#MENU_____________________________#


def MainMenu():
    opciones_principales = ["Leer Archivos", "Inserción", "Buscar", "Salir"]
    subopciones = ["Pais", "Ciudad", "Restaurante", "Menu", "Productos", "Clientes", "Regresar al mantenimiento"] #Para poder ingresar a otro ciclo y muestre un segundo menu

    while True:
        mostrar_menu(opciones_principales)
        print("\n Ingrese que quiere hacer: ")
        x = int(input())
        # verificando que este dentro de las opciones

        if type(x)==int:
            if x == 1:
                cargar_paises()


            #-----------------------------------
            elif x == 2:
                cod_pais = input("Ingrese código de país: ")
                nombre = input("Ingrese nombre del país: ")
                insertar_pais(cod_pais, nombre)

            elif x == 3:
                print("Has seleccionado Buscar.")
                while True:
                    # Mostrar submenú
                    mostrar_menu(subopciones)
                    y = int(input("Selecciona una sub-opción (1-7) para buscar: "))
                    if y == 1:
                        print("\n Has seleccionado buscar Pais.")
                        nombre_archivo = "Archivos/Paises.txt"
                        buscar = input("Ingrese el nombre del pais a buscar: ")
                        buscar_pais(nombre_archivo,buscar)
                    elif y == 2:
                        print("Has seleccionado buscar Ciudad.")
                        buscar_ciudad()
                    elif y == 3:
                        print("Has seleccionado buscar Restaurante.")
                        buscar_rest()
                    elif y == 4:
                        print("Has seleccionado buscar Menu.")
                        buscar_menu()
                    elif y == 5:
                        print("Has seleccionado buscar Productos.")
                        buscar_produ()
                    elif y == 6:
                        print("Has seleccionado buscar Clientes.")
                        buscar_cli()
                    elif y == 7:
                        print("Volviendo al menú principal...")
                        break  # Salir del submenú y volver al menú principal
                    else:
                        print("Opción no válida. Por favor, selecciona una sub-opción del 1 al 7.")
            elif x == 3:
                break #Sale del programa por completo
            else:
                print("\n\n Atención!! \n Ingresa una opción del 1 al 3.")
                continue #Para que el usuario no tenga que reiniciar el programa
MainMenu()
    #----------------------------------------------------------------------------------------------------------------------

#Funciones de verificacion

def abrirArchivo(nombre):
    archivo = open(nombre, "r")
    return archivo
    pass

#para separar cada parte de los txt
#Separa cada linea en una lista diferente, dentro de la lista, separa cada elemento separado con ";"
def Separar():
    obj_arch = open("Archivos/Ciudades.txt", "r")
    matriz_palabras = []
    texto = obj_arch.read()
    lista_lineas = texto.split("\n")
    i=0
    while i < len(lista_lineas):
        matriz_palabras += [lista_lineas[i].split(";")]
        i+=1
    print(matriz_palabras)
    obj_arch.close()
    pass
