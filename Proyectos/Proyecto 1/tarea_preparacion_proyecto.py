#Luis Andres Acunna Perez y Patrick :p

#Cita revision Jueves 19 de marzo en hora consulta de 5 a 7
#Tener inserciones y listas

#----------------------------------------------------------------------------------

#############################
def datos_a_listas(ruta_archivo, separador=";", separador_lineas="\n"):
    try:
        with open(ruta_archivo, "r") as archivo:
            texto = archivo.read()
            lista_lineas = texto.split("\n")
            matriz_datos = []
            for linea in lista_lineas:
                matriz_datos.append(linea.split(separador))

            return matriz_datos
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe")
        return []

paises = []
paises = datos_a_listas("Archivos/Paises.txt", ";")
ciudades = []
ciudades = datos_a_listas("Archivos/Ciudades.txt", ";")
restaurantes = []
restaurantes = datos_a_listas("Archivos/Restaurantes.txt", ";")
menus = []
menus = datos_a_listas("Archivos/Menu.txt", ";")
productos = []
productos = datos_a_listas("Archivos/Productos.txt", ";")
cliente = []
cliente = datos_a_listas("Archivos/Clientes.txt", ";")
def mostrar_menu(opciones):
    print(f"\n=== Bienvenido al menu de Mantenimiento de Bases de Datos ===")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")
#--------------------------------------------------------------------------------------------------
#BUSQUEDAS_----------------------------------------------------------------------------------------
def buscar_pais(paises, nombre):
    """Busca un país por nombre"""
    resultados = [pais for pais in paises if nombre.lower() in pais[1].lower()]
    if resultados:
        print("\nResultados de la búsqueda:")
        for pais in resultados:
            print(f"Código: {pais[0]}, Nombre: {pais[1]}")
    else:
        print(f"No se encontraron países con el nombre '{nombre}'.")
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
#INSERCIONES
def insertar_en_lista(lista, nuevo_registro, indice_unico=None):
    # Validar que el primer parámetro sea una lista
    if not isinstance(lista, list):
        print("Error: El primer parámetro debe ser una lista")
        return False
    # Validar que el nuevo registro sea una lista
    if not isinstance(nuevo_registro, list):
        print("Error: El nuevo registro debe ser una lista")
        return False
    # Validar campo único
    if indice_unico is not None:
        if any(item[indice_unico] == nuevo_registro[indice_unico] for item in lista):
            print(
                f"Error: Ya existe un registro con el valor '{nuevo_registro[indice_unico]}' en la posición {indice_unico}")
            return False
    # Insertar el registro
    lista.append(nuevo_registro)
    print(f"Registro insertado correctamente: {nuevo_registro}")
    return True
# Funciones específicas para cada tipo de lista
def insertar_pais(paises, codigo, nombre):
    """Inserta un país en la lista de países"""

    return insertar_en_lista(paises,[codigo, nombre],indice_unico=0)
#------------------------------------------------------------------------------------------
def insertar_ciudad(paises, ciudades, cod_pais, cod_ciudad, nombre):
    """Inserta una ciudad en la lista de ciudades"""
    if not any(pais[0] == cod_pais for pais in paises):
        print(f"Error: No existe un país con código '{cod_pais}'")
        return False
    return insertar_en_lista(ciudades,[cod_pais, cod_ciudad, nombre], indice_unico=1)
#------------------------------------------------------------------------------------------
def insertar_restaurante(paises, ciudades, restaurantes, cod_pais, cod_ciudad, cod_rest, nombre):
    """Inserta un restaurante en la lista de barrios"""
    if not any(pais[0] == cod_pais for pais in paises):
        print(f"Error: No existe un país con código '{cod_pais}'")
        return False
    # Verificar que exista la ciudad
    if not any(ciudad[0] == cod_pais and ciudad[1] == cod_ciudad for ciudad in ciudades):
        print(f"Error: No existe una ciudad con código '{cod_ciudad}' en el país '{cod_pais}'")
        return False
    return insertar_en_lista(restaurantes, [cod_pais, cod_ciudad, cod_rest, nombre], indice_unico=2)
#------------------------------------------------------------------------------------------
def insertar_menu(paises, ciudades, restaurantes, menus, cod_pais, cod_ciudad, cod_rest, cod_menu, nombre):
    """Inserta un menu en la lista de restaurantes"""
    def validar_menu(menu):
        # Verificar que exista la ciudad
        if not any(rest[0] == cod_pais and rest[1] == cod_ciudad and rest[2] == cod_rest for rest in restaurantes):
            print(f"Error: No existe un restaurante con código '{cod_rest}' en la ciudad '{cod_ciudad}' y el pais '{cod_pais}'")
            return False
        return True
    return insertar_en_lista(menus, [cod_rest, cod_menu, nombre], indice_unico=3)
#------------------------------------------------------------------------------------------
def insertar_productos(paises, ciudades, restaurantes, menus, productos, cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto, nombre, kcal, precio):
    """Inserta un producto en la lista de productos"""
    # Validar que el menú exista
    if not any(menu[0] == cod_pais and menu[1] == cod_ciudad and menu[2] == cod_rest and menu[3] == cod_menu for menu in menus):
        print(f"Error: No existe un menú con código '{cod_menu}' en el restaurante '{cod_rest}', ciudad '{cod_ciudad}' y país '{cod_pais}'")
        return False
    # Insertar el producto
    return insertar_en_lista(productos, [cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto, nombre, kcal, precio], indice_unico=4)
#MENU_____________________________#
def MainMenu():
    opciones_principales = ["Inserción", "Buscar", "Salir"]
    subopciones = ["Pais", "Ciudad", "Restaurante", "Menu", "Productos", "Clientes", "Regresar al mantenimiento"] #Para poder ingresar a otro ciclo y muestre un segundo menu
    while True:
        mostrar_menu(opciones_principales)
        print("\n Ingrese que quiere hacer: ")
        x = int(input())
        # verificando que este dentro de las opciones
        if x == 1:
            print("Has seleccionado la opcion Insertar.")
            while True:
                mostrar_menu(subopciones)
                y = int(input("Selecciona una sub-opción (1-7) para insertar: "))
                if y == 1: #Insercion de Pais
                    print("\n Has seleccionado insertar Pais.")
                    codigo = int(input("Ingrese el codigo del pais: "))
                    nombre = input("Ingrese el nombre del pais: ")
                    insertar_pais(paises, codigo, nombre)
                    print(paises)
                elif y == 2:
                    print("\n Has seleccionado insertar Ciudad.")
                    cod_pais = int(input("Ingrese el codigo del pais: "))
                    cod_ciudad = int(input("Ingrese el codigo de la ciudad: "))
                    nombre = input("Ingrese el nombre del ciudad: ")
                    insertar_ciudad(paises, ciudades, cod_pais, cod_ciudad, nombre)
                    print(ciudades)
                elif y == 3:
                    print("Has seleccionado insertar Restaurante.")
                    cod_pais = int(input("Ingrese el codigo del pais: "))
                    cod_ciudad = int(input("Ingrese el codigo de la ciudad: "))
                    cod_rest = int(input("Ingrese el codigo del restaurante: "))
                    nombre = input("Ingrese el nombre del restaurante: ")
                    insertar_restaurante(paises, ciudades, restaurantes, cod_pais, cod_ciudad, cod_rest, nombre)
                    print(restaurantes)
                elif y == 4:
                    print("Has seleccionado insertar Menu.")
                    cod_rest = int(input("Ingrese el codigo del restaurante: "))
                    cod_menu = int(input("Ingrese el codigo del menu: "))
                    nombre = input("Ingrese el nombre del menu: ")
                    insertar_menu(paises, ciudades, restaurantes, menus, cod_rest, cod_menu, nombre)
                elif y == 5:
                    print("Has seleccionado insertar Productos.")
                    cod_menu = int(input("Ingrese el codigo del menu: "))
                    cod_producto = int(input("Ingrese el codigo del producto: "))
                    nombre = input("Ingrese el nombre del producto: ")
                    insertar_en_lista(paises, ciudades, restaurantes, menus, productos, [cod_menu, cod_producto, nombre])
                elif y == 6:
                    print("Has seleccionado insertar Clientes.")

                elif y == 7:
                    print("Volviendo al menú principal...")
                    break  # Salir del submenú y volver al menú principal
                else:
                    print("Opción no válida. Por favor, selecciona una sub-opción del 1 al 7.")
        elif x == 2:
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
