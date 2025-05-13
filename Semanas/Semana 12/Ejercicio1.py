#Luis Acunna Perez
from Auxiliares import Pasalistacola
from Auxiliares import Largo

#import Auxiliares
def ParesCD(num):
    if type(num)==int:
        ListaNueva=Pasalistacola(abs(num))
        if ListaNueva==[0]:
            return [0]
        else:
            return ParesCD_aux(ListaNueva,[])

def ParesCD_aux(lista, LNueva):
    if lista==[]:
        return LNueva
    elif lista[0]%2==0:
        return ParesCD_aux(lista[1:], LNueva+[lista[0]])
    else:
        return ParesCD_aux(lista[1:], LNueva)

