##

def cargar_datos(nombre_archivo, cantidad_campos):
    """Carga un archivo .txt en una lista de tuplas"""
    with open(nombre_archivo, "r") as archivo:
        return [tuple(linea.strip().split(";")) for linea in archivo if len(linea.strip().split(";")) == cantidad_campos]

# Cargar todos los archivos
paises = cargar_datos("Paises.txt", 2)
ciudades = cargar_datos("Ciudades.txt", 3)
restaurantes = cargar_datos("Restaurantes.txt", 4)
menus = cargar_datos("Menu.txt", 5)
productos = cargar_datos("Productos.txt", 7)
clientes = cargar_datos("Clientes.txt", 2)

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

def insertar_dato(lista, nuevo_dato):
    """Inserta un nuevo dato en la lista si no está repetido"""
    if nuevo_dato not in lista:
        lista += [nuevo_dato]  # Agrega a la lista
        print("✅ Dato insertado correctamente.")
    else:
        print("❌ Error: Ya existe en la lista.")

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
"""
✅ **Explicación:**  
- **Ejecuta el menú en un ciclo infinito (`while True`).**  
- **Permite buscar datos y agregarlos fácilmente.**  
- **Muestra errores si la opción es incorrecta.**  

---

## **📌 Beneficios de esta versión**
| **Aspecto** | **Beneficio** |
|------------|-------------|
| Código corto | Menos líneas, más claro. |
| Modularidad | Funciones reutilizables para búsqueda e inserción. |
| Menú fácil | Solo 3 opciones, sin código complejo. |
| Evita errores | Se validan entradas antes de agregarlas. |
| Búsqueda flexible | Función que sirve para cualquier lista. |

---

## **📌 Resumen final**
🔹 **Carga los archivos en listas de tuplas automáticamente.**  
🔹 **Menú fácil de entender y navegar.**  
🔹 **Funciones reutilizables para búsqueda e inserción.**  
🔹 **No usa estructuras avanzadas (solo listas y tuplas).**  

💡 **Si quieres algo todavía más simple, dime y lo ajustamos más.** 😊 🚀"""