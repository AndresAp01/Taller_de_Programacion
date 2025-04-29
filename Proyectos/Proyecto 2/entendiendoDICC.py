#Archivo para entender los putisimos diccionarios
"""
diccionario = {
    "persona1": {
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Madrid",
        "lenguajes": ["Python", "Java", "C++"]
        },
    "persona2":{
        "nombre": "Andy",
        "edad": 40,
        "ciudad": "Madrid",
        "lenguajes": ["Python", "Java", "C++"]
        }
    }
diccionario["persona1"]["edad"]=26

print (diccionario)
print(list(diccionario))
for clave in diccionario:
    print(clave, diccionario[clave])

for diccionario_interno in diccionario.values():
    for valor_interna in diccionario_interno.values():
        print(valor_interna)

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

