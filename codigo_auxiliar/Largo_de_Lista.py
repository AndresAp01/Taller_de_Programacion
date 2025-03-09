# Escribir una función que recibe una lista, validar que sea lsita
# Calcular el largo e la lista destruyendo y sin destruir

# Destruyendo
def largolista(lista):  # cualquier lista: [5,6,7,8,1,0]
    if type(lista) == list:  # si pregunto por un int me da error
        if lista == []:  # Preguntamos si la lista es vacía
            return 0
        else:
            cont = 0
            # cont   lista
            # 0      [5,6,7,8,1,0]
            # 1      [6,7,8,1,0]
            # 2      [7,8,1,0]
            # 3      [8,1,0]
            # 4      [1,0]
            # 5      [0]
            # 6      []

            while lista != []:  # [5,6,7,8,1,0] si tiene elementos #[6,7,8,1,0] si  [7,8,1,0] si
                # [8,1,0] si tiene, #[1,0] si [0]si []no
                cont = cont + 1  # 1 #2 #3 #4 #5 #6
                lista = lista[1:]  # [6,7,8,1,0] #[7,8,1,0] #[8,1,0] #[1,0] #[0] #[]
            print(cont, lista)  # 6, []
    else:
        print("Parametro incorrecto")


# Sin destruir
def largoSD(lista):
    if type(lista) == list:  # si pregunto por un int me da error
        if lista == []:  # Preguntamos si la lista es vacía
            return 0
        else:
            cont = 0
            i = 0
            # cont   i   lista
            # 0      0   [5, 6, 7, 8, 1, 0]
            # 1      1   [5, 6, 7, 8, 1, 0]
            # 2      1   [5, 6, 7, 8, 1, 0]
            # 3      3   [5, 6, 7, 8, 1, 0]
            # 4      4   [5, 6, 7, 8, 1, 0]
            # 5      5   [5, 6, 7, 8, 1, 0]
            # 6      6   [5, 6, 7, 8, 1, 0]

            while i < len(lista):  # 0<6si 1<6si 2<6si 3<6si 4<6si 5<6 si 6<6 no
                i = i + 1  # 1 2 3 4 5 6
                cont = cont + 1  # 1 2 3 4 5 6
            print(cont,
                  lista)  # 6, {En este ejercicio la variable i es para posiciones, la cont es un contador, pero justo sale que van las dos igual
            # }
    else:
        print("Parametro incorrecto")