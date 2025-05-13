#Luis Andres Acunna Perez
from Auxiliares import Pasalistacola
from Auxiliares import Largo

def ParesCDSD(num):
    if type(num)==int:
        lista_nueva=Pasalistacola(abs(num))
        if lista_nueva == [0]:
            return [0]
        else:
            return ParesCD_auxSD(lista_nueva, 0, [])

def ParesCD_auxSD(lista, i, nueva):
    if i == len(lista):
        return nueva
    elif lista[i]%2==0:
        return ParesCD_auxSD(lista, i+1, nueva+[lista[i]])
    else:
        return ParesCD_auxSD(lista, i + 1, nueva)
