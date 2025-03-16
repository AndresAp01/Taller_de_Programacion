

def mostrar_menu(opciones, titulo):
    """Muestra un menú numerado en consola."""
    print(f"\n=== {titulo} ===")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

def buscar_pais():
    """Busca un país en la lista de países."""
    pais = input("Ingrese el nombre o código del país a buscar: ").strip()
    resultado = [p for p in paises if pais.lower() in p[1].lower() or pais == p[0]]
    if resultado:
        print("✅ País encontrado:", resultado)
    else:
        print("❌ País no encontrado.")

def buscar_ciudad():
    """Busca una ciudad en la lista de ciudades."""
    ciudad = input("Ingrese el nombre o código de la ciudad a buscar: ").strip()
    resultado = [c for c in ciudades if ciudad.lower() in c[2].lower() or ciudad == c[1]]
    if resultado:
        print("✅ Ciudad encontrada:", resultado)
    else:
        print("❌ Ciudad no encontrada.")

def buscar_restaurante():
    """Busca un restaurante en la lista de restaurantes."""
    rest = input("Ingrese el nombre o código del restaurante a buscar: ").strip()
    resultado = [r for r in restaurantes if rest.lower() in r[3].lower() or rest == r[2]]
    if resultado:
        print("✅ Restaurante encontrado:", resultado)
    else:
        print("❌ Restaurante no encontrado.")

def buscar_menu():
    """Busca un menú en la lista de menús."""
    menu = input("Ingrese el nombre o código del menú a buscar: ").strip()
    resultado = [m for m in menus if menu.lower() in m[4].lower() or menu == m[3]]
    if resultado:
        print("✅ Menú encontrado:", resultado)
    else:
        print("❌ Menú no encontrado.")

def menu_busqueda():
    """Menú de búsqueda de elementos en la base de datos."""
    opciones = ["País", "Ciudad", "Restaurante", "Menú", "Regresar"]
    while True:
        mostrar_menu(opciones, "Búsqueda de Datos")
        try:
            seleccion = int(input("Seleccione una opción (1-5): "))
            if seleccion == 1:
                buscar_pais()
            elif seleccion == 2:
                buscar_ciudad()
            elif seleccion == 3:
                buscar_restaurante()
            elif seleccion == 4:
                buscar_menu()
            elif seleccion == 5:
                print("🔙 Volviendo al menú principal...")
                break
            else:
                print("❌ Opción inválida, intente de nuevo.")
        except ValueError:
            print("❌ Entrada no válida, ingrese un número.")

def menu_principal():
    """Menú principal del sistema."""
    opciones = ["Insertar Datos", "Buscar Datos", "Salir"]
    while True:
        mostrar_menu(opciones, "Mantenimiento de Base de Datos")
        try:
            seleccion = int(input("Seleccione una opción (1-3): "))
            if seleccion == 1:
                print("🔧 Función de inserción aún no implementada.")
            elif seleccion == 2:
                menu_busqueda()
            elif seleccion == 3:
                print("👋 Saliendo del sistema...")
                break
            else:
                print("❌ Opción inválida, intente de nuevo.")
        except ValueError:
            print("❌ Entrada no válida, ingrese un número.")

# Listas globales de datos (deben cargarse desde archivos en el proyecto real)
paises = open('Archivos/Paises.txt', 'r')
ciudades = [("10", "123", "San José"), ("20", "456", "CDMX")]
restaurantes = [("10", "123", "789", "Restaurante Tico")]
menus = [("10", "123", "789", "001", "Menú Ejecutivo")]



# Ejecutar el menú principal
menu_principal()