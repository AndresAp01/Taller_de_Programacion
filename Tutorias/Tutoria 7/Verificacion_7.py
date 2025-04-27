#Luis Andres Acunna Perez
#Actividad de verificacion 7

def verif7(lista):
    if type(lista)==list:
        valor_buscar=int(input("Ingrese valor que desee cambiar: "))
        valor_reemplazo=int(input("Ingrese nuevo valor: "))

        i=0
        while i<len(lista):
            if lista[i]==valor_buscar:
                lista[i]=valor_reemplazo
            i+=1
        print(f"Lista modificada:", lista)

verif7([1,2,3,4,5,6,7,8,1,1])