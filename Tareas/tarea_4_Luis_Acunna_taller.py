#Luis Andres Acunna Perez

def largo(num):
    if num == 0:
        print(1)
    else:
        cont = 0
        while num != 0:
            num = num // 10
            cont = cont + 1
        return (cont)

def recibir(num1, num2):
    if type(num1) == int and type(num2) == int and largo(num1) == largo(num2):
        num1=abs(num1)
        num2=abs(num2)

        suma=0
        multi=1
        bandera=0

        if num1==0 and num2==0:
            print("El numero es 0.")

        else:
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
                    multi=multi*ultimo
                else:
                    suma=suma+ultimo
                    bandera=1
                num2=num2//10
            
            if bandera==1:
                print("La suma es: ", suma, "y la multiplicacion es: ", multi)
            else:
                print("La suma es: ", suma)



"""Resultado= con (2349, 5678) : 18 & 1296\
                suma=0+2+4+5+7
                multi=1*2*4*5*7
              con (1234, 4321)
                  suma= 0+2+4+3+1 =10
                  multi= 1*7*7*4*6 =24
              con (224477, 134569)
                suma= 0+2+2+4+4+5+9 = 30 
                multi= 1*7*7*4*6 = 1176 """
