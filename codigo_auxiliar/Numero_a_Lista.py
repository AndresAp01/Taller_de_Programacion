def Pasalista(num):  # 5678  0=[0]
    if isinstance(num, int):
        num = abs(num)
        if num >= 0 and num <= 9:
            return [num]
        else:
            listaNueva = []
            # listaNueva     num
            # []             5678
            # [8]            567
            # [7,8]          56
            # [6,7,8]        5
            # [5,6,7,8]      0

            while num != 0:  # 5678si 567si 56si 5si 0x
                listaNueva = [num % 10] + listaNueva
                # [8]+[]=[8]
                # [7]+[8]=[7,8]
                # [6]+[7,8]=[6,7,8]
                # [5]+[6,7,8]=[5,6,7,8]
                num = num // 10  # 567 56 5 0
            return listaNueva  # [5,6,7,8]
    else:
        print("Parametro incorrecto")