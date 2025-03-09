def promedio(num):
    num=abs(num)
    i=n
    suma=0
    while i>=0:
        suma=suma
        i=i-1
        if num==0:
            print(1)
        else:
            cont=0
            while num!= 0:
                num=num//10
                cont=cont+1
            print(cont)
        print("El promedio es:", num//cont)