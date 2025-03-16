
def verificar_pais_existe(nombre_archivo, pais_buscar):
    nombre_archivo = "Paises.txt"
    pais_buscar = input("Ingrese el nombre del pais a buscar: ")
    try:
        with open("Paises.txt", "r") as archivo: #abrir el archivo
            datos = [] #Crea lista para guardar los datos

            # Leemos el archivo línea por línea
            for linea in archivo:
                # Eliminamos espacios en blanco al inicio y final
                linea = linea.strip()

                # Ignoramos líneas vacías
                if not linea:
                    continue

                # Separamos por punto y coma
                elementos = linea.split(";")

                # Verificamos que la línea tenga al menos 3 elementos
                if len(elementos) >= 3:
                    datos.append(elementos)

            # Buscamos el país en el subíndice 2 (tercera posición)
            for fila in datos:
                if fila[2].lower() == pais_buscar.lower():
                    return True

            # Si llegamos aquí, no se encontró el país
            return False

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {nombre_archivo}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False



def verificar_ciudad_existe():
    # Especificamos la ruta exacta del archivo
    nombre_archivo = "Ciudades.txt"

    # Pedimos al usuario que ingrese la ciudad a buscar
    ciudad_buscar = input("Ingrese el nombre de la ciudad a buscar: ")

    try:
        # Abrimos el archivo específico
        with open(nombre_archivo, "r") as archivo:
            # Leemos el archivo línea por línea
            for linea in archivo:
                # Eliminamos espacios en blanco y saltos de línea
                linea = linea.strip()

                # Ignoramos líneas vacías
                if not linea:
                    continue

                # Separamos por punto y coma
                elementos = linea.split(";")

                # Verificamos que tengamos al menos 3 elementos y que el tercer elemento
                # sea igual a la ciudad buscada (sin importar mayúsculas/minúsculas)
                if len(elementos) >= 3 and elementos[2].lower() == ciudad_buscar.lower():
                    print(f"¡La ciudad '{ciudad_buscar}' fue encontrada! Código: {elementos[1]}")

                    return True

            # Si terminamos de revisar todo el archivo y no encontramos la ciudad
            print(f"La ciudad '{ciudad_buscar}' no existe en el archivo.")
            return False

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        print("Asegúrate de que el archivo exista en la ruta correcta.")
        return False

# Llamamos a la función para ejecutarla
verificar_ciudad_existe()