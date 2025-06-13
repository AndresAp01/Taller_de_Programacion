def SumatoriaCola(n):
    if isinstance(n, int):
        if n==0:
            return 0
        else:
            return SumatoriaC_aux(n,0)
    else:
        print("Parametro incorrecto")

def SumatoriaC_aux(n, resultado):
    if n==0:
        return resultado
    else:
        return SumatoriaC_aux(n-1, resultado+n)

def Sumatoria1(n):
    if type(n)==int:
        if n==0:
            return 0
        else:
            return Sumatoria_aux(n)

    else:
        print("Parametro incorrecto")

def Sumatoria_aux(n):
    if type(n)==0:
        if n==0:
            return 0
        else:
            return n+Sumatoria_aux(n-1)

    else:
        print("Parametro incorrecto")


#SUmatoria compoleja

def Sumatoria_compleja(n):
    if type(n)==int:
        return sumatoria_compleja_aux(n, (((n-2)**n)**3)*((n-1)**4), (n*4), 1, 0)
    else:
        print("Parametro incorrecto")

def sumatoria_compleja_aux(n, numerador, denominador, i, acumulado):
    if i>n:
        return acumulado
    return sumatoria_compleja_aux(n, numerador, denominador, i+1, acumulado+(i*numerador/(2*((denominador)**i)**2)+n))