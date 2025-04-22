#Escribir 4 funciones 
#El parametro es una lista a validar
#Contar los pares de una lista Recursiom cola sin destruir, destruyenfo, pila sd y pila des

def Cuenta_Pares_P(lista):
    if type(lista)==list:
        if lista==[]:
            return None
        else:
            return aux_RC(lista)
    
def cuentaPares_PD_aux(lista):
    if lista==[]:
        return 0
    else:
        contador=0
        for numero in lista:
            if numero%2==0:
                contador+=1
    return cuentaPares_PD_aux(lista)
    

#La misma de la profe
def CuentaParesCSD(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else: 
            return CuentaParesCSD_aux(lista,0,0)
    else:
        print("Parametro incorrecto")

def CuentaParesCSD_aux(lista,cont,i):
    if i==len(lista):
        return cont
    elif lista[i]%2==0:
        return CuentaParesCSD_aux(lista, cont+1,i+1)
    else:
        return CuentaParesCSD_aux(lista, cont, i+1)
    
    #destruyengoon

def CuentaParesCD(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else: 
            return CuentaParesCD_aux(lista,0,0)
    else:
        print("Parametro incorrecto")

def CuentaParesCD_aux(lista, cont):
    if lista==[]:
        return cont
    elif lista[0]%2==0:
        return CuentaParesCD_aux(lista[1:], cont+1)
    else:
        return CuentaParesCD_aux(lista[1:], cont)

#Pila sd
def CuentaParesPD_aux(lista):
    if lista==[]:
        return 0
    elif lista[0]%2==0:
        return 1+CuentaParesPD_aux(lista[1:])
    else:
        return CuentaParesPD_aux(lista[1:])

def CuentaParesPSD_aux(lista,i):
    if i==len(lsita):
        return 0
    elif lista[i]%2==0:
        return 1+CuentaParesPD_aux(lista,i+1)
    else:
        return CuentaParesPD_aux(lista,i+1)
    
#Quiz
#arametro una lista a validar
#Promedio, RCSD

def PromedioRCSD(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else: 
            return PromedioRCSD_aux(lista,0,len(lista),0)
    else:
        print("Parametro incorrecto")

def PromedioRCSD_aux(lista, resultado, largo, i):
    if i==largo:
        return resultado/largo
    else:
        return PromedioRCSD_aux(lista, resultado+lista[i], largo, i+1)
    

def PromedioRCD(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else: 
            return PromedioRPSD_aux(lista,0,len(lista))/len(lista)
    else:
        print("Parametro incorrecto")

    
def PromedioRPSD_aux(lista, i, largo):
    if i==largo:
        return 0
    else:
        return lista[i]+PromedioRPSD_aux(lista, i+1, largo)
    

def PromedioRCD_aux(lista, resultado, largo):
    if lista==[]:
        return resultado/largo
    else:
        return PromedioRCD_aux(lista[1:], resultado+lista[0], largo)

def PromedioRPD_aux(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else:
            return lista[0]+PromedioRPD_aux(lista[1:])   
        
#4 funciones
#WhileSD whileD For Range y For i
#Parametro[6,1,2,3,5,7,8]

"""def Operacion(lista):
    if lista==[]:
        return None
    else:
        return lista[0]+lista[2:3]
resultado=Operacion([6,1,2,3,5,7,8])
print(resultado)"""

def WhileSD(lista):
    if type(lista)!=list or len(lista)==0:
        return "Error"
    nueva_lista=[]
    largo=len(lista)
    i=0
    while i<largo:
        base=lista[i]
        suma=lista[(i+2)%largo]
        resta=lista[(i+4)%largo]
        resultado=base+suma-resta
        nueva_lista.append(resultado)
        i+=1
    return nueva_lista
print(WhileSD([6,1,2,3,5,7,8]))
    
'''
        if lista==[]:
            return 0
        else: 
            return WhileDes_aux(lista,0,0)
    if len(lista)<3:
        return"Error"
    resultado=[0]*len(lista)
    i=0
    while i<len(lista):
        indice_0=i%len(lista)
        indice_2=(i+2)%len(lista)
        indice_4=(i+4)%len(lista)

        resultado[i]=lista[0]+lista[2:3]-lista[1:5]
        i+=1
    return resultado'''

def WhileD(lista):
    if type(lista)!=list or len(lista)==0:
        return "Error"
    nueva_lista=[]
    largo=len(lista)
    i=0
    copia=lista
    while lista!=[]:
        base=lista[0]
        suma=copia[(i+2)%largo]
        resta=copia[(i+4)%largo]
        resultado=base+suma-resta
        nueva_lista.append(resultado)
        lista=lista[1:]
        i+=1
    return nueva_lista
print(WhileD([6,1,2,3,5,7,8]))

def OperarSD(lista):
    if len(lista)<3:
        return"Error"

    i=0
    while i<len(lista):
        indice_0=i%len(lista)
        indice_2=(i+2)%len(lista)
        indice_4=(i+4)%len(lista)

        lista[i]=lista[indice_0]+lista[indice_2]-lista[indice_4]
        i+=1
    return lista

def operar(lista):
    i=lista[0]
    lista=lista[i:2]
    return lista

res=operar([1,2,3,4])
print(res)

def Operar_For_Range(lista):
    if type(lista)!=list or len(lista)==0:
        return"Error"
    resultado=[0]*len(lista)
    for i in range(len(lista)):
        indice_0=i%len(lista)
        indice_2=(i+2)%len(lista)
        indice_4=(i+4)%len(lista)

        resultado[i]=lista[indice_0]+lista[indice_2]-lista[indice_4]
    return resultado
print(Operar_For_Range([6,1,2,3,5,7,8]))

def Operar_For_i(lista):
    if type(lista)!=list or len(lista)==0:
        return"Error"
    resultado=[0]*len(lista)
    i=0
    for x in lista:
        indice_0=i%len(lista)
        indice_2=(i+2)%len(lista)
        indice_4=(i+4)%len(lista)

        resultado[i]=lista[indice_0]+lista[indice_2]-lista[indice_4]
        i+=1
    return resultado
print(Operar_For_i([6,1,2,3,5,7,8]))