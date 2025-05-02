def factorialfor(n):#n=3=>6
    if type(n)==int and n>=0:
        if n==0: #or n==1:
            return 1
        else:
            resultado=n
            #resultado   n    i
            #3           3    2
            
            for i in range(2,n):#1si 2si 3x
                resultado=resultado*i
                #3*2=6          #3*1=3  3*2=6
            return resultado#6
    else:
        print("Parametro incorrecto")
