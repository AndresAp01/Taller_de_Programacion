#Archivo para entender los putisimos diccionarios

diccionario = {
    "persona1": {
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Madrid",
        "lenguajes": ["Python", "Java", "C++"]
        },
    "persona2":{
        "nombre": "Andy",
        "edad": 40,
        "ciudad": "Madrid",
        "lenguajes": ["Python", "Java", "C++"]
        }
    }
diccionario["persona1"]["edad"]=26

print (diccionario)
print(list(diccionario))
for clave in diccionario:
    print(clave, diccionario[clave])

for diccionario_interno in diccionario.values():
    for valor_interna in diccionario_interno.values():
        print(valor_interna)
