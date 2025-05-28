#Luis Andrés Acuña Pérez y Patrick Zúñiga Arroyo
#Mantenimiento de Bases de Datos
####################################################################################################################
import tkinter as tk
from tkinter import *
from tkinter import simpledialog, messagebox, Menu, Label, Frame, font
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER
#Para recibir bien datos
def normalizar_codigo(codigo):
    if not isinstance(codigo, (str, int)):
        print(f"El codigo {codigo} no es alfanumerico")
    else:
        return str(codigo).lstrip('-')
#Construccion de diccionarios
#----------------------------------------------------------------------------------------------------------------
#Funcion para normalizar cada entrada del usuario
input_orig=input
def entrada(prompt=""):
    return simpledialog.askstring("Entrada", prompt)
def entrada_gui(prompt):
    return simpledialog.askstring("Entrada", prompt)
#Funcion para abrir archivos
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
#funcion para crear el diccionario a partir de los archivos
#r_ son rutas
def cargar_datos(r_paises, r_ciudades, r_restaurantes, r_menus, r_prods):
    dic={}
    # Países
    for linea in abrir_archivo(r_paises):
        linea = linea.strip()
        partes = linea.split(';', 1)
        if len(partes) != 2:
            continue
        codigo_pais, nombre_pais = [p.strip() for p in partes]
        dic[codigo_pais] = {"nombre": nombre_pais, "ciudades": {}}

    # Ciudades
    for linea in abrir_archivo(r_ciudades):
        linea = linea.strip()
        partes = linea.split(';', 2)
        if len(partes) != 3:
            continue
        codigo_pais, codigo_ciudad, nombre_ciudad = [p.strip() for p in partes]
        if codigo_pais in dic:
            dic[codigo_pais]['ciudades'][codigo_ciudad] = {"nombre": nombre_ciudad, "restaurantes": {}}

    # Restaurantes
    for linea in abrir_archivo(r_restaurantes):
        linea = linea.strip()
        partes = linea.split(';', 3)
        if len(partes) != 4:
            continue
        codigo_pais, codigo_ciudad, codigo_restaurante, nombre_restaurante = [p.strip() for p in partes]
        if (codigo_pais in dic and
                codigo_ciudad in dic[codigo_pais]['ciudades']):
            dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes'][codigo_restaurante] = {
                "nombre": nombre_restaurante,
                "menus": {}
            }

    # Menús
    for linea in abrir_archivo(r_menus):
        linea = linea.strip()
        partes = linea.split(';', 4)
        if len(partes) != 5:
            continue
        codigo_pais, codigo_ciudad, codigo_restaurante, codigo_menu, nombre_menu = [p.strip() for p in partes]
        if (codigo_pais in dic and
                codigo_ciudad in dic[codigo_pais]['ciudades'] and
                codigo_restaurante in dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes']):
            dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes'][codigo_restaurante]['menus'][codigo_menu] = {
                "nombre": nombre_menu,
                "productos": {}
            }

    # Productos
    for linea in abrir_archivo(r_prods):
        linea = linea.strip()
        partes = linea.split(';')
        if len(partes) < 9:
            continue
        # Extraer primeros 9 campos: país, ciudad, restaurante, menú, producto, nombre, calorías, precio, stock
        codigo_pais, codigo_ciudad, codigo_restaurante, codigo_menu, codigo_producto, nombre_producto, calorias_s, precio_s, stock_s = [
            p.strip() for p in partes[:9]]
        try:
            calorias = int(float(calorias_s))
            precio = float(precio_s)
            stock = int(stock_s)
        except ValueError:
            continue
        if (codigo_pais in dic and
                codigo_ciudad in dic[codigo_pais]['ciudades'] and
                codigo_restaurante in dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes'] and
                codigo_menu in dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes'][codigo_restaurante][
                    'menus']):
            dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes'][codigo_restaurante]['menus'][codigo_menu][
                'productos'][codigo_producto] = {
                "nombre": nombre_producto,
                "calorias": calorias,
                "precio": precio,
                "stock": stock
            }
    return dic
dic=cargar_datos("Paises.txt", "Ciudades.txt", "Restaurantes.txt", "Menu.txt", "Productos.txt") #Diccionario general
def cargar_clientes(ruta_clientes):
    cli={}
    for linea in abrir_archivo(ruta_clientes):
        partes=linea.split(';', 1)
        if len(partes)!=2:
            continue
        cedula, nombre=partes
        cli[cedula]=nombre
    return cli
cli=cargar_clientes("Clientes.txt") #Diccionario de clientes
#ADMINS#
def cargar_administradores(ruta_administradores):
    admin = {}
    for linea in abrir_archivo(ruta_administradores):
        partes = linea.split(';', 1)
        if len(partes) != 2:
            continue
        cedula, nombre = partes
        admin[cedula.strip()] = nombre.strip()
    return admin
admin=cargar_administradores("Administradores.txt")
total_restaurante_busquedas={}
total_menu_busquedas={}
total_producto_busquedas={}
descuentos = {
    "Pago con tarjeta":                0.05,
    "Para llevar - efectivo":          0.03,
    "Para llevar - tarjeta":           0.08,
    "Comer en restaurante - efectivo": 0.01,
    "Comer en restaurante - tarjeta":  0.05,
}
#Funcion para buscar general
def buscar_elemento(diccionario, cod_pais, cod_ciudad=None, cod_rest=None, cod_menu=None, cod_prod=None):
    # Se usa .get
    if cod_pais not in dic:
        print(f"Error: país '{cod_pais}' no existe.")
        return False
        # Confirmación país
    pais=dic[cod_pais]
    print(f"País encontrado: {cod_pais} → {pais.get('nombre', '<sin nombre>')}")
    if cod_ciudad is None:
        return True
    # Nivel ciudad
    if cod_ciudad not in pais.get('ciudades', {}):
        print(f"Error: ciudad '{cod_ciudad}' no existe en país '{cod_pais}'.")
        return False
    # Confirmación ciudad
    ciudad=pais['ciudades'][cod_ciudad]
    print(f"Ciudad encontrada: {cod_ciudad} → {ciudad.get('nombre', '<sin nombre>')}")
    if cod_rest is None:
        return True
    #Restaurantes
    rest_dict=ciudad.get('restaurantes', {})
    if cod_rest not in rest_dict:
        print(f"Error: restaurante '{cod_rest}' no existe en ciudad '{cod_ciudad}'.")
        return False
    # Contador bsuqueda de restaurantes
    total_restaurante_busquedas[cod_rest]=total_restaurante_busquedas.get(cod_rest, 0) + 1
    # Confirmacion restaurante
    rest=rest_dict[cod_rest]
    print(f"Restaurante encontrado: {cod_rest} → {rest.get('nombre', '<sin nombre>')}")
    if cod_menu is None:
        return True
    #Menus
    menu_dict=rest.get('menus', {})
    if cod_menu not in menu_dict:
        print(f"Error: menú '{cod_menu}' no existe en restaurante '{cod_rest}'.")
        return False
    # Contador menu
    total_menu_busquedas[cod_menu]=total_menu_busquedas.get(cod_menu, 0) + 1
    # Confirmacion menú
    menu=menu_dict[cod_menu]
    print(f"Menú encontrado: {cod_menu} → {menu.get('nombre', '<sin nombre>')}")
    if cod_prod is None:
        return True
    # Nivel producto
    prod_dict=menu.get('productos', {})
    if cod_prod not in prod_dict:
        print(f"Error: producto '{cod_prod}' no existe en menú '{cod_menu}'.")
        return False
    # Contador productos buscados
    total_producto_busquedas[cod_prod] =total_producto_busquedas.get(cod_prod, 0) + 1
    # Confirmacion producto
    prod = prod_dict[cod_prod]
    print(f"Producto encontrado: {cod_prod} → {prod.get('nombre', '<sin nombre>')}")
    return True
    pais = dic[cod_pais]
    # Nivel ciudad
    if cod_ciudad not in pais.get('ciudades', {}):
        print(f"Error: ciudad '{cod_ciudad}' no existe en país '{cod_pais}'.")
        return False
    if cod_rest is None:
        return True
    rest_dict = pais['ciudades'][cod_ciudad].get('restaurantes', {})
    if cod_rest not in rest_dict:
        print(f"Error: restaurante '{cod_rest}' no existe en ciudad '{cod_ciudad}'.")
        return False
    # Contador restaurante
    total_restaurante_busquedas[cod_rest] = total_restaurante_busquedas.get(cod_rest, 0) + 1
    if cod_menu is None:
        return True
    menu_dict = rest_dict[cod_rest].get('menus', {})
    if cod_menu not in menu_dict:
        print(f"Error: menú '{cod_menu}' no existe en restaurante '{cod_rest}'.")
        return False
    # Contador men
    total_menu_busquedas[cod_menu] = total_menu_busquedas.get(cod_menu, 0) + 1
    if cod_prod is None:
        return True
    prod_dict = menu_dict[cod_menu].get('productos', {})
    if cod_prod not in prod_dict:
        print(f"Error: producto '{cod_prod}' no existe en menú '{cod_menu}'.")
        return False
    # Contador producto
    total_producto_busquedas[cod_prod]=total_producto_busquedas.get(cod_prod, 0) + 1
    return True
#funciopn para buscar cliente (Porque es en otro diccionario)
def buscar_cli(diccionario, cedula):
    if cedula not in diccionario:
        return f"El cliente con cedula {cedula} no existe"
    nombre=diccionario[cedula]
    print(f"El cliente {cedula} → {nombre} existe")
    return True
def buscar_cliente_gui():
    cedula = entrada_gui("Cédula del cliente:")
    if cedula:
        resultado = buscar_cli(cli, cedula)
        if resultado is True:
            messagebox.showinfo("Éxito", "Cliente encontrado")
        else:
            messagebox.showerror("Error", resultado)
def validar_cliente_existe(diccionario, ced):
    if ced in diccionario:
        nombre=diccionario[ced]
        print(f"La cedula {ced} pertenece a: {nombre}")
        return True
    else:
        return f"El cliente {ced} no existe"
#----------------------------------------------------------------------------------------------------------------------#
#MODIFICAR_____________________________________________________________________________________________________________#
def modificar_pais(codigo_pais, nuevo_nombre):
    if buscar_elemento(dic, codigo_pais) is not True:
        return f"Error: El país {codigo_pais} no existe."
    else:
        dic[codigo_pais]['nombre'] = nuevo_nombre
        return f"País {codigo_pais} modificado exitosamente."
def modificar_ciudad(codigo_pais, codigo_ciudad, nuevo_nombre):
    if buscar_elemento(dic, codigo_pais, codigo_ciudad) is not True:
        return f"Error: La ciudad {codigo_ciudad} en el país {codigo_pais} no existe."
    dic[codigo_pais]['ciudades'][codigo_ciudad]['nombre'] = nuevo_nombre
    return f"Ciudad {codigo_ciudad} modificada exitosamente."
def modificar_restaurante(codigo_pais, codigo_ciudad, codigo_restaurante, nuevo_nombre):
    if buscar_elemento(dic, codigo_pais, codigo_ciudad, codigo_restaurante) is not True:
        return f"Error: El restaurante {codigo_restaurante} en {codigo_ciudad}, {codigo_pais} no existe."
    dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes'][codigo_restaurante]['nombre'] = nuevo_nombre
    return f"Restaurante {codigo_restaurante} modificado exitosamente."
def modificar_menu(codigo_pais, codigo_ciudad, codigo_restaurante, codigo_menu, nuevo_nombre):
    if buscar_elemento(dic, codigo_pais, codigo_ciudad, codigo_restaurante, codigo_menu) is not True:
        return f"Error: El menú {codigo_menu} en restaurante {codigo_restaurante} no existe."
    dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes'][codigo_restaurante]['menus'][codigo_menu]['nombre'] = nuevo_nombre
    return f"Menú {codigo_menu} modificado exitosamente."
def modificar_producto(codigo_pais, codigo_ciudad, codigo_restaurante, codigo_menu, codigo_producto, nuevo_nombre=None, nuevas_calorias=None, nuevo_precio=None):
    if buscar_elemento(dic, codigo_pais, codigo_ciudad, codigo_restaurante, codigo_menu, codigo_producto) is not True:
        return f"Error: El producto {codigo_producto} en menú {codigo_menu} no existe."
    producto = dic[codigo_pais]['ciudades'][codigo_ciudad]['restaurantes'][codigo_restaurante]['menus'][codigo_menu]['productos'][codigo_producto]
    if nuevo_nombre is not None:
        producto['nombre'] = nuevo_nombre
    if nuevas_calorias is not None:
        producto['calorias'] = nuevas_calorias
    if nuevo_precio is not None:
        producto['precio'] = nuevo_precio
    return f"Producto {codigo_producto} modificado exitosamente."
def modificar_cliente(cedula_cliente, nuevo_nombre):
    if buscar_cli(cli, cedula_cliente) is not True:
        return f"Error: El cliente {cedula_cliente} no existe."
    cli[cedula_cliente] = nuevo_nombre
    return f"Cliente {cedula_cliente} modificado exitosamente."
#ELIMINACIONES_________________________________________________________________________________________________________#
def eliminar_pais(codigo_pais):
    if codigo_pais in dic:
        del dic[codigo_pais]
        print(f"País {codigo_pais} y toda su información asociada fue eliminada.")
        return True
    else:
        print(f"El país {codigo_pais} no existe.")
        return False
def eliminar_ciudad(codigo_pais, codigo_ciudad):
    if codigo_pais in dic and codigo_ciudad in dic[codigo_pais]["ciudades"]:
        del dic[codigo_pais]["ciudades"][codigo_ciudad]
        print(f"Ciudad {codigo_ciudad} y toda su información fue eliminada.")
        return True
    else:
        print(f"La ciudad {codigo_ciudad} no existe en el país {codigo_pais}.")
        return False
def eliminar_restaurante(codigo_pais, codigo_ciudad, codigo_restaurante):
    if (codigo_pais in dic and 
        codigo_ciudad in dic[codigo_pais]["ciudades"] and 
        codigo_restaurante in dic[codigo_pais]["ciudades"][codigo_ciudad]["restaurantes"]):
        
        del dic[codigo_pais]["ciudades"][codigo_ciudad]["restaurantes"][codigo_restaurante]
        print(f"Restaurante {codigo_restaurante} eliminado.")
        return True
    else:
        print(f"Restaurante {codigo_restaurante} no encontrado.")
        return False
def eliminar_menu(codigo_pais, codigo_ciudad, codigo_restaurante, codigo_menu):
    try:
        del dic[codigo_pais]["ciudades"][codigo_ciudad]["restaurantes"][codigo_restaurante]["menus"][codigo_menu]
        print(f"Menú {codigo_menu} eliminado.")
        return True
    except KeyError:
        print(f"No se encontró el menú {codigo_menu} para eliminar.")
        return False
def eliminar_producto(codigo_pais, codigo_ciudad, codigo_restaurante, codigo_menu, codigo_producto):
    try:
        del dic[codigo_pais]["ciudades"][codigo_ciudad]["restaurantes"][codigo_restaurante]["menus"][codigo_menu]["productos"][codigo_producto]
        print(f"Producto {codigo_producto} eliminado.")
        return True
    except KeyError:
        print(f"No se encontró el producto {codigo_producto} para eliminar.")
        return False
def eliminar_cliente(cedula):
    if cedula in cli:
        del cli[cedula]
        print(f"Cliente {cedula} eliminado. Ya no podrá comprar.")
        return True
    else:
        print(f"El cliente {cedula} no existe.")
        return False
#______________________________________________________________________________________________________________________#
#INSERCIONES___________________________________________________________________________________________________________#
def insertar_en_diccionario(registro, nivel):
    if not isinstance(registro, list):
        print("Error: El registro debe ser una lista.")
        return False
    try:
        cod_p = normalizar_codigo(registro[0])
        if nivel >= 2: cod_c = normalizar_codigo(registro[1])
        if nivel >= 3: cod_r = normalizar_codigo(registro[2])
        if nivel >= 4: cod_m = normalizar_codigo(registro[3])
        if nivel == 5:
            cod_pr   = normalizar_codigo(registro[4])
            nombre   = registro[5]
            calorias = int(registro[6])
            precio   = float(registro[7])
            stock    = int(registro[8])
    except Exception as e:
        print(f"Error al normalizar campos: {e}")
        return False
    # nivel 1 pais
    if nivel == 1:
        nombre = registro[1]
        if cod_p in dic:
            print(f"Error: El país {cod_p} ya existe.")
            return False
        dic[cod_p] = {'nombre': nombre, 'ciudades': {}}
        print(f"País {cod_p} – {nombre} insertado.")
        return True
    # Nivel ≥ 2: validar padre pais
    ok = buscar_elemento(dic, cod_p)
    if ok is not True:
        print(ok)
        return False
    # nivel 2 ciudad
    if nivel == 2:
        nombre = registro[2]
        ciudades = dic[cod_p].setdefault('ciudades', {})
        if cod_c in ciudades:
            print(f"Error: La ciudad {cod_c} ya existe en {cod_p}.")
            return False
        ciudades[cod_c] = {'nombre': nombre, 'restaurantes': {}}
        print(f"Ciudad {cod_c} – {nombre} insertada en {cod_p}.")
        return True
    # Nivel ≥ 3: validar padre ciudad
    ok = buscar_elemento(dic, cod_p, cod_c)
    if ok is not True:
        print(ok)
        return False
    # Nivel 3 restaurante
    if nivel == 3:
        nombre = registro[3]
        resto  = dic[cod_p]['ciudades'][cod_c].setdefault('restaurantes', {})
        if cod_r in resto:
            print(f"Error: El restaurante {cod_r} ya existe en {cod_c}.")
            return False
        resto[cod_r] = {'nombre': nombre, 'menus': {}}
        print(f"Restaurante {cod_r} – {nombre} insertado en {cod_c}.")
        return True
    # Nivel ≥ 4 validar padre restaurante
    ok = buscar_elemento(dic, cod_p, cod_c, cod_r)
    if ok is not True:
        print(ok)
        return False
    # Nivel 4 menus
    if nivel == 4:
        nombre = registro[4]
        men = dic[cod_p]['ciudades'][cod_c]['restaurantes'][cod_r].setdefault('menus', {})
        if cod_m in men:
            print(f"Error: El menú {cod_m} ya existe en {cod_r}.")
            return False
        men[cod_m] = {'nombre': nombre, 'productos': {}}
        print(f"Menú {cod_m} – {nombre} insertado en {cod_r}.")
        return True
    # Nivel 5 validar padre menú
    ok = buscar_elemento(dic, cod_p, cod_c, cod_r, cod_m)
    if ok is not True:
        print(ok)
        return False
    # Nivel 5 producto
    prod = dic[cod_p]['ciudades'][cod_c]['restaurantes'][cod_r]['menus'][cod_m].setdefault('productos', {})
    if cod_pr in prod:
        print(f"Error: El producto {cod_pr} ya existe en {cod_m}.")
        return False
    prod[cod_pr] = {
        'nombre':   nombre,
        'calorias': calorias,
        'precio':   precio,
        'stock':    stock
    }
    print(f"Producto {cod_pr} – {nombre} insertado en {cod_m}.")
    return True
def insertar_pais():
    codigo=entrada_gui("Código de país:")
    nombre=entrada_gui("Nombre de país:")
    if codigo and nombre:
        return insertar_en_diccionario([codigo, nombre], nivel=1)
    else:
        messagebox.showerror("Error", "Datos incompletos")
        return False
def insertar_ciudad():
    codigo   =entrada("Código de país: ")
    codigo_c =entrada("Código de ciudad: ")
    nombre   =input("Nombre de ciudad: ").upper()
    return insertar_en_diccionario([codigo, codigo_c, nombre], nivel=2)
def insertar_restaurante():
    codigo   =entrada("Código de país: ")
    codigo_c =entrada("Código de ciudad: ")
    codigo_r =entrada("Código de restaurante: ")
    nombre   =input("Nombre de restaurante: ")
    return insertar_en_diccionario([codigo, codigo_c, codigo_r, nombre], nivel=3)
def insertar_menu():
    codigo   =entrada("Código de país: ")
    codigo_c =entrada("Código de ciudad: ")
    codigo_r =entrada("Código de restaurante: ")
    codigo_m =entrada("Código de menú: ")
    nombre   =input("Nombre de menú: ").upper()
    return insertar_en_diccionario([codigo, codigo_c, codigo_r, codigo_m, nombre], nivel=4)
def insertar_producto():
    codigo   =entrada("Código de país: ")
    codigo_c =entrada("Código de ciudad: ")
    codigo_r =entrada("Código de restaurante: ")
    codigo_m =entrada("Código de menú: ")
    codigo_p =entrada("Código de producto: ")
    nombre   =input("Nombre de producto: ")
    calorias =input("Calorías: ")
    precio   =input("Precio: ")
    stock    =input("Stock(Cuanta cantidad hay): ")
    return insertar_en_diccionario([codigo, codigo_c, codigo_r, codigo_m, codigo_p, nombre, calorias, precio, stock],nivel=5)
def insertar_cliente(cli_dict, cedula, nombre):
    if cedula in cli_dict:
        messagebox.showerror("Error", f"Cliente {cedula} ya existe")
        return False
    cli_dict[cedula] = nombre
    return True
#______________________________________________________________________________________________________________________#
#REGISTRO
#Funcion para leer el ultimo codigo de factura
def registrar_compra_menu(dic, cli, entrada, archivo_facturas="facturas.txt"):
    facturas = []
    ced = entrada("Cédula del cliente: ").strip()
    print(f"Buscando cliente: '{ced}'")
    print(f"Clientes registrados: {list(cli.keys())}")
    if ced not in cli:
        print("El cliente no está registrado.")
        return False
    #preguntar llevar o aqui
    condicion=entrada("¿Es para llevar? (s/n): ").strip().lower() == 's'
    pago=""
    while pago not in ("1", "2"):
        pago=entrada("Método de pago (1=Efectivo, 2=Tarjeta): ").strip()
        if pago not in ("1", "2"):
            print("Debe ingresar 1 para Efectivo o 2 para Tarjeta.")
    es_efectivo=(pago=="1")

    productos_seleccionados = []
    total = 0
    while True:
        #pais
        print("\nPaíses disponibles:")
        for c, info in dic.items(): print(f"  {c}: {info.get('nombre','<sin nombre>')}")
        cod_pais = entrada("Código del país: ").strip()
        if not buscar_elemento(dic, cod_pais):
            print("Inténtelo de nuevo.")
            continue
        pais = dic[cod_pais]
        #ciudad
        print("Ciudades en", cod_pais)
        for c, info in pais.get('ciudades', {}).items(): print(f"  {c}: {info.get('nombre','<sin nombre>')}")
        cod_ciudad = entrada("Código de la ciudad: ").strip()
        if not buscar_elemento(dic, cod_pais, cod_ciudad):
            print("Inténtelo de nuevo.")
            continue
        ciudad = pais['ciudades'][cod_ciudad]
        #restaurante
        print("Restaurantes en", cod_ciudad)
        for c, info in ciudad.get('restaurantes', {}).items(): print(f"  {c}: {info.get('nombre','<sin nombre>')}")
        cod_rest = entrada("Código del restaurante: ").strip()
        if not buscar_elemento(dic, cod_pais, cod_ciudad, cod_rest):
            print("Inténtelo de nuevo.")
            continue
        rest = ciudad['restaurantes'][cod_rest]
        #menu
        print("Menús en", cod_rest)
        for c, info in rest.get('menus', {}).items(): print(f"  {c}: {info.get('nombre','<sin nombre>')}")
        cod_menu = entrada("Código del menú: ").strip()
        if not buscar_elemento(dic, cod_pais, cod_ciudad, cod_rest, cod_menu):
            print("Inténtelo de nuevo.")
            continue
        menu = rest['menus'][cod_menu]
        #producto
        print("Productos en", cod_menu)
        for c, info in menu.get('productos', {}).items(): print(f"  {c}: {info.get('nombre','<sin nombre>')}")
        cod_prod = entrada("Código del producto: ").strip()
        if not buscar_elemento(dic, cod_pais, cod_ciudad, cod_rest, cod_menu, cod_prod):
            print("Inténtelo de nuevo.")
            continue
        prod = menu['productos'][cod_prod]

        # Mostrar y validar stock
        stock_disp = prod.get('stock', 0)
        print(f"Stock disponible para {prod.get('nombre','')}: {stock_disp}")
        try:
            cantidad = int(entrada("Cantidad a comprar: ").strip())
            if cantidad <= 0:
                raise ValueError
            if cantidad > stock_disp:
                print(f"No hay suficiente stock. Solo quedan {stock_disp} unidades.")
                continue
        except ValueError:
            print("Cantidad inválida.")
            continue
        # Actualizar stock y acumular
        prod['stock'] = stock_disp - cantidad
        subtotal = cantidad * prod.get('precio', 0)
        total += subtotal
        productos_seleccionados.append({
            'pais': cod_pais,
            'ciudad': cod_ciudad,
            'restaurante': cod_rest,
            'menu': cod_menu,
            'codigo': cod_prod,
            'nombre': prod.get('nombre',''),
            'precio': prod.get('precio',0),
            'cantidad': cantidad
        })
        #Preguntar si hay mas
        if entrada("¿Desea agregar otro producto? (s/n): ").strip().lower() != 's':
            break
    if not productos_seleccionados:
        print("No se seleccionaron productos. Compra cancelada.")
        return False
    #calcular
    if condicion:
        if es_efectivo:
            descuento=0.03
        else:
            descuento=0.08
    else:
        if es_efectivo:
            descuento=0.01
        else:
            descuento=0.05

    monto_descontado=total*descuento
    monto_final=total-monto_descontado
    #Guardar cada factura
    with open(archivo_facturas, "a") as f:
        for item in productos_seleccionados:
            linea = (
                f"{ced};{item['pais']};{item['ciudad']};{item['restaurante']};"
                f"{item['menu']};{item['codigo']};{item['cantidad']};"
                f"{item['precio']:.2f};{pago};"
                f"{'llevar' if condicion else 'local'};{monto_final}\n"
            )
            f.write(linea)
    # Mostrar resumen
    print(f"\nSubtotal: {total:.2f}")
    #.0f para redondear al mas cercano, sin decimales
    #.2f para ver los dos decimales
    print(f"Descuento aplicado: ({descuento*100:.0f}%): {monto_descontado:.2f}")
    print(f"Total a pagar: {monto_final:.2f}")
    return True
#______________________________________________________________________________________________________________________#
#REPORTES
def reporte_paises(data_dict, nombre):
    documento=SimpleDocTemplate(nombre, pagesize=LETTER)
    estilo=getSampleStyleSheet()
    cuerpo=[]
    # Titulo
    cuerpo.append(Paragraph("Reporte de Países", estilo['Title']))
    cuerpo.append(Spacer(1, 12))
    # Iterar
    for i, (code, info) in enumerate(data_dict.items(), start=1):
        # Obtener el nombre desde info
        country_name=info.get('nombre', '<sin nombre>')
        texto=f"{i}. Código: {code}   Nombre: {country_name}"
        cuerpo.append(Paragraph(texto, estilo['Normal']))
        cuerpo.append(Spacer(1, 6))
    # Construccion del PDF
    documento.build(cuerpo)
    # Mensaje de confirmacion
    mensaje_confirma=f"PDF generado correctamente en: {nombre}"
    print(mensaje_confirma)
    return mensaje_confirma
def reporte_ciudades(dict, cod_pais, nombre):
    if cod_pais not in dict:
        raise ValueError(f"Código de país '{cod_pais}' no encontrado en los datos.")
    country_info = dict[cod_pais]
    nombre_pais  = country_info.get('nombre', '<sin nombre>')
    cities = country_info.get('ciudades', {})
    doc    = SimpleDocTemplate(nombre, pagesize=LETTER)
    styles = getSampleStyleSheet()
    cuerpo  = []
    cuerpo.append(Paragraph(f"Reporte de Ciudades - {nombre_pais} ({cod_pais})", styles['Title']))
    cuerpo.append(Spacer(1, 12))
    if not cities:
        cuerpo.append(Paragraph("<i>No hay ciudades registradas para este país.</i>", styles['Normal']))
        cuerpo.append(Spacer(1, 6))
    else:
        for i, (cod_ciudad, info_ciudad) in enumerate(cities.items(), start=1):
            nombre_ciudad = info_ciudad.get('nombre', '<sin nombre>')
            text = f"{i}. Código: {cod_ciudad}   Nombre: {nombre_ciudad}"
            cuerpo.append(Paragraph(text, styles['Normal']))
            cuerpo.append(Spacer(1, 6))
    doc.build(cuerpo)
    mensaje_confirma = f"PDF de ciudades generado correctamente en: {nombre}"
    print(mensaje_confirma)
    return mensaje_confirma
def reporte_restaurantes(dict, cod_pais, cod_ciudad, nombre):
    if cod_pais not in dict:
        raise ValueError(f"Código de país '{cod_pais}' no encontrado en los datos.")
    info_paises = dict[cod_pais]
    nombre_pais = info_paises.get('nombre', '<sin nombre>')
    ciudades    = info_paises.get('ciudades', {})
    if cod_ciudad not in ciudades:
        raise ValueError(f"Código de ciudad '{cod_ciudad}' no encontrado para el país {cod_pais}.")
    info_ciudad     = ciudades[cod_ciudad]
    nombre_ciudad   = info_ciudad.get('nombre', '<sin nombre>')
    restaurantes    = info_ciudad.get('restaurantes', {})
    documento=SimpleDocTemplate(nombre, pagesize=LETTER)
    estilo=getSampleStyleSheet()
    cuerpo=[]
    cuerpo.append(Paragraph(f"Reporte de Restaurantes - {nombre_ciudad} ({cod_ciudad}) - {nombre_pais} ({cod_pais})",
                           estilo['Title']))
    cuerpo.append(Spacer(1, 12))
    if not restaurantes:
        cuerpo.append(Paragraph("<i>No hay restaurantes registrados para esta ciudad.</i>", estilo['Normal']))
        cuerpo.append(Spacer(1, 6))
    else:
        for i, (cod_rest, info_rest) in enumerate(restaurantes.items(), start=1):
            nombre_rest = info_rest.get('nombre', '<sin nombre>')
            text = f"{i}. Código: {cod_rest}   Nombre: {nombre_rest}"
            cuerpo.append(Paragraph(text, estilo['Normal']))
            cuerpo.append(Spacer(1, 6))
    documento.build(cuerpo)
    mensaje_confirma = f"PDF de restaurantes generado correctamente en: {nombre}"
    print(mensaje_confirma)
    return mensaje_confirma
def reporte_clientes(dict, nombre):
    documento = SimpleDocTemplate(nombre, pagesize=LETTER)
    estilo = getSampleStyleSheet()
    cuerpo = []
    cuerpo.append(Paragraph("Reporte de Clientes", estilo['Title']))
    cuerpo.append(Spacer(1, 12))
    if not dict:
        cuerpo.append(Paragraph("<i>No hay clientes registrados.</i>", estilo['Normal']))
        cuerpo.append(Spacer(1, 6))
    else:
        for i, (cedula, nombre_cliente) in enumerate(dict.items(), start=1):
            text = f"{i}. Código: {cedula}   Nombre: {nombre_cliente}"
            cuerpo.append(Paragraph(text, estilo['Normal']))
            cuerpo.append(Spacer(1, 6))
    documento.build(cuerpo)
    mensaje_confirma = f"PDF de clientes generado correctamente en: {nombre}"
    print(mensaje_confirma)
    return mensaje_confirma
def reporte_compras_cliente(cedula, facturas_r, reporte_ruta):
    compras=[]
    try:
        with open(facturas_r, 'r', encoding='utf-8') as f:
            for linea in f:
                campos = linea.strip().split(';')
                if len(campos) >= 8 and campos[0] == cedula:
                    compras.append(campos)
    except FileNotFoundError:
        print(f"Archivo de facturas no encontrado: {facturas_r}. Tal vez no existan facturas aun.")
        return False
    if not compras:
        print(f"No existe la cédula {cedula} en el archivo de facturas.")
        return False
    cuenta = len(compras)
    #generar pdf
    doc= SimpleDocTemplate(reporte_ruta, pagesize=LETTER)
    estilo= getSampleStyleSheet()
    cuerpo= []
    cuerpo.append(Paragraph(f"Reporte de Compras - Cliente {cedula}", estilo['Title']))
    cuerpo.append(Spacer(1, 12))
    cuerpo.append(Paragraph(f"Total de compras realizadas: {cuenta}", estilo['Normal']))
    cuerpo.append(Spacer(1, 12))
    #compras
    if cuenta > 0:
        cuerpo.append(Paragraph("Detalle de compras:", estilo['Heading2']))
        cuerpo.append(Spacer(1, 6))
        for i, compra in enumerate(compras, start=1):
            # campos: cedula,pais,ciudad,restaurante,menu,producto,cantidad,precio
            texto = (
                f"{i}. País: {compra[1]}, Ciudad: {compra[2]}, Restaurante: {compra[3]}, "
                f"Menú: {compra[4]}, Producto: {compra[5]}, Cantidad: {compra[6]}, Precio: {compra[7]}"
            )
            cuerpo.append(Paragraph(texto, estilo['Normal']))
            cuerpo.append(Spacer(1, 6))
    else:
        cuerpo.append(Paragraph("<i>No se encontraron compras para este cliente.</i>", estilo['Normal']))
    doc.build(cuerpo)
    mensaje = f"PDF de reporte de compras guardado en: {reporte_ruta}"
    print(mensaje)
    return True
def reporte_todas_compras(ruta_pdf, archivo_facturas="facturas.txt"):
    documento = SimpleDocTemplate(ruta_pdf, pagesize=LETTER)
    estilo= getSampleStyleSheet()
    cuerpo= []
    cuerpo.append(Paragraph("Reporte de Todas las Compras", estilo['Title']))
    cuerpo.append(Spacer(1, 12))

    try:
        with open(archivo_facturas, "r") as f:
            lineas = [l.strip() for l in f if l.strip()]
    except FileNotFoundError:
        print(f"Archivo no encontrado: {archivo_facturas}")
        return False

    if not lineas:
        cuerpo.append(Paragraph("<i>No hay registros de compras.</i>", estilo['Normal']))
        cuerpo.append(Spacer(1, 6))
    else:
        for i, linea in enumerate(lineas, start=1):
            partes = linea.split(";")
            if len(partes) < 10:
                continue
            cedula, pais, ciudad, rest, menu, prod, cant_str, precio_str, pago, servicio = partes[:10]
            try:
                cantidad     = int(cant_str)
                precio_unit  = float(precio_str)
            except ValueError:
                continue
            total_field = None
            if len(partes) >= 11:
                try:
                    total_field = float(partes[10])
                except ValueError:
                    total_field = None
            total = total_field if total_field is not None else cantidad * precio_unit

            metodo_pago = "Efectivo" if pago == "1" else "Tarjeta"

            texto = (
                f"{i}. Cédula: {cedula}   País: {pais}   Ciudad: {ciudad}   "
                f"Restaurante: {rest}   Menú: {menu}   Producto: {prod}   "
                f"Cantidad: {cantidad}   Precio unit.: {precio_unit:.2f}   "
                f"Método pago: {metodo_pago}   Servicio: {servicio}   "
                f"Total: {total:.2f}"
            )
            cuerpo.append(Paragraph(texto, estilo['Normal']))
            cuerpo.append(Spacer(1, 6))
    # Construcción del PDF
    documento.build(cuerpo)
    mensaje = f"PDF de reporte de todas las compras generado en: {ruta_pdf}"
    print(mensaje)
    return mensaje
def reporte_rest_mas(ruta):

    if not total_restaurante_busquedas:
        print("No hay búsquedas de restaurantes registradas.")
        return False
    top_rest = max(total_restaurante_busquedas, key=total_restaurante_busquedas.get)
    count = total_restaurante_busquedas[top_rest]

    doc = SimpleDocTemplate(ruta, pagesize=LETTER)
    styles = getSampleStyleSheet()
    cuerpo = []
    cuerpo.append(Paragraph(f"Restaurante más buscado: {top_rest}", styles['Title']))
    cuerpo.append(Spacer(1, 12))
    cuerpo.append(Paragraph(f"Veces buscado: {count}", styles['Normal']))
    doc.build(cuerpo)
    print(f"PDF de restaurante más buscado generado en: {ruta}")
    return True
def reporte_menu_mas(ruta):
    if not total_menu_busquedas:
        print("No hay búsquedas de menús registradas.")
        return False
    top_menu = max(total_menu_busquedas, key=total_menu_busquedas.get)
    cuenta = total_menu_busquedas[top_menu]
    doc=SimpleDocTemplate(ruta, pagesize=LETTER)
    styles=getSampleStyleSheet()
    cuerpo=[]
    cuerpo.append(Paragraph(f"Menú más buscado: {top_menu}", styles['Title']))
    cuerpo.append(Spacer(1, 12))
    cuerpo.append(Paragraph(f"Veces buscado: {cuenta}", styles['Normal']))
    doc.build(cuerpo)
    print(f"PDF de menú más buscado generado en: {ruta}")
    return True
def reporte_producto_mas(ruta):
    if not total_producto_busquedas:
        print("No hay búsquedas de productos registradas.")
        return False
    top_prod = max(total_producto_busquedas, key=total_producto_busquedas.get)
    count=total_producto_busquedas[top_prod]
    doc=SimpleDocTemplate(ruta, pagesize=LETTER)
    styles=getSampleStyleSheet()
    cuerpo=[]
    cuerpo.append(Paragraph(f"Producto más buscado: {top_prod}", styles['Title']))
    cuerpo.append(Spacer(1, 12))
    cuerpo.append(Paragraph(f"Veces buscado: {count}", styles['Normal']))
    doc.build(cuerpo)
    print(f"PDF de producto más buscado generado en: {ruta}")
    return True
def reporte_factura_precio_extremo(ruta_pdf, archivo_facturas="facturas.txt", mayor=False):
    total_extremo = None
    factura_extremo = None
    with open(archivo_facturas, "r") as f:
        for linea in f:
            partes = linea.strip().split(";")
            if len(partes) < 11:
                continue
            try:
                total = float(partes[-1])
            except ValueError:
                continue

            if total_extremo is None:
                total_extremo = total
                factura_extremo = partes
            else:
                if mayor and total > total_extremo:
                    total_extremo = total
                    factura_extremo = partes
                elif not mayor and total < total_extremo:
                    total_extremo = total
                    factura_extremo = partes
    if factura_extremo is None:
        print("No se encontró ninguna factura válida en el archivo.")
        return False
    (
        cedula,
        cod_pais,
        cod_ciudad,
        cod_rest,
        cod_menu,
        cod_prod,
        cantidad,
        precio_uni,
        pago,
        servicio,
        _
    ) = factura_extremo
    metodo_pago = "Efectivo" if pago == "1" else "Tarjeta"
    total = total_extremo
    titulo = "Factura de MAYOR precio" if mayor else "Factura de MENOR precio"

    # Construir PDF
    doc    = SimpleDocTemplate(ruta_pdf, pagesize=LETTER)
    styles = getSampleStyleSheet()
    cuerpo = []
    cuerpo.append(Paragraph(titulo, styles["Title"]))
    cuerpo.append(Spacer(1, 12))
    cuerpo.append(Paragraph(f"Cédula:          {cedula}", styles["Normal"]))
    cuerpo.append(Paragraph(f"País:            {cod_pais}", styles["Normal"]))
    cuerpo.append(Paragraph(f"Ciudad:          {cod_ciudad}", styles["Normal"]))
    cuerpo.append(Paragraph(f"Restaurante:     {cod_rest}", styles["Normal"]))
    cuerpo.append(Paragraph(f"Menú:            {cod_menu}", styles["Normal"]))
    cuerpo.append(Paragraph(f"Producto:        {cod_prod}", styles["Normal"]))
    cuerpo.append(Paragraph(f"Cantidad:        {cantidad}", styles["Normal"]))
    cuerpo.append(Paragraph(f"Precio unitario: {float(precio_uni):.2f}", styles["Normal"]))
    cuerpo.append(Paragraph(f"Método de pago:  {metodo_pago}", styles["Normal"]))
    cuerpo.append(Paragraph(f"Servicio:        {servicio}", styles["Normal"]))
    cuerpo.append(Paragraph(f"Total factura:   {total:.2f}", styles["Normal"]))

    doc.build(cuerpo)

    tipo = "mayor" if mayor else "menor"
    print(f"PDF de factura de {tipo} precio generado en: {ruta_pdf}")
    return True
def reporte_precio_producto(dic,cod_pais,cod_ciudad,cod_rest,cod_menu,cod_prod,nombre_pdf,stock=False):
    pais = dic.get(cod_pais)
    if not pais:
        print(f"Código de país '{cod_pais}' no encontrado.")
        return False
    ciudad = pais.get('ciudades', {}).get(cod_ciudad)
    if not ciudad:
        print(f"Código de ciudad '{cod_ciudad}' no encontrado.")
        return False
    rest = ciudad.get('restaurantes', {}).get(cod_rest)
    if not rest:
        print(f"Código de restaurante '{cod_rest}' no encontrado.")
        return False
    menu = rest.get('menus', {}).get(cod_menu)
    if not menu:
        print(f"Código de menú '{cod_menu}' no encontrado.")
        return False
    prod = menu.get('productos', {}).get(cod_prod)
    if not prod:
        print(f"Código de producto '{cod_prod}' no encontrado.")
        return False

    nombre_prod = prod.get('nombre', '<sin nombre>')
    precio_unit = prod.get('precio', 0.0)
    stock_qty   = prod.get('stock', 0)
    # Crear el PDF
    doc    = SimpleDocTemplate(nombre_pdf, pagesize=LETTER)
    styles = getSampleStyleSheet()
    cuerpo = []
    if stock:
        cuerpo.append(Paragraph(f"Reporte de Stock - {nombre_prod} ({cod_prod})", styles['Title']))
        cuerpo.append(Spacer(1, 12))
        cuerpo.append(Paragraph(f"Nombre:        {nombre_prod}", styles['Normal']))
        cuerpo.append(Paragraph(f"Stock disponible: {stock_qty}", styles['Normal']))
    else:
        cuerpo.append(Paragraph(f"Reporte de Producto - {nombre_prod} ({cod_prod})", styles['Title']))
        cuerpo.append(Spacer(1, 12))
        cuerpo.append(Paragraph(f"Precio unitario: {precio_unit:.2f}", styles['Normal']))
        cuerpo.append(Paragraph(f"Stock disponible: {stock_qty}", styles['Normal']))

    doc.build(cuerpo)

    modo = "stock" if stock else "completo"
    print(f"PDF de reporte ({modo}) generado correctamente en: {nombre_pdf}")
    return True
def reporte_descuentos(data_dict, nombre_pdf):
    documento = SimpleDocTemplate(nombre_pdf, pagesize=LETTER)
    estilo = getSampleStyleSheet()
    cuerpo = []

    cuerpo.append(Paragraph("Reporte de Descuentos Aplicados", estilo['Title']))
    cuerpo.append(Spacer(1, 12))

    for i, (descripcion, descuento) in enumerate(data_dict.items(), start=1):
        texto = f"{i}. {descripcion}: {descuento * 100:.0f}%"
        cuerpo.append(Paragraph(texto, estilo['Normal']))
        cuerpo.append(Spacer(1, 6))

    documento.build(cuerpo)

    mensaje = f"PDF generado correctamente en: {nombre_pdf}"
    print(mensaje)
    return mensaje
#______________________________________________________________________________________________________________________#
# ================== FUNCIONES BASE ==================
def ventana_login():
    ventana = tk.Tk()
    ventana.geometry('800x600')
    ventana.title("Sistema de Restaurante")
    ventana.resizable(True, True)

    # Frame principal
    frame_principal = Frame(ventana, padx=20, pady=20)
    frame_principal.pack(expand=True, fill='both')
    Label(frame_principal, text="Inicio de Sesión", font=('Arial', 18)).pack(pady=20)

    # Frame para administradores
    frame_admin = Frame(frame_principal, padx=10, pady=10, relief='groove', borderwidth=2)
    frame_admin.pack(pady=20, fill='x')

    Label(frame_admin, text="Acceso Administrador", font=('Arial', 14)).pack(pady=10)

    # Entrada para cédula de admin
    Label(frame_admin, text="Cédula:").pack()
    entrada_cedula_admin = Entry(frame_admin)
    entrada_cedula_admin.pack(pady=5)

    def verificar_admin():
        cedula = entrada_cedula_admin.get().strip()
        if not cedula:
            messagebox.showerror("Error", "Por favor ingrese una cédula")
            return
        if cedula in admin:
            messagebox.showinfo("Éxito", f"Bienvenido administrador {admin[cedula]}")
            ventana.destroy()
            ventana_principal()
        else:
            messagebox.showerror("Error", "Cédula no registrada como administrador")

    Button(frame_admin, text="Ingresar", command=verificar_admin).pack(pady=10)

    # Frame para clientes
    frame_cliente = Frame(frame_principal, padx=10, pady=10, relief='groove', borderwidth=2)
    frame_cliente.pack(pady=20, fill='x')

    Label(frame_cliente, text="Acceso Cliente", font=('Arial', 14)).pack(pady=10)

    # Entrada para cédula de cliente
    Label(frame_cliente, text="Cédula:").pack()
    entrada_cedula_cliente = Entry(frame_cliente)
    entrada_cedula_cliente.pack(pady=5)

    def verificar_cliente():
        cedula = entrada_cedula_cliente.get().strip()
        if not cedula:
            messagebox.showerror("Error", "Por favor ingrese una cédula")
            return
        if cedula in cli:
            messagebox.showinfo("Éxito", f"Bienvenido {cli[cedula]}")
            ventana.destroy()
            ventana_usuario()
        else:
            messagebox.showerror("Error", "Cédula no registrada como cliente")

    Button(frame_cliente, text="Ingresar", command=verificar_cliente).pack(pady=10)

    ventana.mainloop()
def regresar_login(ventana):
    ventana.destroy()
    ventana_login()
#FUNCIONES GLOBALES
def limpiar_frame():
    for widget in frame_dinamico.winfo_children():
        widget.destroy()
def formulario_insertar_pais():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Insertar País", font=('Arial', 16)).pack(pady=10)
    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_codigo = tk.Entry(frame_dinamico)
    entry_codigo.pack()
    tk.Label(frame_dinamico, text="Nombre de País:").pack()
    entry_nombre = tk.Entry(frame_dinamico)
    entry_nombre.pack()

    def guardar():
        codigo = entry_codigo.get().strip()
        nombre = entry_nombre.get().strip()
        if codigo and nombre:
            resultado = insertar_pais_manual(codigo, nombre)  # Nueva función adaptada
            if resultado:
                messagebox.showinfo("Éxito", "País insertado correctamente")
                limpiar_frame()
        else:
            messagebox.showerror("Error", "Complete todos los campos.")

    tk.Button(frame_dinamico, text="Guardar", command=guardar).pack(pady=10)
def insertar_pais_manual(codigo, nombre):
    return insertar_en_diccionario([codigo, nombre], nivel=1)
def formulario_insertar_ciudad():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Insertar Ciudad", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_codigo_pais = tk.Entry(frame_dinamico)
    entry_codigo_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_codigo_ciudad = tk.Entry(frame_dinamico)
    entry_codigo_ciudad.pack()

    tk.Label(frame_dinamico, text="Nombre de Ciudad:").pack()
    entry_nombre_ciudad = tk.Entry(frame_dinamico)
    entry_nombre_ciudad.pack()

    def guardar():
        codigo_pais = entry_codigo_pais.get().strip()
        codigo_ciudad = entry_codigo_ciudad.get().strip()
        nombre_ciudad = entry_nombre_ciudad.get().strip()
        if codigo_pais and codigo_ciudad and nombre_ciudad:
            resultado = insertar_ciudad_manual(codigo_pais, codigo_ciudad, nombre_ciudad)
            if resultado:
                messagebox.showinfo("Éxito", "Ciudad insertada correctamente")
                limpiar_frame()
        else:
            messagebox.showerror("Error", "Complete todos los campos.")

    tk.Button(frame_dinamico, text="Guardar", command=guardar).pack(pady=10)

    def insertar_ciudad_manual(codigo_pais, codigo_ciudad, nombre_ciudad):
        return insertar_en_diccionario([codigo_pais, codigo_ciudad, nombre_ciudad], nivel=2)
def formulario_insertar_restaurante():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Insertar Restaurante", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_codigo_pais = tk.Entry(frame_dinamico)
    entry_codigo_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_codigo_ciudad = tk.Entry(frame_dinamico)
    entry_codigo_ciudad.pack()

    tk.Label(frame_dinamico, text="Código de Restaurante:").pack()
    entry_codigo_rest = tk.Entry(frame_dinamico)
    entry_codigo_rest.pack()

    tk.Label(frame_dinamico, text="Nombre de Restaurante:").pack()
    entry_nombre_rest = tk.Entry(frame_dinamico)
    entry_nombre_rest.pack()

    def guardar():
        cod_pais = entry_codigo_pais.get().strip()
        cod_ciudad = entry_codigo_ciudad.get().strip()
        cod_rest = entry_codigo_rest.get().strip()
        nombre_rest = entry_nombre_rest.get().strip()

        if cod_pais and cod_ciudad and cod_rest and nombre_rest:
            resultado = insertar_restaurante_manual(cod_pais, cod_ciudad, cod_rest, nombre_rest)
            if resultado:
                messagebox.showinfo("Éxito", "Restaurante insertado correctamente")
                limpiar_frame()
        else:
            messagebox.showerror("Error", "Complete todos los campos.")

    tk.Button(frame_dinamico, text="Guardar", command=guardar).pack(pady=10)
def insertar_restaurante_manual(cod_pais, cod_ciudad, cod_rest, nombre_rest):
    return insertar_en_diccionario([cod_pais, cod_ciudad, cod_rest, nombre_rest], nivel=3)
def formulario_insertar_menu():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Insertar Menú", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_codigo_pais = tk.Entry(frame_dinamico)
    entry_codigo_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_codigo_ciudad = tk.Entry(frame_dinamico)
    entry_codigo_ciudad.pack()

    tk.Label(frame_dinamico, text="Código de Restaurante:").pack()
    entry_codigo_rest = tk.Entry(frame_dinamico)
    entry_codigo_rest.pack()

    tk.Label(frame_dinamico, text="Código de Menú:").pack()
    entry_codigo_menu = tk.Entry(frame_dinamico)
    entry_codigo_menu.pack()

    tk.Label(frame_dinamico, text="Nombre de Menú:").pack()
    entry_nombre_menu = tk.Entry(frame_dinamico)
    entry_nombre_menu.pack()

    def guardar():
        cod_pais = entry_codigo_pais.get().strip()
        cod_ciudad = entry_codigo_ciudad.get().strip()
        cod_rest = entry_codigo_rest.get().strip()
        cod_menu = entry_codigo_menu.get().strip()
        nombre_menu = entry_nombre_menu.get().strip()

        if cod_pais and cod_ciudad and cod_rest and cod_menu and nombre_menu:
            resultado = insertar_menu_manual(cod_pais, cod_ciudad, cod_rest, cod_menu, nombre_menu)
            if resultado:
                messagebox.showinfo("Éxito", "Menú insertado correctamente")
                limpiar_frame()
        else:
            messagebox.showerror("Error", "Complete todos los campos.")

    tk.Button(frame_dinamico, text="Guardar", command=guardar).pack(pady=10)
def insertar_menu_manual(cod_pais, cod_ciudad, cod_rest, cod_menu, nombre_menu):
    return insertar_en_diccionario([cod_pais, cod_ciudad, cod_rest, cod_menu, nombre_menu], nivel=4)
def formulario_insertar_producto():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Insertar Producto", font=('Arial', 16)).pack(pady=10)

    # Entradas necesarias
    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_codigo_pais = tk.Entry(frame_dinamico)
    entry_codigo_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_codigo_ciudad = tk.Entry(frame_dinamico)
    entry_codigo_ciudad.pack()

    tk.Label(frame_dinamico, text="Código de Restaurante:").pack()
    entry_codigo_rest = tk.Entry(frame_dinamico)
    entry_codigo_rest.pack()

    tk.Label(frame_dinamico, text="Código de Menú:").pack()
    entry_codigo_menu = tk.Entry(frame_dinamico)
    entry_codigo_menu.pack()

    tk.Label(frame_dinamico, text="Código de Producto:").pack()
    entry_codigo_prod = tk.Entry(frame_dinamico)
    entry_codigo_prod.pack()

    tk.Label(frame_dinamico, text="Nombre de Producto:").pack()
    entry_nombre_prod = tk.Entry(frame_dinamico)
    entry_nombre_prod.pack()

    tk.Label(frame_dinamico, text="Calorías:").pack()
    entry_calorias = tk.Entry(frame_dinamico)
    entry_calorias.pack()

    tk.Label(frame_dinamico, text="Precio:").pack()
    entry_precio = tk.Entry(frame_dinamico)
    entry_precio.pack()

    tk.Label(frame_dinamico, text="Stock:").pack()
    entry_stock = tk.Entry(frame_dinamico)
    entry_stock.pack()

    def guardar():
        cod_pais = entry_codigo_pais.get().strip()
        cod_ciudad = entry_codigo_ciudad.get().strip()
        cod_rest = entry_codigo_rest.get().strip()
        cod_menu = entry_codigo_menu.get().strip()
        cod_prod = entry_codigo_prod.get().strip()
        nombre_prod = entry_nombre_prod.get().strip()
        calorias = entry_calorias.get().strip()
        precio = entry_precio.get().strip()
        stock = entry_stock.get().strip()

        if all([cod_pais, cod_ciudad, cod_rest, cod_menu, cod_prod, nombre_prod, calorias, precio, stock]):
            resultado = insertar_producto_manual(cod_pais, cod_ciudad, cod_rest, cod_menu, cod_prod, nombre_prod,
                                                 calorias, precio, stock)
            if resultado:
                messagebox.showinfo("Éxito", "Producto insertado correctamente")
                limpiar_frame()
        else:
            messagebox.showerror("Error", "Complete todos los campos.")

    tk.Button(frame_dinamico, text="Guardar", command=guardar).pack(pady=10)
def insertar_producto_manual(cod_pais, cod_ciudad, cod_rest, cod_menu, cod_prod, nombre_prod, calorias, precio,
                             stock):
    return insertar_en_diccionario(
        [cod_pais, cod_ciudad, cod_rest, cod_menu, cod_prod, nombre_prod, calorias, precio, stock], nivel=5)
def formulario_insertar_cliente():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Insertar Cliente", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Cédula del Cliente:").pack()
    entry_cedula = tk.Entry(frame_dinamico)
    entry_cedula.pack()

    tk.Label(frame_dinamico, text="Nombre del Cliente:").pack()
    entry_nombre = tk.Entry(frame_dinamico)
    entry_nombre.pack()

    def guardar():
        cedula = entry_cedula.get().strip()
        nombre = entry_nombre.get().strip()

        if cedula and nombre:
            resultado = insertar_cliente_manual(cedula, nombre)
            if resultado:
                messagebox.showinfo("Éxito", "Cliente insertado correctamente")
                limpiar_frame()
            else:
                messagebox.showerror("Error", "No se pudo insertar el cliente (ya existe o error).")
        else:
            messagebox.showerror("Error", "Complete todos los campos.")

    tk.Button(frame_dinamico, text="Guardar", command=guardar).pack(pady=10)
def insertar_cliente_manual(cedula, nombre):
    return insertar_cliente(cli, cedula, nombre)
def formulario_insertar_administrador():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Insertar Administrador", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Cédula del Administrador:").pack()
    entry_cedula = tk.Entry(frame_dinamico)
    entry_cedula.pack()

    tk.Label(frame_dinamico, text="Nombre del Administrador:").pack()
    entry_nombre = tk.Entry(frame_dinamico)
    entry_nombre.pack()

    def guardar():
        cedula = entry_cedula.get().strip()
        nombre = entry_nombre.get().strip()

        if cedula and nombre:
            resultado = insertar_administrador_manual(cedula, nombre)
            if resultado:
                messagebox.showinfo("Éxito", "Administrador insertado correctamente")
                limpiar_frame()
            else:
                messagebox.showerror("Error", "El administrador ya existe.")
        else:
            messagebox.showerror("Error", "Complete todos los campos.")

    tk.Button(frame_dinamico, text="Guardar", command=guardar).pack(pady=10)
def insertar_administrador_manual(cedula, nombre):
    if cedula in admin:
        return False
    admin[cedula] = nombre
    return True
#FUNCIONES DE BUSQUEDA
def buscar(cod_pais, cod_ciudad=None, cod_rest=None, cod_menu=None, cod_prod=None):
    return buscar_elemento(dic, cod_pais, cod_ciudad, cod_rest, cod_menu, cod_prod)
def formulario_consultar_pais():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Consultar País", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_codigo_pais = tk.Entry(frame_dinamico)
    entry_codigo_pais.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def buscar_pais():
        cod_pais = entry_codigo_pais.get().strip()
        if not cod_pais:
            messagebox.showerror("Error", "Ingrese el código del país.")
            return

        if buscar(cod_pais):
            nombre_pais = dic[cod_pais]['nombre']
            resultado_label.config(text=f"País encontrado: {cod_pais} → {nombre_pais}", fg="green")
        else:
            resultado_label.config(text=f"El país {cod_pais} no existe.", fg="red")

    tk.Button(frame_dinamico, text="Buscar", command=buscar_pais).pack(pady=10)
def formulario_consultar_ciudad():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Consultar Ciudad", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_codigo_pais = tk.Entry(frame_dinamico)
    entry_codigo_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_codigo_ciudad = tk.Entry(frame_dinamico)
    entry_codigo_ciudad.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def buscar_ciudad():
        cod_pais = entry_codigo_pais.get().strip()
        cod_ciudad = entry_codigo_ciudad.get().strip()
        if not cod_pais or not cod_ciudad:
            messagebox.showerror("Error", "Ingrese ambos códigos: País y Ciudad.")
            return

        if buscar(cod_pais, cod_ciudad):
            nombre_ciudad = dic[cod_pais]['ciudades'][cod_ciudad]['nombre']
            resultado_label.config(text=f"Ciudad encontrada: {cod_ciudad} → {nombre_ciudad}", fg="green")
        else:
            resultado_label.config(text=f"La ciudad {cod_ciudad} no existe en el país {cod_pais}.", fg="red")

    tk.Button(frame_dinamico, text="Buscar", command=buscar_ciudad).pack(pady=10)
def formulario_consultar_restaurante():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Consultar Restaurante", font=('Arial', 16)).pack(pady=10)

    # Entradas
    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_pais = tk.Entry(frame_dinamico)
    entry_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_ciudad = tk.Entry(frame_dinamico)
    entry_ciudad.pack()

    tk.Label(frame_dinamico, text="Código de Restaurante:").pack()
    entry_rest = tk.Entry(frame_dinamico)
    entry_rest.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def buscar_rest():
        cp = entry_pais.get().strip()
        cc = entry_ciudad.get().strip()
        cr = entry_rest.get().strip()
        if not cp or not cc or not cr:
            messagebox.showerror("Error", "Ingrese País, Ciudad y Restaurante.")
            return

        if buscar(cp, cc, cr):
            nombre = dic[cp]['ciudades'][cc]['restaurantes'][cr]['nombre']
            resultado_label.config(text=f"Restaurante encontrado: {cr} → {nombre}", fg="green")
        else:
            resultado_label.config(text=f"Restaurante {cr} no encontrado.", fg="red")

    tk.Button(frame_dinamico, text="Buscar", command=buscar_rest).pack(pady=10)
def formulario_consultar_menu():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Consultar Menú", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_pais = tk.Entry(frame_dinamico)
    entry_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_ciudad = tk.Entry(frame_dinamico)
    entry_ciudad.pack()

    tk.Label(frame_dinamico, text="Código de Restaurante:").pack()
    entry_rest = tk.Entry(frame_dinamico)
    entry_rest.pack()

    tk.Label(frame_dinamico, text="Código de Menú:").pack()
    entry_menu = tk.Entry(frame_dinamico)
    entry_menu.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def buscar_menu_():
        cp = entry_pais.get().strip()
        cc = entry_ciudad.get().strip()
        cr = entry_rest.get().strip()
        cm = entry_menu.get().strip()
        if not cp or not cc or not cr or not cm:
            messagebox.showerror("Error", "Ingrese País, Ciudad, Restaurante y Menú.")
            return

        if buscar(cp, cc, cr, cm):
            nombre = dic[cp]['ciudades'][cc]['restaurantes'][cr]['menus'][cm]['nombre']
            resultado_label.config(text=f"Menú encontrado: {cm} → {nombre}", fg="green")
        else:
            resultado_label.config(text=f"Menú {cm} no encontrado.", fg="red")

    tk.Button(frame_dinamico, text="Buscar", command=buscar_menu_).pack(pady=10)
def formulario_consultar_producto():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Consultar Producto", font=('Arial', 16)).pack(pady=10)

    # Entradas
    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_pais = tk.Entry(frame_dinamico)
    entry_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_ciudad = tk.Entry(frame_dinamico)
    entry_ciudad.pack()

    tk.Label(frame_dinamico, text="Código de Restaurante:").pack()
    entry_rest = tk.Entry(frame_dinamico)
    entry_rest.pack()

    tk.Label(frame_dinamico, text="Código de Menú:").pack()
    entry_menu = tk.Entry(frame_dinamico)
    entry_menu.pack()

    tk.Label(frame_dinamico, text="Código de Producto:").pack()
    entry_prod = tk.Entry(frame_dinamico)
    entry_prod.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def buscar_prod():
        cp = entry_pais.get().strip()
        cc = entry_ciudad.get().strip()
        cr = entry_rest.get().strip()
        cm = entry_menu.get().strip()
        cprod = entry_prod.get().strip()

        if not all([cp, cc, cr, cm, cprod]):
            messagebox.showerror("Error", "Ingrese País, Ciudad, Restaurante, Menú y Producto.")
            return

        if buscar(cp, cc, cr, cm, cprod):
            nombre = dic[cp]['ciudades'][cc]['restaurantes'][cr]['menus'][cm]['productos'][cprod]['nombre']
            resultado_label.config(text=f"Producto encontrado: {cprod} → {nombre}", fg="green")
        else:
            resultado_label.config(text=f"Producto {cprod} no encontrado.", fg="red")

    tk.Button(frame_dinamico, text="Buscar", command=buscar_prod).pack(pady=10)
def formulario_consultar_cliente():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Consultar Cliente", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Cédula del Cliente:").pack()
    entry_cedula = tk.Entry(frame_dinamico)
    entry_cedula.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def buscar_cli_():
        cedula = entry_cedula.get().strip()
        if not cedula:
            messagebox.showerror("Error", "Ingrese la cédula del cliente.")
            return

        if cedula in cli:
            nombre = cli[cedula]
            resultado_label.config(text=f"Cliente encontrado: {cedula} → {nombre}", fg="green")
        else:
            resultado_label.config(text=f"Cliente {cedula} no encontrado.", fg="red")

    tk.Button(frame_dinamico, text="Buscar", command=buscar_cli_).pack(pady=10)
def formulario_consultar_administrador():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Consultar Administrador", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Cédula del Administrador:").pack()
    entry_cedula = tk.Entry(frame_dinamico)
    entry_cedula.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def buscar_admin_():
        cedula = entry_cedula.get().strip()
        if not cedula:
            messagebox.showerror("Error", "Ingrese la cédula del administrador.")
            return

        if cedula in admin:
            nombre = admin[cedula]
            resultado_label.config(text=f"Administrador encontrado: {cedula} → {nombre}", fg="green")
        else:
            resultado_label.config(text=f"Administrador {cedula} no encontrado.", fg="red")

    tk.Button(frame_dinamico, text="Buscar", command=buscar_admin_).pack(pady=10)
#FUNCIONES DE MODIFICAR
def formulario_modificar_pais():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Modificar País", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_codigo_pais = tk.Entry(frame_dinamico)
    entry_codigo_pais.pack()

    tk.Label(frame_dinamico, text="Nuevo Nombre de País:").pack()
    entry_nuevo_nombre = tk.Entry(frame_dinamico)
    entry_nuevo_nombre.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def modificar():
        cod_pais = entry_codigo_pais.get().strip()
        nuevo_nombre = entry_nuevo_nombre.get().strip()
        if not cod_pais or not nuevo_nombre:
            messagebox.showerror("Error", "Ingrese el código y el nuevo nombre del país.")
            return

        resultado = modificar_pais(cod_pais, nuevo_nombre)
        resultado_label.config(text=resultado, fg="green" if "modificado" in resultado else "red")

    tk.Button(frame_dinamico, text="Modificar", command=modificar).pack(pady=10)
def formulario_modificar_ciudad():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Modificar Ciudad", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_codigo_pais = tk.Entry(frame_dinamico)
    entry_codigo_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_codigo_ciudad = tk.Entry(frame_dinamico)
    entry_codigo_ciudad.pack()

    tk.Label(frame_dinamico, text="Nuevo Nombre de Ciudad:").pack()
    entry_nuevo_nombre = tk.Entry(frame_dinamico)
    entry_nuevo_nombre.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def modificar():
        cod_pais = entry_codigo_pais.get().strip()
        cod_ciudad = entry_codigo_ciudad.get().strip()
        nuevo_nombre = entry_nuevo_nombre.get().strip()
        if not cod_pais or not cod_ciudad or not nuevo_nombre:
            messagebox.showerror("Error", "Ingrese todos los campos: País, Ciudad y Nuevo Nombre.")
            return

        resultado = modificar_ciudad(cod_pais, cod_ciudad, nuevo_nombre)
        resultado_label.config(text=resultado, fg="green" if "modificada" in resultado else "red")

    tk.Button(frame_dinamico, text="Modificar", command=modificar).pack(pady=10)
def formulario_modificar_restaurante():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Modificar Restaurante", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_codigo_pais = tk.Entry(frame_dinamico)
    entry_codigo_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_codigo_ciudad = tk.Entry(frame_dinamico)
    entry_codigo_ciudad.pack()

    tk.Label(frame_dinamico, text="Código de Restaurante:").pack()
    entry_codigo_rest = tk.Entry(frame_dinamico)
    entry_codigo_rest.pack()

    tk.Label(frame_dinamico, text="Nuevo Nombre de Restaurante:").pack()
    entry_nuevo_nombre = tk.Entry(frame_dinamico)
    entry_nuevo_nombre.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def modificar():
        cod_pais = entry_codigo_pais.get().strip()
        cod_ciudad = entry_codigo_ciudad.get().strip()
        cod_rest = entry_codigo_rest.get().strip()
        nuevo_nombre = entry_nuevo_nombre.get().strip()
        if not all([cod_pais, cod_ciudad, cod_rest, nuevo_nombre]):
            messagebox.showerror("Error", "Ingrese todos los campos: País, Ciudad, Restaurante y Nuevo Nombre.")
            return

        resultado = modificar_restaurante(cod_pais, cod_ciudad, cod_rest, nuevo_nombre)
        resultado_label.config(text=resultado, fg="green" if "modificado" in resultado else "red")

    tk.Button(frame_dinamico, text="Modificar", command=modificar).pack(pady=10)
def formulario_modificar_menu():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Modificar Menú", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_codigo_pais = tk.Entry(frame_dinamico)
    entry_codigo_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_codigo_ciudad = tk.Entry(frame_dinamico)
    entry_codigo_ciudad.pack()

    tk.Label(frame_dinamico, text="Código de Restaurante:").pack()
    entry_codigo_rest = tk.Entry(frame_dinamico)
    entry_codigo_rest.pack()

    tk.Label(frame_dinamico, text="Código de Menú:").pack()
    entry_codigo_menu = tk.Entry(frame_dinamico)
    entry_codigo_menu.pack()

    tk.Label(frame_dinamico, text="Nuevo Nombre de Menú:").pack()
    entry_nuevo_nombre = tk.Entry(frame_dinamico)
    entry_nuevo_nombre.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def modificar():
        cod_pais = entry_codigo_pais.get().strip()
        cod_ciudad = entry_codigo_ciudad.get().strip()
        cod_rest = entry_codigo_rest.get().strip()
        cod_menu = entry_codigo_menu.get().strip()
        nuevo_nombre = entry_nuevo_nombre.get().strip()
        if not all([cod_pais, cod_ciudad, cod_rest, cod_menu, nuevo_nombre]):
            messagebox.showerror("Error", "Ingrese País, Ciudad, Restaurante, Menú y Nuevo Nombre.")
            return

        resultado = modificar_menu(cod_pais, cod_ciudad, cod_rest, cod_menu, nuevo_nombre)
        resultado_label.config(text=resultado, fg="green" if "modificado" in resultado else "red")

    tk.Button(frame_dinamico, text="Modificar", command=modificar).pack(pady=10)
def formulario_modificar_producto():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Modificar Producto", font=('Arial', 16)).pack(pady=10)

    # Entradas necesarias
    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_pais = tk.Entry(frame_dinamico)
    entry_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_ciudad = tk.Entry(frame_dinamico)
    entry_ciudad.pack()

    tk.Label(frame_dinamico, text="Código de Restaurante:").pack()
    entry_rest = tk.Entry(frame_dinamico)
    entry_rest.pack()

    tk.Label(frame_dinamico, text="Código de Menú:").pack()
    entry_menu = tk.Entry(frame_dinamico)
    entry_menu.pack()

    tk.Label(frame_dinamico, text="Código de Producto:").pack()
    entry_prod = tk.Entry(frame_dinamico)
    entry_prod.pack()

    tk.Label(frame_dinamico, text="Nuevo Nombre (opcional):").pack()
    entry_nombre = tk.Entry(frame_dinamico)
    entry_nombre.pack()

    tk.Label(frame_dinamico, text="Nuevas Calorías (opcional):").pack()
    entry_calorias = tk.Entry(frame_dinamico)
    entry_calorias.pack()

    tk.Label(frame_dinamico, text="Nuevo Precio (opcional):").pack()
    entry_precio = tk.Entry(frame_dinamico)
    entry_precio.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def modificar():
        cp = entry_pais.get().strip()
        cc = entry_ciudad.get().strip()
        cr = entry_rest.get().strip()
        cm = entry_menu.get().strip()
        cprod = entry_prod.get().strip()
        nombre = entry_nombre.get().strip() or None
        calorias = entry_calorias.get().strip()
        precio = entry_precio.get().strip()

        calorias = int(calorias) if calorias else None
        precio = float(precio) if precio else None

        if not all([cp, cc, cr, cm, cprod]):
            messagebox.showerror("Error", "Complete todos los códigos.")
            return

        resultado = modificar_producto(cp, cc, cr, cm, cprod, nombre, calorias, precio)
        resultado_label.config(text=resultado, fg="green" if "modificado" in resultado else "red")

    tk.Button(frame_dinamico, text="Modificar", command=modificar).pack(pady=10)
def formulario_modificar_cliente():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Modificar Cliente", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Cédula del Cliente:").pack()
    entry_cedula = tk.Entry(frame_dinamico)
    entry_cedula.pack()

    tk.Label(frame_dinamico, text="Nuevo Nombre:").pack()
    entry_nombre = tk.Entry(frame_dinamico)
    entry_nombre.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def modificar():
        cedula = entry_cedula.get().strip()
        nombre = entry_nombre.get().strip()
        if not cedula or not nombre:
            messagebox.showerror("Error", "Complete ambos campos.")
            return

        resultado = modificar_cliente(cedula, nombre)
        resultado_label.config(text=resultado, fg="green" if "modificado" in resultado else "red")

    tk.Button(frame_dinamico, text="Modificar", command=modificar).pack(pady=10)
def formulario_modificar_administrador():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Modificar Administrador", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Cédula del Administrador:").pack()
    entry_cedula = tk.Entry(frame_dinamico)
    entry_cedula.pack()

    tk.Label(frame_dinamico, text="Nuevo Nombre:").pack()
    entry_nombre = tk.Entry(frame_dinamico)
    entry_nombre.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def modificar():
        cedula = entry_cedula.get().strip()
        nombre = entry_nombre.get().strip()
        if not cedula or not nombre:
            messagebox.showerror("Error", "Complete ambos campos.")
            return

        if cedula in admin:
            admin[cedula] = nombre
            resultado_label.config(text=f"Administrador {cedula} modificado correctamente.", fg="green")
        else:
            resultado_label.config(text=f"Administrador {cedula} no encontrado.", fg="red")

    tk.Button(frame_dinamico, text="Modificar", command=modificar).pack(pady=10)
#FUNCIOONES DE ELIMINAR
def eliminar(tipo, *args):
    if tipo == "pais":
        return eliminar_pais(*args)
    elif tipo == "ciudad":
        return eliminar_ciudad(*args)
    elif tipo == "restaurante":
        return eliminar_restaurante(*args)
    elif tipo == "menu":
        return eliminar_menu(*args)
    elif tipo == "producto":
        return eliminar_producto(*args)
    elif tipo == "cliente":
        return eliminar_cliente(*args)
    elif tipo == "admin":
        cedula = args[0]
        if cedula in admin:
            del admin[cedula]
            return True
        else:
            return False
    else:
        return False
def formulario_eliminar_pais():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Eliminar País", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_pais = tk.Entry(frame_dinamico)
    entry_pais.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def eliminar_p():
        cod_pais = entry_pais.get().strip()
        if not cod_pais:
            messagebox.showerror("Error", "Ingrese el código del país.")
            return

        if eliminar("pais", cod_pais):
            resultado_label.config(text=f"País {cod_pais} eliminado correctamente.", fg="green")
        else:
            resultado_label.config(text=f"País {cod_pais} no encontrado.", fg="red")

    tk.Button(frame_dinamico, text="Eliminar", command=eliminar_p).pack(pady=10)
def formulario_eliminar_ciudad():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Eliminar Ciudad", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_pais = tk.Entry(frame_dinamico)
    entry_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_ciudad = tk.Entry(frame_dinamico)
    entry_ciudad.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def eliminar_c():
        cp = entry_pais.get().strip()
        cc = entry_ciudad.get().strip()
        if not cp or not cc:
            messagebox.showerror("Error", "Ingrese el código de país y ciudad.")
            return

        if eliminar("ciudad", cp, cc):
            resultado_label.config(text=f"Ciudad {cc} eliminada correctamente.", fg="green")
        else:
            resultado_label.config(text=f"Ciudad {cc} no encontrada.", fg="red")

    tk.Button(frame_dinamico, text="Eliminar", command=eliminar_c).pack(pady=10)
def formulario_eliminar_restaurante():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Eliminar Restaurante", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_pais = tk.Entry(frame_dinamico)
    entry_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_ciudad = tk.Entry(frame_dinamico)
    entry_ciudad.pack()

    tk.Label(frame_dinamico, text="Código de Restaurante:").pack()
    entry_rest = tk.Entry(frame_dinamico)
    entry_rest.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def eliminar_r():
        cp = entry_pais.get().strip()
        cc = entry_ciudad.get().strip()
        cr = entry_rest.get().strip()
        if not all([cp, cc, cr]):
            messagebox.showerror("Error", "Ingrese País, Ciudad y Restaurante.")
            return

        if eliminar("restaurante", cp, cc, cr):
            resultado_label.config(text=f"Restaurante {cr} eliminado correctamente.", fg="green")
        else:
            resultado_label.config(text=f"Restaurante {cr} no encontrado.", fg="red")

    tk.Button(frame_dinamico, text="Eliminar", command=eliminar_r).pack(pady=10)
def formulario_eliminar_menu():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Eliminar Menú", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_pais = tk.Entry(frame_dinamico)
    entry_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_ciudad = tk.Entry(frame_dinamico)
    entry_ciudad.pack()

    tk.Label(frame_dinamico, text="Código de Restaurante:").pack()
    entry_rest = tk.Entry(frame_dinamico)
    entry_rest.pack()

    tk.Label(frame_dinamico, text="Código de Menú:").pack()
    entry_menu = tk.Entry(frame_dinamico)
    entry_menu.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def eliminar_m():
        cp = entry_pais.get().strip()
        cc = entry_ciudad.get().strip()
        cr = entry_rest.get().strip()
        cm = entry_menu.get().strip()
        if not all([cp, cc, cr, cm]):
            messagebox.showerror("Error", "Ingrese País, Ciudad, Restaurante y Menú.")
            return

        if eliminar("menu", cp, cc, cr, cm):
            resultado_label.config(text=f"Menú {cm} eliminado correctamente.", fg="green")
        else:
            resultado_label.config(text=f"Menú {cm} no encontrado.", fg="red")

    tk.Button(frame_dinamico, text="Eliminar", command=eliminar_m).pack(pady=10)
def formulario_eliminar_producto():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Eliminar Producto", font=('Arial', 16)).pack(pady=10)

    # Entradas necesarias
    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_pais = tk.Entry(frame_dinamico)
    entry_pais.pack()

    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_ciudad = tk.Entry(frame_dinamico)
    entry_ciudad.pack()

    tk.Label(frame_dinamico, text="Código de Restaurante:").pack()
    entry_rest = tk.Entry(frame_dinamico)
    entry_rest.pack()

    tk.Label(frame_dinamico, text="Código de Menú:").pack()
    entry_menu = tk.Entry(frame_dinamico)
    entry_menu.pack()

    tk.Label(frame_dinamico, text="Código de Producto:").pack()
    entry_prod = tk.Entry(frame_dinamico)
    entry_prod.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def eliminar_p():
        cp = entry_pais.get().strip()
        cc = entry_ciudad.get().strip()
        cr = entry_rest.get().strip()
        cm = entry_menu.get().strip()
        cprod = entry_prod.get().strip()
        if not all([cp, cc, cr, cm, cprod]):
            messagebox.showerror("Error", "Ingrese todos los códigos: País, Ciudad, Restaurante, Menú y Producto.")
            return

        if eliminar("producto", cp, cc, cr, cm, cprod):
            resultado_label.config(text=f"Producto {cprod} eliminado correctamente.", fg="green")
        else:
            resultado_label.config(text=f"Producto {cprod} no encontrado.", fg="red")

    tk.Button(frame_dinamico, text="Eliminar", command=eliminar_p).pack(pady=10)
def formulario_eliminar_cliente():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Eliminar Cliente", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Cédula del Cliente:").pack()
    entry_cedula = tk.Entry(frame_dinamico)
    entry_cedula.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def eliminar_c():
        cedula = entry_cedula.get().strip()
        if not cedula:
            messagebox.showerror("Error", "Ingrese la cédula del cliente.")
            return

        if eliminar("cliente", cedula):
            resultado_label.config(text=f"Cliente {cedula} eliminado correctamente.", fg="green")
        else:
            resultado_label.config(text=f"Cliente {cedula} no encontrado.", fg="red")

    tk.Button(frame_dinamico, text="Eliminar", command=eliminar_c).pack(pady=10)
def formulario_eliminar_administrador():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Eliminar Administrador", font=('Arial', 16)).pack(pady=10)

    tk.Label(frame_dinamico, text="Cédula del Administrador:").pack()
    entry_cedula = tk.Entry(frame_dinamico)
    entry_cedula.pack()

    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def eliminar_a():
        cedula = entry_cedula.get().strip()
        if not cedula:
            messagebox.showerror("Error", "Ingrese la cédula del administrador.")
            return

        if eliminar("admin", cedula):
            resultado_label.config(text=f"Administrador {cedula} eliminado correctamente.", fg="green")
        else:
            resultado_label.config(text=f"Administrador {cedula} no encontrado.", fg="red")

    tk.Button(frame_dinamico, text="Eliminar", command=eliminar_a).pack(pady=10)
#FUNCION REGISTRO COMPRA
def formulario_registrar_compra():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Registrar Compra", font=('Arial', 16)).pack(pady=10)
    # Entradas necesarias
    tk.Label(frame_dinamico, text="Cédula del Cliente:").pack()
    entry_cedula = tk.Entry(frame_dinamico)
    entry_cedula.pack()

    tk.Label(frame_dinamico, text="Código de País:").pack()
    entry_pais = tk.Entry(frame_dinamico)
    entry_pais.pack()
    tk.Label(frame_dinamico, text="Código de Ciudad:").pack()
    entry_ciudad = tk.Entry(frame_dinamico)
    entry_ciudad.pack()

    tk.Label(frame_dinamico, text="Código de Restaurante:").pack()
    entry_rest = tk.Entry(frame_dinamico)
    entry_rest.pack()

    tk.Label(frame_dinamico, text="Código de Menú:").pack()
    entry_menu = tk.Entry(frame_dinamico)
    entry_menu.pack()

    tk.Label(frame_dinamico, text="Código de Producto:").pack()
    entry_prod = tk.Entry(frame_dinamico)
    entry_prod.pack()

    tk.Label(frame_dinamico, text="Cantidad:").pack()
    entry_cantidad = tk.Entry(frame_dinamico)
    entry_cantidad.pack()

    tk.Label(frame_dinamico, text="¿Para llevar? (s/n):").pack()
    entry_condicion = tk.Entry(frame_dinamico)
    entry_condicion.pack()

    tk.Label(frame_dinamico, text="Método de Pago (1=Efectivo, 2=Tarjeta):").pack()
    entry_pago = tk.Entry(frame_dinamico)
    entry_pago.pack()
    resultado_label = tk.Label(frame_dinamico, text="", fg="blue", font=("Arial", 12))
    resultado_label.pack(pady=10)
    def procesar_compra():
        ced = entry_cedula.get().strip()
        cp = entry_pais.get().strip()
        cc = entry_ciudad.get().strip()
        cr = entry_rest.get().strip()
        cm = entry_menu.get().strip()
        cprod = entry_prod.get().strip()
        cant = entry_cantidad.get().strip()
        cond = entry_condicion.get().strip().lower()
        pago = entry_pago.get().strip()
        if not all([ced, cp, cc, cr, cm, cprod, cant, cond, pago]):
            messagebox.showerror("Error", "Complete todos los campos.")
            return
        try:
            cant = int(cant)
            if pago not in ("1", "2"):
                messagebox.showerror("Error", "El método de pago debe ser 1 o 2.")
                return
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un número.")
            return
        # Definir entrada() "dummy" para registrar_compra_menu
        def entrada(prompt=""):
            if "Cédula del cliente" in prompt:
                return entry_cedula.get().strip()
            elif "Es para llevar" in prompt:
                return entry_condicion.get().strip().lower()
            elif "Método de pago" in prompt:
                return entry_pago.get().strip()
            elif "Código del país" in prompt:
                return entry_pais.get().strip()
            elif "Código de la ciudad" in prompt:
                return entry_ciudad.get().strip()
            elif "Código del restaurante" in prompt:
                return entry_rest.get().strip()
            elif "Código del menú" in prompt:
                return entry_menu.get().strip()
            elif "Código del producto" in prompt:
                return entry_prod.get().strip()
            elif "Cantidad a comprar" in prompt:
                return entry_cantidad.get().strip()
            elif "Desea agregar otro producto" in prompt:
                return "n"  # Por ahora, solo una compra
            else:
                return ""

        exito = registrar_compra_menu(dic, cli, entrada)
        if exito:
            resultado_label.config(text="Compra registrada correctamente.", fg="green")
        else:
            resultado_label.config(text="Error al registrar compra.", fg="red")

    tk.Button(frame_dinamico, text="Registrar Compra", command=procesar_compra).pack(pady=10)
#FILA
def formulario_ver_fila_compra():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Fila de Compra (últimas compras registradas)", font=('Arial', 16)).pack(pady=10)
    try:
        with open("facturas.txt", "r", encoding="utf-8") as f:
            lineas = [linea.strip() for linea in f if linea.strip()]
    except FileNotFoundError:
        tk.Label(frame_dinamico, text="No hay facturas registradas.", fg="red").pack(pady=10)
        return

    if not lineas:
        tk.Label(frame_dinamico, text="No hay compras registradas.", fg="red").pack(pady=10)
        return

    for i, linea in enumerate(lineas, start=1):
        campos = linea.split(";")
        texto = f"{i}. Cédula: {campos[0]}, País: {campos[1]}, Ciudad: {campos[2]}, Restaurante: {campos[3]}, Menú: {campos[4]}, Producto: {campos[5]}, Cantidad: {campos[6]}, Precio: {campos[7]}, Pago: {campos[8]}, Servicio: {campos[9]}"
        tk.Label(frame_dinamico, text=texto, wraplength=800, justify="left").pack(anchor="w")
def formulario_vaciar_fila_compra():
    limpiar_frame()
    tk.Label(frame_dinamico, text="Vaciar Fila de Compra", font=('Arial', 16)).pack(pady=10)

    def vaciar():
        try:
            with open("facturas.txt", "w") as f:
                f.write("")
            tk.Label(frame_dinamico, text="Fila de compra vaciada correctamente.", fg="green").pack(pady=10)
        except Exception as e:
            tk.Label(frame_dinamico, text=f"Error al vaciar: {e}", fg="red").pack(pady=10)

    tk.Button(frame_dinamico, text="Vaciar Fila de Compra", command=vaciar).pack(pady=10)
def mostrar_mensaje(seccion):
    limpiar_frame()
    tk.Label(frame_dinamico, text=f"Seleccionaste: {seccion}", font=("Arial", 18)).pack(pady=50)
#___________VENTANA PRINCIPAL_________________
def ventana_principal():
    global frame_dinamico
    ventana = tk.Tk()
    ventana.geometry('1280x900')
    ventana.title("Sistema de Restaurante")
    ventana.config(bg="#e6f0fa")

    frame_iconos = tk.Frame(ventana,bg="#ebe8e3", bd=2, relief="groove", padx=15, pady=10)
    frame_iconos.pack(side="top", pady=10)

    frame_dinamico = tk.Frame(ventana, bg="#f0f0f0", padx=10, pady=10)
    frame_dinamico.pack(fill='both', expand=True)

    #UBICACIONES
    icono_ubi = tk.PhotoImage(file="iconos/ubi.png")
    icono_rest = tk.PhotoImage(file="iconos/rest.png")
    icono_usuar = tk.PhotoImage(file="iconos/usuar.png")
    icono_salir = tk.PhotoImage(file="iconos/salir.png")
    ventana.iconos=[icono_ubi, icono_rest, icono_usuar, icono_salir]
    #BOTONES
    """btn_ubi=tk.Button(frame_iconos, image=icono_ubi, command=lambda: mostrar_mensaje("Ubicaciones"))
    btn_ubi.pack(side="left", padx=20)

    btn_rest=tk.Button(frame_iconos, image=icono_rest, command=lambda: mostrar_mensaje("Restaurantes"))
    btn_rest.pack(side="left", padx=20)

    btn_usuar=tk.Button(frame_iconos, image=icono_usuar, command=lambda: mostrar_mensaje("Usuarios"))
    btn_usuar.pack(side="left", padx=20)

    btn_salir = tk.Button(frame_iconos, image=icono_salir, command=ventana.destroy)
    btn_salir.pack(side="left", padx=20)"""

    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu)

    # ======= Menú de Ubicaciones =======
    menu_ubicaciones=tk.Menu(barra_menu, tearoff=0)
    submenu_paises=tk.Menu(menu_ubicaciones, tearoff=0)
    submenu_paises.add_command(label="Insertar País",command=formulario_insertar_pais)
    submenu_paises.add_command(label="Consultar País", command=formulario_consultar_pais)
    submenu_paises.add_command(label="Modificar País", command=formulario_modificar_pais)
    submenu_paises.add_command(label="Eliminar País", command=formulario_eliminar_pais)
    submenu_ciudades = tk.Menu(menu_ubicaciones, tearoff=0)
    submenu_ciudades.add_command(label="Insertar Ciudad", command=formulario_insertar_ciudad)
    submenu_ciudades.add_command(label="Consultar Ciudad", command=formulario_consultar_ciudad)
    submenu_ciudades.add_command(label="Modificar Ciudad", command=formulario_modificar_ciudad)
    submenu_ciudades.add_command(label="Eliminar Ciudad",command=formulario_eliminar_ciudad)

    menu_ubicaciones.add_cascade(label="Países", menu=submenu_paises)
    menu_ubicaciones.add_cascade(label="Ciudades", menu=submenu_ciudades)
    barra_menu.add_cascade(label="Ubicaciones", menu=menu_ubicaciones)

    # ======= Menú de Restaurantes =======
    menu_restaurantes = tk.Menu(barra_menu, tearoff=0)

    submenu_restaurantes = tk.Menu(menu_restaurantes, tearoff=0)
    submenu_restaurantes.add_command(label="Insertar Restaurante", command=formulario_insertar_restaurante)
    submenu_restaurantes.add_command(label="Consultar Restaurante", command=formulario_consultar_restaurante)
    submenu_restaurantes.add_command(label="Modificar Restaurante", command=formulario_modificar_restaurante)
    submenu_restaurantes.add_command(label="Eliminar Restaurante",command=formulario_eliminar_restaurante)

    submenu_menus = tk.Menu(menu_restaurantes, tearoff=0)
    submenu_menus.add_command(label="Insertar Menú", command=formulario_insertar_menu)
    submenu_menus.add_command(label="Consultar Menú", command=formulario_consultar_menu)
    submenu_menus.add_command(label="Modificar Menú", command=formulario_modificar_menu)
    submenu_menus.add_command(label="Eliminar Menú", command=formulario_eliminar_menu)

    submenu_productos = tk.Menu(menu_restaurantes, tearoff=0)
    submenu_productos.add_command(label="Insertar Producto", command=formulario_insertar_producto)
    submenu_productos.add_command(label="Consultar Producto", command=formulario_consultar_producto)
    submenu_productos.add_command(label="Modificar Producto", command=formulario_modificar_producto)
    submenu_productos.add_command(label="Eliminar Producto", command=formulario_eliminar_producto)

    menu_restaurantes.add_cascade(label="Restaurantes", menu=submenu_restaurantes)
    menu_restaurantes.add_cascade(label="Menús", menu=submenu_menus)
    menu_restaurantes.add_cascade(label="Productos", menu=submenu_productos)
    barra_menu.add_cascade(label="Restaurantes", menu=menu_restaurantes)

    # ======= Menú de Usuarios =======
    menu_usuarios = tk.Menu(barra_menu, tearoff=0)

    submenu_clientes = tk.Menu(menu_usuarios, tearoff=0)
    submenu_clientes.add_command(label="Insertar Cliente", command=formulario_insertar_cliente)
    submenu_clientes.add_command(label="Consultar Cliente", command=formulario_consultar_cliente)
    submenu_clientes.add_command(label="Modificar Cliente", command=formulario_modificar_cliente)
    submenu_clientes.add_command(label="Eliminar Cliente", command=formulario_eliminar_cliente)

    submenu_admins = tk.Menu(menu_usuarios, tearoff=0)
    submenu_admins.add_command(label="Insertar Administrador", command=formulario_insertar_administrador)
    submenu_admins.add_command(label="Consultar Administrador", command=formulario_consultar_administrador)
    submenu_admins.add_command(label="Modificar Administrador", command=formulario_modificar_administrador)
    submenu_admins.add_command(label="Eliminar Administrador", command=formulario_eliminar_administrador)

    submenu_fila = tk.Menu(menu_usuarios, tearoff=0)
    submenu_fila.add_command(label="Ver Fila de Compra", command=formulario_ver_fila_compra)
    submenu_fila.add_command(label="Vaciar Fila de Compra", command=formulario_vaciar_fila_compra)

    submenu_registrar = tk.Menu(menu_usuarios, tearoff=0)
    submenu_registrar.add_command(label="Registrar Compra", command=formulario_registrar_compra)

    menu_usuarios.add_cascade(label="Clientes", menu=submenu_clientes)
    menu_usuarios.add_cascade(label="Administradores", menu=submenu_admins)
    menu_usuarios.add_cascade(label="Fila de Compra", menu=submenu_fila)
    menu_usuarios.add_cascade(label="Registrar Compra", menu=submenu_registrar)
    barra_menu.add_cascade(label="Usuarios", menu=menu_usuarios)

    # ======= Cerrar Ventana =======
    barra_menu.add_command(label="Cerrar Ventana", command=lambda:regresar_login(ventana))

    def mostrar_popup(menu, event):
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()
    # Botones de iconos (sin bordes ni efectos)
    btn_ubi = tk.Button(frame_iconos, image=icono_ubi, bd=0, relief='flat', bg="#f0f0f0",
                        command=lambda: None)
    btn_ubi.pack(side="left", padx=20)
    btn_ubi.bind("<Button-1>", lambda e: mostrar_popup(menu_ubicaciones, e))

    btn_rest = tk.Button(frame_iconos, image=icono_rest, bd=0, relief='flat', bg="#f0f0f0",
                         command=lambda: None)
    btn_rest.pack(side="left", padx=20)
    btn_rest.bind("<Button-1>", lambda e: mostrar_popup(menu_restaurantes, e))

    btn_usuar = tk.Button(frame_iconos, image=icono_usuar, bd=0, relief='flat', bg="#f0f0f0",
                          command=lambda: None)
    btn_usuar.pack(side="left", padx=20)
    btn_usuar.bind("<Button-1>", lambda e: mostrar_popup(menu_usuarios, e))

    btn_salir = tk.Button(frame_iconos, image=icono_salir, bd=0, relief='flat', bg="#f0f0f0",
                          command=ventana.destroy)
    btn_salir.pack(side="left", padx=20)
    ventana.mainloop()
def ventana_usuario():
    global frame_dinamico
    ventana = tk.Tk()
    ventana.geometry('1280x900')
    ventana.title("Sistema de Restaurante - Usuario")
    ventana.config(bg="#e6f0fa")
    frame_iconos = tk.Frame(ventana, bg="#cce0f5", bd=2, relief="groove", padx=15, pady=10)
    frame_iconos.pack(side="top", pady=10)
    frame_dinamico = tk.Frame(ventana, bg="#f0f0f0", padx=10, pady=10)
    frame_dinamico.pack(fill='both', expand=True)

    # Cargar iconos
    icono_ubi = tk.PhotoImage(file="iconos/ubi.png")
    icono_rest = tk.PhotoImage(file="iconos/rest.png")
    icono_salir = tk.PhotoImage(file="iconos/salir.png")
    ventana.iconos = [icono_ubi, icono_rest, icono_salir]

    # Menús solo de consulta
    menu_ubicaciones = tk.Menu(ventana, tearoff=0)
    menu_ubicaciones.add_command(label="Consultar País", command=formulario_consultar_pais)
    menu_ubicaciones.add_command(label="Consultar Ciudad", command=formulario_consultar_ciudad)

    menu_restaurantes = tk.Menu(ventana, tearoff=0)
    menu_restaurantes.add_command(label="Consultar Restaurante", command=formulario_consultar_restaurante)
    menu_restaurantes.add_command(label="Consultar Menú", command=formulario_consultar_menu)
    menu_restaurantes.add_command(label="Consultar Producto", command=formulario_consultar_producto)

    # Mostrar menú al hacer clic en íconos
    def mostrar_popup(menu, event):
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()

    estilo_btn = {"bd": 0, "relief": "flat", "bg": "#cce0f5", "activebackground": "#b3d1f0"}

    # Íconos con leyenda
    def crear_icono(frame_padre, icono, texto, comando):
        frame = tk.Frame(frame_padre, bg="#cce0f5")
        frame.pack(side="left", padx=15)

        btn = tk.Button(frame, image=icono, **estilo_btn)
        btn.pack()
        btn.bind("<Button-1>", comando)

        tk.Label(frame, text=texto, bg="#cce0f5", font=("Arial", 10)).pack()

    crear_icono(frame_iconos, icono_ubi, "Ubicaciones", lambda e: mostrar_popup(menu_ubicaciones, e))
    crear_icono(frame_iconos, icono_rest, "Restaurantes", lambda e: mostrar_popup(menu_restaurantes, e))
    crear_icono(frame_iconos, icono_salir, "Salir", lambda e: ventana.destroy())

    ventana.mainloop()

ventana_login()


