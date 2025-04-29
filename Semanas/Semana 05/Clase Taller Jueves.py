#Escribir una funcion que recibe 3 parametros
#nuevo debe ser entero, puede ser positivo o negativo
#buscar debe ser entero, puede ser positivo o negativo
#lista se valida como lista
#buscar el parametro de nombre buscar dentro de la lista, si lo encuentra
#coloca a nuevo delante del parametro buscado
#Ejemplo nuevo=12   buscar=4  lista=[4,12,5,4,7,4,4]
                              #=>[12,4,12,5,12,4,7,12,4,12,4]

def buscar_agregarnum(nuevo,buscar,lista):#nuevo=-12   buscar=4  lista=[4,12,5,4,7,4,4]
    if type(nuevo)==int and isinstance(buscar,int)and type(lista)==list:
        if lista==[]:
            print("Lista no tiene elementos")
        else:
            i=0#
            
            while i<=(len(lista)-1):#
                if i==0 and buscar==lista[i]:
                    #
                    lista=[nuevo]+lista[0:]
                          #
                    i=i+1#
                elif buscar==lista[i]:
                    
                    lista=lista[0:i]+[nuevo]+lista[i:]
                    
                    i=i+1

                else:
                    lista=lista
                i=i+1
            print(lista)#
           
    else:
        print("Parametro incorrecto")
#buscar_agregarnum(12,4,[4,12,5,4,7,4,4])
        
#************************************************
def nuevalistacentro(lista1,lista2): #Puede que ayude en el examen
    #[3,5,7,9,11],
    #[1,0,4,2,8] [] []
    if type(lista1)==list and type(lista2)==list and len(lista1)== len(lista2) and len(lista1)!=0 :
        i=1#
        CentroIL2=0                     # Inicia un índice que apunta al primer elemento de la lista 2
        CentroFL2=len(lista2)-1         # Inicia un índice que apunta al último elemento de la lista 2
        print(CentroFL2)
        CentroIL1=(len(lista1)//2)-1    # Inicializa un índice que apunta al elemento a la izquierda del centro de lista1.
        CentroDL1=(len(lista1)//2)+1    # Para la derecha del centro de la lista 1 #5//2 = 2+3
        print(CentroDL1)
        LNueva=[]                       # Crea una nueva lista vacía donde se almacenarán los resultados.
        centro1=len(lista1)//2          # Inicializa un índice que apunta al elemento central de lista1.
        centro2=len(lista2)//2          # Para la lista 2
#i   CentroIL2  CentroFL2 CentroIL1 CentroDL1  LNueva     centro1 centro2

        while i<=len(lista1)//2: #Comienza un bucle que se ejecutará la mitad de veces(//2) que la longitud de lista1.
            LNueva=LNueva+[lista1[centro1]\
                           +lista2[CentroIL2]]\
                           +[lista1[centro1]+lista2[CentroFL2]]\
                           +[lista2[centro2]+lista1[CentroIL1]]\
                           +[lista2[centro2]+lista1[CentroDL1]]
            #        
            i=i+1 #Incrementa el contador
            CentroIL2=CentroIL2+1       # Avanza el índice desde el inicio de lista2.
            CentroFL2=CentroFL2-1       # Retrocede el índice desde el final de lista2.
            CentroIL1=CentroIL1-1       #
            CentroDL1=CentroDL1+1#
        print(LNueva)#
    else:
        print("Parametro incorrecto")
nuevalistacentro([3,5,7,9,11],[1,0,4,2,8])


#_____________________________________
"""Al trabajar con una lista se puede trabajar de dos formas:
Por contenido y por posicion
Contenido: [] buscar pares => [4,6,8]
Posicion: [] buscar elemento de posicion par => [3,5,7]
Escribir una funcion que recibe una lista, validar, separar los elementos en dos listas
Una lista de pares y otra de impares."""

def separarimparesD(lista): #[3,4,5,6,7,8]
    if type(lista)==list: #Si
        if lista == []:     #No
            return [[],[]]  
        else:
            ListaPares = []
            ListaImpares = []
            
            while lista!= []:
                if lista[0]%2 == 0:
                    ListaPares = ListaPares + [lista[0]]
                else:
                    ListaImpares = ListaImpares + [lista[0]]
                lista=lista[1:]
            return [ListaPares, ListaImpares]
    else:
        print("Parametros incorrectos.")

def separarimparesD(lista): #[3,4,5,6,7,8]
    if type(lista)==list: #Si
        if lista == []:     #No
            return [[],[]]  
        else:
            ListaPares = []
            ListaImpares = []
            i=0
            while i < len(lista):
                if lista[0]%2 == 0:
                    ListaPares = ListaPares + [lista[i]]
                else:
                    ListaImpares = ListaImpares + [lista[i]]
                i=i-1|
            return [ListaPares, ListaImpares]
    else:
        print("Parametros incorrectos.")    