def largofor(num):#234
    if isinstance(num,int):
        num=abs(num)
        if num==1:
            return 1
        else:
            cont=0
            for i in range(0,num,1):#i=0si,1si,2si,3si......,233
                if num==0:
                   #233x 23x 2x 0si
                   # print(i)
                    #print("Contador: ",cont)#3
                    #return cont
                    break
                cont=cont+1#1 2 3
                num=num//10#23 2 0
            print(cont)
    else:
        print("Parametro incorrecto")
