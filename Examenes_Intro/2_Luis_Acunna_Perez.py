#Luis Andres Acunna Perez
#Segundo examen parcial

#funciones auxiliares copiadas y pegadas del archivo de la profe:
#validacion de matriz
def ValidaMatriz(matriz):
    a = 0
    b = 0
    if matriz == []:
        return False
    elif matriz[0] == [] and matriz[1] == []:
        return "La matriz no es valida"
    else:
        for i in range(len(matriz)):
            if matriz == []:
                a = 1
            elif matriz[0] == []:
                a = 1
            elif len(matriz[0]) != len(matriz[1]):
                return False
            matriz = matriz + [matriz[0]]
            matriz = matriz[1:]
    if a == b:
        return True
    else:
        return False
# validacion de conjuntos NO es conjunto
def conjunto(lista):  # [3,2,1,3]
    largo = 0  # 0
    pos = 0  # 0

    # largo      pos       lista
    while largo < len(lista):  # Afuera o Externo mas lento
        while pos < len(lista):  # Adentro o Interno, corre mas rapido
            if largo != pos:  #
                if lista[pos] == lista[largo]:
                    return (False)
                else:
                    pos = pos + 1
            else:
                pos = pos + 1
        # Antes del externo
        pos = 0
        largo = largo + 1
    return (True)


#primera funcion
def UNO(lista):
    if isinstance(lista, list):
    pass

def DOS:
    pass

def TRES:
    pass

def CUATRO:
    pass
