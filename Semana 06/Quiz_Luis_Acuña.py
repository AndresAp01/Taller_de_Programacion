#Luis Andrés Acuña Pérez
#Quiz

def pasalista(n):
    #n=4567093606
    lista=[]
    for i in range(n):
        if n!=0:
            #n!=0 si (4567093606 =/ 0)
            #n!=0 si (456709360 =/ 0)
            #n!=0 si (45670936 =/ 0)
            #n!=0 si (4567093 =/ 0)
            #n!=0 si (456709 =/ 0)
            #n!=0 si (45670 =/ 0)
            #n!=0 si (4567 =/ 0)
            #n!=0 si (456 =/ 0)
            #n!=0 si (45 =/ 0)
            #n!=0 si (4 =/ 0)
            #n!=0 no ( 0 = 0) sale del if
            lista=[n%10]+lista
            #n%10  lista
            #6      [6] - []+[6]
            #0      [0,6] - [0]+[6]
            #6      [6,0,6] - [6]+[0,6]
            #3      [3,6,0,6] - ...
            #9      [9,3,6,0,6]
            #0      [0,9,3,6,0,6]
            #7      [7,0,9,3,6,0,6]
            #6      [6,7,0,9,3,6,0,6]
            #5      [5,7,0,9,3,6,0,6]
            #4      [4,5,7,0,9,3,6,0,6]
            n//=10
            #n//=10
            #456709360
            #45670936
            #4567093
            #456709
            #45670
            #4567
            #456
            #45
            #4
            #
        else:
            return lista
            break
    return lista #[4,5,7,0,9,3,6,0,6]
"""
QUIZ
Escribir una funcion que recibe dos parametros digito entero y positivo
num entero y positivo pasa a lista
contar las apariciones del digito dentro del numero
WhileSD
WhileD
For range
For item
"""

def contar_digito(digito, n): #(6, 4567093606)
    if isinstance(digito, int) and isinstance(n, int):
        digito=abs(digito)
        n=abs(n)
        if digito>9: #6 < 9
            return "El dígito debe estar entre 0 y 9"
        lista_digitos=pasalista(n)
        #lista_digitos
        #[4,5,6,7,0,9,3,6,0,6]
        contador=0
        # contador = 0, 1, 2, 3
        for i in range(len(lista_digitos)):
            #i in range(10)
            if lista_digitos[i]==digito:
                #i      digito
                #4  =   6 no
                #5  =   6 no
                #6  =   6 si cont+1
                #7  =   6 no
                #0  =   6 no
                #9  =   6 no
                #3  =   6 no
                #6  =   6 si cont + 1
                #0  =   6 no
                #6  =   6 si cont +1
                contador+=1
        
        return contador
    else:
        print("Los parametros deben ser enteros positivos")
    
def EncontrarNumWSD(busq, num):
    lista=[]
    num=abs(num)
    busq=abs(busq)
    if isinstance(num, int) and  isinstance(busq, int):
        lista=pasalista(num)
        #lista = [4,5,6,7,0,9,3,6,0,6]
        cont=0 #0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        contapariciones=0 #0, 1, 
        while len(lista)>cont:
            if lista[cont]==busq:
                #list  busq digito
                #[0] == 4 == 6 no
                #[1] == 5 == 6 no
                #[2] == 6 == 6 si
                #[3] == 7 == 6 no
                #[4] == 0 == 6 no
                #[5] == 9 == 6 no
                #[6] == 3 == 6no
                #[7] == 6 == 6 si
                #[8] == 0 == 6 no
                #[9] == 6 == 6 si
                contapariciones+=1 #0, 1, 2, 3
            cont+=1
        print(contapariciones)
    else:
        print("Parametros incorrectos")

def whileD(digito, num):
    #digito=6 num=4567093606
    if isinstance(digito, int) and isinstance(num, int):
        digito = abs(digito)
        num = abs(num)
        num=pasalista(num)
        #num = [4,5,6,7,0,9,3,6,0,6]
        cont=0 #0, 0, 1, 1, 1, 1, 1, 2, 2, 3
        while num!=[]:
            #num=[4,5,6,7,0,9,3,6,0,6]
            #num=[5,6,7,0,9,3,6,0,6]
            #num=[6,7,0,9,3,6,0,6]
            #num=[7,0,9,3,6,0,6]
            #num=[0,9,3,6,0,6]
            #num=[9,3,6,0,6]
            #num=[3,6,0,6]
            #num=[6,0,6]
            #num=[0,6]
            #num=[6]
            #num=[] sale del while
            if digito==num[0]:
                #digito num
                #4 == 6 no
                #5 == 6 no
                #6 == 6 si
                #7 == 6 no
                #0 == 6 no
                #9 == 6 no
                #3 == 6 no
                #6 == 6 si
                #0 == 6 no
                #6 == 6 si
                cont+=1 #+1, +1, +1
            num=num[1:]
        return cont #3
    else:
        print("Parametro incorrecto")

def item(digito, num):
    if type(digito)==int and type(num)==int:
        digito=abs(digito)
        num=abs(num)
        listanum=pasalista(num)
        #lista = [4,5,6,7,0,9,3,6,0,6]
        i=0 #innecesario?
        cont=0 #0, 1, 2, 3
        for item in listanum:
            if digito==item:
                #digito   item
                #6  ==  4 no
                #6  ==  5
                #6  ==  6 si
                #6  ==  7
                #6  ==  0
                #6  ==  9
                #6  ==  3
                #6  ==  6 si
                #6  ==  0
                #6  ==  6 si 
                cont=cont+1
        print(cont) #3
    else:
        print("Parametro incorrecto")
        


