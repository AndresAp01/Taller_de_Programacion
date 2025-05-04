#Luis Andres Acunna Perez
#Segundo examen parcial

#funciones auxiliares copiadas y pegadas del archivo de la profe:
#validacion de matriz
def ValidaMatriz(matriz):
    a = 0
    b = 0
    if matriz == []:
        return False
    elif matriz[0] == [] and matriz[1] == []:
        return "La matriz no es valida"
    else:
        for i in range(len(matriz)):
            if matriz == []:
                a = 1
            elif matriz[0] == []:
                a = 1
            elif len(matriz[0]) != len(matriz[1]):
                return False
            matriz = matriz + [matriz[0]]
            matriz = matriz[1:]
    if a == b:
        return True
    else:
        return False
# validacion de conjuntos NO es conjunto
def conjunto(lista):  # [3,2,1,3]
    largo = 0  # 0
    pos = 0  # 0

    # largo      pos       lista
    while largo < len(lista):  # Afuera o Externo mas lento
        while pos < len(lista):  # Adentro o Interno, corre mas rapido
            if largo != pos:  #
                if lista[pos] == lista[largo]:
                    return (False)
                else:
                    pos = pos + 1
            else:
                pos = pos + 1
        # Antes del externo
        pos = 0
        largo = largo + 1
    return (True)

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
#primera funcion
#Comentarios sobre las variables y que hacen las funciones

def UNO(lista):
    if isinstance(lista, list):
        if conjunto(lista)==True:
            if not lista:
                return []
            else:
                resultado=[]
                nueva_lista=[]
                desordenada=False
                for i in range(len(lista)):
                    actual=lista[i]
                    bloque=[actual-1, actual, -actual, actual+1]
                    if i==0:
                        nueva_lista=[bloque]
                    elif lista[i]>=lista[i-1]:
                        nueva_lista=nueva_lista+[bloque]
                    else:
                        if not desordenada:
                            resultado=[[1, 0, nueva_lista, 0, 1]]
                            desordenada=True
                        else:
                            resultado=resultado+[[1, 0, nueva_lista, 0, 1]]
                        nueva_lista=[bloque]
                if desordenada:
                    resultado=resultado+[[1, 0, nueva_lista, 0, 1]]
                    return f"Lista original: {lista}, Resultado: {resultado}"
                else:
                    return [lista]
        else:
            return "La lista no es un conjunto, por favor remover digitos repetidos."

#resultado=UNO([6, -1, 2, 7, 8, 16, 100, -200])
#print(result)
#Lista original: [6, -1, 2, 7, 8, 16, 100, -200], Resultado: [[1, 0, [[5, 6, -6, 7]], 0, 1], [1, 0, [[-2, -1, 1, 0], [1, 2, -2, 3], [6, 7, -7, 8], [7, 8, -8, 9], [15, 16, -16, 17], [99, 100, -100, 101]], 0, 1], [1, 0, [[-201, -200, 200, -199]], 0, 1]]

#resultado=UNO([1,2,3,4])
#print(resultado)
#[[1, 2, 3, 4]]

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
                    nuevo_num2=nuevo_num2*10+digitos2

    else:
        return "Los numeros no son enteros"

print(DOS(1234,1234))

def TRES():
    pass

def CUATRO(elem, lista):
    if isinstance(lista, list):
        if isinstance(elem, (int,list)):
            i=0
            nueva=[]
            while i<len(lista):
                item=lista[i]
                if item==elem:
                    nueva=nueva+[item, item]
                elif isinstance(item, list) and elem in item:
                    nueva_sub=[]
                    x=0
                    while x<len(item):
                        nueva_sub=nueva_sub+[item[x]]
                        if item[x]==elem:
                            nueva_sub=nueva_sub+[elem]
                        x+=1
                    nueva=nueva+[nueva_sub]
                else:
                    nueva=nueva+[item]
                i+=1
            return nueva
        else:
            return "El segundo parametro debe ser un numero entero o una lista."
    else:
        return "El primer parametro debe ser una lista."

"""resultado=CUATRO(3, [1,2,3,3,[4,3,3], 4, [3]])
print(resultado)"""
