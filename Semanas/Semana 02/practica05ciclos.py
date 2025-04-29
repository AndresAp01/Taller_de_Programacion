#Al programar podemos hacerlo en incrementos o en decrimentos, los numeros van subiendo o bajando

def quehace(num):
    contador=0
    while num>=0:
        if num%2==0:
            contador = contador+1
        num = num-1
    print(contador)
