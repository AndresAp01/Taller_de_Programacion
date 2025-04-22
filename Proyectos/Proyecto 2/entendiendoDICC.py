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
