def largo(num):
    if num==0:
        return 1
    else:
        cont=0
        while num!=0:
            num=num//10
            cont=cont+1
        return cont

def ManejoNumporlargo(num1,num2):#123 456
    if type(num1)==int and type(num2)==int and largo(num1)==largo(num2):
        num1=abs(num1)
        num2=abs(num2)
        larg1=largo(num1)-1
        larg2=largo(num2)-1
        suma=0
        mult=1

        #larg1    larg2    suma    mult    num1   num2
        #2        2        0       1       123    456  inicio
        #1        2        3       1       12     456
        #0        2        3       2       1      456
        #-1       2        4       2       0      456
        #-1       1        4       12      0      45
        #-1       0        9       12      0      4
        #-1       -1       9       48      0      0

        while num1!=0:#123si 12si 1si 0x
            temp=num1%10#3 2 1
            if larg1%2==0:#2%2si 1%2x 0%2si
                suma=suma+temp
                #0+3=3
                #3+1=4
            else:
                mult=mult*temp
                #1*2=2
            num1=num1//10#12 1 0
            larg1=larg1-1#1 0 1
        print(suma,mult)#4,2

        while num2!=0:#456si 45si 4si 0x
            temp=num2%10#6 5 4
            if larg2%2!=0:#2%2x 1%2si 0%2x
                suma=suma+temp
                #4+5=9
            else:
                mult=mult*temp
                #2*6=12
                #12*4=48
            num2=num2//10#45 4 0
            larg2=larg2-1#1 0 -1
        print(suma,mult)#9,48

    else:
        print("Parametro incorrecto")

def quiz(num1, num2): #(123,456)
    if type(num1)==int and type(num2)==int and largo(num1)==largo(num2):
        num1=abs(num1)
        num2=abs(num2)
        larg1=largo(num1)-1
        larg2=largo(num2)-1
        suma=0
        mult=1
        #larg1 larg2    suma    mult
        #3     3        0       1
        #2     2        3       6
        #1     1        8       12
        #0     0        9       48

        while num1!=0 and num2!=0:
            temp1=num1%10 #123%10=3 / 12%10=2 / 1%10=1
            temp2=num2%10 #456%10=5 / 45%10=5 / 4%10=4
            if larg1%2==0: #2si
                suma=suma+temp1 #0+3=3 / 8+1=9
            else:
                mult=mult*temp1 #6*2=12
            if larg2%2!=0:
                suma=suma+temp2 #3+5=8
            else:
                mult=mult*temp2 #1*6=6 / 12*4=48
            num1=num1//10 #123//10 = 12 #12//10=1 #1//10=0
            num2=num2//10 #456//10=45 #45//10=4   #4//10=0
            larg1-=1 #2-1=1 #0
            larg2-=1 #2-1=1 #0
        print(suma, mult)
    else:
        print("Parametro incorrecto")

quiz(123, 456)