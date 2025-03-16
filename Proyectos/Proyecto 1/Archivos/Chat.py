### **🔥 Forma más optimizada y sencilla para estudiantes novatos**
### **📌 1. Cargar los archivos**

def cargar_datos(nombre_archivo, cantidad_campos):
    """Carga un archivo .txt en una lista de tuplas"""
    with open(nombre_archivo, "r") as archivo:
        return [tuple(linea.strip().split(";")) for linea in archivo if len(linea.strip().split(";")) == cantidad_campos]

# Cargar todos los archivos
paises = cargar_datos("Paises.txt", 2)
ciudades = cargar_datos("Ciudades.txt", 3)
restaurantes = cargar_datos("Restaurantes.txt", 4)
menus = cargar_datos("Menú.txt", 5)
productos = cargar_datos("Productos.txt", 7)
clientes = cargar_datos("Clientes.txt", 2)

### **📌 2. Menú principal**

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n=== Menú Principal ===")
    print("1. Buscar datos")
    print("2. Insertar datos")
    print("3. Salir")
    return input("Seleccione una opción: ")


def buscar_en_lista(lista, campo, valor):
    """Busca un valor en una lista de tuplas en un campo específico"""
    resultados = [fila for fila in lista if fila[campo].lower() == valor.lower()]
    return resultados if resultados else "❌ No encontrado."

# Uso
print(buscar_en_lista(ciudades, 2, "San José"))  # Busca ciudad por nombre
print(buscar_en_lista(paises, 1, "México"))      # Busca país por nombre

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        dato = input("Ingrese el nombre o código a buscar: ")
        print(buscar_en_lista(ciudades, 2, dato))  # Buscar ciudades

    elif opcion == "2":
        nuevo_pais = (input("Código de país: "), input("Nombre del país: "))
        insertar_dato(paises, nuevo_pais)

    elif opcion == "3":
        print("👋 Saliendo del programa...")
        break

    else:
        print("❌ Opción no válida.")
