#Escribir una funcion que recibe una lista
#Invertir la lista
#For range y item


def InvertirlistaFR(lista):#[3,4,5,6]
    if type(lista)==list:
        if lista==[]:
            return []
        else:
            Linvertida=[]
            #Linvertida      lista
            #[]              #[3,4,5,6]
            #[3]             #[3,4,5,6]
            #[4,3]           #[3,4,5,6]
            
            for i in range(len(lista)):#i=0si 1si 2si 3si 4x
                Linvertida=[lista[i]]+Linvertida
                #[3]+[]=[3]
                #[4]+[3]=[4,3]
                #[5]+[4,3]=[5,4,3]
                #[6]+[5,4,3]=[6,5,4,3]
            return Linvertida
    else:
        print("Parametro incorrecto")

def InvertirlistaFI(lista):#[3,4,5,6]
    if isinstance(lista,list):
        if lista==[]:
            return []
        else:
            Linvertida=[]
            #Linvertida    lista
            #[]            [3,4,5,6]
            #[3]           [3,4,5,6]
            #[4,3]         [3,4,5,6]
            #[5,4,3]       [3,4,5,6]
            #[6,5,4,3]     [3,4,5,6]
            
            for item in lista:#3 4 5 6
                Linvertida=[item]+Linvertida
                #[3]+[]=[3]
                #[4]+[3]=[4,3]
                #[5]+[4,3]=[5,4,3]
                #[6]+[5,4,3]=[6,5,4,3]
            return Linvertida#[6,5,4,3]
    else:
        print("Parametro incorrecto")

#Escribir una funion que recibe dos numeros enteros positivos del mismo largo
#Sumar y multiplicar por posicion. Numeros trabajados desde posicion 0
#Quiz realizado y agregar el quiz con un solo while
#23:59

def largo(num):#4567890  
    if num==0:
        return 1
    else:
        cont=0
        #contador    num
        #0       4567890
        #1       456789
        #2       45678
        #3       4567
        #4       456
        #5       45
        #6       4
        #7       0
        
        while num!=0:#4567890si 456789si 45678si 4567si 456si 45si 4si 0x
            num=num//10#456789 45678 4567 456 45 4 0
            cont=cont+1#1 2 3 4 5 6 7
        return cont#7

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


x=5
y=x
print(x,y)
x=x+1
print(x,y)

matriz=[[4,5],[4,1]]
matriz1=matriz
print(matriz,matriz1)
matriz=[[6,10],[8,2]]
print(matriz,matriz1)
