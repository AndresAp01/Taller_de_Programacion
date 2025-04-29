#Escribir una funcion que recibe dos parametros, un numero y un digito. Lo que quiero es buscar la cantidad de apariciones del digito dentro del numero. Que ambos sean enteros y positivos.
#Recursion de cola
#Debe tener funcion auxiliar

def aparicionesRC(num, dig): #23456633, 3
    if isinstance(num, int) and (dig, int):
        if num==dig:
            return 1
        else:
            dig=abs(dig)
            return aparicionesRC_aux(abs(num), dig,0)
    else:
        print()

def aparicionesRC_aux(num, dig, resultado):

    #23456633, 3, 0
    #2345663, 3, 1
    #234566, 3, 2
    #23456, 3, 2
    #2345, 3, 2
    #2345, 3, 2
    #234, 3, 2
    #23, 3, 2
    #2, 3, 3
    #0, 3, 3
    if isinstance(num, int) and (dig, int, resultado):
        if num==0:
            return resultado
        elif (num%10)==dig: #3=3si 3=3si 6=3no 5=3no 4=3no 3=3si 2=3no
            return aparicionesRC_aux(num//10, dig,resultado+1)
        #return aparicionesRC_aux(23456633//10, 3, 0 +1)
        # return aparicionesRC_aux(2345663//10, 3, 1 +1)
        # return aparicionesRC_aux(23//10, 3, 2 +1)
        else:
            return aparicionesRC_aux(num//10, dig, resultado)
            #return aparicionesRC_aux(23456//10, 3, 2)
            #return aparicionesRC_aux(2345//10, 3, 2)
            #return aparicionesRC_aux(234//10, 3, 2)
            # return aparicionesRC_aux(2//10, 3, 3)


#2
def aparicionesRP(num, dig):
    if isinstance(num, int) and (dig, int):
        if num==dig:
            return 1
        else:
            return aparicionesRP_aux(abs(num), abs(dig))
    else:
        print("Parametro incorrecto")

def aparicionesRP_aux(num, dig):
    #num
    #2345633 3
    # 234563 3
    # 23456 3
    # 2345 3
    # 234 3
    # 23 3
    # 2 3
    # 0 3
    if num==0:
        return 0
    elif (num%10)==dig:# 3=3si, 3=3si, 6=3no, 5=3no 4=3no 3=3si 2=3no
        return 1+aparicionesRP_aux(num//10, dig)
    #return  1+aparicionesRP_aux(2345633, 3)
    # return  1+return 1+aparicionesRP_aux(234563, 3)
    # return 1+return 1+return 1+aparicionesRP_aux(23, 3)=>0
    #rteturn 1+return 1+return 1+1
    #return 1+2
    #return 3

    else:
        return aparicionesRP_aux(num//10,dig)
    #return aparicionesRP_aux(2345633 // 10, 3)
    #return aparicionesRP_aux(2345 // 10, 3)
    # return aparicionesRP_aux(234 // 10, 3)
    # return aparicionesRP_aux(2 // 10, 3)
#quiz 3
def largoRC(num):
    if type(num)==int:
        if num==0:
            return 0
        else:
            return largo_aux(num, 0)
    else:
        print("parametro incorrecto")

def largo_aux(num, contador):
    if num==0:
        return contador
    else:
        return largo_aux(num//10, contador+1)

#Escribir una funcion que recibe un numero, entero positivo
#Invertir el numero
def invertir(num):#345
    if isinstance(num, int):
        if num==0:
            return 0
        else:
            return ((num%10)*(10**(largoRC(num)-1)))+invertir_aux(num//10)
            #return ((3%10)*(10**(largoRC(3)-1)))+ invertir_aux(345//10)
            #return ((5)*(10**(2)))+ invertir_aux(34)
            #return (5*100)+ invertir_aux(34)
            #return (500)+ invertir_aux(34) => 43
            #return 500+43
            #return 543
    else:
        print("Parametro incorrecto")

def invertir_aux(num):
    if largoRC(num)==1:
        return (num%10)*(10**(largoRC(num)-1))
        #return (3%10)*(10**(1-1))
        #return 3*1
    else:
        return ((num%10)*(10**(largoRC(num)-1)))+invertir_aux(num//10)
        #return ((34%10)*(10**(largoRC(2)-1))) + invertir_aux(34//10)=> 3
        #return (40) + invertir_aux(34//10)=> 3
        #return ((4)*(10**(1)) + invertir_aux(3)
        #return (40)+invertir_aux(3) => 3
        #return 43
