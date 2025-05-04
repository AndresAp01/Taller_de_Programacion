def largofor(num):
    if isinstance(num,int):
        num=abs(num)
        if num==1:
            return 1
        else:
            cont=0
            for i in range(0,num,1):
                if num==0:
                    break
                cont=cont+1
                num=num//10
            return cont
    else:
        print("Parametro incorrecto")

def valida_matriz(matriz):
    if not isinstance(matriz, list) or len(matriz) == 0:
        return False
    primera = matriz[0]
    if not isinstance(primera, list) or len(primera) == 0:
        return False
    cols = len(primera)
    for fila in matriz:
        if not isinstance(fila, list) or len(fila) != cols:
            return False
    return True


def DOS(num1, num2):
    if isinstance(num1, int) and (num2, int):
        num1=abs(num1)
        num2=abs(num2)
        if largofor(num1)!=largofor(num2):
            return False
        elif largofor(num1 or num2)%5!=0:
            return "Los numeros deben ser multiplos de 5"
        elif largofor(num1 or num2)%2==0:
            return "Los numeros deben tener largo impar"
        else:
            nuevo_num1=0
            nuevo_num2=0
            n=largofor(num1)
            for i in range(n):
                digitos1=(num1//(10**(n-i-1)))%10
                digitos2=(num2//(10**(n-i-1)))%10
                digitos1inverso=(num1//(10**i))%10
                digitos2inverso=(num2//(10**i))%10
                if i%2==0:
                    nuevo_num1=nuevo_num1*10+digitos1
                    nuevo_num2=nuevo_num2*10+digitos2inverso
                else:
                    nuevo_num1=nuevo_num1*10+digitos2
                    nuevo_num2=nuevo_num2*10+digitos1inverso
            print(nuevo_num1, nuevo_num2)
            nuevo_largo=largofor(nuevo_num1)
            if nuevo_largo%5==0 and nuevo_largo%3==0:
                lista1=[]
                lista2=[]
                grupos=nuevo_largo//3
                for j in range(grupos):
                    vamos=nuevo_largo-(j+1)*3
                    bloque1=(nuevo_num1//(10**vamos))%1000
                    bloque2=(nuevo_num2//(10**vamos))%1000
                    separar=bloque1//100
                    separar11=(bloque1//10)%10
                    separar12=bloque1%10

                    separar2=bloque2//100
                    separar21=(bloque2//10)%10
                    separar22=bloque2%10

                    sub1=[separar**2, separar11**3, separar12**2]
                    sub2=[separar2**2, separar21**3, separar22**2]
                    lista1=lista1+[sub1]
                    lista2=lista2+[sub2]
                if not (valida_matriz(lista1) and valida_matriz(lista2)):
                    return "Matrices inválidas"

                    # 2) Sumarlas elemento a elemento
                suma = []
                for i in range(len(lista1)):
                    fila_suma = []
                    for j in range(len(lista1[i])):
                        fila_suma = fila_suma + [lista1[i][j] + lista2[i][j]]
                    suma = suma + [fila_suma]

                return suma
            elif largofor(nuevo_num1)!=largofor(nuevo_num2):
                return "Los nuevos numeros quedaron de diferentes largos, no se puede construir la lista"
            elif nuevo_largo%5==0 and nuevo_largo%3!=0:
                lista1=[]
                lista2=[]
                center=nuevo_largo//2
                shift1=nuevo_largo-3
                bloque1=(nuevo_num1//(10**shift1))%1000
                bloque2=(nuevo_num2//(10**shift1))%1000
                d10=bloque1//100
                d11=(bloque1//10)%10
                d12=bloque1%10

                d20=bloque2//100
                d21=(bloque2//10)%10
                d22=bloque2%10

                lista1=lista1+[[d10**2, d11**3, d12**2]]
                lista2=lista2+[[d20**2, d21**3, d22**2]]
                # segunda sublista
                shift2=nuevo_largo-(center+3)
                bloque1=(nuevo_num1//(10**shift2))%1000
                bloque2=(nuevo_num2//(10**shift2))%1000

                d10=bloque1//100
                d11=(bloque1//10)%10
                d12=bloque1%10

                d20=bloque2//100
                d21=(bloque2//10)%10
                d22=bloque2%10

                lista1=lista1+[[d10**2, d11**3, d12**2]]
                lista2=lista2+[[d20**2, d21**3, d22**2]]

                if not (valida_matriz(lista1) and valida_matriz(lista2)):
                    return "Matrices invalidas"
                suma=[]
                for i in range(len(lista1)):
                    fila_suma=[]
                    for j in range(len(lista1[i])):
                        fila_suma=fila_suma+[lista1[i][j] + lista2[i][j]]
                    suma=suma+[fila_suma]

                return suma
            else:
                return "Algo no previsto ha pasao"
    else:
        return "Los numeros no son enteros"