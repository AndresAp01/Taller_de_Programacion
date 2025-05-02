# validacion de conjuntos NO es conjunto
def conjunto(lista):#[3,2,1,3]
    largo=0 #0
    pos=0 #0
   
    #largo      pos       lista
    while largo<len(lista):# Afuera o Externo mas lento
        while pos<len(lista):#Adentro o Interno, corre mas rapido
            if largo!=pos:#
                if lista[pos]==lista[largo]:#
                    return(False)
                else:
                    pos=pos+1#
            else:
                pos=pos+1#
        #Antes del externo
        pos=0
        largo=largo+1
    return( True)
