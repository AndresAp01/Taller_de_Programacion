#Luis Andres Acunna Perez

#ORDEN DE FUNCIONES
"""
    1. Pasalista principal y aux RECIBE NUM
    2. CuentaPares: Recibe numero tal tal
    3. CuentaImpares: Recibe numero tal tal
    4. PromedioPares_Impares: Recibe numero
    5. PromedioPares_aux: Recibe lista

"""
#******************Pasa lista Pila
def Pasalista(num):
    if type(num)==int:
        num=abs(num)
        if num>=0 and num<10:
            return [num]
        else:
            return Pasalista_aux(num)
    else:
        print("Parametro incorrecto")

def Pasalista_aux(num):
    if num==0:
        return []
    else:
        return Pasalista_aux(num//10)+[num%10]


def cuentaPares(num):
    if num==0:
        return 0
    elif num%10%2==0:
        return 1+cuentaPares(num//10)
    else:
        return cuentaPares(num//10)

def cuentaImpares(num):
    if num==0:
        return 0
    elif num%10%2==1:
        return 1+cuentaImpares(num//10)
    else:
        return cuentaImpares(num//10)


def PromedioPares_aux(lista):
    if lista==[]:
        return 0
    elif lista[0]%2==0:
        return PromedioPares_aux(lista[1:])+lista[0]**2
    else:
        return PromedioPares_aux(lista[1:])

def PromedioImpares_aux(lista):
    if lista==[]:
        return 0
    elif lista[0]%2!=0:
        return PromedioImpares_aux(lista[1:])+lista[0]**3
    else:
        return PromedioImpares_aux(lista[1:])  # Llamada recursiva
#print(PromedioImpares_aux([3,4,5,6,7,8,9]))

def PromedioPares_Impares(num):
    if type(num)==int:
        if num==0:
            return ("Promedio pares: ", 0, "Promedio impares: ", 0)
        else:
            lista=Pasalista(abs(num))
            return [PromedioPares_aux(lista)/cuentaPares(num),
                    PromedioImpares_aux(lista)/cuentaImpares(num)]
    else:
        print("Parametro incorrecto")

#print(PromedioPares_Impares(3456789))