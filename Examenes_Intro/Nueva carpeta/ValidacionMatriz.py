def ValidaMatriz(matriz):
    a=0
    b=0
    
    if matriz==[]:
        return False
    elif matriz[0]==[] and matriz[1]==[]:
        return "La matriz no es valida"
    else:
        for i in range(len(matriz)):#
            if matriz==[]:
                a=1
            elif matriz[0]==[]:
                a=1
            elif len(matriz[0])!=len(matriz[1]):#
               return False
            matriz=matriz+[matriz[0]]#
            matriz=matriz[1:]#
        
    if a==b:
        return True
    else:
        return False
