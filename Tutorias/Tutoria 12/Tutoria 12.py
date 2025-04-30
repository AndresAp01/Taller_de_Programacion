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

#MENU
while True:
    op = input("---MENU---\n 1. Insercion, 2. Busqueda, 3. Modificacion, 4. Eliminacion, 5. Ver inventario, 6. Salir")
    if op == "1":
        codigo = input("Ingrese el codigo: ")
        nombre = input("Ingrese el nombre: ")
        try:
            cantidad=int(input("Ingrese la cantidad: "))
            insertar(codigo, nombre, cantidad)
            print("Insercion exitosa")
        except ValueError:
            input("Error, no es un numero.")
    elif op == "2":
        codigo = input("Ingrese el codigo: ")
        resultado=buscar(codigo)
        if resultado:
            nombre=resultado["nombre"]
            cantidad=resultado["cantidad"]
            print(f"El producto existe: {nombre}, canditad: {cantidad}")
        else:
            input("El codigo no existe")
        print(buscar(codigo))
    elif op == "3":
        codigo=input("Ingrese el codigo: ")
        nombre=input("Ingrese el nombre: ")
        try:
            cantidad=int(input("Ingrese la cantidad: "))
            resultado=modificar(codigo, nombre, cantidad)
            if resultado:
                input("Modificado correctamente")
            else:
                print("El codigo no existe")
        except ValueError:
            input("Error, no es un numero.")
    elif op == "4":
        codigo=input("Ingrese el codigo: ")
        resultado=buscar(codigo)
        if resultado:
            op=input"Seguro que sdesea eliminarlo? s/n"
            if op.upper() == "s":
                eliminar(codigo)
                print("Eliminado correctamente")
            elif op.upper()=="n":
                input("Operacion cancelada")
            else:
                input("Error, no es una opcion valida")
        else:
            input("El codigo no existe")
    elif op == "5":
        print(inventario)
    elif op == "6":
        break


