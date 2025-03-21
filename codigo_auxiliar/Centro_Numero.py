# Centro de un numero,posiciones  se estan manejando desde 0

def centronum(num):  # 18965  centro=9 1867995
    if isinstance(num, int):
        num = abs(num)
        if len(num) % 2 != 0:  # 5%2!=0si
            larg = (len(num) - 1) // 2  # (5-1)//2=2 7-1//2=3
            cont = len(num) - 1  # 5-1=4

            while num != 0:  # 18965si 1896si 189si
                temp = num % 10  # 5 6 9
                if cont == larg:  # 4==2x 3==2x 2==2si
                    centro = temp  # 9
                    break
                num = num // 10  # 1896 189
                cont = cont - 1  # 3 2
            return centro  # 9
        else:
            print("Tamaño incorrecto")
    else:
        print("Parametro incorrecto")

