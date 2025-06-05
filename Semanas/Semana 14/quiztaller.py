#Luis Andres Acuna Perez
class Estudiante:                       #encabezado
    nombre="" # atributo
    carnet=0 # atributo

    def modificarnombre(self, nom):
        self.nombre=nom

    def ImprimirEstudiantes(self): #metodo para imprimir estudiantes
        print("Nombre: ", self.nombre, "Carnet: ", self.carnet)

    def obtenerDatosEstudiante(self):
        return self.nombre, self.carnet

    def obtenerNombreEstudiante(self):
        print(self.nombre)

    def obtenerCarnetEstudiante(self):
        return self.carnet

    def imprimeEstudiante(x):
        print("%-40d %10s"%(x.obtenerCarnetEstudiante(), x.obtenerNombreEstudiante()))

    def asignarDatosEstudiante(self, car, nom):
        self.carnet=car
        self.nombre=nom

"""    def asignarDatosEstudiante(self,nom,car): # método para asignar valores
        self.nombre=nom
        self.carnet=car"""
"""    
    def modificarcarnewt(self, car):
        self.carnet=car"""



Estudiantes=[]
opcion=""
while opcion.upper()!="S":
    print(" 1.Ingresar estudiantes")
    print(" 2.Imprimir estudiantes")
    print(" 3.Modificar nombre")
    print(" 4.Imprimir nombre")
    print(" S.Salir")
    print("")
    print("----------------------------")
    opcion=input("Digite la opcion: ")
    if opcion=="1":
        p=Estudiante()
        p.carnet=int(input("Digite el carnet: "))
        p.nombre=input("Digite el nombre: ")
        Estudiantes.append(p)
        print("----------------------------")
    elif opcion=="2":
        print("Lista de Estudiantes")
        print("----------------------------")
        for i in range(len(Estudiantes)):
            Estudiantes[i].ImprimirEstudiantes()
        print("----------------------------")
    elif opcion=="3":
        car=int(input("Ingrese el carnet a buscar: "))
        encontro=-1
        for i in range(len(Estudiantes)):
            if Estudiantes[i].carnet==car:
                encontro=i
        if encontro!=-1:
            nom=input("Digite el nombre: ")
            Estudiantes[encontro].modificarnombre(nom)
        else:
            print ("Estudainte no existe!")
    elif opcion=="4":
        car=int(input("Ingrese el carnet a buscar: "))
        encontro=-1
        for i in range(len(Estudiantes)):
            if Estudiantes[i].carnet==car:
                encontro=i
        if encontro!=-1:
            Estudiantes[encontro].obtenerNombreEstudiante()
        else:
            print ("Estudainte no existe!")
    else:
        print("Terminamos")