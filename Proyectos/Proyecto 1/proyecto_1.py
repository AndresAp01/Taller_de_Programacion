#Luis Andrés Acuña Pérez y Patrick Zúñiga Arroyo
#Mantenimiento de Bases de Datos
####################################################################################################################
def datos_a_dicc(ruta_paises, ruta_ciudades, ruta_restaurantes, ruta_menus):

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
                diccionario[cod_pais]["ciudades"][cod_ciudad]["restaurantes"][cod_rest]["menus"][cod_menu]=nombre_menu

    return diccionario


def imprimir_cascada(diccionario):
    for cod_pais, info_pais in diccionario.items():
        print(f"{cod_pais} — {info_pais['nombre']}")
        for cod_ciudad, info_ciudad in info_pais["ciudades"].items():
            print(f"  {cod_ciudad} — {info_ciudad['nombre']}")
            for cod_rest, info_rest in info_ciudad["restaurantes"].items():
                print(f"    {cod_rest} — {info_rest['nombre']}")
                # Nivel de menús (puede estar vacío)
                for cod_menu, nombre_menu in info_rest.get("menus", {}).items():
                    print(f"      {cod_menu} — {nombre_menu}")


paises="Paises.txt"
ciudades="Ciudades.txt"
restaurantes="Restaurantes.txt"
menus="Menu.txt"
dic=datos_a_dicc(paises, ciudades, restaurantes, menus)
print(dic)
print (imprimir_cascada(dic))

def datos_a_listas(ruta_archivo):
    try:
        #paises_unicos para las claves de paises
        with open(ruta_archivo, "r") as archivo:
            texto=archivo.read()
            lista_lineas=texto.split("\n")
            matriz_datos=[]
            paises_unicos=[]
            ciudades_unicas=[]
            restaurantes_unicos=[]
            menus_unicos=[]
            productos_unicos=[]
            for linea in lista_lineas:
                if not linea.strip():
                    continue
                campos=linea.split(";")
                if len(campos)<2:
                    continue
                #Las claves unicas
                if len(campos)==2:  #Para paises
                    clave=[campos[0]]
                    if clave in paises_unicos:
                        continue
                    paises_unicos.append(clave)
                elif len(campos)==3:    #Para ciudades
                    clave=[campos[0], campos[1]]
                    if clave in ciudades_unicas:
                        continue
                    ciudades_unicas.append(clave)
                elif len(campos)==4:    #Para restaurantes
                    clave = [campos[0], campos[1], campos[2]]
                    if clave in restaurantes_unicos:
                        continue
                    restaurantes_unicos.append(clave)
                elif len(campos)==5:    #Para menus
                    clave=[campos[0], campos[1], campos[2], campos[3]]
                    if clave in menus_unicos:
                        continue
                    menus_unicos.append(clave)
                elif len(campos)>=6:    #Para producto
                    clave = [campos[0], campos[1], campos[2], campos[3], campos[4]]
                    if clave in productos_unicos:
                        continue
                    productos_unicos.append(clave)
                else:
                    continue

                matriz_datos.append(campos)
            return matriz_datos
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe")
        return None
paises=datos_a_listas("Paises.txt")
ciudades=datos_a_listas("Ciudades.txt")
restaurantes=datos_a_listas("Restaurantes.txt")
menus=datos_a_listas("Menu.txt")
productos=datos_a_listas("Productos.txt")
clientes=datos_a_listas("Clientes.txt")
compras=datos_a_listas("registro_compras.txt")
#Listas para estadisticas
contador_busquedas_rest=[]
contador_busquedas_menu=[]
contador_compras_producto=[]

def normalizar_codigo(codigo):
    if not isinstance(codigo, (str, int)):
        print(f"El codigo {codigo} no es alfanumerico")
    return str(codigo).lstrip('-')
def validar_pais_existe(cod_pais):
    cod_pais=normalizar_codigo(cod_pais)
    for i in range(len(paises)):
        #Se accede al elemento i, indice 0. Se usan dos porque es una lista de listas
        if paises[i][0]==cod_pais:
            return True
    print(f"Error: No existe un país con código '{cod_pais}'")
    return False
def validar_ciudad_existe(cod_pais, cod_ciudad):
    global paises, ciudades
    cod_pais = normalizar_codigo(cod_pais)
    cod_ciudad = normalizar_codigo(cod_ciudad)
    for i in range(len(ciudades)):
        if ciudades[i][0]==cod_pais and ciudades[i][1]==cod_ciudad:
            return True
    print(f"Error: No existe una ciudad con código '{cod_ciudad}' en el país '{cod_pais}'")
    return False

def validar_restaurante_existe(cod_pais, cod_ciudad, cod_rest):
    global paises, ciudades, restaurantes
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    cod_rest=normalizar_codigo(cod_rest)
    for i in range(len(restaurantes)):
        if restaurantes[i][0]==cod_pais and restaurantes[i][1]==cod_ciudad and restaurantes[i][2]==cod_rest:
            return True
    print(f"Error: No existe un restaurante con codigo '{cod_rest}' en la ciudad '{cod_ciudad}'")
    return False
def validar_menu_existe(cod_pais, cod_ciudad, cod_rest, cod_menu):
    global paises, ciudades, restaurantes, menus
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    cod_rest=normalizar_codigo(cod_rest)
    cod_menu=normalizar_codigo(cod_menu)
    for i in range(len(menus)):
        if menus[i][0]==cod_pais and menus[i][1]==cod_ciudad and menus[i][2]==cod_rest and menus[i][3]==cod_menu:
            return True
    print(f"Error: No existe un menu con codigo '{cod_menu}' en el restaurante '{cod_rest}'")
    return False
def validar_producto_existe(cod_pais, cod_ciudad, cod_rest, cod_menu, cod_producto):
    global paises, ciudades, restaurantes, menus, productos
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    cod_rest=normalizar_codigo(cod_rest)
    cod_menu=normalizar_codigo(cod_menu)
    cod_producto=normalizar_codigo(cod_producto)
    if not any(producto[0]==cod_pais and producto[1]==cod_ciudad and producto[2]==cod_rest and producto[3]==cod_menu and producto[4]==cod_producto for producto in productos):
        print(f"Error: No existe un producto con código '{cod_producto}' en el menú '{cod_menu}' del restaurante '{cod_rest}' de la ciudad '{cod_ciudad}' del país '{cod_pais}'")
        return False
    return True
def validar_cliente_existe(cedula):
    global clientes
    cedula=normalizar_codigo(cedula)
    if not any(cliente[0]==cedula for cliente in clientes):
        print(f"Error: No existe un cliente con cédula '{cedula}'")
        return False
    return True
#--------------------------------------------------------------------------------------------------
#MODIFICAR_____________________________________________________________________________________________________________#
def modificar_pais():
    global paises
    codigo = input("Ingrese el código del país a modificar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre del país: ")
    codigo=normalizar_codigo(codigo)
    for pais in paises:
        if pais[0]==codigo:
            pais[1]=nuevo_nombre
            print(f"País con código {codigo} modificado a '{nuevo_nombre}'")
            return True
    print(f"Error: No se encontró un país con código {codigo}")
    return False
def modificar_ciudad():
    global paises, ciudades
    cod_pais = input("Ingrese el código del país: ")
    cod_ciudad = input("Ingrese el código de la ciudad: ")
    nuevo_nombre = input("Ingrese el nuevo nombre de la ciudad: ")
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    for ciudad in ciudades:
        if ciudad[0]==cod_pais and ciudad[1]==cod_ciudad:
            ciudad[2]=nuevo_nombre
            print(f"Ciudad con código {cod_ciudad} en país {cod_pais} modificada a '{nuevo_nombre}'")
            return True
    print(f"Error: No se encontró la ciudad con código {cod_ciudad} en el país {cod_pais}")
    return False
def modificar_restaurante():
    global paises, ciudades, restaurantes, menus, productos
    cod_pais = input("Ingrese el código del país: ")
    cod_ciudad = input("Ingrese el código de la ciudad: ")
    cod_rest = input("Ingrese el código del restaurante: ")
    nuevo_nombre = input("Ingrese el nuevo nombre del restaurante: ")
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
def modificar_menu():
    global paises, ciudades, restaurantes, menus
    cod_pais=input("Ingrese el código del país: ")
    cod_ciudad=input("Ingrese el código de la ciudad: ")
    cod_rest=input("Ingrese el código del restaurante: ")
    cod_menu=input("Ingrese el código del menú: ")
    nuevo_nombre=input("Ingrese el nuevo nombre del menú: ")
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
def modificar_producto():
    global paises, ciudades, restaurantes, menus, productos
    cod_pais=input("Ingrese el código del país: ")
    cod_ciudad=input("Ingrese el código de la ciudad: ")
    cod_rest=input("Ingrese el código del restaurante: ")
    cod_menu=input("Ingrese el código del menú: ")
    cod_producto=input("Ingrese el código del producto: ")
    nuevo_nombre=input("Ingrese el nuevo nombre del producto: ")
    nuevas_calorias=input("Ingrese las nuevas calorías (o deje vacío para no cambiar): ") or 0
    nuevo_precio=input("Ingrese el nuevo precio (o deje vacío para no cambiar): ") or 0
    cod_pais=normalizar_codigo(cod_pais)
    cod_ciudad=normalizar_codigo(cod_ciudad)
    cod_rest=normalizar_codigo(cod_rest)
    cod_menu=normalizar_codigo(cod_menu)
    cod_producto=normalizar_codigo(cod_producto)
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
def modificar_cliente():
    global clientes
    cedula=input("Ingrese la cedula del cliente: ")
    nuevo_nombre=input("Ingrese el nuevo nombre del cliente: ")
    cedula=normalizar_codigo(cedula)
    for cliente in clientes:
        if cliente[0]==cedula:
            cliente[1]=nuevo_nombre
            print(f"Cliente con cédula {cedula} modificado a '{nuevo_nombre}'")
            return True
    print(f"Error: No se encontró un cliente con cédula {cedula}")
    return False
#______________________________________________________________________________________________________________________#
#BUSQUEDAS_____________________________________________________________________________________________________________#
def buscar_pais(): #FUNCIONA
    global paises
    print("\n Has seleccionado buscar Pais.")
    codigo=input("Ingrese el codigo del pais a buscar: ")
    codigo=normalizar_codigo(codigo)
    resultados=[pais for pais in paises if codigo.lower() in pais[0].lower()]
    if resultados:
        print("\n Resultados de la búsqueda:")
        for pais in resultados:
            print(f"Código: {pais[0]}, Nombre: {pais[1]}")
    else:
        print(f"No se encontraron países con el nombre '{codigo}'.")
def buscar_ciudad(): #FUNCIONA
    global ciudades
    print("Has seleccionado buscar Ciudad.")
    codigo = input("Ingrese el codigo de la ciudad a buscar: ")
    codigo=normalizar_codigo(codigo)
    resultados=[ciudad for ciudad in ciudades if codigo.lower() in ciudad[1].lower()]
    if resultados:
        print("\n Resultados de la búsqueda:")
        for ciudad in resultados:
            print(f"Código: {ciudad[1]}, Nombre: {ciudad[2]}")
    else:
        print(f"No se encontraron países con el codigo '{codigo}'.")
def buscar_rest():
    global restaurantes, contador_busquedas_rest
    print("Has seleccionado buscar Restaurante.")
    codigo = input("Ingrese el codigo del restaurante: ")
    codigo=normalizar_codigo(codigo)
    resultados=[rest for rest in restaurantes if codigo==rest[2].lower()]
    if resultados:
        for rest in resultados:
            nombre_restaurante=rest[3]
            encontrado=False
            for contador in contador_busquedas_rest:
                if contador[0]==nombre_restaurante:
                    contador[1]+=1
                    encontrado=True
                    break
            if not encontrado:
                contador_busquedas_rest.append([nombre_restaurante, 1])

    if resultados:
        print("\nResultados de la búsqueda:")
        for rest in resultados:
            print(f"País: {rest[0]}, Ciudad: {rest[1]}, Código: {rest[2]}, Nombre: {rest[3]}")
        return resultados[0][3]
    else:
        print(f"No se encontraron restaurantes con el nombre '{codigo}'.")
def buscar_menu(): #FUNCIONA
    global menus, contador_busquedas_menu
    print("Has seleccionado buscar Menu.")
    codigo=input("Ingrese el codigo del menu: ")
    codigo=normalizar_codigo(codigo)
    resultados=[menu for menu in menus if codigo.lower() in menu[3].lower()]
    if resultados:
        for menu in menus:
            codigo_menu=menu[3]
            encontrado=False
            for contador in contador_busquedas_menu:
                if contador[0]==codigo_menu:
                    contador[1]+=1
                    encontrado=True
                    break
            if not encontrado:
                contador_busquedas_menu.append([codigo_menu, 1])
    if resultados:
        print("\nResultados de la búsqueda:")
        for menu in resultados:
            print(
                f"País: {menu[0]}, Ciudad: {menu[1]}, Restaurante: {menu[2]}, Código: {menu[3]}, Nombre: {menu[4]}")
    else:
        print(f"No se encontraron menús con el nombre '{codigo}'.")
def buscar_produ(retornar_precio=False): #FUNCIONA
    global productos
    print("Has seleccionado buscar Productos.")
    codigo=input("Ingrese el codigo del producto: ")
    codigo=normalizar_codigo(codigo)
    resultados=[prod for prod in productos if codigo.lower() in prod[4]]
    if retornar_precio:
        if resultados:
            return resultados[0][7]  # Retorna el precio
        else:
            return None
    if resultados:
        print("\nResultados de la búsqueda: ")
        for prod in resultados:
            print(
                f"País: {prod[0]}, Ciudad: {prod[1]}, Restaurante: {prod[2]}, Menú: {prod[3]}, "
                +
                f"Código: {prod[4]}, Nombre: {prod[5]}, Calorias : kcal {prod[6]}, Precio:${prod[7]}")
    else:
        print(f"No se encontraron productos con el nombre '{codigo}'.")
def buscar_cliente():
    global clientes
    print("Has seleccionado buscar Clientes.")
    cedula = int(input("Ingrese la cédula del cliente a buscar: "))
    cedula_a_buscar = str(cedula)
    resultados=[cliente for cliente in clientes if cliente[0] == cedula_a_buscar]
    if resultados:
        print("\n Resultaods de la busqueda: ")
        for cliente in resultados:
            print(f"Cliente encontrado: Cedula: {cliente[0]}, Nombre: {cliente[1]}")
            return cliente
    else:
        print(f"Cliente no encontrado con cedula '{cedula_a_buscar}'.")
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
def insertar_en_lista(lista, nuevo_registro, indices_unicos=None):
    print(f"Insertando: {nuevo_registro}")
    print(f"Lista actual: {lista}")
    if not isinstance(lista, list) or not isinstance(nuevo_registro, list):
        print("Error: Los parámetros deben ser listas")
        return False
    if indices_unicos is not None:
        for i in range(len(lista)):
            coincide=True
            for ix in indices_unicos:
                if lista[i][ix]!=nuevo_registro[ix]:
                    coincide=False
                    break
            if coincide:
                valores=[nuevo_registro[ix] for ix in indices_unicos]
                print(f"Error: Ya existe un registro con los valores {valores}")
                return False
    lista.append(nuevo_registro)
    print(f"Registro insertado correctamente: {nuevo_registro}")
    return True
def insertar_pais():
    global paises
    print("Lista actual:", paises)
    cod_pais=input("Ingrese el codigo del pais: ")
    nombre=input("Ingrese el nombre del pais: ")
    resultado=insertar_en_lista(paises, [str(cod_pais), nombre], indices_unicos=[0])
    if resultado:
        print(f"Registro insertado correctamente: {paises}")
    return resultado

def insertar_ciudad():
    global paises, ciudades
    print(ciudades)
    cod_pais=input("Ingrese el código del país: ")
    if not validar_pais_existe(cod_pais):
        return False
    cod_ciudad=input("Ingrese el código de la ciudad: ")
    nombre=input("Ingrese el nombre de la ciudad: ")
    resultado=insertar_en_lista(ciudades, [str(cod_pais), str(cod_ciudad), nombre], indices_unicos=[0, 1])
    if resultado:
        print(f"Registro insertado correctamente: {ciudades}")
    return resultado
def insertar_restaurante():
    global paises, ciudades, restaurantes
    print(restaurantes)
    cod_pais=input("Ingrese el código del país: ")
    if not validar_pais_existe(cod_pais):
        return False
    cod_ciudad=input("Ingrese el código de la ciudad: ")
    if not validar_ciudad_existe(cod_pais, cod_ciudad):
        return False
    cod_rest=input("Ingrese el código del restaurante: ")
    nombre=input("Ingrese el nombre del restaurante: ")
    resultado=insertar_en_lista(restaurantes, [str(cod_pais), str(cod_ciudad), str(cod_rest), nombre], indices_unicos=[0, 1, 2])

    if resultado:
        print(f"Registro insertado correctamente: {restaurantes}")
    return resultado
def insertar_menu():
    global paises, ciudades, restaurantes, menus
    cod_pais=input("Ingrese el código del país: ")
    if not validar_pais_existe(cod_pais):
        return False
    cod_ciudad=input("Ingrese el código de la ciudad: ")
    if not validar_ciudad_existe(cod_pais, cod_ciudad):
        return False
    cod_rest=input("Ingrese el código del restaurante: ")
    if not validar_restaurante_existe(cod_pais, cod_ciudad, cod_rest):
        return False
    cod_menu=input("Ingrese el código del menú: ")
    nombre=input("Ingrese el nombre del menú: ")
    resultado=insertar_en_lista(menus, [str(cod_pais), str(cod_ciudad), str(cod_rest), str(cod_menu), nombre],indices_unicos=[0, 1, 2, 3])

    if resultado:
        print(f"Registro insertado correctamente: {menus}")
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
                if y==1:buscar_pais()
                elif y==2:buscar_ciudad()
                elif y==3:buscar_rest()
                elif y==4:buscar_menu()
                elif y==5:buscar_produ()
                elif y==6:buscar_cliente()
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