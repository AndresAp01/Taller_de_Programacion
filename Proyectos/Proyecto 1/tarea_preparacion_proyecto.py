#Luis Andres Acunna Perez y Patrick :p
#Cita revision Jueves 19 de marzo en hora consulta de 5 a 7
#Tener inserciones y listas
#############################
def datos_a_listas(ruta_archivo, separador=";", separador_lineas="\n", posiciones_cod=[0]):
    #Como funciona
    #   ruta_archivo: Es la ruta del archivo a leer
    #   Separador: El caracter que separa las lineas
    #Separador_lineas: Caracter que separa las lineas
    #Convertir codigo: Si es True convierte los codigos a enteros
    #posiciones: Lista de posiciones de los codigos a convertir
    try:
        with open(ruta_archivo, "r") as archivo:
            texto = archivo.read()
            lista_lineas = texto.split(separador_lineas)
            matriz_datos = []

            for linea in lista_lineas:
                if not linea.strip():  # Ignorar líneas vacías
                    continue

                campos = linea.split(separador)

                # Convertir los códigos a enteros si es posible
                for pos in posiciones_cod:
                    if len(campos) > pos:
                        try:
                            campos[pos] = int(campos[pos])
                        except (ValueError, TypeError):
                            # Si no se puede convertir, dejarlo como está
                            pass

                matriz_datos.append(campos)

            return matriz_datos
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe")
        return []
'''
            for linea in lista_lineas:
                matriz_datos.append(linea.split(separador))

            return matriz_datos
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe")
        return [] '''
#Para pasar los datos de los archivos a listas
paises = []
paises = datos_a_listas("Archivos/Paises.txt", ";", posiciones_cod=[0])
ciudades = []
ciudades = datos_a_listas("Archivos/Ciudades.txt", ";", posiciones_cod=[0, 1])
restaurantes = []
restaurantes = datos_a_listas("Archivos/Restaurantes.txt", ";", posiciones_cod=[0, 1, 2])
menus = []
menus = datos_a_listas("Archivos/Menu.txt", ";", posiciones_cod=[0, 1, 2, 3])
productos = []
productos = datos_a_listas("Archivos/Productos.txt", ";", posiciones_cod=[0, 1, 2, 3, 4])
cliente = []
cliente = datos_a_listas("Archivos/Clientes.txt", ";", posiciones_cod=[0, 1, 2, 3, 4, 5])
def mostrar_menu(opciones):
    print(f"\n=== Bienvenido al menu de Mantenimiento de Bases de Datos ===")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

#VALIDACION----------------------------------------------------------------------------------------
#FUNCIONA

def validar_pais_existe(paises, cod_pais):
    #Si existe un pais con el codigo cod_pais en la lista paises
    #Primer elemento pais[0] de cada pais en la lista coincide con el codigo
    #Primero lo convertimos a entero
    cod_pais = abs(int(cod_pais))
    if not any(pais[0] == cod_pais for pais in paises):
        print(f"Error: No existe un país con código '{cod_pais}'")
        return False
    return True
def validar_ciudad_existe(ciudades, cod_pais, cod_ciudad):
    """Valida que exista una ciudad con el código especificado en el país indicado"""
    cod_pais = abs(int(cod_pais))
    cod_ciudad = abs(int(cod_ciudad))
    if not any(ciudad[0] == cod_pais and ciudad[1] == cod_ciudad for ciudad in ciudades):
        print(f"Error: No existe una ciudad con código '{cod_ciudad}' en el país '{cod_pais}'")
        return False
    return True
def validar_restaurante_existe(restaurantes, cod_pais, cod_ciudad, cod_rest):
    cod_pais = abs(int(cod_pais))
    cod_ciudad = abs(int(cod_ciudad))
    cod_rest = abs(int(cod_rest))
    if not any(restaurante[0] == cod_pais and restaurante[1] == cod_ciudad and restaurante[2] == cod_rest for restaurante in restaurantes):
        print(f"Error: No existe un restaurante con código '{cod_rest}' en la ciudad '{cod_ciudad}' del país '{cod_pais}'")
        return False
    return True
def validar_menu_existe(menus, cod_pais, cod_ciudad, cod_rest, cod_menu):
    """Valida que exista un menu con el codigo especificado en el restaurante en la ciudad y pais indicados"""
    cod_pais = abs(int(cod_pais))
    cod_ciudad = abs(int(cod_ciudad))
    cod_rest = abs(int(cod_rest))
    cod_menu = abs(int(cod_menu))

    if not any(menu[0] == cod_pais and menu[1] == cod_ciudad and
               menu[2] == cod_rest and menu[3] == cod_menu for menu in menus):
        print(f"Error: No existe un menú con código '{cod_menu}' en el restaurante '{cod_rest}' "
              f"de la ciudad '{cod_ciudad}' del país '{cod_pais}'")
        return False
    return True
def validar_producto_existe(productos, cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto):
    """Valida que exista un producto con el código especificado en el menú, restaurante, ciudad y país indicados"""
    cod_pais = abs(int(cod_pais))
    cod_ciudad = abs(int(cod_ciudad))
    cod_rest = abs(int(cod_rest))
    cod_menu = abs(int(cod_menu))
    cod_producto = abs(int(cod_producto))

    if not any(producto[0] == cod_pais and producto[1] == cod_ciudad and
              producto[2] == cod_rest and producto[3] == cod_menu and
              producto[4] == cod_producto for producto in productos):
        print(f"Error: No existe un producto con código '{cod_producto}' en el menú '{cod_menu}' "
              f"del restaurante '{cod_rest}' de la ciudad '{cod_ciudad}' del país '{cod_pais}'")
        return False
    return True
#--------------------------------------------------------------------------------------------------
#BUSQUEDAS_----------------------------------------------------------------------------------------
#FUNCIONA
def buscar_pais(paises, nombre):
    resultados = [pais for pais in paises if nombre.lower() in pais[1].lower()]
    if resultados:
        print("\n Resultados de la búsqueda:")
        for pais in resultados:
            print(f"Código: {pais[0]}, Nombre: {pais[1]}")
    else:
        print(f"No se encontraron países con el nombre '{nombre}'.")
'''
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
        
'''
def buscar_ciudad(ciudades): #FUNCIONA
    """Busca una ciudad en la lista de ciudades"""
    if not ciudades:
        print("No hay ciudades registradas para buscar.")
        return False
    buscar = input("Ingrese el nombre de la ciudad a buscar: ")
    encontrado = False
    for ciudad in ciudades:
        if len(ciudad) >= 3 and buscar.lower() in ciudad[2].lower():
            print(f"¡La ciudad '{ciudad[2]}' fue encontrada!")
            print(f"País: {ciudad[0]}, Código: {ciudad[1]}")
            encontrado = True

    if not encontrado:
        print(f"La ciudad '{buscar}' no existe en los registros.")
        return False

    return True
def buscar_rest(restaurantes, nombre): #FUNCIONA
    """Busca un restaurante por nombre"""
    resultados = [rest for rest in restaurantes if nombre.lower() in rest[3].lower()]
    if resultados:
        print("\nResultados de la búsqueda:")
        for rest in resultados:
            print(f"País: {rest[0]}, Ciudad: {rest[1]}, Código: {rest[2]}, Nombre: {rest[3]}")
    else:
        print(f"No se encontraron restaurantes con el nombre '{nombre}'.")
def buscar_menu(menus, nombre): #FUNCIONA
    """Busca un menú por nombre"""
    resultados = [menu for menu in menus if nombre.lower() in menu[4].lower()]
    if resultados:
        print("\nResultados de la búsqueda:")
        for menu in resultados:
            print(f"País: {menu[0]}, Ciudad: {menu[1]}, Restaurante: {menu[2]}, Código: {menu[3]}, Nombre: {menu[4]}")
    else:
        print(f"No se encontraron menús con el nombre '{nombre}'.")
def buscar_produ(productos, nombre): #FUNCIONA
    """Busca un producto por nombre"""
    resultados = [prod for prod in productos if nombre.lower() in prod[5].lower()]
    if resultados:
        print("\nResultados de la búsqueda:")
        for prod in resultados:
            print(f"País: {prod[0]}, Ciudad: {prod[1]}, Restaurante: {prod[2]}, Menú: {prod[3]}, " +
                  f"Código: {prod[4]}, Nombre: {prod[5]}, Calorias : kcal {prod[6]}, Precio: ${prod[7]}")
    else:
        print(f"No se encontraron productos con el nombre '{nombre}'.")
'''
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
'''
#______________________________________________________________#
#Funcion para insertar nuevos elementos en lista_______________#
#FUNCIONA
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
''' def insertar_pais(paises, codigo, nombre):
    """Inserta un país en la lista de países"""

    return insertar_en_lista(paises,[codigo, nombre],indice_unico=0)
#------------------------------------------------------------------------------------------
def insertar_ciudad(paises, ciudades, cod_pais, cod_ciudad, nombre):
    """Inserta una ciudad en la lista de ciudades"""
    if not any(pais[0] == cod_pais for pais in paises): #Para Verificar la existencia del codigo de pais
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
    if not any(pais[0] == cod_pais for pais in paises):
        print(f"Error: No existe un país con código '{cod_pais}'")
        return False
    if not any(ciudad[0] == cod_pais and ciudad[1] == cod_ciudad for ciudad in ciudades):
        print(f"Error: No existe una ciudad con código '{cod_ciudad}' en el país '{cod_pais}'")
        return False
        
    #Explicacion:
    #   any devuelve True si al menos uno de los elementos satisface la condicion
    #   le ponemos not any para que devuelva True si NINGUN Restaurante en la lista coincide con (pais, ciudad y codigo)

    # restaurante[0]==cod_pais verifica si el primer elemento del restaurante actual, es decir, el codigo del pais, coincide con el codigo de pais que buscamos
    # restaurante[1]==cod_ciudad lo mismo pero con el segundo elemento, es decir, el codigo de la ciudad
    # restaurante[2]==cod_rest lo mismo pero con el tercer elemento, es decir, el codigo del restaurante

    if not any(restaurante[0] == cod_pais and restaurante[1] == cod_ciudad and restaruante[2] == cod_rest for restaurante in restaurantes):
        print(f"Error: No existe un restaurante con codigo '{cod_rest}' en la ciudad con código '{cod_ciudad}' en el país '{cod_pais}'")
        return False
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
'''

#Inserciones con funciones de validacion_______________________#
#FUNCIONA

def insertar_pais(paises, codigo, nombre):
    return insertar_en_lista(paises, [codigo, nombre], indice_unico=0)

def insertar_ciudad(paises, ciudades, cod_pais, cod_ciudad, nombre):
    if not validar_pais_existe(paises, cod_pais):
        return False
    return insertar_en_lista(ciudades, [cod_pais, cod_ciudad, nombre], indice_unico=1)

def insertar_restaurante(paises, ciudades, restaurantes, cod_pais, cod_ciudad, cod_rest, nombre):
    if not validar_pais_existe(paises, cod_pais):
        return False
    if not validar_ciudad_existe(ciudades, cod_pais, cod_ciudad):
        return False
    return insertar_en_lista(restaurantes, [cod_pais, cod_ciudad, cod_rest, nombre], indice_unico=2)

def insertar_menu(paises, ciudades, restaurantes, menus, cod_pais, cod_ciudad, cod_rest, cod_menu, nombre):
    if not validar_pais_existe(paises, cod_pais):
        return False
    if not validar_ciudad_existe(ciudades, cod_pais, cod_ciudad):
        return False
    if not validar_restaurante_existe(restaurantes, cod_pais, cod_ciudad, cod_rest):
        return False
    return insertar_en_lista(menus, [cod_pais, cod_ciudad, cod_rest, cod_menu, nombre], indice_unico=3)

def insertar_producto(paises, ciudades, restaurantes, menus, productos, cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto, nombre, calorias, precio):
    if not validar_pais_existe(paises, cod_pais):
        return False
    if not validar_ciudad_existe(ciudades, cod_pais, cod_ciudad):
        return False
    if not validar_restaurante_existe(restaurantes, cod_pais, cod_ciudad, cod_rest):
        return False
    if not validar_menu_existe(menus, cod_pais, cod_ciudad, cod_rest, cod_menu):
        return False
    return insertar_en_lista(productos,[cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto, nombre, calorias, precio],indice_unico=4)
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
                    if insertar_pais(paises, codigo, nombre):
                        print(paises)
                elif y == 2:
                    print("\n Has seleccionado insertar Ciudad.")
                    cod_pais = int(input("Ingrese el codigo del pais: "))
                    cod_ciudad = int(input("Ingrese el codigo de la ciudad: "))
                    nombre = input("Ingrese el nombre del ciudad: ")
                    if insertar_ciudad(paises, ciudades, cod_pais, cod_ciudad, nombre):
                        print(ciudades)
                elif y == 3:
                    print("Has seleccionado insertar Restaurante.")
                    cod_pais = int(input("Ingrese el codigo del pais: "))
                    cod_ciudad = int(input("Ingrese el codigo de la ciudad: "))
                    cod_rest = int(input("Ingrese el codigo del restaurante: "))
                    nombre = input("Ingrese el nombre del restaurante: ")
                    if insertar_restaurante(paises, ciudades, restaurantes, cod_pais, cod_ciudad, cod_rest, nombre):
                        print(restaurantes)
                elif y == 4:
                    print("Has seleccionado insertar Menu.")
                    cod_pais = int(input("Ingrese el codigo del pais: "))
                    cod_ciudad = int(input("Ingrese el codigo de la ciudad: "))
                    cod_rest = int(input("Ingrese el codigo del restaurante: "))
                    cod_menu = int(input("Ingrese el codigo del menu: "))
                    nombre = input("Ingrese el nombre del menu: ")
                    if insertar_menu(paises, ciudades, restaurantes, menus, cod_pais, cod_ciudad, cod_rest, cod_menu, nombre):
                        print(menus)
                elif y == 5:
                    print("Has seleccionado insertar Productos.")
                    cod_pais = input("Ingrese el código del país: ")
                    cod_ciudad = input("Ingrese el código de la ciudad: ")
                    cod_rest = input("Ingrese el código del restaurante: ")
                    cod_menu = input("Ingrese el código del menú: ")
                    cod_producto = input("Ingrese el código del producto: ")
                    nombre = input("Ingrese el nombre del producto: ")
                    calorias = float(input("Ingrese las calorias del producto: "))
                    precio = float(input("Ingrese el precio: "))
                    if insertar_producto(paises, ciudades, restaurantes, menus, productos, cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto, nombre, calorias, precio):
                        print(productos)
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
                if y == 1: #FUNCIONA
                    print("\n Has seleccionado buscar Pais.")
                    nombre = input("Ingrese el nombre del pais a buscar: ")
                    buscar_pais(paises, nombre)
                elif y == 2: #FUNCIONA
                    print("Has seleccionado buscar Ciudad.")
                    buscar_ciudad(ciudades)
                elif y == 3: #FUNCIONA
                    print("Has seleccionado buscar Restaurante.")
                    nombre = input("Ingrese el nombre del restaurante: ")
                    buscar_rest(restaurantes, nombre)
                elif y == 4: #Funciona
                    print("Has seleccionado buscar Menu.")
                    nombre = input("Ingrese el nombre del menu: ")
                    buscar_menu(menus, nombre)
                elif y == 5:
                    print("Has seleccionado buscar Productos.")
                    nombre = input("Ingrese el nombre del producto: ")
                    buscar_produ(productos, nombre)
                elif y == 6:
                    print("Has seleccionado buscar Clientes.")
                    #buscar_cli() #AQUI INSERTAR LA FUNCION FUNCIONANDO xd
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
