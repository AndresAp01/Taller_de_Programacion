#Luis Andres Acunna Perez y Patrick Zúñiga Arroyo
#Mantenimiento de Bases de Datos
#############################
#Funcion para pasar los datos a las listas
def datos_a_listas(ruta_archivo, separador=";", separador_lineas="\n"):
    #Como funciona
    #   ruta_archivo: Es la ruta del archivo a leer
    #   Separador: El caracter que separa las lineas
    #   Separador_lineas: Caracter que separa las lineas
    #   Convertir codigo: Si es True convierte los codigos a enteros
    try:
        with open(ruta_archivo, "r") as archivo:
            texto = archivo.read() #Abre el archivo y lee el contenido
            lista_lineas = texto.split(separador_lineas) #Separa las lineas del texto
            matriz_datos = [] #Crea matriz vacia
            codigos_repetidos = [] #Crea matriz vacia para almacenar los codigos repetidos
            for linea in lista_lineas: #Para cada linea en la lista de lineas
                if not linea.strip():  # Ignorar líneas vacías
                    continue
                campos = linea.split(separador) #Separa los campos de la linea
                if len(campos) < 2: #Si la linea teine menos de dos campos
                    continue
                codigo = str(campos[0]) #obtiene el codigo de la linea
                if codigo not in codigos_repetidos: #Verifica que le codigo no este en la lista de repetidos
                    matriz_datos.append(campos)
                    codigos_repetidos.append(codigo)
            return matriz_datos
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe")
        return None
#Para pasar los datos de los archivos a listas
paises = datos_a_listas("Paises.txt", ";")
ciudades = datos_a_listas("Ciudades.txt", ";")
restaurantes = datos_a_listas("Restaurantes.txt", ";")
menus = datos_a_listas("Menu.txt", ";")
productos = datos_a_listas("Productos.txt", ";")
clientes = datos_a_listas("Clientes.txt", ";")

#Funcion para normalizar las entradas de los codigos, que sean enteros o strings pero que no contenga
#Caracteres especiales o booleanos o asi
def normalizar_codigo(codigo):
    if not isinstance(codigo, (str, int)):
        print(f"El codigo {codigo} no es alfanumerico")
    return str(codigo).lstrip('-')
    # Paso cod_pais a str para poder compararlo con los codigos de las listas y le elimino el signo - por si acaso

def mostrar_menu(opciones):
    print(f"\n=== Bienvenido al menu de Mantenimiento de Bases de Datos ===")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

#VALIDACION----------------------------------------------------------------------------------------
#FUNCIONA
def validar_pais_existe(paises, codigo):
    #Si existe un pais con el codigo cod_pais en la lista paises
    #Primer elemento pais[0] de cada pais en la lista coincide con el codigo
    codigo = normalizar_codigo(codigo)
    if not any(pais[0].lstrip('-') == codigo for pais in paises):
        print(f"Error: No existe un país con código '{codigo}'")
        return False
    return True

def validar_ciudad_existe(ciudades, cod_pais, cod_ciudad):
    cod_pais = normalizar_codigo(cod_pais)
    cod_ciudad = normalizar_codigo(cod_ciudad)
    if not any(ciudad[0] == cod_pais and ciudad[1] == cod_ciudad for ciudad in ciudades):
        print(f"Error: No existe una ciudad con código '{cod_ciudad}' en el país '{cod_pais}'")
        return False
    return True

def validar_restaurante_existe(restaurantes, cod_pais, cod_ciudad, cod_rest):
    cod_pais = normalizar_codigo(cod_pais)
    cod_ciudad = normalizar_codigo(cod_ciudad)
    cod_rest = normalizar_codigo(cod_rest)

    if not any(restaurante[0] == cod_pais and restaurante[1] == cod_ciudad and restaurante[2] == cod_rest for restaurante in restaurantes):
        print(f"Error: No existe un restaurante con código '{cod_rest}' en la ciudad '{cod_ciudad}' del país '{cod_pais}'")
        return False
    return True

def validar_menu_existe(menus, cod_pais, cod_ciudad, cod_rest, cod_menu):
    """Valida que exista un menu con el codigo especificado en el restaurante en la ciudad y pais indicados"""
    cod_pais = normalizar_codigo(cod_pais)
    cod_ciudad = normalizar_codigo(cod_ciudad)
    cod_rest = normalizar_codigo(cod_rest)
    cod_menu = normalizar_codigo(cod_menu)
    if not any(menu[0] == cod_pais and menu[1] == cod_ciudad and
               menu[2] == cod_rest and menu[3] == cod_menu for menu in menus):
        print(f"Error: No existe un menú con código '{cod_menu}' en el restaurante '{cod_rest}' "
              f"de la ciudad '{cod_ciudad}' del país '{cod_pais}'")
        return False
    return True

def validar_producto_existe(productos, cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto):
    """Valida que exista un producto con el código especificado en el menú, restaurante, ciudad y país indicados"""
    cod_pais = normalizar_codigo(cod_pais)
    cod_ciudad = normalizar_codigo(cod_ciudad)
    cod_rest = normalizar_codigo(cod_rest)
    cod_menu = normalizar_codigo(cod_menu)
    cod_producto = normalizar_codigo(cod_producto)

    if not any(producto[0] == cod_pais and producto[1] == cod_ciudad and
              producto[2] == cod_rest and producto[3] == cod_menu and
              producto[4] == cod_producto for producto in productos):
        print(f"Error: No existe un producto con código '{cod_producto}' en el menú '{cod_menu}' "
              f"del restaurante '{cod_rest}' de la ciudad '{cod_ciudad}' del país '{cod_pais}'")
        return False
    return True

def validar_cliente_existe(clientes, cedula):
    #Aqui si cambiamos a abs(int()) porque siempre sera un entero positivo
    cedula = normalizar_codigo(cedula)
    if not any(cliente[0] == cedula for cliente in clientes):
        print(f"Error: No existe un cliente con cédula '{cedula}'")
        return False
    return True

#--------------------------------------------------------------------------------------------------
#BUSQUEDAS_----------------------------------------------------------------------------------------
#FUNCIONA
def buscar_pais(paises, codigo): #FUNCIONA
    codigo = normalizar_codigo(codigo)
    resultados = [pais for pais in paises if codigo.lower() in pais[0].lower()]
    if any(pais[0].lstrip('-') == codigo for pais in paises):
        print("\n Resultados de la búsqueda:")
        for pais in resultados:
            print(f"Código: {pais[0]}, Nombre: {pais[1]}")
    else:
        print(f"No se encontraron países con el nombre '{codigo}'.")
def buscar_ciudad(ciudades, codigo): #FUNCIONA
    codigo = normalizar_codigo(codigo)
    resultados = [ciudad for ciudad in ciudades if codigo.lower() in ciudad[1].lower()]
    if any(ciudad[1].lstrip('-') == codigo for ciudad in ciudades):
        print("\n Resultados de la búsqueda:")
        for ciudad in resultados:
            print(f"Código: {ciudad[1]}, Nombre: {ciudad[2]}")
    else:
        print(f"No se encontraron países con el codigo '{codigo}'.")

def buscar_rest(restaurantes, codigo):
    codigo = normalizar_codigo(codigo)
    resultados = [rest for rest in restaurantes if codigo == rest[2].lower()]
    if resultados:
        print("\nResultados de la búsqueda:")
        for rest in resultados:
            print(f"País: {rest[0]}, Ciudad: {rest[1]}, Código: {rest[2]}, Nombre: {rest[3]}")
    else:
        print(f"No se encontraron restaurantes con el nombre '{codigo}'.")

def buscar_menu(menus, codigo): #FUNCIONA
    codigo = normalizar_codigo(codigo)
    resultados = [menu for menu in menus if codigo.lower() in menu[4].lower()]
    if resultados:
        print("\nResultados de la búsqueda:")
        for menu in resultados:
            print(
                f"País: {menu[0]}, Ciudad: {menu[1]}, Restaurante: {menu[2]}, Código: {menu[3]}, Nombre: {menu[4]}")
    else:
        print(f"No se encontraron menús con el nombre '{codigo}'.")

def buscar_produ(productos, codigo): #FUNCIONA
    codigo = normalizar_codigo(codigo)
    resultados = [prod for prod in productos if codigo.lower() in prod[5].lower()]
    if resultados:
        print("\nResultados de la búsqueda: ")
        for prod in resultados:
            print(
                f"País: {prod[0]}, Ciudad: {prod[1]}, Restaurante: {prod[2]}, Menú: {prod[3]}, "
                +
                f"Código: {prod[4]}, Nombre: {prod[5]}, Calorias : kcal {prod[6]}, Precio:${prod[7]}")
    else:
        print(f"No se encontraron productos con el nombre '{codigo}'.")

def buscar_cliente(clientes, cedula):
    cedula_a_buscar = str(cedula)
    resultados = [cliente for cliente in clientes if cliente[0] == cedula_a_buscar]
    if resultados:
        print("\n Resultados de la busqueda: ")
        for cliente in resultados:
            print(f"Cliente encontrado: Cedula: {cliente[0]}, Nombre: {cliente[1]}")
            return cliente
    else:
        print(f"Cliente no encontrado con cedula '{cedula_a_buscar}'.")

#______________________________________________________________#
#Funcion para insertar nuevos elementos en lista_______________#

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
            print(f"Error: Ya existe un registro con el valor '{nuevo_registro[indice_unico]}' en la posición {indice_unico + 1}") #Sumo 1 para que se pueda entender en la base de daotos
            return False
    # Insertar el registro
    lista.append(nuevo_registro)
    print(f"Registro insertado correctamente: {nuevo_registro}")
    return True

#Inserciones con funciones de validacion_______________________#
#FUNCIONA

def insertar_pais(paises, codigo, nombre):
    try:
        codigo = normalizar_codigo(codigo)
        return insertar_en_lista(paises, [str(codigo), nombre], indice_unico=0)
    except:
        print("Error: El código debe ser alfanumerico")
        return False

def insertar_ciudad(paises, ciudades, cod_pais, cod_ciudad, nombre):
    if not validar_pais_existe(paises, cod_pais):
        return False
    return insertar_en_lista(ciudades, [str(cod_pais), str(cod_ciudad), nombre], indice_unico=1)

def insertar_restaurante(paises, ciudades, restaurantes, cod_pais, cod_ciudad, cod_rest, nombre):
    if not validar_pais_existe(paises, cod_pais):
        return False
    if not validar_ciudad_existe(ciudades, cod_pais, cod_ciudad):
        return False
    return insertar_en_lista(restaurantes,[str(cod_pais), str(cod_ciudad), str(cod_rest), nombre], indice_unico=2)

def insertar_menu(paises, ciudades, restaurantes, menus, cod_pais, cod_ciudad,
                  cod_rest, cod_menu, nombre):
    if not validar_pais_existe(paises, cod_pais):
        return False
    if not validar_ciudad_existe(ciudades, cod_pais, cod_ciudad):
        return False
    if not validar_restaurante_existe(restaurantes, cod_pais, cod_ciudad, cod_rest):
        return False
    cod_pais = normalizar_codigo(cod_pais)
    cod_ciudad = normalizar_codigo(cod_ciudad)
    cod_rest = normalizar_codigo(cod_rest)
    cod_menu = normalizar_codigo(cod_menu)
    for menu in menus:
        if menu[0] == cod_pais and menu[1] == cod_ciudad and menu[2] == cod_rest and menu[3] == cod_menu:
            print(f"Error, ya existe el menu '{menu}' en el restaurante '{cod_rest}'")
            return False
    nuevo_menu = [cod_pais, cod_ciudad, cod_rest, cod_menu, nombre]
    menus.append(nuevo_menu)
    print(f"Menú insertado correctamente: {nuevo_menu}")

    return True

def insertar_producto(paises, ciudades, restaurantes, menus, productos,
                      cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto,
                      nombre, calorias, precio):
    if not validar_pais_existe(paises, cod_pais):
        return False
    if not validar_ciudad_existe(ciudades, cod_pais, cod_ciudad):
        return False
    if not validar_restaurante_existe(restaurantes, cod_pais, cod_ciudad,cod_rest):
        return False
    if not validar_menu_existe(menus, cod_pais, cod_ciudad, cod_rest,cod_menu):
        return False
    return insertar_en_lista(productos, [str(cod_pais),str(cod_ciudad),str(cod_rest),str(cod_menu),str(cod_producto), nombre, calorias, precio],indice_unico=4)

def insertar_cliente(clientes, cedula, nombre):
    if any(cliente[0] == cedula for cliente in clientes):
        print("Error: La cédula ya está registrada.")
        return False
    clientes.append([cedula, nombre])  # Se mantiene el formato de listas
    print("Cliente agregado exitosamente.")
    return True

#para reistrar compra

def registrar_compra(paises, ciudades, restaurantes, menus, productos, compras):
    # Solicitar los datos de la compra
    codigo_pais = None
    codigo_ciudad = None
    codigo_rest = None
    codigo_menu = None
    codigo_producto = None
    cantidad = None
    opcion = None

    # Validar que los códigos existan en las listas correspondientes
    if not validar_pais_existe(paises, codigo_pais):
        print("Error: El código de país no existe.")
        return
    if not validar_ciudad_existe(ciudades, codigo_ciudad):
        print("Error: El código de ciudad no existe.")
        return
    if not validar_restaurante_existe(restaurantes, codigo_rest):
        print("Error: El código de restaurante no existe.")
        return
    if not validar_menu_existe(menus, codigo_menu):
        print("Error: El código de menú no existe.")
        return
    if not validar_producto_existe(productos, codigo_producto):
        print("Error: El código de producto no existe.")
        return

    # Crear un diccionario con la información de la compra
    compra = {
        'codigo_pais': codigo_pais,
        'codigo_ciudad': codigo_ciudad,
        'codigo_restaurante': codigo_rest,
        'codigo_menu': codigo_menu,
        'codigo_producto': codigo_producto,
        'cantidad': cantidad,
        'opcion': opcion
    }

    # Agregar la compra a la lista de compras
    compras.append(compra)
    print("Compra registrada con éxito.")

def validar_existencia(lista, codigo):
    # Función para validar si un código existe en una lista
    for item in lista:
        if item['codigo'] == codigo:
            return True
    return False

#MENU_____________________________#
def MainMenu():
    opciones_principales = ["Inserción", "Buscar", "Registrar compra", "Salir"]
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
                    codigo = input("Ingrese el codigo del pais: ")
                    nombre = input("Ingrese el nombre del pais: ")
                    if insertar_pais(paises, codigo, nombre):
                        print(paises)
                elif y == 2:
                    print("\n Has seleccionado insertar Ciudad.")
                    cod_pais = input("Ingrese el codigo del pais: ")
                    cod_ciudad = input("Ingrese el codigo de la ciudad: ")
                    nombre = input("Ingrese el nombre del ciudad: ")
                    if insertar_ciudad(paises, ciudades, cod_pais, cod_ciudad, nombre):
                        print(ciudades)
                elif y == 3:
                    print("Has seleccionado insertar Restaurante.")
                    cod_pais = input("Ingrese el codigo del pais: ")
                    cod_ciudad = input("Ingrese el codigo de la ciudad: ")
                    cod_rest = input("Ingrese el codigo del restaurante: ")
                    nombre = input("Ingrese el nombre del restaurante: ")
                    if insertar_restaurante(paises, ciudades, restaurantes, cod_pais, cod_ciudad, cod_rest, nombre):
                        print(restaurantes)
                elif y == 4:
                    print("Has seleccionado insertar Menu.")
                    cod_pais = input("Ingrese el codigo del pais: ")
                    cod_ciudad = input("Ingrese el codigo de la ciudad: ")
                    cod_rest = input("Ingrese el codigo del restaurante: ")
                    cod_menu = input("Ingrese el codigo del menu: ")
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
                    cedula = input("Ingrese la cédula del cliente: ")
                    nombre = input("Ingrese el nombre del cliente: ")
                    if insertar_cliente(clientes, cedula, nombre):
                        print("Lista actualizada de clientes:", clientes)
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
                    codigo = input("Ingrese el codigo del pais a buscar: ")
                    buscar_pais(paises, codigo)
                elif y == 2: #FUNCIONA
                    print("Has seleccionado buscar Ciudad.")
                    codigo = input("Ingrese el codigo de la ciudad a buscar: ")
                    buscar_ciudad(ciudades, codigo)
                elif y == 3: #FUNCIONA
                    print("Has seleccionado buscar Restaurante.")
                    codigo = input("Ingrese el codigo del restaurante: ")
                    buscar_rest(restaurantes, codigo)
                elif y == 4: #Funciona
                    print("Has seleccionado buscar Menu.")
                    codigo = input("Ingrese el codigo del menu: ")
                    buscar_menu(menus, codigo)
                elif y == 5:
                    print("Has seleccionado buscar Productos.")
                    codigo = input("Ingrese el codigo del producto: ")
                    buscar_produ(productos, codigo)
                elif y == 6:
                    print("Has seleccionado buscar Clientes.")
                    cedula = int(input("Ingrese la cédula del cliente a buscar: "))
                    buscar_cliente(clientes, cedula)
                elif y == 7:
                    print("Volviendo al menú principal...")
                    break  # Salir del submenú y volver al menú principal
                else:
                    print("Opción no válida. Por favor, selecciona una sub-opción del 1 al 7.")
        elif x == 3:
            print("Has seleccionado Registrar compra.")
            codigo_pais = input("Ingrese el código del país: ")
            codigo_ciudad = input("Ingrese el código de la ciudad: ")
            codigo_rest = input("Ingrese el código del restaurante: ")
            codigo_menu = input("Ingrese el código del menú: ")
            codigo_producto = input("Ingrese el código del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            opcion = input("¿Es para llevar o comer en el restaurante? (llevar/comer): ").lower()
            if registrar_compra(paises, ciudades, restaurantes, menus, productos, compras):
                print(f"Compra exitosa. {compra}")
        elif x == 4:
            break #Sale del programa por completo
        else:
            print("\n\n Atención!! \n Ingresa una opción del 1 al 3.")
            continue #Para que el usuario no tenga que reiniciar el programa
MainMenu()
#----------------------------------------------------------------------------------------------------------------------
