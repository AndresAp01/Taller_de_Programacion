#Luis Andres Acunna Perez
Paises=[]
Ciudades=[]
Codigos_Paises=[]
Codigos_Ciudades=[]

def abrir_archivo(ruta, n):
    lista_final=[]
    lista_codigos=[]
    with open(ruta, "r") as archivo:
        for linea in archivo:
            if linea.strip()=="":
                continue
            lista_temp=linea.strip().split(";")
            if n==1:
                if lista_temp[0] not in lista_codigos:
                    lista_final += [lista_temp]
                    lista_codigos += [lista_temp[0]]
            elif n==2:
                if lista_temp[0] not in lista_codigos:
                    lista_final += [lista_temp]
                    lista_codigos += [lista_temp[0]]
    return lista_final, lista_codigos

Paises, Codigos_Paises = abrir_archivo("Paises.txt", 1)
Ciudades, Codigos_Ciudades=abrir_archivo("Ciudades.txt", 2)

def crear_reporte(ruta, contenido):
    with open(ruta, "w") as archivo:
        archivo.write(contenido)

def reporte_paises():
    texto="----Paises----\n"
    for pais in Paises:
        texto+="Nombre del pais: "+ pais[1]+" codigo: "+pais[0]+"\n"
    print(texto)
    return texto

def reporte_ciudades_por_paises(cod):
    texto="----Ciudades----\n"
    for pais in Paises:
        if pais[0]==cod:
            texto+=pais[1]+":\n"
            break
    for ciudad in Ciudades:
        if ciudad[0]==cod:
            texto+="Nombre de la ciudad: "+ ciudad[2]+", codigo: "+ ciudad[1] +", en el pais: " + ciudad[0] +"\n"
    print(texto)
    return texto


while True:
    opciones=input("---MENU---\n 1. Insercion, 2. Busqueda, 3. Reportes, 4. Salir")
    if opciones=="1":
        pass
    elif opciones=="2":
        pass
    elif opciones=="3":
        while True:
            opcion=input("Ingrese la opcion que desea realizar: 1. Paises, 2. Ciudades, 3. Regresar")
            if opcion=="1":
                contenido=reporte_paises()
                crear_reporte("Reporte_de_Paises.txt", contenido)
            elif opcion=="2":
                while True:
                    cod_pais=input("Codigo del pais: ")
                    if cod_pais not in Codigos_Paises:
                        input("Error, no existe este pais.")
                    else:
                        for pais in Paises:
                            if pais[0]==cod_pais:
                                no_pais=pais[1]
                                break

                        contenido=reporte_ciudades_por_paises(cod_pais)
                        crear_reporte("Reporte_de_Ciudades_"+no_pais+".txt", contenido)
            elif opcion=="3":
                break
    elif opciones=="4":
        break
    else:
        print("Opcion no valida")
