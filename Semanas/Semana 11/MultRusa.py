#Luis Andres Acunna Perez Quiz Taller
#Trabajo Multiplicacion Rusa

def MultRusa(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        if num1==0 or num2==0:
            print(0)
        bandera=0
        #Empiezo otro if porque tengo un return arriba, para que no imprima lo demas y solo imprima 0
        if num1<0 and num2>0:
            num1, num2=abs(num1), abs(num2)
            bandera=1
        elif num1<0 and num2<0:
            num1, num2=abs(num1), abs(num2)
        elif num1>0 and num2<0:
            num1, num2=abs(num1), abs(num2)
            bandera=1

        L1=[]
        L2=[]

        print("num1: ", num1)
        print("num1: ", num2)

        L1+=[num1]
        while num1>1:
            num1//=2
            L1+=[num1]

        L2+=[num2]
        while len(L2)<len(L1):
            num2*=2
            L2+=[num2]

        pos_impares=[]
        for i in range(len(L1)):
            if L1[i]%2!=0:
                pos_impares+=[i]

        valores_en_posiciones=[]
        for pos in pos_impares:
            valores_en_posiciones+=[L2[pos]]

        suma=0
        for valor in valores_en_posiciones:
            suma+=valor

        if bandera==1:
            suma*=(-1)
        print("L1", L1)
        print("L2", L2 )
        print("largo:", len(L1))
        print("Posiciones de los numeros impares", pos_impares)
        print("suma: ", suma)#suma
    else:
        print("Los numeros deben ser enteros.")

#MultRusa(5,0)
#Trabaja correctamente