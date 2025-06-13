#Largo recursivo de Pila
def Largo_Rec_Pila(n):
    if type(n)==int:
        if n==0:
            return 1
        else:
            return Largo_Rec_Pila_Aux(n)
    else:
        print("parametro incorrecto")

def Largo_Rec_Pila_Aux(n):
    if n==0:
        return 0
    else:
        return 1+Largo_Rec_Pila_Aux(n//10)