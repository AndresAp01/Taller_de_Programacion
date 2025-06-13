#Luis Andres Acunna Perez
#Segundo Examen de Taller de Programacion

from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import os

#Funciones auxiliares
"""
apilar:
    Esta funciopn es como un push
    Recibe una lista y un valor
    Construye una nueva lista con el operador + y lo coloca en valor al final
    Devuelve lista nueva
"""
def apilar(pila, valor):
    return pila+[valor]
"""
desapilar:
    Esta funcion es como un pop
    Toma el ultimo elemento con pila[-1]
    Toma todo menos el ultimo son slicing
    Devuelve elemento extraido, pila restante para saber que quitamos y como quedo la pila
"""
def desapilar(pila): #como un pop
    return pila[-1], pila[:-1]#slicing

#Diccionarios de prioridad
PRIORIDAD_DENTRO={
    '^': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0
}
PRIORIDAD_FUERA={
    '^': 4,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 5,
    ')': -1
}
#Mientras la prioridad-dentro del operador de la cima sea >= la prioridad-fuera del operador nuevo, uso desapilar
# y lo envio a la salida. Si la prioridad-fuera es mayor, apilamos directamente.

def leer_archivos(lista_rutas):
    """
        #1 Se lee el archivo
        #2 construye lista de trabajo
        #Agarro la primera sublista para trabajarla
        Crear expresion como lista (utilizando ListaPila y ListaExpresion)
        Evaluar Expresion con recursividad (de pila o de cola)
        Imprimir expresion matematica de cada archivo, cada sublista de la listaArchivos, listaExpresion y Evaluacion, para cada archivo
        """
    resultado=[]# Lista principal

    for i in range(len(lista_rutas)):
        elemento=[] # Guardara los elementos del archivo
        with open(lista_rutas[i], "r") as archivo:
            for linea in archivo:
                linea=linea.strip() #quita espacios y saltos de linea
                if linea=="": #ignora lineas vacias
                    continue
                palabras=linea.split()
                elemento=elemento+palabras
        sublista=[i+1]+elemento
        resultado=resultado+[sublista]
    return resultado

def principal(exp_infija):
    """
        Devuelve la misma expresion en postfijo
        Convierte la expresion matematica en notacion ExpresionOriginal a notacion postfija (operadores despues de operandos)
        Se crea una lista pila vacia y una lista para ListaExpresion
        Numeros se annaden directamente al ListaExpresion
        parentesis abierto se apila en la pila de operadores
        parenteiss cerrado se desapila operadores hasta encontrar el (
        operadores + - * /
            Mientras haya operadores en la pila mayor o igual prioridad se desapila el ListaExpresion
            leugo se le apila el operador actual
        Termina con desapilar todos los operadores restantes al ListaExpresion
    """
    ListaPila=[]  #Entran los operadores, nunca entran numeros, sera la pila de operadores cuando convirtamos la expresion.
    ListaExpresion=[]   # Entran los numeros, combinoacion de numeros y operadores

    for elem in exp_infija:
        # a) numero
        if elem.isdigit():
            ListaExpresion=apilar(ListaExpresion, elem)
        # b) '('
        elif elem=='(':
            ListaPila=apilar(ListaPila, elem)
        # c) ')'
        elif elem==')':
            op, ListaPila=desapilar(ListaPila)
            while op!='(':
                ListaExpresion=apilar(ListaExpresion, op)
                op, ListaPila=desapilar(ListaPila)
        # d) operador + - * / ^
        else:
            while (ListaPila and PRIORIDAD_DENTRO[ListaPila[-1]]>=PRIORIDAD_FUERA[elem]):
                op, ListaPila=desapilar(ListaPila)
                ListaExpresion=apilar(ListaExpresion, op)
            ListaPila=apilar(ListaPila, elem)
    # vaciar pila restante
    while ListaPila:
        op, ListaPila=desapilar(ListaPila)
        ListaExpresion=apilar(ListaExpresion, op)
    return ListaExpresion

OPERADORES={
    '+',
    '-',
    '*',
    '/',
    '^'
}
#Evalua
"""
    Evalua
    elementos es lista[str] secuencia de operandos y operadores como cadena
    devuelve un resultado numerico si es correcta o error 
"""
def Evaluar(elementos):
    try:
        return Evaluar_Aux(elementos, 0, [])# indice 0 y pila vacia
    except ZeroDivisionError:
        return "Error: division entre cero"
    except Exception:# operandos insuficientes, etc.
        return "Error: expresión invalida"

#Funcion auxiliar de Evaluar
def Evaluar_Aux(elementos, indice, pila):
    """
        Evalua recursivamente una expresion
        elementos es la lista de cadenas
        indice es la posicion actual que se esta procesando
        pila es la lista que actua como pila de operandos
    """
    if indice==len(elementos): #finalizacion, cuando se haya leido todo
        if len(pila)==1: #si indice alcanza la longitus de la lista, ya se leyo todo
            return pila[0] #resultado final
        else:
            return "Error: expresión inválida"
    #2. si es operando
    if elementos[indice] not in OPERADORES: #no es operador?
        return Evaluar_Aux(elementos, indice+1, pila+[int(elementos[indice])])
        #retorna la misma lista, siguiente simboolo, pila nueva
    #3. si es operador
    if len(pila)<2:# falta operandos
        raise ValueError
    #cada llamada crea una NUEVA pila quitando los dos ultimos
    #y agregando el resultado correspondiente
    if elementos[indice]=='+':
        return Evaluar_Aux(elementos, indice+1, pila[:-2]+[pila[-2]+pila[-1]])
    if elementos[indice]=='-':
        return Evaluar_Aux(elementos, indice+1, pila[:-2]+[pila[-2]-pila[-1]])
    if elementos[indice]=='*':
        return Evaluar_Aux(elementos, indice+1, pila[:-2]+[pila[-2]*pila[-1]])
    if elementos[indice]=='/':
        if pila[-1]==0: #comprobacion de division entre cero
            raise ZeroDivisionError
        return Evaluar_Aux(elementos, indice+1, pila[:-2]+[pila[-2]/pila[-1]])
    #para potencia
    return Evaluar_Aux(elementos, indice+1, pila[:-2]+[pila[-2]**pila[-1]])

#Para crear los PDFs
def crear_reportes_pdf(lista_rutas):
    expresiones=leer_archivos(lista_rutas)
    for sublista in expresiones:
        n_archivo=sublista[0] #numero de archivo
        ListaExpresion=sublista[1:] #expresion en infijo
        Expresion=" ".join(ListaExpresion)
        ExpresionPostFija=principal(ListaExpresion)#postfijo
        ListaExpresion=" ".join(ExpresionPostFija)#para imprimir
        valor=Evaluar(ExpresionPostFija)

        nombre_pdf=f"Reporte_{n_archivo}.pdf"
        c=canvas.Canvas(nombre_pdf, pagesize=LETTER)
        ancho, alto=LETTER

        y=alto-72
        c.setFont("Helvetica-Bold", 14)
        c.drawString(72, y, f"Reporte de Expresión #{n_archivo}")
        c.setFont("Helvetica", 12)
        y-=36
        c.drawString(72, y, "Expresión matemática:")
        y-=18
        c.drawString(100, y, Expresion)
        y-=30
        c.drawString(72, y, "ListaExpresion (postfija):")
        y-=18
        c.drawString(100, y, ListaExpresion)

        y-=30
        c.drawString(72, y, f"Evaluación: {valor}")
        # opcional: pie de página
        c.setFont("Helvetica-Oblique", 8)
        c.drawString(72, 36, "Generado automáticamente con ReportLab")

        c.save()
        print(f"✓ Generado {nombre_pdf}")

ListaArchivos=[
    "Archivos/Arch1.txt",
    "Archivos/Arch2.txt",
    "Archivos/Arch3.txt",
    "Archivos/Arch4.txt",
    "Archivos/Arch5.txt"
]
expresiones=leer_archivos(ListaArchivos)

for sub in expresiones:
    n_archivo=sub[0]
    ExpresionOriginal=sub[1:]
    postfijo=principal(ExpresionOriginal)
    valor=Evaluar(postfijo)
    print(f"\nArchivo #{n_archivo}")
    print("  Expresion Original :", ExpresionOriginal)
    print("  ListaExpresion :", postfijo)
    print("  Resultado:", valor)
    print("_________________________________________________")

crear_reportes_pdf(ListaArchivos)