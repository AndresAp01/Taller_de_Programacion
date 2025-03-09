# Escribir una funcion que permite saber si un numero tiene un digito par
# Recibe un numero entero y positivo, si llega a negativo, puede utilizar abs()
# Retornar True or False (booleana)
# num=23456789
#    =3579 False
#    =35769 True

def espar(num):  # Funciona #57891
    if not type(num) == int:
        print("Parametro incorrecto")
    elif num == 0 or num == 2 or num == 4 or num == 6 or num == 8:
        return True
    else:

        haypar = False  # Equivale a una bandera
        # y saquemosle una copia al numero para no eliminar el original
        copia = abs(num)

        # copia  espar   num
        # 57891  False   57891
        # 5789   False   57891
        # 578   False   57891

        while copia != 0:  # 57891si 5789 578 si
            temp = copia % 10  # 1 9
            if temp % 2 == 0:  # 1%2 no 9%2 no 8%2si
                haypar = True  # TRUE
                break  # Para porque ya encontró UNO no hace falta buscar más
            copia = copia // 10  # 5789 578
        return haypar, copia