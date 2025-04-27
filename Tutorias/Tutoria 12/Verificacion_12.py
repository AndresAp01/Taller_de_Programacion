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
    else:
        palabras[palabra] = {"inglés": ingles, "francés": frances, "portugués": portugues}

# Función de eliminar
def eliminar(palabra):
    if not buscar(palabra):
        return "Error, la palabra no existe."
    else:
        del palabras[palabra]

print(buscar("manzana"))

print(insertar("casa", "house", "maison", "casa"))

print(modificar("perro", "doggy", "chien", "cachorrinho"))

print(eliminar("casa"))