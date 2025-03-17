#/////////////////////MENU

def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Buscar datos")
    print("2. Insertar datos")
    print("3. Salir")
    return input("Seleccione una opción: ")

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        dato = input("Ingrese el nombre o código a buscar: ")
        print(buscar_en_lista(ciudades, 2, dato))  # Buscar ciudades

    elif opcion == "2":
        nuevo_pais = (input("Código de país: "), input("Nombre del país: "))
        insertar_dato(paises, nuevo_pais)

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")

