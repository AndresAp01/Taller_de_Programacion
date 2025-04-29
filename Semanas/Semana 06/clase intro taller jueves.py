#Lista se puede trabajar de dos maneras:
#Por contenido [3,4,5,6,7,8] busque los pares [4,6,8]
#Posicion [3,4,5,6,7,8] dusque los elementos de posiciones pares [3,5,7]

#Contenido *********************************
#Escribir una funcion  que recibe una lista, validar que sea lista
#Separar la lista en dos. Una Listapares y otra Listaimpares. 
#Destruyendo y sin destruir

def separaparesimparesD(lista):#[3,4,5,6,7,8]
    if type(lista)==list :
        ListaPares=[]
        ListaImpares=[]
        #ListaPares      ListaImpares      lista
        
        while lista!=[]:
            if lista[0]%2==0:
                ListaPares=ListaPares+[lista[0]]
               
            else:
                ListaImpares=ListaImpares+[lista[0]]
                
            lista=lista[1:]#
        print(ListaPares,ListaImpares,lista)#
    else:
        print("Parametro incorrecto")

def separaparesimparesSD(lista):#[3,4,5,6,7,8]
    if type(lista)==list :
        ListaPares=[]
        ListaImpares=[]
        i=0
        #ListaPares      ListaImpares    i         lista
       
        
        while i<len(lista):     #i<=len(lista)-1
          
            if lista[i]%2==0:#
                ListaPares=ListaPares+[lista[i]]
               
            else:
                ListaImpares=ListaImpares+[lista[i]]
                
            i=i+1#
        print(ListaPares,ListaImpares,lista)#
    else:
        print("Parametro incorrecto")

#Posicion destruyendo y sin destruir

def separaParesImparesPosD(lista):#[3,4,5,6,7,8]
    if isinstance(lista,list):
        ListaPares=[]
        ListaImpares=[]
        i=0
        #ListaPares      ListaImpares     i        lista
        #[]              []               0        [3,4,5,6,7,8] si

        while lista!=[]:
            if i%2==0:#
                ListaPares=ListaPares+[lista[0]]
               
            else:
                ListaImpares=ListaImpares+[lista[0]]
               
            lista=lista[1:]#
            i=i+1#
        print(ListaPares,ListaImpares,lista)#
    else:
        print("Parametro incorrecto")


def separaParesImparesPosSD(lista):#[3,4,5,6,7,8]
    if isinstance(lista,list):
        ListaPares=[]
        ListaImpares=[]
        i=0
        #ListaPares     ListaImpares     i     lista
        #[]             []               0
        #{3]            []               1
        #[3]            [4]              2
        #[3,5]          [4]              3
        #[3,5]          [4,6]            4
        #[3,5,7]        [4,6]            5
        #[3,5,7]        [4,6,8]
        
        while i<=len(lista)-1:#
            if i%2==0:#
                ListaPares=ListaPares+[lista[i]]
               
            else:
                ListaImpares=ListaImpares+[lista[i]]
                
            i=i+1#
        print(ListaPares,ListaImpares,lista)#
    else:
        print("Parametro incorrecto")
        
def largo(num):#2345
    if num==0:
        return 1
    else:
        #cont   num
        #0      2345
        #1      234
        #2      23
        #3      2
        #4      0
            
        cont=0
        while num!=0:#2345si  234si  23si 2si 0x
            num=num//10#234  23  2  0
            cont=cont+1#1 2 3 4
        return cont#4

#Escribir una funcion que recibe un numero entero positivo de cualquier tamaño,
#y se construye uno nuevo sumando los extremos y si es impar
#agregando el centro.
        
def suma(num):# 2578639
    resultado = 0# 
    mayorExp = largo(num)-1# 7-6=6
    menorExp = 1# 1
    resultadoExp = 0# 
    #**********************************************************
    #resultado    mayorExp     menorExp         resultadoExp
    #0            6            1                0
    #6            3            2                1
    #612          2            3                2
    
    while menorExp <= largo(num)/2:
      #1<=7/2 =>1<=3.5 si

           
        
      if resultado != 0:#
            resultado *= 10#
            
        #Calcular numeros en los extremos
      n1 = (num//(10**mayorExp))%10
        #(2578639//(10**6))%10
        #(2578639//(10**6))
      n2 = (num%(10**menorExp))//(10**resultadoExp)
    
      print("Primer numero: ",n1) #
      print("Segundo numero: ",n2)#
      suma = n1 + n2#
      if suma >= 10:#
            resultado *= 10# 
      resultado += suma#
      print("Suma: ",resultado)#
      mayorExp -= 1#
      menorExp += 1#
      resultadoExp += 1#
        
    # fuera del while           
    if largo(num)%2 == 1:#
        #Si es impar se saca el del centro
        n = (num//(10**mayorExp))%10#
        print("Numero del centro: ", n)#
        resultado *= 10#612*10=
        resultado += n#
    return resultado# 


def Operacionlistafor(num, lista):
    if type(num)==int and isinstance(lista, list):
        num = abs(num)
        if lista == []:
            return []
        else:
            listaNueva = []
            #num    listaNueva
            #0      [3,4,5,6,7] [9]  
            for i in range(len(lista)):
                if lista[i]%2==0:
                    listaNueva=listaNueva+[lista[i]+num]
                else:
                    listaNueva=listaNueva+[lista[i]**num]
            return listaNueva
    else:
        print("Parametro incorrecto")
 
def OperacionesListaformisma(num, lista): #2, [3,4,5,6,7]
    if type(num)==int and isinstance(lista, list):
        num=abs(num)
        if lista==[]:
            return[]
        else:
            for i in range(len(lista)):
                if lista[i]%2==0:
                    lista[i]=lista[i]+num
                else:
                    lista[i]=lista[i]**num
            return lista
    else:
        print("Incorrecto")


"""def OperacionItem(lista):
    if type(num)==int and type(lista)==list:
        num=abs(num)
        if lista==[]:
            return []
        else:
            for item in lista:
                if lista

    else:
        print("parametro incorrect")"""


#Escribir una funcionque recibe una lista(validar)
#cambiar por -1 los pares de la lista
#while sin dest
#while destr
#for range
#for item

def with_whileSD(lista):
    if type(lista)==list:
        if lista==[]:
            return []
        else:
            i=0
            while i<len(lista):
                if lista[i]%2==0:
                    lista[i]=-1
                i=i+1
            print(lista) 
    else:
        print("parametro incorrecto") 


def contar_pares_d(lista):
    if type(lista)==list:
        if lista==[]:
            return[]
        else:
            listaNueva=[]
            while lista!=[]:
                if lista[0]%2==0:
                    listaNueva=listaNueva+[-1]
                else:
                    listaNueva=listaNueva + [lista[0]]
                lista=lista[1:]
            print(listaNueva)
    else:
        print("parametro incorrecto")

def CambiaParesFR(lista):
    if isinstance(lista,list):
        if lista==[]:
            return[]
        else:
            for i in range(len(lista)):
                if lista[i]%2==0:
                    lista[i]=-1
            return lista
    else:
        print("Parametro incorrecto")

