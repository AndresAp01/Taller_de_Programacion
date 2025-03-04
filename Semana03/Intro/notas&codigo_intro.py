#Clase 1 sem3 Intro ejemplos profe

def contapares(num):
    num=abs(num)
    contador=0
    if num==0 or num==2 or num==4 or num==6 or num==8:
        print(1)
    else:
        while num != 0:
            # <<<temp=num%10 >>>
            if temp%2==0:
                contador=contador+1
            num=num+1
            num=num//10
        print(contador)

def contafloat(num):
    if type(num)==int:
        num=abs(num)
        contador=0
        if num==0 or num==2 or num==4 or num==6 or num==8:
            print(1)
        else:
            while num != 0:
                # <<<temp=num%10 >>>
                if num%10%2==0:
                    contador=contador+1
                num=num//10
            print(contador)
    else:
        print("El parametro no es entero")

#------------------------------------------------------------------------#
def largo(num):
    if num==0:
        print(1)
    else:
        cont=0
        
        while num!=0:
            num=num//10
            cont=cont+1
        return(cont)

        
def promedio(num):
    if type(num)==int:
        num=abs(num)
        
        if num==0:
            print(0)
        else:
            suma=0
            larg=largo(num)
            while num!=0:
                suma=suma+num%10
                num=num//10
            print(suma//larg)
