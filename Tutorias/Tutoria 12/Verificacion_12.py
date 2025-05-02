#Luis Andres Acunna Perez verificacion 12
palabras = {
    "manzana": {
        "inglés": "apple",
        "francés": "pomme",
        "portugués": "maçã"
    },
    "perro": {
        "inglés": "dog",
        "francés": "chien",
        "portugués": "cachorro"
    },
    "casa": {
        "inglés": "house",
        "francés": "maison",
        "portugués": "casa"
    },
    "libro": {
        "inglés": "book",
        "francés": "livre",
        "portugués": "livro"
    },
    "agua": {
        "inglés": "water",
        "francés": "eau",
        "portugués": "água"
    }
}

def buscar(palabra):
    try:
        return palabras[palabra]
    except KeyError:
        return False

# Función de insertar
def insertar(palabra, ingles, frances, portugues):
    if buscar(palabra):
        return "Error, la palabra ya existe."
    else:
        palabras[palabra] = {"inglés": ingles, "francés": frances, "portugués": portugues}

# Función de modificar
def modificar(palabra, ingles, frances, portugues):
    if not buscar(palabra):
        return "Error, la palabra no existe."
    palabras[palabra]={"inglés": ingles, "francés": frances, "portugués": portugues}
    return "Modificado correctamente."

# Función de eliminar
def eliminar(palabra):
    if not buscar(palabra):
        return "Error, la palabra no existe."
    del palabras[palabra]
    return "Eliminado correctamente."

"""print(buscar("manzana"))

print(insertar("casa", "house", "maison", "casa"))

print(modificar("perro", "doggy", "chien", "cachorrinho"))

print(eliminar("casa"))"""

#MENU
while True:
    op = input("---MENU---\n 1. Insercion, 2. Busqueda, 3. Modificacion, 4. Eliminacion, 5. Ver inventario, 6. Salir")
    #INSERTAR
    if op == "1":
        palabra = str(input("Ingrese la palabra en español: "))
        ingles = str(input("Ingrese la traducción al inglés: "))
        frances = str(input("Ingrese la traducción al francés: "))
        portugues = input("Ingrese la traducción al portugués: ")
        try:
            resultado=insertar(palabra, ingles, frances, portugues)
            print("Insercion exitosa")
        except ValueError:
            input("Error, no es una palabra")
    #BUSCAR
    elif op == "2":
        palabra = input("Ingrese la palabra a buscar: ")
        resultado = buscar(palabra)
        if resultado:
            print(f"Traducciones de '{palabra}': {resultado}")
        else:
            print("La palabra no existe.")
        print(buscar(palabra))
    #MODIFICAR
    elif op == "3":
        palabra = input("Ingrese la palabra a modificar: ").strip().lower()
        ingles = input("Nueva traducción al inglés: ")
        frances = input("Nueva traducción al francés: ")
        portugues = input("Nueva traducción al portugués: ")
        resultado=modificar(palabra, ingles, frances, portugues)
        if resultado:
            input("Modificado correctamente")
        else:
            print(" La palabra no existe")
    elif op == "4":
        palabra = input("Ingrese la palabra a eliminar: ")
        if buscar(palabra):
            confirmar = input("Seguro que desea eliminarla? (s/n): ")
            if confirmar.lower() == "s":
                print(eliminar(palabra))
            else:
                print("Operación cancelada.")
        else:
            print("La palabra no existe.")
    elif op == "5":
        print(palabras)
    elif op == "6":
        break