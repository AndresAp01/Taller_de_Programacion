#Taller de diccionarios
#modificables, indexados, no ordenados
"""diccionario1={'clave1':'valor1'}
diccionario=dict()"""
#para acceder a los valores se usa la clave
#diccionario.get(clave)
#para limpiar el diccionario completo

#keys genera una lista con todas las claves
#values crea una lista con todos los valores


#actividad
def abrir_archivo():
    inventario = dict()
    with open("inventario.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip() == "":
                continue
            lista_linea = linea.strip().split(";")
            inventario[lista_linea[2]] = {
                "nombre": lista_linea[0],
                "precio": float(lista_linea[1])
            }
            print(lista_linea)
    return inventario
inventario = abrir_archivo()
abrir_archivo()

def buscar(codigo):
    try:
        return inventario[codigo]
    except KeyError:
        return False

print(buscar("FVR001"))

def insertar(codigo, nombre, precio):
    if buscar(codigo):
        return "Error, el codigo ya existe."
    else:
        inventario[codigo]={"nombre": nombre, "precio": precio}

def modificar(codigo, nombre, precio):
    if not buscar(codigo):
        return "Error, el codigo ya existe."
    else:
        inventario[codigo] = {"nombre": nombre, "precio": precio}

def eliminar(codigo):
    if not buscar(codigo):
        return "Error, el codigo ya existe."
    else:
        del inventario[codigo]


