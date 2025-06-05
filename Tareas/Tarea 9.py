#Luis Andres Acunna Perez
#Tarea #9
#Pasalista
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

#CUENTA PARES E IMPARES
def cuentaPares_RC(num):
    return cuentaPares_RC_aux(num, 0)

def cuentaPares_RC_aux(num, cont):
    if num==0:
        return cont
    elif num%10%2==0:
        return cuentaPares_RC_aux(num//10, cont+1)
    else:
        return cuentaPares_RC_aux(num//10, cont)

def cuentaImpares(num):
    return cuentaImpares_RC_aux(num, 0)

def cuentaImpares_RC_aux(num, cont):
    if num==0:
        return cont
    elif num%10%2==1:
        return cuentaImpares_RC_aux(num//10, cont+1)
    else:
        return cuentaImpares_RC_aux(num//10, cont)

#PRomedio
def PromedioPares_ImparesRP(num):
    if type(num)==int:
        num=abs(num)
        lista=Pasalista(num)
        if num==0:
            return ("Par:,0, impar:, 0")
        else:
            return [Promedio_Pares_Aux(lista, 0, 0) / cuentaPares_RC(num), Promedio_Impares_Aux(lista, 0, 0) / cuentaImpares_RC_aux(num, 0)]
    else:
        print ("Parametro incorrecto")

def Promedio_Pares_Aux(lista, lista_nueva, i):
    if i>=len(lista):
        return lista_nueva
    elif lista[i]%2==0:
        return Promedio_Pares_Aux(lista, lista_nueva+lista[i]**2, i+1)
    else:
        return Promedio_Pares_Aux(lista, lista_nueva, i+1)

def Promedio_Impares_Aux(lista, lista_nueva, i):
    if i>=len(lista):
        return lista_nueva
    elif lista[i]%2!=0:
        return Promedio_Impares_Aux(lista, lista_nueva+lista[i]**3, i+1)
    else:
        return Promedio_Impares_Aux(lista, lista_nueva, i+1)

