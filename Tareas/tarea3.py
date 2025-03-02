#Luis Andres Acunna Perez

def sumaparesimpares(num):  # 2345678
    if num == 0:
        print(0)
    else:
        suma = 0  # acumulador
        
        while num != 0:
            temp = num % 10 #8, 7, 6, 5, 4, 3, 2
            if temp % 2 == 0:  # pares # 8%2si, 7%2no, 6%2si, 5%2no, 4%2si, 3%2no, 2%2si
                suma = suma + (temp ** 3)
                #8 = 0 + (8**3) = 512
                #6 = 512 + (6**3) = 728
                #4 = 728 + (4**3) = 792
                #2 = 792 + (2**3) = 800
                """--> <-- aqui habia un num = num // 10 en el codigo original del documento.
                lo que estaba haciendo que se dividiera dos veces dentro del while,
                por lo que no dejaba que se sumaran los impares y diera solo {800}"""
            else:
                suma = suma + (temp ** 2)  # impares
                #7 = 0 + (7**2) = 49
                #5 = 49 + (5**2) = 74
                #3 = 74 + (3**2) = 83
            num = num // 10
        print("La suma de los digitos pares e impares del num es: ", suma)
        #variable asignada: 2345678
        #resultado= 883, 800 suma de los pares, 83 suma de los impares;)
