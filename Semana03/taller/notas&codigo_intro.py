#Clase 1 sem3 Intro ejemplos profe
# type return bandera and abs
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
            return(suma//larg)
        
#{Escribir una funcion que recibe dos parametros}


def prac1(num1, num2):
    if type(num1)==int and type(num2)==int and largo(num1)==largo(num2):
        num1=abs(num1)
        num2=abs(num2)
        
        suma=0
        multi=1
        bandera=0

        while num1!=0:
            ultimo=num1%10
            if ultimo%2==0:
                suma=suma+ultimo
            else:
                multi=multi*ultimo
                bandera=1
            num1=num1//10

        while num2!=0:
            ultimo=num2%10
            if ultimo%2==0:
                suma=suma+ultimo
            else:
                multi=multi*ultimo
                bandera=1
            num2=num2//10
        if bandera==1:
            print("La suma es: ",suma," la multiplicación es: ",multi)
        else:
            print("La suma es: ",suma, "la multiplicación es: ", 0)

#otra forma }
def prac2(num1, num2):
    if type(num1)==int and type(num2)==int and largo(num1)==largo(num2):
        num1=abs(num1)
        num2=abs(num2)
        suma=0
        multi=1
        bandera=0
        while num1!=0:
            temp1=num1%10
            temp2=num2%10
            if temp1%2==0 and temp2%2==0:
                suma=suma+temp1+temp2
            elif temp1%2==0 and temp2%2!=0:
                suma=suma+temp1
                mult = mult*temp2
                bandera=1
            elif temp1%2!=0 and temp2%2==0: #8346 1412
                suma=suma+temp2
                mult=mult*temp1
                bandera=1
            else:
                mult=mult*temp1*temp2
                bandera=1
                num1=num1//10
                num2=num2//10
        if bandera==1:
            print("La suma es:", suma, "y ", mult)
        else:
            print("La suma es: ", suma,"la mult", 0)
        
