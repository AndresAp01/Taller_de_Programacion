"""
Listas, splits y archivos

Las lsitas son una estructura de datos permiten almacenar colecciones
de elementos, puede ser de cualquier tipo y son mutables
podemos tener una lista y dentro otra lista
mutables es que se pueden cambiar

lista_vacia = []
lista = [dato_1, dato_2, ..., dato_n]

#agregar al inicio
    lista = [elemento] + lista
    lista = lista + [elemento]


"""
#Lee un archivo llamado texto.txt, separa las palabras de cada linea y las almaca en una lsita

def Ejercicio1():
    obj_arch = open("objeto.txt", "r")
    matriz_palabras = []
    texto = obj_arch.read()
    lista_lineas = texto.split("\n")
    i=0
    while i < len(lista_lineas):
        matriz_palabras += [lista_lineas[i].split(" ")]
        i+=1
    print(matriz_palabras)
    obj_arch.close()
Ejercicio1()

#Ejercicio1()
#lea u archivo nombre, edad
#almacena los nombres en una lista y guiarda las edades en otro archivo

def ejercicio2():
    obj_arch = open("datos.txt", "r")
    texto = obj_arch.read()
    lista_lineas = texto.split("\n")
    lista_nombres = []
    lista_edades = []
    archivo_edades = open("edades.txt", "a")

    i = 0
    while i < len(lista_lineas):
        lista_nombres += [lista_lineas[i].split(",")[0]]
        #print(lista_lineas[i]) #para ver cual es el error
        archivo_edades.write(lista_lineas[i].split(",")[1]+"\n")
        i += 1
    print(lista_nombres)
    archivo_edades.close()
#ejercicio2()

#ejercicio3 lee un archivo.txt que selecciona las palabras con mas
# de 5 caract y las guarda en un archivo llamado palabras_largas.txt

def cuenta_car(str):
    cant = 0
    while str != "":
        cant += 1
        str = str[1:]

    return cant

def ejercicio3():
    obj_arch = open("objeto.txt", "r")
    texto = obj_arch.read()
    lista_lineas = texto.split("\n")
    archivo_pal_lar = open("palabras_largas.txt", "w")
    pal_lar = ""
    i = 0
    while i < len(lista_lineas):
        if cuenta_car(lista_lineas[i]) > 5:
            pal_lar += lista_lineas[i] + "\n"
        i += 1
    archivo_pal_lar.write(pal_lar)
    archivo_pal_lar.close()
    obj_arch.close()

ejercicio3()

def ejercicio4():
    obj_arch = open("objeto.txt", "r")
    texto = obj_arch.read()
    lista_palabras = texto.split()
    lista_palabras_cont = []
    print(lista_palabras)
    i = 0
    while i < len(lista_palabras):
        if lista_palabras[i] not in lista_palabras_cont:
            lista_palabras_cont += (lista_palabras[i])
            print(lista_palabras[i] + " :" + str(lista_palabras.count))
    pass

