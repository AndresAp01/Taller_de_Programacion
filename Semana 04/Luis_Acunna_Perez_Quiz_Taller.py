#Luis Acunna Perez, Quiz Taller

def largo(num):
    if num==0:
        print(1)
    else:
        cont=0
        
        while num!=0:
            num=num//10
            cont=cont+1
        return(cont)

#Escribir una funcion que recibedos num de cualq largo igual tamaño
def sumasinceros(num1, num2):
    #num1 = abs(num1)
    #num2 = abs(num2)
    if type(num1)==int and isinstance(num2, int) and largo(num1)==largo(num2):
        num1 = abs(num1)
        num2 = abs(num2)
        exp1=0
        exp2=0
        nuevo_num_1=0
        nuevo_num_2=0

        while num1!=0:
            if num1%10==0:
                num1=num1//10
            
            else:
                nuevo_num_1=nuevo_num_1 + ((num1%10)*(10**exp1))
                num1=num1//10
                exp1=exp1+1

        print(nuevo_num_1)

        while num2!=0:
            if num2%10==0:
                num2=num2//10
            
            else:
                nuevo_num_2=nuevo_num_2 + ((num2%10)*(10**exp2))
                num2=num2//10
                exp2=exp2+1

        print(nuevo_num_2)
        print("La suma total es: ",nuevo_num_1 + nuevo_num_2)
    else:
        print("Algun parametro es incorrecto.")
        

#Eliminar los 0 y contruir dos numeros nuevos
    
#------------ Suma sin ceros ---------------
