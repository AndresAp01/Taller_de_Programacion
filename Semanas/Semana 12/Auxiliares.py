def Largo(n):
    if n<10 or n==0:
        return 1
    else:
        return 1+Largo(n//10)

def Pasalistacola(num):
    if isinstance(num, int):
        if num==0:
            return [0]
        else:
            return Pasalistacola_aux(num, [])
    else:
        print("Par invalido")

def Pasalistacola_aux(num, lista):
    if num==0:
        return lista
    else:
        return Pasalistacola_aux(num//10, [num%10]+lista)

