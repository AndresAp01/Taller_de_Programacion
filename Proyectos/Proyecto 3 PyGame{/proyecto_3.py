#Luis Andrés Acuña Pérez y Patrick Zúñiga Arroyo
#Mantenimiento de Bases de Datos
####################################################################################################################
import tkinter
from tkinter import *

import tkinter as tk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()

# Creating a button with specified options
boton_admin = tk.Button(root,
                   text="Administrador",
                   command=button_clicked,
                   activebackground="blue",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

boton_admin.pack(padx=10, pady=10)
cliente = tk.Button(root,
                   text="Cliente",
                   command=button_clicked,
                   activebackground="green",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
cliente.pack(padx=40, pady=40)
root.mainloop()
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER
#Construccion de diccionarios
#----------------------------
def normalizar_codigo(codigo):
    if not isinstance(codigo, (str, int)):
        print(f"El codigo {codigo} no es alfanumerico")
    else:
        return str(codigo).lstrip('-')
#Funcion para normalizar cada entrada del usuario
input_orig=input
def entrada(prompt=""):
    respuesta=input_orig(prompt)
    return normalizar_codigo(respuesta)
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
    codigo =entrada("Código de país: ")
    nombre =input("Nombre de país: ")
    return insertar_en_diccionario([codigo, nombre], nivel=1)
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
        print(f"Cliente con cédula {cedula} ya existe como '{cli_dict[cedula]}'")
        return False
    cli_dict[cedula] = nombre
    print(f"Cliente '{nombre}' con cédula {cedula} agregado correctamente.")
    return True
#______________________________________________________________________________________________________________________#
#REGISTRO
#Funcion para leer el ultimo codigo de factura
def registrar_compra_menu(dic, cli, entrada, archivo_facturas="facturas.txt"):
    facturas = []
    ced = entrada("Cédula del cliente: ").strip()
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
#MENU__________________________________________________________________________________________________________________#
def mostrar_menu(opciones):
    print(f"\n=== Bienvenido al menu de Mantenimiento de Bases de Datos ===")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")
def MainMenu():
    opciones_principales=["Inserción", "Buscar", "Modificar","Eliminar","Reportes", "Salir"]
    subopciones=["Pais", "Ciudad", "Restaurante", "Menu", "Productos", "Clientes", "Regresar al mantenimiento"] #Para poder ingresar a otro ciclo y muestre un segundo menu
    subopciones_insertar=["Pais", "Ciudad", "Restaurante", "Menu", "Productos", "Clientes", "Registrar compra", "Regresar al mantenimiento"]
    opciones_reportes=["Lista de Países", "Ciudades de un País", "Restaurantes de una Ciudad", "Lista de Clientes", "Reporte de todas las compras", "Compras de un Cliente", "Estadisticas", "Regresar al menú principal"]
    opciones_rep_estadisticas=["Restaurante mas buscado", "Menu mas buscado", "Producto mas buscado", "Factura de mayor monto", "Factura de menor monto", "Precio de un producto", "Consultar Descuentos", "Consultar Stock/Cantidad de Producto", "Regresar al menu principal"]
    while True:
        mostrar_menu(opciones_principales)
        print("\n Ingrese que quiere hacer: ")
        x=int(entrada())
        if x==1:
            print("Has seleccionado la opcion Insertar.")
            while True:
                mostrar_menu(subopciones_insertar)
                y=int(entrada("Selecciona una sub-opción (1-8) para insertar: "))
                if y==1:insertar_pais()
                elif y==2:insertar_ciudad()
                elif y==3:insertar_restaurante()
                elif y==4:insertar_menu()
                elif y==5:insertar_producto()
                elif y==6:
                    cedula=entrada("Ingrese la cedula de la persona: ")
                    nombre=entrada("Ingrese el nombre de la persona: ")
                    insertar_cliente(cli, cedula, nombre)
                elif y==7:
                    print("Has seleccionado Registrar compra")
                    if registrar_compra_menu(dic, cli, entrada):
                        print("Operación exitosa")
                    else:
                        print("No se completó la compra")
                    entrada("Presione Enter para continuar...")
                elif y==8:
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción no válida. Por favor, selecciona una sub-opción del 1 al 8.")
        elif x==2:
            print("Has seleccionado Buscar.")
            while True:
                mostrar_menu(subopciones)
                y=int(entrada("Selecciona una sub-opción (1-7) para buscar: "))
                if y==1:
                    cod_pais=entrada("Ingrese el codigo del pais a buscar: ")
                    buscar_elemento(dic, cod_pais)
                elif y==2:
                    cod_pais=entrada("Ingrese el codigo del pais donde se encuentra la ciudad: ")
                    cod_ciudad=entrada("Ingrese el codigo de la ciudad a buscar: ")
                    buscar_elemento(dic, cod_pais, cod_ciudad)
                    #validar_ciudad_existe(dic, cod_pais, cod_ciudad)
                elif y==3:
                    cod_pais=entrada("Ingrese el codigo del pais: ")
                    cod_ciudad=entrada("Ingrese el codigo de la ciudad: ")
                    cod_rest=entrada("Ingrese el codigo del restaurante a buscar: ")
                    buscar_elemento(dic, cod_pais, cod_ciudad, cod_rest)
                    #validar_restaurante_existe(dic, cod_pais, cod_ciudad, cod_rest)
                elif y==4:
                    cod_pais=entrada("Ingrese el codigo del pais: ")
                    cod_ciudad=entrada("Ingrese el codigo de la ciudad: ")
                    cod_rest=entrada("Ingrese el codigo del restaurante: ")
                    cod_menu=entrada("Ingrese el codigo del menu a buscar: ")
                    buscar_elemento(dic, cod_pais, cod_ciudad, cod_rest, cod_menu)
                    #validar_menu_existe(dic, cod_pais, cod_ciudad, cod_rest, cod_menu)
                elif y==5:
                    cod_pais=entrada("Ingrese el codigo del pais: ")
                    cod_ciudad=entrada("Ingrese el codigo de la ciudad: ")
                    cod_rest=entrada("Ingrese el codigo del restaurante: ")
                    cod_menu=entrada("Ingrese el codigo del menu: ")
                    cod_prod=entrada("Ingrese el codigo del producto a buscar: ")
                    buscar_elemento(dic, cod_pais, cod_ciudad, cod_rest, cod_menu, cod_prod)
                elif y==6:
                    ced=entrada("Ingrese la cedula del cliente a buscar")
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
                y=int(entrada("Selecciona una sub-opción (1-7) para modificar: "))
                if y==1:
                    cod_pais=entrada("Ingrese el codigo del pais a modificar: ")
                    nuevo_nombre=entrada("Ingrese el nuevo nombre del pais: ")
                    modificar_pais(cod_pais, nuevo_nombre)
                elif y==2:
                    cod_pais=entrada("Ingrese el codigo del pais donde se encuentra la ciudad: ")
                    cod_ciudad=entrada("Ingrese el codigo de la ciudad a modificar: ")
                    nuevo_nombre=entrada("Ingrese el nuevo nombre de la ciudad: ")
                    modificar_ciudad(cod_pais, cod_ciudad, nuevo_nombre)
                elif y==3:
                    cod_pais = entrada("Ingrese el codigo del pais donde se encuentra la ciudad: ")
                    cod_ciudad = entrada("Ingrese el codigo de la ciudad del restaurante: ")
                    cod_rest = entrada("Ingrese el codigo del restaurante a modificar: ")
                    nuevo_nombre = entrada("Ingrese el nuevo nombre del restaurante: ")
                    modificar_restaurante(cod_pais, cod_ciudad, cod_rest, nuevo_nombre)
                elif y==4:
                    cod_pais = entrada("Ingrese el codigo del pais donde se encuentra la ciudad: ")
                    cod_ciudad = entrada("Ingrese el codigo de la ciudad del restaurante: ")
                    cod_rest=entrada("Ingrese el codigo del restaurante donde esta el menu: ")
                    cod_menu=entrada("Ingrese el codigo del menu a modificar: ")
                    nuevo_nombre=entrada("Ingrese el nuevo nombre del menu: ")

                    modificar_menu(cod_pais, cod_ciudad, cod_rest, cod_menu, nuevo_nombre)
                elif y==5:
                    cod_pais = entrada("Ingrese el codigo del pais: ")
                    cod_ciudad = entrada("Ingrese el codigo de la ciudad: ")
                    cod_rest = entrada("Ingrese el codigo del restaurante: ")
                    cod_menu = entrada("Ingrese el codigo del menu: ")
                    cod_prod = entrada("Ingrese el codigo del producto a modificar: ")
                    nuevo_nombre = entrada("Ingrese el nuevo nombre del producto: ")
                    nuevas_calorias=entrada("Ingrese el nuevo valor de las calorias del producto: ")
                    nuevo_precio=entrada("Ingrese el nuevo valor del precio del producto: ")

                    modificar_producto(cod_pais, cod_ciudad, cod_rest, cod_menu, cod_prod, nuevo_nombre,  nuevas_calorias, nuevo_precio)
                elif y==6:
                    cedula_cliente=entrada("Ingrese la cedula del cliente a modificar: ")
                    nuevo_nombre=entrada("Ingrese el nuevo nombre del cliente: ")
                    modificar_cliente(cedula_cliente, nuevo_nombre)

                elif y==7:
                    print("Volviendo al menú principal...")
                    break
        elif x==4:
            print("Has seleccionado Eliminar.")
            while True:
                mostrar_menu(subopciones)
                y = int(entrada("Selecciona una sub-opción (1-7) para eliminar: "))
                if y == 1:
                    cod_pais = entrada("Ingrese el código del país a eliminar: ")
                    eliminar_pais(cod_pais)
                elif y == 2:
                    cod_pais = entrada("Ingrese el código del país: ")
                    cod_ciudad = entrada("Ingrese el código de la ciudad a eliminar: ")
                    eliminar_ciudad(cod_pais, cod_ciudad)
                elif y == 3:
                    cod_pais = entrada("Ingrese el código del país: ")
                    cod_ciudad = entrada("Ingrese el código de la ciudad: ")
                    cod_rest = entrada("Ingrese el código del restaurante a eliminar: ")
                    eliminar_restaurante(cod_pais, cod_ciudad, cod_rest)
                elif y == 4:
                    cod_pais = entrada("Ingrese el código del país: ")
                    cod_ciudad = entrada("Ingrese el código de la ciudad: ")
                    cod_rest = entrada("Ingrese el código del restaurante: ")
                    cod_menu = entrada("Ingrese el código del menú a eliminar: ")
                    eliminar_menu(cod_pais, cod_ciudad, cod_rest, cod_menu)
                elif y == 5:
                    cod_pais = entrada("Ingrese el código del país: ")
                    cod_ciudad = entrada("Ingrese el código de la ciudad: ")
                    cod_rest = entrada("Ingrese el código del restaurante: ")
                    cod_menu = entrada("Ingrese el código del menú: ")
                    cod_prod = entrada("Ingrese el código del producto a eliminar: ")
                    eliminar_producto(cod_pais, cod_ciudad, cod_rest, cod_menu, cod_prod)
                elif y == 6:
                    cedula = entrada("Ingrese la cédula del cliente a eliminar: ")
                    eliminar_cliente(cedula)
                elif y == 7:
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción no válida. Por favor, selecciona una sub-opción del 1 al 7.")
        elif x==5:
            print("Has seleccionado Reportes.")
            while True:
                mostrar_menu(opciones_reportes)
                y=int(entrada("Selecciona un reporte (1-8): "))
                if y==1:reporte_paises(dic,"reporte_de_paises.pdf")
                elif y==2:
                    cod_pais=entrada("Ingrese el codigo del pais: ")
                    reporte_ciudades(dic, cod_pais, "reporte_de_ciudades.pdf")
                elif y==3:
                    cod_pais=entrada("Ingrese el codigo del pais: ")
                    cod_ciudad=entrada("Ingrese el codigo de la ciudad: ")
                    reporte_restaurantes(dic, cod_pais, cod_ciudad, "reporte_de_rests.pdf")
                elif y==4:reporte_clientes(cli, "reporte_de_clientes.pdf")
                elif y==5:reporte_todas_compras("Reporte_todas_las_compras.pdf", archivo_facturas="facturas.txt")
                elif y==6:
                    cedula=entrada("Ingrese la cedula del cliente")
                    reporte_compras_cliente(cedula, "facturas.txt", "reporte_de_compras.pdf")
                elif y==7:
                    while True:
                        mostrar_menu(opciones_rep_estadisticas)
                        x=int(entrada("Selecciona una opcion del 1-7: "))
                        if x==1:reporte_rest_mas("reporte_restaurante_mas_buscado.pdf")
                        if x==2:reporte_menu_mas("reporte_menu_mas_buscado.pdf")
                        if x==3: reporte_producto_mas("reporte_prod_mas_buscado.pdf")
                        if x==4: reporte_factura_precio_extremo("Reporte_PrecioMayor.pdf", archivo_facturas="facturas.txt", mayor=True)
                        if x==5: reporte_factura_precio_extremo("Reporte_PrecioMenor.pdf", archivo_facturas="facturas.txt", mayor=False)
                        if x==6:
                            cod_pais=entrada("Código del país: ").strip()
                            cod_ciudad=entrada("Código de la ciudad: ").strip()
                            cod_rest=entrada("Código del restaurante: ").strip()
                            cod_menu=entrada("Código del menú: ").strip()
                            cod_prod=entrada("Código del producto: ").strip()
                            reporte_precio_producto(dic,cod_pais,cod_ciudad,cod_rest,cod_menu,cod_prod,"Reporte_Consulta_Producto.pdf",stock=False)
                        if x==7: reporte_descuentos(descuentos, "Reporte_Descuentos.pdf")
                        if x==8:
                            cod_pais=entrada("Código del país: ").strip()
                            cod_ciudad=entrada("Código de la ciudad: ").strip()
                            cod_rest=entrada("Código del restaurante: ").strip()
                            cod_menu=entrada("Código del menú: ").strip()
                            cod_prod=entrada("Código del producto: ").strip()
                            reporte_precio_producto(dic, cod_pais, cod_ciudad, cod_rest, cod_menu, cod_prod,"Reporte_Consulta_Cantidad.pdf", stock=True)
                        if x==9: break
                elif y==8:
                    print("Volviendo al menú principal...")
                    break
        elif x==6:
            break
        else:
            print("\n\n Atención!! \n Ingresa una opción del 1 al 5.")
            continue #Para que el usuario no tenga que reiniciar el programa
MainMenu()
#______________________________________________________________________________________________________________________#
