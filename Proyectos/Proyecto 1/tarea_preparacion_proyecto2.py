#Luis Andrés Acuña Pérez y Patrick Zúñiga Arroyo
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
            texto=archivo.read() #Abre el archivo y lee el contenido
            lista_lineas=texto.split(separador_lineas) #Separa las lineas del texto
            matriz_datos=[] #Crea matriz vacia
            codigos_repetidos=[] #Crea matriz vacia para almacenar los codigos repetidos
            for linea in lista_lineas: #Para cada linea en la lista de lineas
                if not linea.strip():  # Ignorar líneas vacías
                    continue
                campos=linea.split(separador) #Separa los campos de la linea
                if len(campos)<2: #Si la linea teine menos de dos campos
                    continue
                codigo=str(campos[0]) #obtiene el codigo de la linea
                if codigo not in codigos_repetidos: #Verifica que le codigo no este en la lista de repetidos
                    matriz_datos.append(campos)
                    codigos_repetidos.append(codigo)
            return matriz_datos
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe")
        return None
#Para pasar los datos de los archivos a listas
paises=datos_a_listas("Paises.txt", ";")
ciudades=datos_a_listas("Ciudades.txt", ";")
restaurantes=datos_a_listas("Restaurantes.txt", ";")
menus=datos_a_listas("Menu.txt", ";")
productos=datos_a_listas("Productos.txt", ";")
clientes=datos_a_listas("Clientes.txt", ";")
compras=[]
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
#Funciona pero se deberia implementar una funcion global y no una para cada una
#Funcion para validar si un pais existe
def validar_pais_existe(paises, cod_pais):
    cod_pais=normalizar_codigo(cod_pais)
    if not any(pais[0].lstrip('-')==cod_pais for pais in paises):
        print(f"Error: No existe un país con código '{cod_pais}'")
        return False
    return True
def validar_ciudad_existe(ciudades, cod_pais, cod_ciudad):
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    if not any(ciudad[0]==cod_pais and ciudad[1]==cod_ciudad for ciudad in ciudades):
        print(f"Error: No existe una ciudad con código '{cod_ciudad}' en el país '{cod_pais}'")
        return False
    return True
def validar_restaurante_existe(restaurantes, cod_pais, cod_ciudad, cod_rest):
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    cod_rest=normalizar_codigo(cod_rest)

    if not any(restaurante[0]==cod_pais and restaurante[1]==cod_ciudad and restaurante[2]==cod_rest for restaurante in restaurantes):
        print(f"Error: No existe un restaurante con código '{cod_rest}' en la ciudad '{cod_ciudad}' del país '{cod_pais}'")
        return False
    return True
def validar_menu_existe(menus, cod_pais, cod_ciudad, cod_rest, cod_menu):
    """Valida que exista un menu con el codigo especificado en el restaurante en la ciudad y pais indicados"""
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    cod_rest=normalizar_codigo(cod_rest)
    cod_menu=normalizar_codigo(cod_menu)
    if not any(menu[0]==cod_pais and menu[1]==cod_ciudad and menu[2]==cod_rest and menu[3]==cod_menu for menu in menus):
        print(f"Error: No existe un menú con código '{cod_menu}' en el restaurante '{cod_rest}' de la ciudad '{cod_ciudad}' del país '{cod_pais}'")
        return False
    return True
def validar_producto_existe(productos, cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto):
    """Valida que exista un producto con el código especificado en el menú, restaurante, ciudad y país indicados"""
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    cod_rest=normalizar_codigo(cod_rest)
    cod_menu=normalizar_codigo(cod_menu)
    cod_producto=normalizar_codigo(cod_producto)
    if not any(producto[0]==cod_pais and producto[1]==cod_ciudad and producto[2]==cod_rest and producto[3]==cod_menu and producto[4]==cod_producto for producto in productos):
        print(f"Error: No existe un producto con código '{cod_producto}' en el menú '{cod_menu}' del restaurante '{cod_rest}' de la ciudad '{cod_ciudad}' del país '{cod_pais}'")
        return False
    return True
def validar_cliente_existe(clientes, cedula):
    cedula=normalizar_codigo(cedula)
    if not any(cliente[0]==cedula for cliente in clientes):
        print(f"Error: No existe un cliente con cédula '{cedula}'")
        return False
    return True
#--------------------------------------------------------------------------------------------------
#MODIFICAR
#Modifica el nombre de un país, ciudad, etc dado su código
def modificar_pais(paises, codigo, nuevo_nombre):
    codigo=normalizar_codigo(codigo)
    for pais in paises:
        if pais[0]==codigo:
            pais[1]=nuevo_nombre
            print(f"País con código {codigo} modificado a '{nuevo_nombre}'")
            return True
    print(f"Error: No se encontró un país con código {codigo}")
    return False
def modificar_ciudad(ciudades, cod_pais, cod_ciudad, nuevo_nombre):
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    for ciudad in ciudades:
        if ciudad[0]==cod_pais and ciudad[1]==cod_ciudad:
            ciudad[2]=nuevo_nombre
            print(f"Ciudad con código {cod_ciudad} en país {cod_pais} modificada a '{nuevo_nombre}'")
            return True
    print(f"Error: No se encontró la ciudad con código {cod_ciudad} en el país {cod_pais}")
    return False
def modificar_restaurante(restaurantes, cod_pais, cod_ciudad, cod_rest, nuevo_nombre):
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    cod_rest=normalizar_codigo(cod_rest)
    for rest in restaurantes:
        if rest[0]==cod_pais and rest[1]==cod_ciudad and rest[2]==cod_rest:
            rest[3]=nuevo_nombre
            print(f"Restaurante con código {cod_rest} modificado a '{nuevo_nombre}'")
            return True
    print(f"Error: No se encontró el restaurante con código {cod_rest}")
    return False
def modificar_menu(menus, cod_pais, cod_ciudad, cod_rest, cod_menu, nuevo_nombre):
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    cod_rest=normalizar_codigo(cod_rest)
    cod_menu = normalizar_codigo(cod_menu)
    for menu in menus:
        if menu[0]==cod_pais and menu[1]==cod_ciudad and menu[2]==cod_rest and menu[3]==cod_menu:
            menu[4]=nuevo_nombre
            print(f"Menú con código {cod_menu} modificado a '{nuevo_nombre}'")
            return True
    print(f"Error: No se encontró el menú con código {cod_menu}")
    return False
def modificar_producto(productos, cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto, nuevo_nombre=None, nuevas_calorias=None, nuevo_precio=None):
    cod_pais = normalizar_codigo(cod_pais)
    cod_ciudad = normalizar_codigo(cod_ciudad)
    cod_rest = normalizar_codigo(cod_rest)
    cod_menu = normalizar_codigo(cod_menu)
    cod_producto = normalizar_codigo(cod_producto)
    for producto in productos:
        if producto[0]==cod_pais and producto[1]==cod_ciudad and producto[2]==cod_rest and producto[3]==cod_menu and producto[4]==cod_producto:
            if nuevo_nombre:
                producto[5]=nuevo_nombre
            if nuevas_calorias is not None:
                producto[6]=nuevas_calorias
            if nuevo_precio is not None:
                producto[7]=nuevo_precio
            print(f"Producto con código {cod_producto} modificado correctamente.")
            return True
    print(f"Error: No se encontró el producto con código {cod_producto}")
    return False
def modificar_cliente(clientes, cedula, nuevo_nombre):
    cedula=normalizar_codigo(cedula)
    for cliente in clientes:
        if cliente[0]==cedula:
            cliente[1]=nuevo_nombre
            print(f"Cliente con cédula {cedula} modificado a '{nuevo_nombre}'")
            return True
    print(f"Error: No se encontró un cliente con cédula {cedula}")
    return False

#--------------------------------------------------------------------------------------------------
#BUSQUEDAS_----------------------------------------------------------------------------------------
#FUNCIONA
def buscar_pais(paises, codigo): #FUNCIONA
    codigo=normalizar_codigo(codigo)
    resultados=[pais for pais in paises if codigo.lower() in pais[0].lower()]
    if resultados:
        print("\n Resultados de la búsqueda:")
        for pais in resultados:
            print(f"Código: {pais[0]}, Nombre: {pais[1]}")
    else:
        print(f"No se encontraron países con el nombre '{codigo}'.")
def buscar_ciudad(ciudades, codigo): #FUNCIONA
    codigo=normalizar_codigo(codigo)
    resultados=[ciudad for ciudad in ciudades if codigo.lower() in ciudad[1].lower()]
    if resultados:
        print("\n Resultados de la búsqueda:")
        for ciudad in resultados:
            print(f"Código: {ciudad[1]}, Nombre: {ciudad[2]}")
    else:
        print(f"No se encontraron países con el codigo '{codigo}'.")
def buscar_rest(restaurantes, codigo):
    codigo=normalizar_codigo(codigo)
    resultados=[rest for rest in restaurantes if codigo == rest[2].lower()]
    if resultados:
        print("\nResultados de la búsqueda:")
        for rest in resultados:
            print(f"País: {rest[0]}, Ciudad: {rest[1]}, Código: {rest[2]}, Nombre: {rest[3]}")
    else:
        print(f"No se encontraron restaurantes con el nombre '{codigo}'.")
def buscar_menu(menus, codigo): #FUNCIONA
    codigo=normalizar_codigo(codigo)
    resultados=[menu for menu in menus if codigo.lower() in menu[4].lower()]
    if resultados:
        print("\nResultados de la búsqueda:")
        for menu in resultados:
            print(
                f"País: {menu[0]}, Ciudad: {menu[1]}, Restaurante: {menu[2]}, Código: {menu[3]}, Nombre: {menu[4]}")
    else:
        print(f"No se encontraron menús con el nombre '{codigo}'.")
def buscar_produ(productos, codigo): #FUNCIONA
    codigo=normalizar_codigo(codigo)
    resultados=[prod for prod in productos if codigo.lower() in prod[5].lower()]
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
    resultados=[cliente for cliente in clientes if cliente[0] == cedula_a_buscar]
    if resultados:
        print("\n Resultaods de la busqueda: ")
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
        if any(item[indice_unico]==nuevo_registro[indice_unico] for item in lista):
            print(f"Error: Ya existe un registro con el valor '{nuevo_registro[indice_unico]}' en la posición {indice_unico + 1}") #Sumo 1 para que se pueda entender en la base de daotos
            return False
    # Insertar el registro
    lista.append(nuevo_registro)
    print(f"Registro insertado correctamente: {nuevo_registro}")
    return True
#Inserciones con funciones de validacion_______________________#
def insertar_pais(paises, codigo, nombre):
    try:
        codigo=normalizar_codigo(codigo)
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
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    cod_rest=normalizar_codigo(cod_rest)
    cod_menu=normalizar_codigo(cod_menu)
    for menu in menus:
        if menu[0]==cod_pais and menu[1]==cod_ciudad and menu[2]==cod_rest and menu[3]==cod_menu:
            print(f"Error, ya existe el menu '{menu}' en el restaurante '{cod_rest}'")
            return False
    nuevo_menu = [cod_pais, cod_ciudad, cod_rest, cod_menu, nombre]
    menus.append(nuevo_menu)
    print(f"Menú insertado correctamente: {nuevo_menu}")

    return True
def insertar_producto(paises, ciudades, restaurantes, menus, productos,
                      cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto,
                      nombre, calorias, precio): #se pone vertical porque hay muchos parametros
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
    if any(cliente[0]==cedula for cliente in clientes):
        print("Error: La cédula ya está registrada.")
        return False
    clientes.append([cedula, nombre])  # Se mantiene el formato de listas
    print("Cliente agregado exitosamente.")
    return True
#_____________________________________________________________________
#REGISTRO
def registrar_compra_menu(paises, ciudades, restaurantes, menus, productos, archivo_facturas):
    print("\n=== REGISTRAR NUEVA COMPRA ===")
    print("Por favor ingrese los siguientes datos:")
    # Mostrar paises disponibles
    print("\nPaíses disponibles:")
    for pais in paises:
        print(f"- {pais[0]}: {pais[1]}")
    cod_pais=input("\nIngrese el código del país: ").strip()
    if not validar_pais_existe(paises, cod_pais):
        print(f"Error: País {cod_pais} no existe")
        return False

    #  ciudades disponibles para ese pais
    print("\nCiudades disponibles en este país:")
    ciudades_pais = [c for c in ciudades if c[0] == cod_pais]
    for ciudad in ciudades_pais:
        print(f"- {ciudad[1]}: {ciudad[2]}")
    cod_ciudad = input("\nIngrese el código de la ciudad: ").strip()
    if not validar_ciudad_existe(ciudades_pais, cod_pais, cod_ciudad):
        print(f"Error: Ciudad {cod_ciudad} no existe")
        return False

    #  restaurantes disponibles en esa ciudad
    print("\nRestaurantes disponibles en esta ciudad:")
    restaurantes_ciudad = [r for r in restaurantes if r[0] == cod_pais and r[1] == cod_ciudad]
    for rest in restaurantes_ciudad:
        print(f"- {rest[2]}: {rest[3]}")
    cod_restaurante = input("\nIngrese el código del restaurante: ").strip()
    if not validar_restaurante_existe(restaurantes_ciudad, cod_pais, cod_ciudad, cod_restaurante):
        print(f"Error: Restaurante {cod_restaurante} no existe")
        return False

    #  menus disponibles en ese restaurante
    print("\nMenús disponibles en este restaurante:")
    menus_restaurante = [m for m in menus if m[0] == cod_pais and m[1] == cod_ciudad and m[2] == cod_restaurante]
    for menu in menus_restaurante:
        print(f"- {menu[3]}: {menu[4]})")
    cod_menu = input("\nIngrese el código del menú: ").strip()
    if not validar_menu_existe(menus_restaurante, cod_pais, cod_ciudad, cod_restaurante, cod_menu):
        print(f"Error: Menu {cod_menu} no existe")
        return False

    # productos disp[onibles en ese menu
    print("\nProductos disponibles en este restaurante: ")
    productos_menu=[prod for prod in productos if prod[0]==cod_pais and prod[1]==cod_ciudad and prod[2]==cod_restaurante and prod[3]==cod_menu]
    for producto in productos_menu:
        print(f"- {producto[4]}: {producto[5]}")
    cod_producto=input("\nIngrese el codigo del producto: ").strip()
    if not validar_producto_existe(productos_menu, cod_pais, cod_ciudad, cod_restaurante, cod_menu, cod_producto):
        print(f"Error: Producto {cod_menu} no existe")
        return False

    cedula = input("\nIngrese cédula del cliente: ").strip()
    cliente = next((c for c in clientes if c[0] == cedula), None)
    if not cliente:
        print("Error: Cliente no registrado")
        return False
    print(f"Cliente: {cliente[1]}")

    while True:
        try:
            cantidad=int(input("\nIngrese la cantidad: "))
            if cantidad<=0:
                print("La cantidad debe ser mayor a 0")
                continue
            break
        except ValueError:
            print("Por favor ingrese un número válido")

    orden = input("\nIngrese la si es para llevar o comer aqui: (llevar/aqui): ")
    producto_encontrado=None
    for producto in productos:
        if (producto[0]==cod_pais and
                producto[1]==cod_ciudad and
                producto[2]==cod_restaurante and
                producto[3]==cod_menu and
                producto[4]==cod_producto):
            producto_encontrado=producto
            break
    if not producto_encontrado:
        print("Error: Producto no encontrado con los códigos proporcionados")
        return False

    precio_unitario = float(producto_encontrado[7])
    total = precio_unitario * cantidad
    confirmar = input("\n¿Confirmar compra? (S/N): ").strip().upper()
    if confirmar != "S":
        print("\nCompra cancelada")
        return False
    with open(archivo_facturas, "a") as archivo:
        archivo.write(
            f"{cliente[0]};{cliente[1]};"
            f"{cod_pais};{cod_ciudad};{cod_restaurante};"
            f"{cod_menu};{cod_producto};{producto_encontrado[5]};"
            f"{cantidad};{precio_unitario:.2f};{total:.2f};{orden}\n"
        )
    print("\nCompra registrada exitosamente!")
    return True

#___________________________________________________________________________________________________
#REPORTES
def guardar_reporte(nombre_reporte, contenido):
    with open("reportes.txt", "a") as archivo:
        archivo.write("\n"+"="*30+f"\n   REPORTE: {nombre_reporte}\n"+"="*30+"\n")
        archivo.write(contenido+"\n")
    print(f"📄 Reporte '{nombre_reporte}' guardado en 'reportes.txt'.")
#Genera un reporte con la lista de todos los países.
def reporte_paises(paises):
    if not paises:
        print("No hay países registrados.")
        return
    contenido="\n".join([f"{pais[0]}. {pais[1]}" for pais in paises])
    print("\n=== LISTA DE PAÍSES ===\n"+contenido)
    guardar_reporte("Lista de Países", contenido)
def reporte_ciudades(ciudades, cod_pais):
    cod_pais = normalizar_codigo(cod_pais)
    ciudades_filtradas = [ciudad for ciudad in ciudades if ciudad[0] == cod_pais]

    if not ciudades_filtradas:
        print(f"No hay ciudades registradas para el país {cod_pais}.")
        return

    contenido="\n".join([f"{ciudad[1]}. {ciudad[2]}" for ciudad in ciudades_filtradas])
    print(f"\n=== CIUDADES DEL PAÍS {cod_pais} ===\n"+contenido)
    guardar_reporte(f"Ciudades del País {cod_pais}", contenido)
def reporte_restaurantes(restaurantes, cod_pais, cod_ciudad):
    """Genera un reporte con la lista de restaurantes en una ciudad específica."""
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    restaurantes_filtrados=[rest for rest in restaurantes if rest[0]==cod_pais and rest[1]==cod_ciudad]

    if not restaurantes_filtrados:
        print(f"No hay restaurantes registrados en la ciudad {cod_ciudad}, país {cod_pais}.")
        return

    contenido="\n".join([f"{rest[2]}. {rest[3]}" for rest in restaurantes_filtrados])
    print(f"\n=== RESTAURANTES EN CIUDAD {cod_ciudad}, PAÍS {cod_pais} ===\n"+contenido)
    guardar_reporte(f"Restaurantes en {cod_ciudad}, {cod_pais}", contenido)
def reporte_clientes(clientes):
    if not clientes:
        print("No hay clientes registrados.")
        return
    contenido="\n".join([f"{cliente[0]} - {cliente[1]}" for cliente in clientes])
    print("\n=== LISTA DE CLIENTES ===\n"+contenido)
    guardar_reporte("Lista de Clientes", contenido)
def reporte_compras_cliente(compras):
    if not compras:
        print("No hay compras registrados.")
        return
    contenido="\n".join([f"{compra[0]} - {compra[1]}" for compra in clientes])
    pass
#_______________________________________________________________________________________________________

#MENU_____________________________#
def MainMenu():
    opciones_principales=["Inserción", "Buscar", "Registrar Compra", "Modificar", "Reportes", "Salir"]
    subopciones=["Pais", "Ciudad", "Restaurante", "Menu", "Productos", "Clientes", "Regresar al mantenimiento"] #Para poder ingresar a otro ciclo y muestre un segundo menu
    subopciones_compra=["Registrar compra", "Regresar al mantenimiento"]
    opciones_reportes = ["Lista de Países", "Ciudades de un País", "Restaurantes de una Ciudad", "Lista de Clientes", "Compras de un Cliente", "Regresar al menú principal"]
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
        elif x==2:
            print("Has seleccionado Buscar.")
            while True:
                mostrar_menu(subopciones)
                y=int(input("Selecciona una sub-opción (1-7) para buscar: "))
                if y==1: #FUNCIONA
                    print("\n Has seleccionado buscar Pais.")
                    codigo=input("Ingrese el codigo del pais a buscar: ")
                    buscar_pais(paises, codigo)
                elif y==2: #FUNCIONA
                    print("Has seleccionado buscar Ciudad.")
                    codigo=input("Ingrese el codigo de la ciudad a buscar: ")
                    buscar_ciudad(ciudades, codigo)
                elif y==3: #FUNCIONA
                    print("Has seleccionado buscar Restaurante.")
                    codigo=input("Ingrese el codigo del restaurante: ")
                    buscar_rest(restaurantes, codigo)
                elif y==4: #Funciona
                    print("Has seleccionado buscar Menu.")
                    codigo=input("Ingrese el codigo del menu: ")
                    buscar_menu(menus, codigo)
                elif y==5:
                    print("Has seleccionado buscar Productos.")
                    codigo = input("Ingrese el codigo del producto: ")
                    buscar_produ(productos, codigo)
                elif y==6:
                    print("Has seleccionado buscar Clientes.")
                    cedula = int(input("Ingrese la cédula del cliente a buscar: "))
                    buscar_cliente(clientes, cedula)
                elif y==7:
                    print("Volviendo al menú principal...")
                    break  # Salir del submenú y volver al menú principal
                else:
                    print("Opción no válida. Por favor, selecciona una sub-opción del 1 al 7.")
        elif x==3:
            print("Has seleccionado Registrar compra")
            if registrar_compra_menu(paises, ciudades, restaurantes, menus, productos, "facturas.txt"):
                print("Operación exitosa")
            else:
                print("No se completó la compra")
            input("Presione Enter para continuar...")
        elif x==4:
            print("Has seleccionado Modificar.")
            while True:
                mostrar_menu(subopciones)
                y=int(input("Selecciona una sub-opción (1-7) para modificar: "))
                if y==1:
                    codigo=input("Ingrese el código del país a modificar: ")
                    nuevo_nombre=input("Ingrese el nuevo nombre del país: ")
                    modificar_pais(paises, codigo, nuevo_nombre)
                elif y==2:
                    cod_pais=input("Ingrese el código del país: ")
                    cod_ciudad=input("Ingrese el código de la ciudad: ")
                    nuevo_nombre=input("Ingrese el nuevo nombre de la ciudad: ")
                    modificar_ciudad(ciudades, cod_pais, cod_ciudad, nuevo_nombre)
                elif y==3:
                    cod_pais=input("Ingrese el código del país: ")
                    cod_ciudad=input("Ingrese el código de la ciudad: ")
                    cod_rest=input("Ingrese el código del restaurante: ")
                    nuevo_nombre=input("Ingrese el nuevo nombre del restaurante: ")
                    modificar_restaurante(restaurantes, cod_pais, cod_ciudad, cod_rest, nuevo_nombre)
                elif y==4:
                    cod_pais=input("Ingrese el código del país: ")
                    cod_ciudad=input("Ingrese el código de la ciudad: ")
                    cod_rest=input("Ingrese el código del restaurante: ")
                    cod_menu=input("Ingrese el código del menú: ")
                    nuevo_nombre=input("Ingrese el nuevo nombre del menú: ")
                    modificar_menu(menus, cod_pais, cod_ciudad, cod_rest, cod_menu, nuevo_nombre)
                elif y==5:
                    cod_pais =input("Ingrese el código del país: ")
                    cod_ciudad=input("Ingrese el código de la ciudad: ")
                    cod_rest=input("Ingrese el código del restaurante: ")
                    cod_menu=input("Ingrese el código del menú: ")
                    cod_producto=input("Ingrese el código del producto: ")
                    nuevo_nombre=input("Ingrese el nuevo nombre del producto: ")
                    nuevas_calorias=float(input("Ingrese las nuevas calorías (o deje vacío para no cambiar): ") or 0)
                    nuevo_precio=float(input("Ingrese el nuevo precio (o deje vacío para no cambiar): ") or 0)
                    modificar_producto(productos, cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto, nuevo_nombre,
                                       nuevas_calorias, nuevo_precio)

                elif y==7:
                    print("Volviendo al menú principal...")
                    break
        elif x==5:
            print("Has seleccionado Reportes.")
            while True:
                mostrar_menu(opciones_reportes)
                y=int(input("Selecciona un reporte (1-6): "))
                if y==1:
                    reporte_paises(paises)
                elif y==2:
                    cod_pais = input("Ingrese el código del país: ")
                    reporte_ciudades(ciudades, cod_pais)
                elif y==3:
                    cod_pais = input("Ingrese el código del país: ")
                    cod_ciudad = input("Ingrese el código de la ciudad: ")
                    reporte_restaurantes(restaurantes, cod_pais, cod_ciudad)
                elif y==4:
                    reporte_clientes(clientes)
                elif y==5:
                    cliente_cedula = input("Ingrese la cédula del cliente: ")
                    reporte_compras_cliente(compras, cliente_cedula)
                elif y==6:
                    print("Volviendo al menú principal...")
                    break
        elif x == 6:
            break
        else:
            print("\n\n Atención!! \n Ingresa una opción del 1 al 6.")
            continue #Para que el usuario no tenga que reiniciar el programa
MainMenu()
#----------------------------------------------------------------------------------------------------------------------