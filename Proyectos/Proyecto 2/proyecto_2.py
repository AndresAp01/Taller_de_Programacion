#Luis Andrés Acuña Pérez y Patrick Zúñiga Arroyo
#Mantenimiento de Bases de Datos
####################################################################################################################
#Construccion de diccionarios
def normalizar_codigo(codigo):
    if not isinstance(codigo, (str, int)):
        print(f"El codigo {codigo} no es alfanumerico")
    else:
        return str(codigo).lstrip('-')
input_orig=input
def entrada(prompt=""):
    respuesta=input_orig(prompt)
    return normalizar_codigo(respuesta)
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
        try:
            calorias = int(float(partes[6]))
            precio = float(partes[7])
        except ValueError:
            continue
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
    cli={}
    for linea in abrir_archivo(ruta_clientes):
        partes=linea.split(';', 1)
        if len(partes)!=2:
            continue
        cedula, nombre=partes
        cli[cedula]=nombre
    return cli
clientes="Clientes.txt"
cli=cargar_clientes(clientes)
def buscar_elemento(diccionario, cod_pais, cod_ciudad=None, cod_restaurante=None, cod_menu=None, cod_prod=None):
    #paises
    if cod_pais not in diccionario:
        return f"El país {cod_pais} no existe"
    pais_info=diccionario[cod_pais]
    # Si solo era validar pais:
    if cod_ciudad is None:
        nombre=pais_info["nombre"]
        print(f"El país {cod_pais} → {nombre} existe")
        return True
    #ciudades
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
    if "menus" not in rest_info:
        return f"No hay menús definidos en el restaurante {cod_restaurante}"
    if cod_menu not in rest_info["menus"]:
        return f"El menu {cod_menu} no existe en el restaurante {cod_restaurante}"
    menu_info=rest_info["menus"][cod_menu]
    if cod_prod is None:
        nombre_menu=menu_info["nombre"]
        print(f"El menu {cod_menu} → {nombre_menu} existe en {cod_restaurante}")
        return True
    # exito en nivel menu
    #productos
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
#funciona
def modificar_pais():
    cod_pais=entrada("Ingrese el código del país a modificar: ")
    if cod_pais not in dic:
        print("El pais no existe")
        return
    nuevo_nombre=entrada("Ingrese el nuevo nombre del país: ")
    dic[cod_pais]["nombre"]=nuevo_nombre
    print(f"El pais {cod_pais} ha sido renombrado como: {nuevo_nombre}")
    print(dic)
#funciona
def modificar_ciudad():
    cod_pais=entrada("Ingrese el código del país donde se encuentra la ciudad: ")
    cod_ciudad=entrada("Ingrese el codigo de la ciudad a modificar: ")
    if cod_pais not in dic:
        print("El pais no existe")
        return
    if cod_ciudad not in dic[cod_pais]["ciudades"]:
        print("La ciudad no existe")
        return
    nuevo_nombre=entrada("Ingrese el nuevo nombre del ciudad: ")
    dic[cod_pais]["ciudades"][cod_ciudad]["nombre"]=nuevo_nombre
    print(f"La ciudad {cod_ciudad} se ha renombrado como: {nuevo_nombre}")
    print(dic)
def modificar_restaurante():
    cod_pais=entrada("Ingrese el código del país: ")
    cod_ciudad=entrada("Ingrese el código de la ciudad: ")
    cod_rest=entrada("Ingrese el código del restaurante a modificar: ")
    ok=buscar_elemento(dic, cod_pais, cod_ciudad, cod_rest)
    if ok is not True:
        print(ok)
        return
    # Pedir nuevo nombre y aplicar cambio
    nuevo_nombre=entrada("Ingrese el nuevo nombre del restaurante: ")
    dic[cod_pais]['ciudades'][cod_ciudad]['restaurantes'][cod_rest]['nombre']=nuevo_nombre
    print(f"El restaurante {cod_rest} se ha renombrado como: {nuevo_nombre}")
    print(dic)
def modificar_menu():
    cod_pais=entrada("Ingrese el código del país: ")
    cod_ciudad=entrada("Ingrese el código de la ciudad: ")
    cod_rest=entrada("Ingrese el código del restaurante: ")
    cod_menu=entrada("Ingrese el código del menú a modificar: ")
    # Validar menú (incluye validación de niveles anteriores)
    ok=buscar_elemento(dic, cod_pais, cod_ciudad, cod_rest, cod_menu)
    if ok is not True:
        print(ok)
        return
    # Pedir nuevo nombre y aplicar cambio
    nuevo_nombre=entrada("Ingrese el nuevo nombre del menú: ")
    dic[cod_pais]['ciudades'][cod_ciudad]['restaurantes'][cod_rest]['menus'][cod_menu]['nombre']=nuevo_nombre
    print(f"El menú {cod_menu} se ha renombrado como: {nuevo_nombre}")
    print(dic)
def modificar_producto():
    cod_pais=entrada("Ingrese el codigo del pais: ")
    cod_ciudad=entrada("Ingrese el codigo de la ciudad: ")
    cod_rest=entrada("Ingrese el codigo del restaurante: ")
    cod_menu=entrada("Ingrese el codigo del menu: ")
    cod_prod=entrada("Ingrese el codigo del producto a modificar: ")
    # Validar que el producto exista
    ok=buscar_elemento(dic, cod_pais, cod_ciudad, cod_rest, cod_menu)
    if ok is not True:
        print(ok)
        return
    menu_info=dic[cod_pais]['ciudades'][cod_ciudad]['restaurantes'][cod_rest]['menus'][cod_menu]
    if 'productos' not in menu_info or cod_prod not in menu_info['productos']:
        print(f"El producto {cod_prod} no existe en el menú {cod_menu}")
        return
    # Pedir nuevos datos
    nuevo_nombre=entrada("Ingrese el nuevo nombre del producto: ")
    try:
        nuevas_cal =int(entrada("Ingrese las nuevas calorías: "))
        nuevo_precio=float(entrada("Ingrese el nuevo precio: "))
    except ValueError:
        print("Calorías o precio inválidos.")
        return
    # Aplicar cambios
    prod=menu_info['productos'][cod_prod]
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
    cedula=entrada("Ingrese la cedula del cliente: ")
    if cedula not in cli:
        print(f"El cliente con cedula: {cedula} no existe")
        return
    nuevo_nombre = entrada("Ingrese el nuevo nombre del cliente: ")
    cli[cedula]["nombre"]=nuevo_nombre
    print(f"El cliente con cedula {cedula} ha sido renombrado como: {nuevo_nombre}")
    print(cli)
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
    cod_pais=entrada("Ingrese el codigo del pais: ")
    nombre=entrada("Ingrese el nombre del pais: ")
    resultado=insertar_en_lista
    if resultado:
        print(f"Registro insertado correctamente: {paises}")
    return resultado
def insertar_producto():
    global paises, ciudades, restaurantes, menus, productos
    cod_pais=entrada("Ingrese el código del país: ")
    if not validar_pais_existe(cod_pais):
        return False
    cod_ciudad=entrada("Ingrese el código de la ciudad: ")
    if not validar_ciudad_existe(cod_pais, cod_ciudad):
        return False
    cod_rest=entrada("Ingrese el código del restaurante: ")
    if not validar_restaurante_existe(cod_pais, cod_ciudad,cod_rest):
        return False
    cod_menu=entrada("Ingrese el código del menú: ")
    if not validar_menu_existe(cod_pais, cod_ciudad, cod_rest, cod_menu):
        return False
    cod_producto=entrada("Ingrese el código del producto: ")
    nombre=entrada("Ingrese el nombre del producto: ")
    calorias=float(entrada("Ingrese las calorías del producto: "))
    precio=float(entrada("Ingrese el precio: "))
    resultado=insertar_en_lista(productos, [str(cod_pais),str(cod_ciudad),str(cod_rest),str(cod_menu),str(cod_producto), nombre, calorias, precio],indices_unicos=[0, 1, 2, 3, 4])

    if resultado:
        print(f"Registro insertado correctamente: {productos}")
    return resultado
def insertar_cliente():
    global clientes
    cedula=entrada("Ingrese la cédula del cliente: ")
    nombre=entrada("Ingrese el nombre del cliente: ")
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
    cod_pais=entrada("\nIngrese el código del país: ").strip()
    if not validar_pais_existe(cod_pais):
        print(f"Error: País {cod_pais} no existe")
        return False
    #ciudades disponibles para ese pais
    print("\nCiudades disponibles en este país:")
    ciudades_pais=[c for c in ciudades if c[0]==cod_pais]
    for ciudad in ciudades_pais:
        print(f"- {ciudad[1]}: {ciudad[2]}")
    cod_ciudad=entrada("\nIngrese el código de la ciudad: ").strip()
    if not validar_ciudad_existe(cod_pais, cod_ciudad):
        print(f"Error: Ciudad {cod_ciudad} no existe")
        return False

    #restaurantes disponibles en esa ciudad
    print("\nRestaurantes disponibles en esta ciudad:")
    restaurantes_ciudad=[r for r in restaurantes if r[0]==cod_pais and r[1]==cod_ciudad]
    for rest in restaurantes_ciudad:
        print(f"- {rest[2]}: {rest[3]}")
    cod_restaurante=entrada("\nIngrese el código del restaurante: ").strip()
    if not validar_restaurante_existe(cod_pais, cod_ciudad, cod_restaurante):
        print(f"Error: Restaurante {cod_restaurante} no existe")
        return False
    #  menus disponibles en ese restaurante
    print("\nMenus disponibles en este restaurante:")
    menus_restaurante=[m for m in menus if m[0]==cod_pais and m[1]==cod_ciudad and m[2]==cod_restaurante]
    for menu in menus_restaurante:
        print(f"- {menu[3]}: {menu[4]})")
    cod_menu=entrada("\nIngrese el código del menú: ").strip()
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
        cod_producto=entrada("\nIngrese el código del producto (o 'fin' para terminar): ").strip()
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
                cantidad=int(entrada(f"\nIngrese la cantidad para {producto_encontrado[5]}: "))
                if cantidad<=0:
                    print("La cantidad debe ser mayor a 0")
                    continue
                break
            except ValueError:
                print("Por favor ingrese un número válido")
        productos_seleccionados.append({'producto': producto_encontrado, 'cantidad': cantidad})
        print(f"Producto {producto_encontrado[5]} agregado con éxito")

    cedula=entrada("\nIngrese la cédula del cliente: ").strip()
    cliente=next((c for c in clientes if c[0]==cedula), None)
    if not cliente:
        print("Error: Cliente no registrado")
        return False
    print(f"Cliente: {cliente[1]}")

    orden=entrada("\nIngrese si la orden es para llevar o comer aqui: (llevar/aqui): ").strip().lower()
    while orden not in ['llevar', 'aqui']:
        print("Opción no válida. Ingrese 'llevar' o 'aqui'")
        orden=entrada("\nIngrese si es para llevar o comer aquí (llevar/aqui): ").strip().lower()

    metodo_pago=entrada("\nIngrese el metodo de pago: (efectivo/tarjeta): ").strip().lower()
    while metodo_pago not in ['efectivo', 'tarjeta']:
        print("Opcion no valida. Ingrese 'efectivo' o 'tarjeta'")
        metodo_pago=entrada("\nIngrese el metodo de pago: (efectivo/tarjeta): ").strip().lower()
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

    modificar=entrada("\n¿Desea modificar la compra? (S/N): ").strip().upper()
    while modificar=="S":
        print("\n¿Qué desea modificar?")
        print("1. Cambiar un producto")
        print("2. Cambiar la cantidad de un producto")
        print("3. Eliminar un producto")
        print("4. Agregar otro producto")
        print("5. Terminar modificaciones")

        opcion=entrada("\nSeleccione una opción (1-5): ").strip()

        if opcion=="1":  # Cambiar producto
            print("\nProductos en su pedido:")
            for i, item in enumerate(productos_seleccionados, 1):
                print(f"{i}. {item['producto'][5]} - Cantidad: {item['cantidad']}")

            try:
                num= int(entrada("\nIngrese el número del producto a cambiar: ")) - 1
                if num<0 or num>=len(productos_seleccionados):
                    print("Número de producto inválido")
                    continue

                print("\nSeleccione el nuevo producto:")
                for producto in productos_menu:
                    print(f"- {producto[4]}: {producto[5]} (Precio: {producto[7]})")

                nuevo_cod=entrada("\nIngrese el código del nuevo producto: ").strip()
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
                num= int(entrada("\nIngrese el número del producto a modificar: ")) - 1
                if num<0 or num>=len(productos_seleccionados):
                    print("Número de producto inválido")
                    continue
                nueva_cantidad=int(entrada(f"\nIngrese la nueva cantidad para {productos_seleccionados[num]['producto'][5]}: "))
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
                num= int(entrada("\nIngrese el número del producto a eliminar: ")) - 1
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
            cod_producto=entrada("\nIngrese el código del producto a agregar: ").strip()
            producto_encontrado=next((p for p in productos_en_menu if p[4]==cod_producto), None)
            if not producto_encontrado:
                print("Error: Producto no encontrado en este menú")
                continue
            cantidad=int(entrada(f"\nIngrese la cantidad para {producto_encontrado[5]}: "))
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

        modificar = entrada("\n¿Desea realizar más modificaciones? (S/N): ").strip().upper()
    confirmar=entrada("\n¿Confirmar compra? (S/N): ").strip().upper()
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
                elif y==6:insertar_cliente()
                elif y==7:
                    print("Has seleccionado Registrar compra")
                    if registrar_compra_menu():
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
                y=int(entrada("Selecciona un reporte (1-8): "))
                if y==1:reporte_paises()
                elif y==2:reporte_ciudades()
                elif y==3:reporte_restaurantes()
                elif y==4:reporte_clientes()
                elif y==5:reporte_compras()
                elif y==6:reporte_compras_cliente()
                elif y==7:
                    while True:
                        mostrar_menu(opciones_rep_estadisticas)
                        x=int(entrada("Selecciona una opcion del 1-7: "))
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
