#Archivo para entender los putisimos diccionarios

diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "lenguajes": ["Python", "Java", "C++"],
    }

items = diccionario.values()
print(items)

diccionario.pop("edad")
print(diccionario)

diccionario.update({"pais": "España"})
print(diccionario)

print(list(diccionario))

def construir_diccionario(ruta_archivo):
    diccionario = {}
    try:
        with open(ruta_archivo) as archivo:
            for linea in archivo:
                codigo, nombre=linea.strip().split(";")
                diccionario[codigo]={"nombre": nombre, "ciudades": {}}

        with open(ruta_archivo) as f:
            for linea in f:
                cp, cc, nc = linea.strip().split(";")
                if cp in diccionario:
                    diccionario[cp]["ciudades"][cc] = {"nombre": nc, "restaurantes": {}}

        with open(ruta_archivo) as f:
            for linea in f:
                cp, cc, cr, nr = linea.strip().split(";")
                if cp in diccionario and cc in diccionario[cp]["ciudades"]:
                    diccionario[cp]["ciudades"][cc]["restaurantes"][cr] = nr

        return diccionario
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no existe")
        return None
diccionario=construir_diccionario("Paises.txt", "Ciudades.txt", "Restaurantes.txt")
print(diccionario)
