x=27
if (x%4)==0:
    print(x*x)
elif (x%4)==1:
    print(x/6)
elif (x%4)==2:
    print(((x**2)*(x**3))**2)
elif (x%4)==3:
    print(x**3+5)
else:
    print("No hay nada que hacer")

print(x**3+5)
