def validar_nombres (nombre:str) -> bool:
   """ Valida que el nombre ingresado no este vacio
    args:
        str:nombre ingresado
    Returns:
        bool: True si el nombre no esta vacio, si no, retorna False
    """
    i=0
    resultado= False
    while i < len(nombre):
        if nombre[i] != " ":
            resultado= True
        i=i + 1
    return resultado

def nombre_estudiante() -> str:
    while True:
        nombre= input ("Ingrese el nombre del estudiante: ")
        if validar_nombres(nombre):
            break
        print ("Error, nombre invalido, reingrese un nombre correspondiente: ")
    return nombre


def validar_genero (genero:str) -> bool:
    resultado= False
    if genero == "M" or genero == "F" or genero == "X":
        resultado= True
    return resultado

def genero_estudiante () -> str:
    while True:
        genero= input ("Ingrese el genero del estudiante (F, M, X): ")
        if validar_genero(genero):
            break
        print ("Error, Genero incorrecto, debe ser 'F'', 'M', O 'X'.")
    return genero


def validar_legajo (legajo:int)-> bool:
    Valido=False
    if legajo >=1 and legajo <= 9999:
        Valido= True
    return Valido

def legajo_estudiante () -> bool:
    while True:
        legajo_numero= input("Ingrese el legajo_numero del estudiante: ")
    
        digito= True
        for numero in legajo_numero:
            if numero <"0" or numero > "9":
                    digito=False
        if digito == True:
            legajo = 0
            for numero in legajo_numero:
                legajo= legajo * 10 + (ord(numero) - ord("0"))
        
        if validar_legajo(legajo):
            return legajo
        print("Legajo invalido, Debe ingresar un numero valido: ")
    

def validar_nota (nota:int)-> bool:
    nota_valida= False
    if nota >= 1 and nota <= 10:
        nota_valida= True
    return nota_valida

def nota_estudiante () -> int:
    valido = False
    nota = 0

    while valido == False:
        entrada = input("Ingrese la nota del estudiante (1 a 10): ")

        digito = True
        for caracter in entrada:
            if caracter < "0" or caracter > "9":
                digito = False

        if digito == True:
            nota = int(entrada)
            if validar_nota(nota) == True:
                valido = True
        else:
            print("ERROR: Ingreso inválido. Intente nuevamente.")
    return nota
