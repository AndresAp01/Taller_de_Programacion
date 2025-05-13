#Luis Acunna Perez
#Taller
from Auxiliares import Pasalistacola
from Auxiliares import Largo
#Escrbir
def ParesCD(num):
    if type(num)==int:
        lista=Pasalistacola(abs(num))
        if lista==[0]:
            return [0]
        else:
            return ParesCD_pila(lista)
            

def ParesCD_pila(lista):
    print(lista)
    if lista==[]:
        return []
    elif lista[0]%2==0:
        return [lista[0]]+ParesCD_pila(lista[1:])
    else:
        return ParesCD_pila(lista[1:])
        
print(ParesCD(62345))
