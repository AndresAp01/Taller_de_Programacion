#Cramer Luis Andres Acunna Perez
import matplotlib.pyplot as grafica

def crammer():
    with open("ecuaciones.txt", "r") as archivo: #abre
        #line.strip para eliminar saltos
        #for line recorrer linea x linea
        ecuaciones=[int(line.strip()) for line in archivo if line.strip()!=""]
        #range(0, len, 3) para tener indices de 0 hasta la longitud de ecuaciones, incremento de 3 en 3
        #ecuaciones[i:i+3] sublista de 3 el;ementos desde i
        #[x, y, soluc]
    ecuaciones=[ecuaciones[i:i+3] for i in range(0, len(ecuaciones), 3)]

    a1=ecuaciones[0][0]
    b1=ecuaciones[0][1]
    c1=ecuaciones[0][2]
    a2=ecuaciones[1][0]
    b2=ecuaciones[1][1]
    c2=ecuaciones[1][2]

    print("Ecuaciones:", ecuaciones)
    determinante=ecuaciones[0][0]*ecuaciones[1][1]-ecuaciones[1][0]*ecuaciones[0][1]
    determinantey=(ecuaciones[0][0]*ecuaciones[1][2])-(ecuaciones[1][0]*ecuaciones[0][2])
    determinantex=ecuaciones[0][2]*ecuaciones[1][1]-ecuaciones[1][2]*ecuaciones[0][1]

    print(f"Ecuación 1: {a1}x + {b1}y = {c1}")
    print(f"Ecuación 2: {a2}x + {b2}y = {c2}")

    if determinante!=0:
        difx=determinantex/determinante
        dify=determinantey/determinante
        par_ordenado=(difx, dify)
        print("Punto de intersección:", par_ordenado)
    else:
        print("Las ecuaciones son paralelas, no hay punto de intersección.")
        par_ordenado=None

    #Si detGen=0 no hay punto de interseccion
    valorx=list(range(-60, 60))

    y1=[(ecuaciones[0][2]-a1*i)/b1 for i in valorx]
    y2=[(c2-a2*i)/b2 for i in valorx]

    grafica.figure()
    grafica.title("Regla de cramer")
    grafica.xlabel("Eje x")
    grafica.ylabel("Eje y")
    grafica.grid(True)
    grafica.tight_layout()
    grafica.plot(valorx, y1)
    grafica.plot(valorx, y2)
    if par_ordenado is not None:
        grafica.scatter(difx, dify, color='red', s=100, label=f"Intersección ({difx:.2f}, {dify:.2f})")

    else:
        grafica.text(0, 0, "Ecuaciones paralelas")
    grafica.legend()
    print(par_ordenado)
print(crammer())
grafica.show()
