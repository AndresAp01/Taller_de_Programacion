#Luis Andres Acunna Perez

def operacion(num): # variable: 2345678
    sumador_par = 0 # Acumulara los digitos pares
    sumador_impar = 0 # Acumulara los digitos impares

    #sumador_impar  num*
    #7              49
    #5              49+(5**2)=74
    #3              74+(3**2)=83
    
    if num==0: # Si la variable es =0, no hara todo el procedimiento
        print(0)
    else:
        while num!=0:
            # para obtener el ultimo digito:
            ultimo = num % 10 #8, 7, 6, 5, 4, 3, 2
            # podria usar +=
            if ultimo % 2 == 0: # 8%2si, 7%2no, 6%2si, 5%2no, 4%2si, 3%2no, 2%2si
                sumador_par=sumador_par+(ultimo**3)
                #sumador_par    num*
                #8 = 0 + (8**3) = 512
                #6 = 512 + (6**3) = 728
                #4 = 728 + (4**3) = 792
                #2 = 792 + (2**3) = 800

            else:
                sumador_impar=sumador_impar+(ultimo**2)
                #sumador_impar  num*
                #7 = 0 + (7**2) = 49
                #5 = 49 + (5**2) = 74
                #3 = 74 + (3**2) = 83
                
            # podria hacerse con num //=10
            num=num//10
    print("La suma de los digitos pares e impares del numero es: ",sumador_par+sumador_impar)

    #variable asignada: 2345678
    #resultado= 883, 800 suma de los pares, 83 suma de los impares;)


