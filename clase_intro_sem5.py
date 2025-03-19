def Centro(num): #123
    if isinstance(num, int):
        num=abs(num)
        temp = num
        contador = 0
        while temp > 0: 
            temp = temp // 10 
            contador = contador + 1 
            
        if contador%2 == 0: 
            print("Error, el numero debe tener una cantidad impar de digitos")
            return "Ninguno"
            
        pos_medio = contador // 2 
        num = num // (10 ** pos_medio) 
        digito_medio = num % 10
        return digito_medio

    else:
        print("Error, debe ser un numero entero")
        return "Ninguno"

def Centro_posicional(num):
    if largo(n)%2 != 0:
        i=1
        while i<=n:
            n//=10
            i+=1
        return(i)
#________________________________________________________________________________________

def largo(num):
    if num==0:
        print(1)
    else:
        cont=0
        
        while num!=0:
            num=num//10
            cont=cont+1
        return(cont)

def sumatoria1(num):
    if type(num) == int and largo(num)%2 != 0:
        num=abs(num)
        suma = 0
        centro=(largo(num)-1)//2
        cont=largo(num)-1
        centrovalor=Centro(num)
        while num!=0:
            temp = num%10
            if cont == centro:
                num = num//10
            else:
                suma=suma+(temp+centrovalor)
                num=num//10
            cont = cont-1
        
        print(suma)
    else:
        print("Parametro incorrecto")
        
def Suma_que(num): #posicional
    larg = largo(num)
    num = abs(num)
    i = Centro(num)
    j = 0
    suma = 0
    while j <= larg:
        if j != i:
            suma+=num%10
        num//=10
        j+=1
    print(suma)

def sumafactorial(lista):
    if type(lista)==list:
        i = lista[0]
        n = lista[-1] # Ultimo elemento
        resultado = 0
        while i <= n:
            factoriali = factorialINC(i)
            operacion = ((((factoriali)**3)/((n + 1)**2))**3)
            resultado = resultado + operacion
            i+=1
        return resultado

def sumafactorial(num):
    if type(num)==int:
        i=1
        suma=0
        while i <= num:
            factoriali = factorialINC(i)
            suma=suma+(((factoriali)**3)/((num+1)**2))
            i+=1
        return (suma**3)

    
def factorialINC(num):  # Funciona
    if num < 0 or not type(num) == int:
        print("Parametro de entrada no valido")
    elif num == 0:
        return 1
    else:
        resultado = num
        i = 1
        while i < num: 
            resultado = resultado * i
            i = i + 1 
        return resultado

def BuscarNumD(lista, num):
    if type(lista)==int and isinstance(num, int):
        if lista == []:
            print("Elemento no se encuentra")
            i=0
        else:
            Esta = False
            while i<len(lista):
                if lista[i] == num:
                    Esta = True
                    break
                i=i+1
            return Esta
    else:
        print("Parametro incorrecto")

def BuscarNumSD(lista, num):
    pass

def pasalista(num):
    if isinstance(num, int):
        num = abs(num)
        if num >= 0 and num<= 9:
            return num
        else:
            listaNueva = []
            while num!=0:
                listaNueva=[]+listaNueva
                num=num//10
            return listaNueva
    else:
        print("nah")

def posNum(num, elemento):
    if type(num) == int and isinstance(elemento, int):
        num=abs(num)
        elemento=abs(elemento)
        lista = pasalista(num)
        ListaNueva = []
        if lista == [0]:
            return [0 + elemento]
        else:
            larg=len(lista)-1
            while lista!=[]:
                if larg%2==0:
                    ListaNueva = [lista[larg] + elemento] + ListaNueva
                else:
                    ListaNueva = [lista[larg]] + ListaNueva
                larg = larg-1
                lista = lista[0:len(lista)-1]
            print(ListaNueva)
    else:
        prit("Parametro incorrecto")
        

            
            
            
            
