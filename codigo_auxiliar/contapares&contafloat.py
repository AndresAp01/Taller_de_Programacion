def contapares(num):
    num=abs(num)
    contador=0
    while num != 0:
        if num%2==0:
            contador=contador+1
        num=num+1
        num=num//10
    print(contador)

def contafloat(num):
    if type(num)==int:
        num=abs(num)
        contador=0
        while num != 0:
            if num%2==0:
                contador=contador+1
            num=num//10
        print(contador)
    else:
        print("El parametro no es entero")