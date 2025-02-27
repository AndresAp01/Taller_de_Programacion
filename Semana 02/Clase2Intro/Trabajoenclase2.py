Trabajo clase - Luis Andres Acunna Perez

def SumatoriaInc(n):
    if n==0:
        print(0)
    else:
        i=0
        suma=0
        #i  suma    n
        #0  0       3
        #1  0       3
        #2  1       3
        #3  3       3
        #4  6       3
        #
        
        while i<=n:#0<=3si, 1<=3si, 2<=3si, 3<=3si, 4<=3no
            suma=suma+1 #0+0=0, 0+1=1, 1+2=3, 3+3=6
            i=i+1#0+1=1, 1+1=2, 3+1=3, 3+1=4
        print(suma)#6

def SumatoriaDec(n):
    if n==0:
        print(0)
    else:
        i=n
        suma=0
        while i>=0:
            suma=suma+i
            i=i-1
            print(suma)
