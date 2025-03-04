#-------------------------------------------------------------------------#
#----Lista de codigos auxiliares-----------#

#Para saber el largo de un numero:

def largo(num):
    if num==0:
        print(1)
    else:
        cont=0
        
        while num!=0:
            num=num//10
            cont=cont+1
        return(cont)

#P
