#Luis Andrés Acuña Pérez
#Verificacion #3

def procesar_archivo():

    lista_principal=[]

    with open("lineas.txt", 'r') as archivo:
        for linea in archivo:
            lista_palabras=linea.strip().split(" ")   # Para dividir la línea por espacios para obtener lista de palabras
            lista_principal.append(lista_palabras)      # Agregar la lista de palabras a la lista principal
    print(lista_principal)

procesar_archivo()