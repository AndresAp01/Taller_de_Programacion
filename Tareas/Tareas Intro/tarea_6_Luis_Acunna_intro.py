#Luis Andres Acunna Perez
#while sin destruir
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

#while destruyendo
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

#for range
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

#for i
def Operar_For_i(lista):
    if type(lista)!=list or len(lista)==0:
        return"Error"
    resultado=[0]*len(lista)
    i=0
    for item in lista:
        indice_0=i%len(lista)
        indice_2=(i+2)%len(lista)
        indice_4=(i+4)%len(lista)

        resultado[i]=lista[indice_0]+lista[indice_2]-lista[indice_4]
        i+=1
    return resultado
print(Operar_For_i([6,1,2,3,5,7,8]))