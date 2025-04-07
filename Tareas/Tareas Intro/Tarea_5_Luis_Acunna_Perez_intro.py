#Tarea 5 Intro Luis Andres Acunna Perez
#En Radix_explicacion() Viene el codigo con la corrida
#codigo auxiliar par obtener el largo de un num
def largo(num):
    if num==0:
        print(1)
    else:
        cont=0
        while num!=0:
            num=num//10
            cont=cont+1
        return cont
#codigo auxiliar de ordenamiento por insercion
def insercion(lista):
    for i in range (1,len(lista)):
        v=lista[i]
        j=i-1
        while j>=0 and lista[j]>v:
            lista[j+1]=lista[j]
            j=j-1
        lista[j+1]=v
    return lista

def Radix(lista):
    print(lista)
    max_num=lista[0]
    for num in lista:
        if num>max_num:
            max_num=num
    largo_mayor=largo(max_num)
    print(max_num, largo_mayor)
    for _ in range(largo_mayor):
        lista_temp=[]
        for i in range(10):
            lista_temp=lista_temp+[[]]
        for i in range(len(lista)):
            digito=(lista[i]//(10**_))%10
            lista_temp[digito]=lista_temp[digito]+[lista[i]]
            print(lista_temp)
        lista_completa=[]
        for i in range(10):
            lista_temp_ordenada=insercion(lista_temp[i])
            lista_completa=lista_completa+lista_temp_ordenada
        lista=lista_completa
    print(lista)
Radix([45, 2, 170])

def Radix_explicacion(lista): #CON [45, 2, 170]
    print(lista)
    #Obtenemos el numero mas grande de la lista
    #Empieza en 45
    max_num=lista[0]
    for num in lista:
        if num>max_num:
            # 45>45=45
            # 45>2=45
            # 45>170=170
            max_num=num
    largo_mayor=largo(max_num)
    print(max_num, largo_mayor)

    for _ in range(largo_mayor):
        #desde _ = 0 hasta _ = largo_mayor - 1
        #_ = 0 : unidades
        #_ = 1 : decenas
        #_ = 2: centenas

        #Abro 10 listas de trabhajo
        lista_temp=[]
        for i in range(10):
            lista_temp=lista_temp+[[]]
        #para cada numero en la lista de trab
        for i in range(len(lista)):
            digito=(lista[i]//(10**_))%10 #obtengo el ultimo digito
            #diigito
            #lista[0]=45
            #45//(10**0)%10 =5

            #lista[1]=2:
            #2//1%10=2

            #lista[2]=170
            #170//1%10 = 0
            lista_temp[digito]=lista_temp[digito]+[lista[i]] #actualizo las lista temporal
            #lista_temp[5]= []+[45]
            #lista_temp[2]= []+[2]
            #lsita_temp[0]= [0]+[170]
            print(lista_temp) #para imprimir cada iteracion
        #unimos todas las temporales
        lista_completa=[]
        for i in range(10):
            lista_temp_ordenada=insercion(lista_temp[i])
            lista_completa=lista_completa+lista_temp_ordenada
            #lista completa = [170] + [] + [2] + [] + []+ [45] + []+[]+[]+[]
            #[170,2,45]
            #[2,45,170]
            #[2,45,170]
        lista=lista_completa
    print(lista)
