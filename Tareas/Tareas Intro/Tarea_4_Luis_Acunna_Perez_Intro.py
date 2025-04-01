#Luis Andres Acunna Perez

#funcion auxiliar
def pasalista(num):
    if isinstance(num, int):
        num=abs(num)
        if num>=0 and num<=9:
            return [num]
        else:
            listaNueva=[]
            while num!=0:
                listaNueva=[num%10]+listaNueva
                num=num//10
            return listaNueva
    else:
        print("Parametro incorrecto")
#--------------------------------------------
#Primer problema
#corrida con num1=123 y num2=456
def Problema1(num1, num2):
    if type(num1)==int and type(num2)==int:
        lista1=pasalista(num1)
        lista2=pasalista(num2)
        if len(lista1)!=len(lista2):
            print("Los números deben tener el mismo largo")
            return []
        listaNueva=[(lista1[i]+lista2[i])**3 for i in range(len(lista1))]
        #i
        #0      lista1[0]+lista2[0] = 1+4 = 5
        #        5**3 = 125
        #1      lista1[1]+lista2[1] = 2+5 = 7
        #       7**3 = 343
        #2      lista[2]+lista2[2] = 3+6 = 9
        #       9**3 = 729

        return listaNueva
        #listaNueva = [125, 343, 729]
    else:
        return 0

#---------------------------------------------------------------------------------------
#Segundo problema
#Corrida con num1=6789054 num2=1234567 con otra manera
def Problema_2(num1, num2):
    if not (isinstance(num1, int) and isinstance(num2, int)):
        print("Los numeros deben ser enteros")
        return []
    lista1=pasalista(num1)
    lista2=pasalista(num2)
    #lista1=[6, 7, 8, 9, 0, 5, 4]
    #lista2=[1, 2, 3, 4, 5, 6, 7]
    if len(lista1)!=len(lista2):#Si son del mismo largo
        print("Los numeros deben tener el mismo largo")
        return []
    n=len(lista1)
    lista_c=[0]*(2*n)#len(lista1)+len(lista2)
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #[6, 1, 7, 2, 8, 3, 9, 4, 0, 5, 5, 6, 4, 7]
    lista_c[::2]=lista1
    #[6, 0, 7, 0, 8, 0, 9, 0, 0, 0, 5, 0, 4, 0]
    lista_c[1::2]=lista2
    #[6, 1, 7, 2, 8, 3, 9, 4, 0, 5, 5, 6, 4, 7]
    lista_nueva=[0]*n
    for i in range(n):
        #i      lista_c[2*n-1-i]    lista_nueva[]
        #0      lista_c[2*7-1-0]=13 lista_nueva[0]=lista_c[0]+lista_c[13]=6+7
        #1      lista_c[2*7-1-1]=12 lista_nueva[1]=lista_c[1]+lista_c[12]=1+4
        #2      ...                 lista_nueva[2]=lista_c[2]+lista_c[11]=7+6
        #3                          lista_nueva[3]=lista_c[3]+lista_c[10]=2+5
        #4                          lista_nueva[4]=lista_c[4]+lista_c[9]=8+5
        #5                          lista_nueva[5]=lista_c[5]+lista_c[8]=3+0
        #6                          lista_nueva[6]=lista_c[6]+lista_c[7]=9+4
        lista_nueva[i]=lista_c[i]+lista_c[2*n-1-i]
        #lista_nueva=[13, 5, 13, 7, 13, 3, 13]
    return lista_nueva
#----------------------------------
#Segundo problema diferente logica
#Corrida con num1=6789054 num2=1234567
def Problema2_1(num1, num2):
    lista1=pasalista(num1)
    lista2=pasalista(num2)
    if len(lista1)!=len(lista2):
        print("Los numeros deben tener el mismo largo")
    n=len(lista1)
    #7
    lista=[]
    izquierda=range(0, n, 1)
    #(0, 7, 1) [0,1,2,3,4,5,6]
    derecha=range(n-1, -1, -1)
    #(6, -1, -1) [6,5,4,3,2,1,0]
    for i in range(n):
        if i%2==0:
            #i
            #0 0//2=0
            #2 2//2=0
            #4 4//2=0
            #6 6//2=0

            lista+=[lista1[izquierda[i//2]]+lista2[derecha[i//2]]]
            #izquierda[0]+derecha[0]
            #lsita1[0]+lista2[6]        =6+7
            #izquierda[1]+derecha[1]
            # lsita1[1]+lista2[5]       =7+6
            #izquierda[2]+derecha[2]
            #lista1[2]+lista2[4]        =8+5
            # izquierda[3]+derecha[3]
            # lista1[3]+lista2[3]        =9+4

        else:
            #i
            #1 1//2=1
            #3 3//2=1
            #5 5//2=1

            lista+=[lista1[derecha[i//2]]+lista2[izquierda[i//2]]]
            # derecha[0]+izquierda[0]
            # lista1[6]+lsita2[0]       =4+1
            # derecha[1]+izquierda[1]
            # lista1[5]+lsita2[1]       =5+2
            # derecha[2]+izquierda[2]
            # lista1[4]+lsita2[2]       =0+3

    return lista
    #[13, 5, 13, 7, 13, 3, 13]
#---------------------------------------------------------------------
#Problema 3
#corrida con 2,[3,4,5,6,7]
def Problema_3(num,lista):
    if type(num)==int and type(lista)==list:
        num=abs(num)
        if not lista:
            return []
        else:
            lista_nueva=[]
            for item in lista:
               #item
               #3 3%2=1
               #4 4%2=0
               #5 5%2=1
               #6 6%2+0
               #7 7%2=1
                if item%2==0:
                    lista_nueva=lista_nueva+[item+num]
                    #[6,8]
                else:
                    lista_nueva=lista_nueva+[item**num]
                    #[9,25,49]
            return lista_nueva
        #[9,6,25,8,49]