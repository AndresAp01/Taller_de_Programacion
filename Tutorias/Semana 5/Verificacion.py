#Luis Andres Acunna Perez, Tarea de Verificacion

#Cree una función que reciba un carácter, este carácter puede ser cualquiera de los operadores que hemos visto en la tutoría,
# además, debe retornar o
# imprimir el funcionamiento de dicho operador, use funciones, condicionales y operadores.
print(f"Hola, para saber el funcionamiento de los tipos de datos, llame a la funcion explicar() y dentro del parentesis escriba entre comillas "" el tipo de dato u operador que quiera saber.")
print("Para tipos de datos: int, float, complex, str, bool")
print("Para tipos de operadores aritmeticos: +, -, *, /, //, %, **")
print("Para saber sobre el de asignacion: = ")
print("Para saber sobre condicionales: if, elif, else")
print("Para saber sobre comparacion: ==, !=, >, <, >=, <=")
print("Para saber de operadores logicos: and, or, not")
def explicar(caracter):
    caracter = str(caracter)
    if caracter in ["int", "float", "complex", "str", "bool"]:
        if caracter == "int":
            print("Tipo de dato 'int': Devuelve un numero entero...")
        if caracter == "float":
            print("Tipo de dato 'float': Devuelve un numero flotante, esto es, perteneciente a los reales...")
        
        if caracter == "complex":
            print("Tipo de dato 'int': Devuelve un numero complejo...")

    elif caracter in ["if", "elif", "else"]:
        if caracter == "if":
            print("Estructura condicional 'if': Ejecuta un bloque de código si la condición es True (Verdadera).")
        elif caracter == "elif":
            print(
                "Estructura condicional 'elif': Ejecuta un bloque de código si la condición anterior es False y la suya es True(Verdadera).")
        elif caracter == "else":
            print(
                "Estructura condicional 'else': Ejecuta un bloque de código si todas las condiciones anteriores son False.")

    elif caracter in ["and", "or", "not"]:
        if caracter == "and":
            print("Operador lógico 'and': Devuelve True(Verdadera) si ambos operandos son True(Verdadera).")
        elif caracter == "or":
            print("Operador lógico 'or': Devuelve True(Verdadera) si al menos uno de los operandos es True(Verdadera).")
        elif caracter == "not":
            print("Operador lógico 'not': Invierte el valor de verdad del operando (de True -> a False, de False -> a True).")

    # Verificar si el carácter es un operador de asignación
    elif caracter == "=":
        print("Operador de asignación '=': Asigna el valor de la derecha a la variable de la izquierda.")

    # Verificar si el carácter es un operador aritmético
    elif caracter in ["+", "-", "*", "/", "//", "%", "**"]:
        if caracter == "+":
            print("Operador aritmético '+': Suma dos valores.")
        elif caracter == "-":
            print("Operador aritmético '-': Resta el segundo valor del primero.")
        elif caracter == "*":
            print("Operador aritmético '*': Multiplica dos valores.")
        elif caracter == "/":
            print("Operador aritmético '/': Divide el primer valor por el segundo (resultado flotante).")
        elif caracter == "//":
            print("Operador aritmético '//': Divide el primer valor por el segundo (resultado entero).")
        elif caracter == "%":
            print("Operador aritmético '%': Devuelve el residuo de la división del primer valor por el segundo.")
        elif caracter == "**":
            print("Operador aritmético '**': Eleva el primer valor a la potencia del segundo.")

    # Verificar si el carácter es un operador de comparación
    elif caracter in ["==", "!=", ">", "<", ">=", "<="]:
        if caracter == "==":
            print("Operador de comparación '==': Devuelve True(Verdadera) si ambos valores son iguales.")
        elif caracter == "!=":
            print("Operador de comparación '!=': Devuelve True(Verdadera) si los valores son diferentes.")
        elif caracter == ">":
            print("Operador de comparación '>': Devuelve True(Verdadera) si el primer valor es mayor que el segundo.")
        elif caracter == "<":
            print("Operador de comparación '<': Devuelve True(Verdadera) si el primer valor es menor que el segundo.")
        elif caracter == ">=":
            print("Operador de comparación '>=': Devuelve True(Verdadera) si el primer valor es mayor o igual que el segundo.")
        elif caracter == "<=":
            print("Operador de comparación '<=': Devuelve True(Verdadera) si el primer valor es menor o igual que el segundo.")

    # Si el carácter no es un operador válido
    else:
        print(f"'{caracter}' no es un operador válido.")
