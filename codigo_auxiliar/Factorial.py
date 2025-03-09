def factorialINC(num):  # Funciona
    if num < 0 or not type(num) == int:
        print("Parametro de entrada no valido")
    elif num == 0:
        return 1
    else:
        # resultado  i   num
        # 4          1   4
        # 4          2   4
        # 8          3   4
        # 24         4   4

        resultado = num
        i = 1
        while i < num:  # 1<4? si 2<4 si 3<4si 4<4no
            resultado = resultado * i
            # 4*1=4 4*2=8 8*3=24
            i = i + 1  # 2 3 4
        return resultado  # 24


def factorialDEC(num):  # Funciona
    if num < 0 or not type(num) == int:
        print("Parametro de entrada no valido")
    elif num == 0:
        return 1
    else:
        # resultado  i   num
        # 1          4   4
        # 4          3   4
        # 12         2   4
        # 24         1   4
        # 24         0   4

        resultado = 1
        i = num
        while i > 0:  # 4>0 si 3>0 si 2>0si 1>0 SI 0>0X
            resultado = resultado * i
            # 1*4=4 4*3=12 12*2=24 24*1=24
            i = i - 1  # 3 2 1 0
        return resultado  # 24