#Luis Andrés Acuña Pérez y Patrick Zúñiga Arroyo
#Mantenimiento de Bases de Datos
####################################################################################################################
#Construccion de diccionarios
"""def leer_archivo(ruta):
    filas=[]
    with open(ruta,'r') as archivo:
        for linea in archivo:
            linea=linea.strip()
            if linea:
                filas.append(linea.split(';'))
    return filas
def cargar_datos(paises_archivo, ciudades_archivo, restaurantes_archivo, menus_archivo, productos_archivo):
    diccionario={}
    #para paises
    for cod_pais, nombre in leer_archivo(paises_archivo):
        diccionario[cod_pais]={'nombre':nombre, 'ciudades':{}}

    #para ciudades
    for cod_pais, cod_ciudad, nombre in leer_archivo(ciudades_archivo):
        if cod_pais in diccionario:
            diccionario[cod_pais]['ciudades'][cod_ciudad]={
                'nombre': nombre,
                'restaurantes': {}
                }
    #para restaurantes
    for cod_pais, cod_ciudad, cod_rest, nombre in leer_archivo(restaurantes_archivo):
        if cod_pais in diccionario and cod_ciudad in diccionario[cod_pais]['ciudades']:
            diccionario[cod_pais]['ciudades'][cod_ciudad]['restaurantes'][cod_rest]={
                'nombre': nombre,
                'menus': {}
                }
    #para menus
    for cod_pais, cod_ciudad, cod_rest, cod_menu, nombre in leer_archivo(menus_archivo):
        if (cod_pais in diccionario and
            cod_ciudad in diccionario[cod_pais]['ciudades'] and
            cod_rest in diccionario[cod_pais]['ciudades'][cod_ciudad]['restaurantes']):
            diccionario[cod_pais]['ciudades'][cod_ciudad]['restaurantes'][cod_rest]['menus'][cod_menu]={
                'nombre': nombre,
                'productos': {}
                }
    #para productos
    for campos in leer_archivo(productos_archivo):
        # esperamos: cod_pais;cod_ciudad;cod_rest;cod_menu;cod_prod;nombre;calorias;precio
        if len(campos)!=8:
            continue
        cod_pais, cod_ciudad, cod_rest, cod_menu, cod_prod, nombre, cal, precio=campos
        if (cod_pais in diccionario and
            cod_ciudad in diccionario[cod_pais]['ciudades'] and
            cod_rest in diccionario[cod_pais]['ciudades'][cod_ciudad]['restaurantes'] and
            cod_menu in diccionario[cod_pais]['ciudades'][cod_ciudad]['restaurantes'][cod_rest]['menus']):
            diccionario[cod_pais]['ciudades'][cod_ciudad]['restaurantes'][cod_rest]['menus'][cod_menu]['productos'][
                cod_prod]={
                'nombre': nombre,
                'calorias': int(float(cal)),
                'precio': float(precio)
                }
    return diccionario
"""
def abrir_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:
            return [linea.strip() for linea in archivo if linea.strip()]
    except FileNotFoundError:
        print(f"Advertencia: No se encontró el archivo '{ruta}'")
        return []
    except Exception as e:
        print(f"Error al leer '{ruta}': {e}")
        return []
#Elimina espacios y convierte a mayusculas
def normalizar(c):
    return c.strip().upper()

def cargar_datos(r_paises, r_ciudades, r_restaurantes, r_menus, r_prods):
    dic={}
    #paises
    for linea in abrir_archivo(r_paises):
        partes=linea.split(";", 1)
        if len(partes)!=2:
            continue
        codigo_pais, nombre_pais=partes
        dic[codigo_pais]={
            "nombre":nombre_pais,
            "ciudades":{}
        }

    #ciudades
    for linea in abrir_archivo(r_ciudades):
        partes=linea.split(';', 2)
        if len(partes)!=3:
            continue
        codigo_pais, codigo_ciudad, nombre_ciudad = partes

        # Verificar que el país exista antes de añadir la ciudad
        if codigo_pais in dic:
            dic[codigo_pais]['ciudades'][codigo_ciudad] = {
                'nombre': nombre_ciudad,
                'restaurantes': {}
            }

    #rest
    for linea in abrir_archivo(r_restaurantes):
        partes=linea.split(';', 3)
        if len(partes)!=4:
            continue
        codigo_pais, codigo_ciudad, codigo_restaurante, nombre_restaurante=partes
        # Verificar que el país y la ciudad existan
        if codigo_pais in dic and codigo_ciudad in dic[codigo_pais]['ciudades']:
            dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes'][codigo_restaurante] = {
                'nombre': nombre_restaurante,
                'menus': {}
            }
    #menus
    for linea in abrir_archivo(r_menus):
        partes=linea.split(';', 4)
        if len(partes)!=5:
            continue
        codigo_pais, codigo_ciudad, codigo_restaurante, codigo_menu, nombre_menu=partes
        # Verificar ruta completa hasta restaurante
        if (codigo_pais in dic and
                codigo_ciudad in dic[codigo_pais]['ciudades'] and
                codigo_restaurante in dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes']):
            dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes'][codigo_restaurante]['menus'][codigo_menu] = {
                'nombre': nombre_menu,
                'productos': {}
            }
    #prods
    for linea in abrir_archivo(r_prods):
        partes=linea.split(';')
        if len(partes)!=8:
            continue
        codigo_pais=partes[0]
        codigo_ciudad=partes[1]
        codigo_restaurante=partes[2]
        codigo_menu=partes[3]
        codigo_producto=partes[4]
        nombre_producto=partes[5]

        # Convertir valores numéricos, ignorando línea si hay error
        try:
            calorias = int(float(partes[6]))
            precio = float(partes[7])
        except ValueError:
            continue

        # Verificar ruta completa hasta menú
        if (codigo_pais in dic and
                codigo_ciudad in dic[codigo_pais]['ciudades'] and
                codigo_restaurante in dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes'] and
                codigo_menu in dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes'][codigo_restaurante][
                    'menus']):
            dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes'][codigo_restaurante]['menus'][codigo_menu][
                'productos'][codigo_producto] = {
                'nombre': nombre_producto,
                'calorias': calorias,
                'precio': precio
            }

    return dic
dic=cargar_datos("Paises.txt", "Ciudades.txt", "Restaurantes.txt", "Menu.txt", "Productos.txt")

def cargar_clientes(ruta_clientes):
    """
    Crea un diccionario de clientes a partir de un archivo con formato cedula;nombre

    Args:
        ruta_clientes (str): Ruta al archivo de clientes

    Returns:
        dict: Diccionario con cédulas como llaves y nombres como valores
    """
    cli={}
    # Procesar cada línea del archivo
    for linea in abrir_archivo(ruta_clientes):
        partes=linea.split(';', 1)

        # Verificar que la línea tenga el formato correcto
        if len(partes)!=2:
            continue

        cedula, nombre=partes
        # Añadir al diccionario
        cli[cedula]=nombre

    return cli

#SEGUNDA MANERA
"""def datos_a_dicc(ruta_paises, ruta_ciudades, ruta_restaurantes, ruta_menus, ruta_productos):

    diccionario={}
    with open(ruta_paises, "r") as archivo:
        for linea in archivo:
            linea=linea.strip()
            if not linea:
                continue

            cod_pais, nombre_pais=linea.split(";", 1)
            diccionario[cod_pais.strip()]= {
                "nombre": nombre_pais,
                "ciudades": {}
                }
    with open(ruta_ciudades, "r") as archivo:
        for linea in archivo:
            linea=linea.strip()
            if not linea:
                continue
            cod_pais, cod_ciudad, nombre_ciudad=linea.split(";", 2)
            if cod_pais in diccionario:
                diccionario[cod_pais]["ciudades"][cod_ciudad]={
                    "nombre": nombre_ciudad,
                    "restaurantes": {}
                    }
    with open(ruta_restaurantes, "r") as archivo:
        for linea in archivo:
            linea=linea.strip()
            if not linea:
                continue
            cod_pais, cod_ciudad, cod_rest, nombre_rest=linea.split(";", 3)
            if cod_pais in diccionario and cod_ciudad in diccionario[cod_pais]["ciudades"]:
                diccionario[cod_pais]["ciudades"][cod_ciudad]["restaurantes"][cod_rest]= {
                    "nombre": nombre_rest,
                    "menus": {}
                    }

    with open(ruta_menus, "r") as archivo:
        for linea in archivo:
            linea=linea.strip()
            if not linea:
                continue
            cod_pais, cod_ciudad, cod_rest, cod_menu, nombre_menu=linea.split(";", 4)
            if cod_pais in diccionario and cod_ciudad in diccionario[cod_pais]["ciudades"] and cod_rest in diccionario[cod_pais]["ciudades"][cod_ciudad]["restaurantes"]:
                diccionario[cod_pais]["ciudades"][cod_ciudad]["restaurantes"][cod_rest]["menus"][cod_menu]={
                    "nombre": nombre_menu,
                    "productos": {}
                    }

    with open(ruta_productos, "r") as archivo:
        for linea in archivo:
            linea=linea.strip()
            if not linea:
                continue

            algo=linea.split(";", 7)
            if len(algo)!=8:
                continue

            (cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto, nombre_producto, calorias, precio)=algo
            if (cod_pais in diccionario
                and cod_ciudad in diccionario[cod_pais]["ciudades"]
                and cod_rest in diccionario[cod_pais]["ciudades"][cod_ciudad]["restaurantes"]
                and cod_menu in diccionario[cod_pais]["ciudades"][cod_ciudad]["restaurantes"][cod_rest]["menus"]):
                diccionario[cod_pais]["ciudades"][cod_ciudad]["restaurantes"][cod_rest]["menus"][cod_menu]["productos"][cod_producto]={
                    "nombre": nombre_producto,
                    "calorias": int(float(calorias)),
                    "precio": float(precio)
                    }
    return diccionario"""
#FIN
clientes="Clientes.txt"
cli=cargar_clientes(clientes)


"""
#Listas para estadisticas
contador_busquedas_rest=[]
contador_busquedas_menu=[]
contador_compras_producto=[]"""

def normalizar_codigo(codigo):
    if not isinstance(codigo, (str, int)):
        print(f"El codigo {codigo} no es alfanumerico")
    return str(codigo).lstrip('-')
#Funciones de validacion, sirven para buscar
def validar_pais_existe(diccionario, cod_pais):
    cod=normalizar_codigo(cod_pais)
    if cod in diccionario:
        nombre=diccionario[cod]["nombre"]
        print(f"El código {cod} pertenece a: {nombre}")
        return cod in diccionario
    else:
        return f"El codigo {cod} no existe"
#otra
def validar_ciudad_existe(diccionario, cod_pais, cod_ciudad):
    cod_pais=normalizar_codigo(cod_pais)
    ok=validar_pais_existe(diccionario, cod_pais)
    if ok is not True:
        return ok
    cod_ciudad=normalizar_codigo(cod_ciudad)
    if "ciudades" not in diccionario[cod_pais]:
        return f"No hay ciudades definidas en el pais {cod_pais}"
    if cod_ciudad not in diccionario[cod_pais]["ciudades"]:
        return f"El país {cod_pais} existe, pero la ciudad {cod_ciudad} no."
    nombre_ciudad=diccionario[cod_pais]["ciudades"][cod_ciudad]["nombre"]
    print(f"La ciudad {cod_ciudad}, {nombre_ciudad}, SI existe en: {cod_pais}")
    return True
def validar_restaurante_existe(diccionario, cod_pais, cod_ciudad, cod_rest):
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    ok=validar_ciudad_existe(diccionario, cod_pais, cod_ciudad)
    if ok is not True:
        return ok
    cod_rest=normalizar_codigo(cod_rest)
    ciudad_info=diccionario[cod_pais]["ciudades"][cod_ciudad]
    if "restaurantes" not in ciudad_info:
        return f'No hay restaurantes definidos en la ciudad {cod_ciudad}'
    if cod_rest not in ciudad_info["restaurantes"]:
        return f"El restaurante {cod_rest} no existe en la ciudad {cod_ciudad}"
    nombre_rest=ciudad_info["restaurantes"][cod_rest]["nombre"]
    print(f"El restaurante {cod_rest}, {nombre_rest} SI existe en la ciudad {cod_ciudad}")
    return True
def validar_menu_existe(diccionario, cod_pais, cod_ciudad, cod_rest, cod_menu):
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    cod_rest=normalizar_codigo(cod_rest)
    ok=validar_restaurante_existe(diccionario, cod_pais, cod_ciudad, cod_rest)
    if ok is not True:
        return ok
    cod_menu=normalizar_codigo(cod_menu)
    rest_info=diccionario[cod_pais]["ciudades"][cod_ciudad]["restaurantes"][cod_rest]
    if "menus" not in rest_info:
        return f"No hay menús definidos en el restaurante {cod_rest}"
    if cod_menu not in rest_info["menus"]:
        return f"El menu {cod_menu} no existe en el restaurante {cod_rest}"
    nombre_menu=rest_info["menus"][cod_menu]["nombre"]
    print(f"El menu {cod_menu}, {nombre_menu}, SI existe en el restuarante: {cod_rest}")
    return True
#funcion general
def buscar_elemento(diccionario, cod_pais, cod_ciudad=None, cod_restaurante=None, cod_menu=None, cod_prod=None):
    #paises
    cod_pais=normalizar_codigo(cod_pais)
    if cod_pais not in diccionario:
        return f"El país {cod_pais} no existe"
    pais_info=diccionario[cod_pais]
    # Si solo era validar pais:
    if cod_ciudad is None:
        nombre=pais_info["nombre"]
        print(f"El país {cod_pais} → {nombre} existe")
        return True

    #ciudades
    cod_ciudad=normalizar_codigo(cod_ciudad)
    if "ciudades" not in pais_info:
        return f"No hay ciudades definidas en el país {cod_pais}"
    if cod_ciudad not in pais_info["ciudades"]:
        return f"La ciudad {cod_ciudad} no existe en el país {cod_pais}"
    ciudad_info=pais_info["ciudades"][cod_ciudad]
    # Si solo era validar ciudad:
    if cod_restaurante is None:
        nombre_ciudad=ciudad_info["nombre"]
        print(f"La ciudad {cod_ciudad} → {nombre_ciudad} existe en {cod_pais}")
        return True

    #rests
    cod_restaurante=normalizar_codigo(cod_restaurante)
    if "restaurantes" not in ciudad_info:
        return f"No hay restaurantes definidos en la ciudad {cod_ciudad}"
    if cod_restaurante not in ciudad_info["restaurantes"]:
        return f"El restaurante {cod_restaurante} no existe en la ciudad {cod_ciudad}"
    rest_info=ciudad_info["restaurantes"][cod_restaurante]
    # Si solo era validar restaurante:
    if cod_menu is None:
        nombre_rest=rest_info["nombre"]
        print(f"El restaurante {cod_restaurante} → {nombre_rest} existe en {cod_ciudad}")
        return True

    #menus
    cod_menu=normalizar_codigo(cod_menu)
    if "menus" not in rest_info:
        return f"No hay menús definidos en el restaurante {cod_restaurante}"
    if cod_menu not in rest_info["menus"]:
        return f"El menu {cod_menu} no existe en el restaurante {cod_restaurante}"
    menu_info=rest_info["menus"][cod_menu]
    if cod_prod is None:
        nombre_menu=menu_info["nombre"]
        print(f"El menu {cod_menu} → {nombre_menu} existe en {cod_restaurante}")
        return True
    # Éxito en nivel menú

    #productos
    cod_prod=normalizar_codigo(cod_prod)
    if "productos" not in menu_info:
        return f"No hay productos definidos en el menu {cod_menu}"
    if cod_prod not in menu_info["productos"]:
        return f"El producto {cod_prod} no existe en el menu {cod_menu}"
    prod_info=menu_info["productos"][cod_prod]
    nombre_prod=prod_info["nombre"]
    print(f"El producto {cod_prod} → {nombre_prod} existe en {cod_menu}")
    return True
#funciopn para buscar cliente (Porque es en otro diccionario)
def buscar_cli(diccionario, cedula):

    if cedula not in diccionario:
        return f"El cliente con cedula {cedula} no existe"
    nombre=diccionario[cedula]
    print(f"El cliente {cedula} → {nombre} existe")
    return True

def validar_cliente_existe(diccionario, ced):
    ced=normalizar_codigo(ced)
    if ced in diccionario:
        nombre=diccionario[ced]
        print(f"La cedula {ced} pertenece a: {nombre}")
        return True
    else:
        return f"El cliente {ced} no existe"
"""muestra=validar_ciudad_existe(dic,'123', "101")
print(muestra)"""
"""muestra=validar_pais_existe(dic, "123")
print(muestra)"""
#--------------------------------------------------------------------------------------------------
#MODIFICAR_____________________________________________________________________________________________________________#
#funciona
#con fiunciones de validacion
"""def modificar_pais():
    cod_pais=input("Ingrese el código del país a modificar: ")
    cod_pais=normalizar_codigo(cod_pais)
    if not validar_pais_existe(dic,cod_pais):
        print("El pais no existe")
        return
    nuevo_nombre=input("Ingrese el nuevo nombre del país: ")
    dic[cod_pais]["nombre"]=nuevo_nombre
    print(f"El pais {cod_pais} ha sido renombrado como: {nuevo_nombre}")"""
#funciona
def modificar_pais():
    cod_pais=input("Ingrese el código del país a modificar: ")
    cod_pais=normalizar_codigo(cod_pais)
    if cod_pais not in dic:
        print("El pais no existe")
        return
    nuevo_nombre=input("Ingrese el nuevo nombre del país: ")
    dic[cod_pais]["nombre"]=nuevo_nombre
    print(f"El pais {cod_pais} ha sido renombrado como: {nuevo_nombre}")
    print(dic)
#funciona
def modificar_ciudad():
    cod_pais=input("Ingrese el código del país donde se encuentra la ciudad: ")
    cod_ciudad=input("Ingrese el codigo de la ciudad a modificar: ")
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    if cod_pais not in dic:
        print("El pais no existe")
        return
    if cod_ciudad not in dic[cod_pais]["ciudades"]:
        print("La ciudad no existe")
        return
    nuevo_nombre=input("Ingrese el nuevo nombre del ciudad: ")
    dic[cod_pais]["ciudades"][cod_ciudad]["nombre"]=nuevo_nombre
    print(f"La ciudad {cod_ciudad} se ha renombrado como: {nuevo_nombre}")
    print(dic)
#por hacer:
def modificar_restaurante():
    cod_pais=normalizar_codigo(input("Ingrese el código del país: "))
    cod_ciudad=normalizar_codigo(input("Ingrese el código de la ciudad: "))
    cod_rest=normalizar_codigo(input("Ingrese el código del restaurante a modificar: "))
    ok=validar_restaurante_existe(dic, cod_pais, cod_ciudad, cod_rest)
    if ok is not True:
        print(ok)
        return
    # Pedir nuevo nombre y aplicar cambio
    nuevo_nombre=input("Ingrese el nuevo nombre del restaurante: ")
    dic[cod_pais]['ciudades'][cod_ciudad]['restaurantes'][cod_rest]['nombre']=nuevo_nombre
    print(f"El restaurante {cod_rest} se ha renombrado como: {nuevo_nombre}")
    print(dic)

def modificar_menu():
    cod_pais=normalizar_codigo(input("Ingrese el código del país: "))
    cod_ciudad=normalizar_codigo(input("Ingrese el código de la ciudad: "))
    cod_rest=normalizar_codigo(input("Ingrese el código del restaurante: "))
    cod_menu=normalizar_codigo(input("Ingrese el código del menú a modificar: "))
    # Validar menú (incluye validación de niveles anteriores)
    ok=validar_menu_existe(dic, cod_pais, cod_ciudad, cod_rest, cod_menu)
    if ok is not True:
        print(ok)
        return
    # Pedir nuevo nombre y aplicar cambio
    nuevo_nombre=input("Ingrese el nuevo nombre del menú: ")
    dic[cod_pais]['ciudades'][cod_ciudad]['restaurantes'][cod_rest]['menus'][cod_menu]['nombre']=nuevo_nombre
    print(f"El menú {cod_menu} se ha renombrado como: {nuevo_nombre}")
    print(dic)

def modificar_producto():
    cod_pais=normalizar_codigo(input("Ingrese el código del país: "))
    cod_ciudad=normalizar_codigo(input("Ingrese el código de la ciudad: "))
    cod_rest=normalizar_codigo(input("Ingrese el código del restaurante: "))
    cod_menu=normalizar_codigo(input("Ingrese el código del menú: "))
    cod_prod=normalizar_codigo(input("Ingrese el código del producto a modificar: "))
    # Validar que el producto exista
    ok = validar_menu_existe(dic, cod_pais, cod_ciudad, cod_rest, cod_menu)
    if ok is not True:
        print(ok)
        return
    menu_info = dic[cod_pais]['ciudades'][cod_ciudad]['restaurantes'][cod_rest]['menus'][cod_menu]
    if 'productos' not in menu_info or cod_prod not in menu_info['productos']:
        print(f"El producto {cod_prod} no existe en el menú {cod_menu}")
        return
    # Pedir nuevos datos
    nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
    try:
        nuevas_cal  = int(input("Ingrese las nuevas calorías: "))
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
    except ValueError:
        print("Calorías o precio inválidos.")
        return
    # Aplicar cambios
    prod = menu_info['productos'][cod_prod]
    prod['nombre']   = nuevo_nombre
    prod['calorias'] = nuevas_cal
    prod['precio']   = nuevo_precio
    print(f"El producto {cod_prod} ha sido actualizado:")
    print(f"  Nombre:   {nuevo_nombre}")
    print(f"  Calorías: {nuevas_cal}")
    print(f"  Precio:   {nuevo_precio}")
    print(dic)

#funcioooona
def modificar_cliente():
    cedula=input("Ingrese la cedula del cliente: ")
    cedula=normalizar_codigo(cedula)
    if cedula not in cli:
        print(f"El cliente con cedula: {cedula} no existe")
        return
    nuevo_nombre = input("Ingrese el nuevo nombre del cliente: ")
    cli[cedula]["nombre"]=nuevo_nombre
    print(f"El cliente con cedula {cedula} ha sido renombrado como: {nuevo_nombre}")
    print(cli)
#______________________________________________________________________________________________________________________#
#BUSQUEDAS_____________________________________________________________________________________________________________#
def obtener_restaurante_mas_buscado():
    global contador_busquedas_rest
    if not contador_busquedas_rest:
        return None, 0
    mas_buscado=contador_busquedas_rest[0]
    for contador in contador_busquedas_rest:
        if contador[1]>mas_buscado[1]:
            mas_buscado=contador
    return mas_buscado[0], mas_buscado[1]
def obtener_menu_mas_buscado():
    global contador_busquedas_menu
    if not contador_busquedas_menu:
        return None, 0
    mas_buscado=contador_busquedas_menu[0]
    for contador in contador_busquedas_menu:
        if contador[1]>mas_buscado[1]:
            mas_buscado=contador
    return mas_buscado[0], mas_buscado[1]
def obtener_producto_mas_buscado():
    global contador_busquedas_producto
    if not contador_busquedas_producto:
        return None, 0
    mas_buscado=contador_busquedas_producto[0]
    for contador in contador_busquedas_producto:
        if contador[1]>mas_buscado[1]:
            mas_buscado=contador
    return mas_buscado[0], mas_buscado[1]
def buscar_precio():
    pass
def buscar_descuento():
    pass

#______________________________________________________________________________________________________________________#
#INSERCIONES___________________________________________________________________________________________________________#
def insertar_en_diccionario(diccionario, nuevo_registro, indices_unicos=None):
    print(f"Insertando: {nuevo_registro}")
    print(f"En el Diccionario actual: {diccionario}")
    if not isinstance(diccionario, dict):
        print("Error: El primer parámetro debe ser un diccionario")
        return False
    if indices_unicos is not None:
        for clave in diccionario:
            coincide=True
            for ix in indices_unicos:
                if diccionario(nuevo_registro)!=nuevo_registro:
                    coincide=False
                    break
            if coincide:
                valores=[nuevo_registro[ix] for ix in indices_unicos]
                print(f"Error: Ya existe un registro con los valores {valores}")
                return False
def insertar_pais():
    print("Diccionario actual:", paises)
    cod_pais=input("Ingrese el codigo del pais: ")
    nombre=input("Ingrese el nombre del pais: ")
    resultado=insertar_en_lista
    if resultado:
        print(f"Registro insertado correctamente: {paises}")
    return resultado
def insertar_producto():
    global paises, ciudades, restaurantes, menus, productos
    cod_pais=input("Ingrese el código del país: ")
    if not validar_pais_existe(cod_pais):
        return False
    cod_ciudad=input("Ingrese el código de la ciudad: ")
    if not validar_ciudad_existe(cod_pais, cod_ciudad):
        return False
    cod_rest=input("Ingrese el código del restaurante: ")
    if not validar_restaurante_existe(cod_pais, cod_ciudad,cod_rest):
        return False
    cod_menu=input("Ingrese el código del menú: ")
    if not validar_menu_existe(cod_pais, cod_ciudad, cod_rest, cod_menu):
        return False
    cod_producto=input("Ingrese el código del producto: ")
    nombre=input("Ingrese el nombre del producto: ")
    calorias=float(input("Ingrese las calorías del producto: "))
    precio=float(input("Ingrese el precio: "))
    resultado=insertar_en_lista(productos, [str(cod_pais),str(cod_ciudad),str(cod_rest),str(cod_menu),str(cod_producto), nombre, calorias, precio],indices_unicos=[0, 1, 2, 3, 4])

    if resultado:
        print(f"Registro insertado correctamente: {productos}")
    return resultado
def insertar_cliente():
    global clientes
    cedula=input("Ingrese la cédula del cliente: ")
    nombre=input("Ingrese el nombre del cliente: ")
    resultado=insertar_en_lista(clientes, [str(cedula), nombre], indices_unicos=[0])
    if resultado:
        print(f"Registro insertado correctamente: {clientes}")
    return resultado
#______________________________________________________________________________________________________________________#
#REGISTRO
#Funcion para leer el ultimo codigo de factura
def obtener_ultimo_codigo_factura(archivo):
    try:
        with open(archivo, 'r') as archivo:
            lineas=archivo.readlines()
            if lineas:
                ultima_linea=lineas[-1]
                ultimo_codigo=int(ultima_linea.split(';')[0])
                return ultimo_codigo
            else: #Si el archivo existiera pero esta vacio
                return 234500
    except FileNotFoundError:
        print("Error al cargar el archivo, verifica que se haya registrado al menos una factura")
        with open(archivo, 'w') as nuevo_archivo:
            pass
    return 234500
def registrar_compra_menu():
    global paises, ciudades, restaurantes, menus, productos, clientes
    print("\n=== REGISTRAR NUEVA COMPRA ===")
    print("Por favor ingrese los siguientes datos:")
    #Mostrar paises disponibles
    print("\nPaíses disponibles:")
    for pais in paises:
        print(f"- {pais[0]}: {pais[1]}")
    cod_pais=input("\nIngrese el código del país: ").strip()
    if not validar_pais_existe(cod_pais):
        print(f"Error: País {cod_pais} no existe")
        return False
    #ciudades disponibles para ese pais
    print("\nCiudades disponibles en este país:")
    ciudades_pais=[c for c in ciudades if c[0]==cod_pais]
    for ciudad in ciudades_pais:
        print(f"- {ciudad[1]}: {ciudad[2]}")
    cod_ciudad=input("\nIngrese el código de la ciudad: ").strip()
    if not validar_ciudad_existe(cod_pais, cod_ciudad):
        print(f"Error: Ciudad {cod_ciudad} no existe")
        return False

    #restaurantes disponibles en esa ciudad
    print("\nRestaurantes disponibles en esta ciudad:")
    restaurantes_ciudad=[r for r in restaurantes if r[0]==cod_pais and r[1]==cod_ciudad]
    for rest in restaurantes_ciudad:
        print(f"- {rest[2]}: {rest[3]}")
    cod_restaurante=input("\nIngrese el código del restaurante: ").strip()
    if not validar_restaurante_existe(cod_pais, cod_ciudad, cod_restaurante):
        print(f"Error: Restaurante {cod_restaurante} no existe")
        return False
    #  menus disponibles en ese restaurante
    print("\nMenus disponibles en este restaurante:")
    menus_restaurante=[m for m in menus if m[0]==cod_pais and m[1]==cod_ciudad and m[2]==cod_restaurante]
    for menu in menus_restaurante:
        print(f"- {menu[3]}: {menu[4]})")
    cod_menu=input("\nIngrese el código del menú: ").strip()
    if not validar_menu_existe(cod_pais, cod_ciudad, cod_restaurante, cod_menu):
        print(f"Error: Menu {cod_menu} no existe")
        return False
    # productos disp[onibles en ese menu
    productos_seleccionados = []
    while True:
        productos_menu=[prod for prod in productos if prod[0]==cod_pais and prod[1]==cod_ciudad and prod[2]==cod_restaurante and prod[3]==cod_menu]
        if not productos_menu:
            print("\nNo hay productos disponibles en este menu.")
            return False

        print(f"\n Productos disponibles en este menu {cod_menu}: ")
        for prod in productos_menu:
            print(f"├─ Código: {prod[4]}")
            print(f"│  Nombre: {prod[5]}")
            print(f"│  Precio: ${prod[7]}")
            print("└──────────────────")
        cod_producto=input("\nIngrese el código del producto (o 'fin' para terminar): ").strip()
        if cod_producto.lower()=='fin':
            if not productos_seleccionados:
                print("Debe seleccionar al menos un producto")
                continue
            break
        producto_encontrado = None
        for p in productos_menu:
            if str(p[4])==str(cod_producto):
                producto_encontrado = p
                break
        if not producto_encontrado:
            print(f"\nError: Código {cod_producto} no válido")
            print("Códigos disponibles:", ", ".join([str(p[4]) for p in productos_menu]))
            continue
        while True:
            try:
                cantidad=int(input(f"\nIngrese la cantidad para {producto_encontrado[5]}: "))
                if cantidad<=0:
                    print("La cantidad debe ser mayor a 0")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un número válido")
        productos_seleccionados.append({'producto': producto_encontrado, 'cantidad': cantidad})
        print(f"Producto {producto_encontrado[5]} agregado con éxito")

    cedula=input("\nIngrese la cédula del cliente: ").strip()
    cliente=next((c for c in clientes if c[0]==cedula), None)
    if not cliente:
        print("Error: Cliente no registrado")
        return False
    print(f"Cliente: {cliente[1]}")

    orden=input("\nIngrese si la orden es para llevar o comer aqui: (llevar/aqui): ").strip().lower()
    while orden not in ['llevar', 'aqui']:
        print("Opción no válida. Ingrese 'llevar' o 'aqui'")
        orden=input("\nIngrese si es para llevar o comer aquí (llevar/aqui): ").strip().lower()

    metodo_pago=input("\nIngrese el metodo de pago: (efectivo/tarjeta): ").strip().lower()
    while metodo_pago not in ['efectivo', 'tarjeta']:
        print("Opcion no valida. Ingrese 'efectivo' o 'tarjeta'")
        metodo_pago=input("\nIngrese el metodo de pago: (efectivo/tarjeta): ").strip().lower()
    # Mostrar resumen de la compra
    print("\nResumen de su compra:")
    total_compra=0
    for i, item in enumerate(productos_seleccionados, 1):
        producto=item['producto']
        cantidad=item['cantidad']
        subtotal=float(producto[7])*cantidad
        total_compra+=subtotal
        if orden=="llevar" and metodo_pago=="efectivo":
            total_compra=total_compra
        elif orden=="llevar" and metodo_pago=="tarjeta":
            total_compra*=0.92
        elif orden=="aqui" and metodo_pago=="efectivo":
            total_compra=total_compra
        else:
            total_compra*=0.95
        print(f"{i}. {producto[5]} - Cantidad: {cantidad} - Subtotal: {subtotal:.2f}")
    print(f"\nTotal a pagar: {total_compra:.2f}")

    modificar=input("\n¿Desea modificar la compra? (S/N): ").strip().upper()
    while modificar=="S":
        print("\n¿Qué desea modificar?")
        print("1. Cambiar un producto")
        print("2. Cambiar la cantidad de un producto")
        print("3. Eliminar un producto")
        print("4. Agregar otro producto")
        print("5. Terminar modificaciones")

        opcion=input("\nSeleccione una opción (1-5): ").strip()

        if opcion=="1":  # Cambiar producto
            print("\nProductos en su pedido:")
            for i, item in enumerate(productos_seleccionados, 1):
                print(f"{i}. {item['producto'][5]} - Cantidad: {item['cantidad']}")

            try:
                num=int(input("\nIngrese el número del producto a cambiar: ")) - 1
                if num<0 or num>=len(productos_seleccionados):
                    print("Número de producto inválido")
                    continue

                print("\nSeleccione el nuevo producto:")
                for producto in productos_menu:
                    print(f"- {producto[4]}: {producto[5]} (Precio: {producto[7]})")

                nuevo_cod=input("\nIngrese el código del nuevo producto: ").strip()
                nuevo_prod=next((p for p in productos_menu if p[4] == nuevo_cod), None)

                if not nuevo_prod:
                    print("Producto no encontrado")
                    continue
                #Para Mantener la misma cantidad
                cantidad_actual = productos_seleccionados[num]['cantidad']
                productos_seleccionados[num] = {'producto': nuevo_prod,'cantidad': cantidad_actual}
                print(f"Producto cambiado a {nuevo_prod[5]}")
            except ValueError:
                print("Por favor ingrese un número válido")

        elif opcion=="2":  # Paracambiar cantidad
            print("\nProductos en su pedido:")
            for i, item in enumerate(productos_seleccionados, 1):
                print(f"{i}. {item['producto'][5]} - Cantidad: {item['cantidad']}")
            try:
                num=int(input("\nIngrese el número del producto a modificar: ")) - 1
                if num<0 or num>=len(productos_seleccionados):
                    print("Número de producto inválido")
                    continue
                nueva_cantidad=int(input(f"\nIngrese la nueva cantidad para {productos_seleccionados[num]['producto'][5]}: "))
                if nueva_cantidad<=0:
                    print("La cantidad debe ser mayor a 0")
                    continue
                productos_seleccionados[num]['cantidad']=nueva_cantidad
                print("Cantidad actualizada")
            except ValueError:
                print("Por favor ingrese un número válido")
        elif opcion=="3":  # Para eliminar producto
            print("\nProductos en su pedido:")
            for i, item in enumerate(productos_seleccionados, 1):
                print(f"{i}. {item['producto'][5]} - Cantidad: {item['cantidad']}")
            try:
                num=int(input("\nIngrese el número del producto a eliminar: ")) - 1
                if num<0 or num>=len(productos_seleccionados):
                    print("Número de producto inválido")
                    continue
                producto_eliminado=productos_seleccionados.pop(num)
                print(f"Producto {producto_eliminado['producto'][5]} eliminado")
                if not productos_seleccionados:
                    print("No hay productos en el pedido. Volviendo al menú principal...")
                    return False
            except ValueError:
                print("Por favor ingrese un número válido")

        elif opcion=="4":  # Agregar producto
            print("\nProductos disponibles en este menú:")
            productos_en_menu=[prod for prod in productos if prod[0]==cod_pais and prod[1]==cod_ciudad and prod[2]==cod_restaurante and prod[3] == cod_menu]
            if not productos_en_menu:
                print("No hay productos disponibles en este menú")
                continue
            for producto in productos_en_menu:
                print(f"- {producto[4]}: {producto[5]} (Precio: {producto[7]})")
            cod_producto=input("\nIngrese el código del producto a agregar: ").strip()
            producto_encontrado=next((p for p in productos_en_menu if p[4]==cod_producto), None)
            if not producto_encontrado:
                print("Error: Producto no encontrado en este menú")
                continue
            cantidad=int(input(f"\nIngrese la cantidad para {producto_encontrado[5]}: "))
            if cantidad<= 0:
                print("La cantidad debe ser mayor a 0")
                continue
            productos_seleccionados.append({'producto': producto_encontrado,'cantidad': cantidad})
            print(f"Producto {producto_encontrado[5]} agregado")
        elif opcion=="5":  # Terminar modificaciones
            break
        else:
            print("Opción no válida. Por favor seleccione 1-5")

        print("\nResumen actualizado de su compra:")
        total_compra=0
        for i, item in enumerate(productos_seleccionados, 1):
            producto=item['producto']
            cantidad=item['cantidad']
            subtotal=float(producto[7])*cantidad
            total_compra+=subtotal
            print(f"{i}. {producto[5]} - Cantidad: {cantidad} - Subtotal: {subtotal:.2f}")
        print(f"\nTotal a pagar: {total_compra:.2f}")

        modificar = input("\n¿Desea realizar más modificaciones? (S/N): ").strip().upper()
    confirmar=input("\n¿Confirmar compra? (S/N): ").strip().upper()
    if confirmar!="S":
        print("\nCompra cancelada")
        return False


    registro_compras=f"registro_compras.txt"
    codigo_factura=obtener_ultimo_codigo_factura(registro_compras)+1

    with open(registro_compras,"a") as archivo:
        for item in productos_seleccionados:
            producto=item['producto']
            cantidad=item['cantidad']
            subtotal=float(producto[7])
            total=subtotal*cantidad
            if orden=="llevar" and metodo_pago=="efectivo":
                total=total
            elif orden=="llevar" and metodo_pago=="tarjeta":
                total*=0.92
            elif orden=="aqui" and metodo_pago=="efectivo":
                total=total
            else:
                total*=0.95
            archivo.write(
                f"{codigo_factura};"
                f"{cliente[0]};{cliente[1]};"
                f"{cod_pais};{cod_ciudad};{cod_restaurante};"
                f"{cod_menu};{producto[4]};{producto[5]};"
                f"{cantidad};{subtotal:.2f};{total:.2f};{orden}\n"
            )
        print("\nCompra registrada exitosamente!")
    # Un archivo para cada cliente
    nombre_archivo=f"factura_{cedula}_{codigo_factura}.txt"
    with open(nombre_archivo, "a") as archivo:
        for item in productos_seleccionados:
            producto=item['producto']
            cantidad=item['cantidad']
            subtotal=float(producto[7])
            total=subtotal*cantidad
            if orden=="llevar" and metodo_pago=="efectivo":
                total=total
            elif orden=="llevar" and metodo_pago=="tarjeta":
                total*=0.92
            elif orden=="aqui" and metodo_pago=="efectivo":
                total=total
            else:
                total*=0.95
            archivo.write(
                f"{codigo_factura};"
                f"{cliente[0]};{cliente[1]};"
                f"{cod_pais};{cod_ciudad};{cod_restaurante};"
                f"{cod_menu};{producto[4]};{producto[5]};"
                f"{cantidad};{subtotal:.2f};{total:.2f};{orden}\n"
            )
        print(f"\nCompra registrada exitosamente! Factura #{codigo_factura}, Total: ${total_compra:.2f}")
    return True
#______________________________________________________________________________________________________________________#
#REPORTES
def guardar_reporte(nombre_reporte, contenido):
    with open("reportes.txt", "a") as archivo:
        archivo.write("\n"+"="*30+f"\n   REPORTE: {nombre_reporte}\n"+"="*30+"\n")
        archivo.write(contenido+"\n")
    print(f"📄 Reporte '{nombre_reporte}' guardado en 'reportes.txt'.")
def reporte_paises():
    global paises
    if not paises:
        print("No hay países registrados.")
        return
    contenido="\n".join([f"{pais[0]}. {pais[1]}" for pais in paises])
    print("\n=== LISTA DE PAÍSES ===\n"+contenido)
    guardar_reporte("Lista de Países", contenido)
def reporte_ciudades():
    global paises, ciudades
    cod_pais = input("Ingrese el código del país: ")
    cod_pais = normalizar_codigo(cod_pais)
    ciudades_filtradas = [ciudad for ciudad in ciudades if ciudad[0] == cod_pais]

    if not ciudades_filtradas:
        print(f"No hay ciudades registradas para el país {cod_pais}.")
        return

    contenido="\n".join([f"{ciudad[1]}. {ciudad[2]}" for ciudad in ciudades_filtradas])
    print(f"\n=== CIUDADES DEL PAÍS {cod_pais} ===\n"+contenido)
    guardar_reporte(f"Ciudades del País {cod_pais}", contenido)
def reporte_restaurantes():
    global paises, ciudades, restaurantes
    cod_pais = input("Ingrese el código del país: ")
    cod_ciudad = input("Ingrese el ciudad: ")
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    restaurantes_filtrados=[rest for rest in restaurantes if rest[0]==cod_pais and rest[1]==cod_ciudad]
    if not restaurantes_filtrados:
        print(f"No hay restaurantes registrados en la ciudad {cod_ciudad}, país {cod_pais}.")
        return
    contenido="\n".join([f"{rest[2]}. {rest[3]}" for rest in restaurantes_filtrados])
    print(f"\n=== RESTAURANTES EN CIUDAD {cod_ciudad}, PAÍS {cod_pais} ===\n"+contenido)
    guardar_reporte(f"Restaurantes en {cod_ciudad}, {cod_pais}", contenido)
def reporte_menus():
    global paises, ciudades, restaurantes, menus
    cod_pais = input("Ingrese el código del país: ")
    cod_ciudad = input("Ingrese el ciudad: ")
    cod_restaurante = input("Ingrese el restaurante: ")
    cod_pais=normalizar_codigo(cod_pais)
    cod_restaurante = normalizar_codigo(cod_restaurante)
    cod_ciudad = normalizar_codigo(cod_ciudad)
    menus_filtrados=[m for m in menus if m[0]==cod_pais and m[1]==cod_ciudad and m[2]==cod_restaurante]
    if not menus_filtrados:
        print("No hay menus registrados.")
        return
    contenido="\n".join([f"{m[3]}. {m[4]}" for m in menus_filtrados])
    print(f"\n=== MENUS IN RESTAURANTE {cod_restaurante}, PAÍS {cod_pais} ===\n" + contenido)
    guardar_reporte(f"Menus en {cod_restaurante}, {cod_pais}", contenido)
def reporte_productos():
    global paises, ciudades, restaurantes, menus, productos
    cod_pais=input("Ingrese el código del país: ")
    cod_ciudad=input("Ingrese el ciudad: ")
    cod_restaurante=input("Ingrese el restaurante: ")
    cod_menu=input("Ingrese el menu: ")
    cod_menu=normalizar_codigo(cod_menu)
    cod_restaurante=normalizar_codigo(cod_restaurante)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    cod_pais=normalizar_codigo(cod_pais)
    productos_filtrados=[prod for prod in productos if prod[0]==cod_pais and prod[1]==cod_ciudad and prod[2]==cod_restaurante and prod[3]==cod_menu]
    if not productos_filtrados:
        print("No hay productos registrados.")
        return
    contenido="\n".join([f"{prod[4]}. {prod[5]}" for prod in productos_filtrados])
    print(f"\n=== PRODUCTOS EN MENU {cod_menu}, RESTAURANTE {cod_restaurante} ===\n"+contenido)
    guardar_reporte(f"Productos en {cod_menu}", contenido)
def reporte_clientes():
    global clientes
    if not clientes:
        print("No hay clientes registrados.")
        return
    contenido="\n".join([f"{cliente[0]} - {cliente[1]}" for cliente in clientes])
    print("\n=== LISTA DE CLIENTES ===\n"+contenido)
    guardar_reporte("Lista de Clientes", contenido)
def reporte_compras():
    global compras
    if not compras:
        print("No hay compras registrados.")
        return
    print("\n=== LISTA DE COMPRAS ===\n")
    print("Lista de compras completa en el archivo: registro_compras.txt")
#Funciones de estadisticas
def leer_compras():
    try:
        with open("registro_compras.txt", "r") as archivo:
            lineas=archivo.readlines()
            if not lineas:
                print("No hay compras registradas en el sistema.")
                return
            return [linea.strip().split(';') for linea in lineas]  # Devuelve lista de campos
    except FileNotFoundError:
        print("El archivo registro_compras.txt no existe, intenta registrar una compra primero.")
        return
def reporte_compras_cliente():
    global compras
    cedula=input("Ingrese la cedula del cliente: ").strip()
    cedula=normalizar_codigo(cedula)
    compras=leer_compras()
    if not compras:
        return
    contador=0
    nombre_cliente=None
    for campos in compras:  # Iteramos directamente sobre la lista de campos
        cedula_extraida=campos[1]  # Posición 1 es la cédula
        if cedula_extraida==cedula:
            if nombre_cliente is None:
                nombre_cliente=campos[2]  # Posición 2 es el nombre
            contador+=1

    if contador==0:
        print(f"No hay compras registradas para el cliente con cedula {cedula}.")
        return
    contenido=f"Cliente: {nombre_cliente}\nCedula: {cedula}\nCantidad de items comprados: {contador}"
    print(f"\n=== COMPRAS DEL CLIENTE {cedula} ===\n{contenido}")
    guardar_reporte(f"Compras del Cliente {cedula}", contenido)
def reporte_restaurante_mas_buscado():
    nombre_rest, cantidad=obtener_restaurante_mas_buscado()
    if nombre_rest is None:
        print("No hay datos, se necesita buscar un restaurante al menos.")
        return
    contenido=f"El restaurante mas buscado es: {nombre_rest}\nCantidad de busquedas: {cantidad}"
    print(f"\n=== RESTAURANTE MAS BUSCADO ===\n{contenido}")
    guardar_reporte("Menu mas buscado", contenido)
def reporte_menu_mas_buscado():
    nombre_menu, cantidad=obtener_menu_mas_buscado()
    if nombre_menu is None:
        print("No hay datos, se ncesita buscar un menu antes.")
        return
    contenido=f"El menu mas buscado es: {nombre_menu}\nCantidad de busquedas: {cantidad}"
    print(f"\n=== MENU MAS BUSCADO ===\n{contenido}")
    guardar_reporte("Menu mas buscado", contenido)
def obtener_producto_mas_comprado():
    global contador_compras_producto
    try:
        with open("registro_compras.txt", "r") as archivo:
            lineas=archivo.readlines()
    except FileNotFoundError:
        print("No se encontró el archivo 'registro_compras.txt'.")
        return None, None

    for linea in lineas:
        datos=linea.strip().split(";")
        try:
            cantidad=int(datos[9])
        except ValueError:
            continue
        producto=datos[8]
        encontrado=False
        for registro in contador_compras_producto:
            if registro[0]==producto:
                registro[1]+=cantidad
                encontrado=True
                break
        if not encontrado:
            contador_compras_producto.append([producto, cantidad])
    producto_mas_comprado=None
    max_cantidad=0
    for registro in contador_compras_producto:
        if registro[1]>max_cantidad:
            max_cantidad=registro[1]
            producto_mas_comprado=registro[0]

    return producto_mas_comprado, max_cantidad
def reporte_producto_mas_comprado():
    nombre_producto, cantidad=obtener_producto_mas_comprado()
    if nombre_producto is None:
        print("No hay datos para generar el reporte.")
        return
    contenido=f"El producto más comprado es: {nombre_producto}\nCantidad de compras: {cantidad}"
    print(f"\n=== PRODUCTO MÁS COMPRADO ===\n{contenido}")
    guardar_reporte("Producto más comprado", contenido)
def reporte_facturas_extremas(mayor=True):
    try:
        with open("registro_compras.txt", "r") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print("No se encuentra el archivo 'registro_compras.txt', trata de hacer compras primero.")
        return
    factura_mayor=None
    factura_menor=None
    monto_mayor=float('-inf')
    monto_menor=float('inf')
    for linea in lineas:
        datos = linea.strip().split(";")
        if len(datos)<12:
            continue  # línea malformada
        try:
            monto=float(datos[11])
        except ValueError:
            continue  # si no se puede convertir a número, ignoramos
        if monto>monto_mayor:
            monto_mayor=monto
            factura_mayor=datos
        if monto<monto_menor:
            monto_menor=monto
            factura_menor=datos

    if not (factura_mayor and factura_menor):
        print("No se encontraron facturas válidas en el archivo.")
        return

    if mayor:
        contenido=f"""\
        === FACTURA DE MAYOR MONTO ===
        Factura N°: {factura_mayor[0]}
        Cliente: {factura_mayor[2]}
        Producto: {factura_mayor[8]}
        Cantidad: {factura_mayor[9]}
        Total: {factura_mayor[11]}
        """
        titulo="Factura de Mayor Monto"
    else:
        contenido=f"""\
            === FACTURA DE MENOR MONTO ===
            Factura N°: {factura_menor[0]}
            Cliente: {factura_menor[2]}
            Producto: {factura_menor[8]}
            Cantidad: {factura_menor[9]}
            Total: {factura_menor[11]}
            """
        titulo="Factura de Menor Monto"
    print(contenido)
    guardar_reporte(titulo, contenido)
def reporte_factura_menor_monto():
    pass
def reporte_descuentos():
    orden=input("Ingrese el tipo de servicio ('llevar' o 'aqui'): ").strip().lower()
    metodo_pago=input("Ingrese el tipo de pago ('tarjeta' o 'efectivo'): ").strip().lower()
    descuento=None
    if orden=="llevar":
        if metodo_pago=="efectivo":
            descuento=3
        elif metodo_pago=="tarjeta":
            descuento=8
    elif orden=="aqui":
        if metodo_pago=="tarjeta":
            descuento=5
        elif metodo_pago== "efectivo":
            descuento=0
    contenido = (f"Para el servicio '{orden}' y pago con '{metodo_pago}', "
                 f"se aplica un descuento del {descuento}%.")
    print("\n=== DESCUENTO APLICADO ===\n"+contenido)
    guardar_reporte("Descuento aplicado", contenido)

def reporte_precio_produ():
    global productos
    precio=buscar_produ(retornar_precio=True)
    if precio is None:
        print("No se encontro el producto solicitado.")
        return
    codigo=input("Confirme el codigo del producto para el reporte: ")
    codigo=normalizar_codigo(codigo)
    for prod in productos:
        if codigo.lower() in prod[4].lower():
            nombre_producto=prod[4]
            restaurante=prod[2]
            break
    else:
        nombre_producto="Producto desconocido"
        restaurante="Restaurante desconocido"
    titulo=f"REPORTE DE PRECIO - {nombre_producto}"
    contenido=f"Producto: {nombre_producto}\n"
    contenido+=f"Restaurante: {restaurante}\n"
    contenido+=f"Código: {codigo}\n"
    contenido+=f"Precio: ${precio}"

    print(f"\n=== {titulo} ===\n{contenido}")
    guardar_reporte(titulo, contenido)
#______________________________________________________________________________________________________________________#
#MENU__________________________________________________________________________________________________________________#
def mostrar_menu(opciones):
    print(f"\n=== Bienvenido al menu de Mantenimiento de Bases de Datos ===")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")
def MainMenu():
    opciones_principales=["Inserción", "Buscar", "Modificar", "Reportes", "Salir"]
    subopciones=["Pais", "Ciudad", "Restaurante", "Menu", "Productos", "Clientes", "Regresar al mantenimiento"] #Para poder ingresar a otro ciclo y muestre un segundo menu
    subopciones_insertar=["Pais", "Ciudad", "Restaurante", "Menu", "Productos", "Clientes", "Registrar compra", "Regresar al mantenimiento"]
    opciones_reportes=["Lista de Países", "Ciudades de un País", "Restaurantes de una Ciudad", "Lista de Clientes", "Reporte de todas las compras", "Compras de un Cliente", "Estadisticas", "Regresar al menú principal"]
    opciones_rep_estadisticas=["Restaurante mas buscado", "Menu mas buscado", "Producto mas comprado", "Factura de mayor monto", "Factura de menor monto", "Precio de un producto", "Descuento por pagar con tarjeta", "Regresar al menu principal"]
    while True:
        mostrar_menu(opciones_principales)
        print("\n Ingrese que quiere hacer: ")
        x=int(input())
        if x==1:
            print("Has seleccionado la opcion Insertar.")
            while True:
                mostrar_menu(subopciones_insertar)
                y=int(input("Selecciona una sub-opción (1-8) para insertar: "))
                if y==1:insertar_pais()
                elif y==2:insertar_ciudad()
                elif y==3:insertar_restaurante()
                elif y==4:insertar_menu()
                elif y==5:insertar_producto()
                elif y==6:insertar_cliente()
                elif y==7:
                    print("Has seleccionado Registrar compra")
                    if registrar_compra_menu():
                        print("Operación exitosa")
                    else:
                        print("No se completó la compra")
                    input("Presione Enter para continuar...")
                elif y==8:
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción no válida. Por favor, selecciona una sub-opción del 1 al 8.")
        elif x==2:
            print("Has seleccionado Buscar.")
            while True:
                mostrar_menu(subopciones)
                y=int(input("Selecciona una sub-opción (1-7) para buscar: "))
                if y==1:
                    cod_pais=input("Ingrese el codigo del pais a buscar: ")
                    buscar_elemento(dic, cod_pais)
                    """validar_pais_existe(dic, cod_pais)"""
                elif y==2:
                    cod_pais=input("Ingrese el codigo del pais donde se encuentra la ciudad: ")
                    cod_ciudad=input("Ingrese el codigo de la ciudad a buscar: ")
                    buscar_elemento(dic, cod_pais, cod_ciudad)
                    #validar_ciudad_existe(dic, cod_pais, cod_ciudad)
                elif y==3:
                    cod_pais=input("Ingrese el codigo del pais: ")
                    cod_ciudad=input("Ingrese el codigo de la ciudad: ")
                    cod_rest=input("Ingrese el codigo del restaurante a buscar: ")
                    buscar_elemento(dic, cod_pais, cod_ciudad, cod_rest)
                    #validar_restaurante_existe(dic, cod_pais, cod_ciudad, cod_rest)
                elif y==4:
                    cod_pais=input("Ingrese el codigo del pais: ")
                    cod_ciudad=input("Ingrese el codigo de la ciudad: ")
                    cod_rest=input("Ingrese el codigo del restaurante: ")
                    cod_menu=input("Ingrese el codigo del menu a buscar: ")
                    buscar_elemento(dic, cod_pais, cod_ciudad, cod_rest, cod_menu)
                    #validar_menu_existe(dic, cod_pais, cod_ciudad, cod_rest, cod_menu)
                elif y==5:
                    cod_pais=input("Ingrese el codigo del pais: ")
                    cod_ciudad=input("Ingrese el codigo de la ciudad: ")
                    cod_rest=input("Ingrese el codigo del restaurante: ")
                    cod_menu=input("Ingrese el codigo del menu: ")
                    cod_prod=input("Ingrese el codigo del producto a buscar: ")
                    buscar_elemento(dic, cod_pais, cod_ciudad, cod_rest, cod_menu, cod_prod)
                elif y==6:
                    ced=input("Ingrese la cedula del cliente a buscar")
                    buscar_cli(cli, ced)
                elif y==7:
                    print("Volviendo al menú principal...")
                    break  # Salir del submenú y volver al menú principal
                else:
                    print("Opción no válida. Por favor, selecciona una sub-opción del 1 al 7.")
        elif x==3:
            print("Has seleccionado Modificar.")
            while True:
                mostrar_menu(subopciones)
                y=int(input("Selecciona una sub-opción (1-7) para modificar: "))
                if y==1:modificar_pais()
                elif y==2:modificar_ciudad()
                elif y==3:modificar_restaurante()
                elif y==4:modificar_menu()
                elif y==5:modificar_producto()
                elif y==6:modificar_cliente()
                elif y==7:
                    print("Volviendo al menú principal...")
                    break
        elif x==4:
            print("Has seleccionado Reportes.")
            while True:
                mostrar_menu(opciones_reportes)
                y=int(input("Selecciona un reporte (1-8): "))
                if y==1:reporte_paises()
                elif y==2:reporte_ciudades()
                elif y==3:reporte_restaurantes()
                elif y==4:reporte_clientes()
                elif y==5:reporte_compras()
                elif y==6:reporte_compras_cliente()
                elif y==7:
                    while True:
                        mostrar_menu(opciones_rep_estadisticas)
                        x=int(input("Selecciona una opcion del 1-7: "))
                        if x==1:reporte_restaurante_mas_buscado()
                        if x==2:reporte_menu_mas_buscado()
                        if x==3: reporte_producto_mas_comprado()
                        if x==4: reporte_facturas_extremas(mayor=True)
                        if x==5: reporte_facturas_extremas(mayor=False)
                        if x==6: reporte_precio_produ()
                        if x==7: reporte_descuentos()
                        if x==8: break
                elif y==8:
                    print("Volviendo al menú principal...")
                    break
        elif x==5:
            break
        else:
            print("\n\n Atención!! \n Ingresa una opción del 1 al 5.")
            continue #Para que el usuario no tenga que reiniciar el programa
MainMenu()
#______________________________________________________________________________________________________________________#
