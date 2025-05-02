import copy

def sumatrices(ma1,ma2):#[2,3],[4,6]]  [[4,6],[7,8]]=[[6,9],[11,14]]
    if ValidaMatrizSI(ma1)==False or ValidaMatrizSI(ma2)==False or len(ma1[0])!=len(ma2[0])or len(ma1)!=len(ma2):
        print("matrices no validas")
    else:
        filas=len(ma1)#
        columnas=len(ma1[0])#
        filas1=len(ma2)#
        columnas1=len(ma2[0])#
        matriznueva=copy.deepcopy(ma1)
        for i in range(filas):#
            for j in range(columnas):#
                           
               matriznueva[i][j]=ma1[i][j]+ma2[i][j]
               
        print(matriznueva,ma1)
