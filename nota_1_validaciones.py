def validar_nombres (nombre:str) -> bool:
    """ 
   Valida que el nombre ingresado no este vacio
    args:
        str:nombre ingresado
    Returns:
        bool: True si el nombre no esta vacio, si no, retorna False    
    """
    i=0
    resultado= False
    while i < len(nombre):
        if nombre[i] != " ": #Si se ingresa un caracter distinto al espacio, el resultado se vuelve verdadero
            resultado= True
        i=i + 1
    return resultado

def nombre_estudiante() -> str:
    """ 
   Solicita el ingreso de un nombre valido
    args:
        sin argumentos
    Returns:
        str: nombre ingresado
    """
    while True:
        nombre= input ("Ingrese el nombre del estudiante: ")
        if validar_nombres(nombre): #si el if de la funcion validar_nombres es true, sale del while
            break
        print ("Error, nombre invalido, reingrese un nombre correspondiente: ")
    return nombre


def validar_genero (genero:str) -> bool:
    """
    Valida que el ingreso del genero sean las opciones 'F' 'M' 'X'
    Args:
        str: genero ingresado
    returns:
        bool_ True si es un genero valido, false en su caso contrario
    """
    resultado= False
    if genero == "M" or genero == "F" or genero == "X":
        resultado= True
    return resultado

def genero_estudiante () -> str:
    """
    Solicita al usuario el ingreso de un genero valido
    Args:
    sin argumentos
    Returns:
    str: genero valido ingresado
    """
    while True:
        genero= input ("Ingrese el genero del estudiante (F, M, X): ")
        if validar_genero(genero): #Verifica que en la funcion validar_genero no se ingrese un dato distinto a "M" "F" "X", si es True, sale del while
            break
        print ("Error, Genero incorrecto, debe ser 'F'', 'M', O 'X'.")
    return genero


def validar_legajo (legajo:int)-> bool:
    """
    Solicita el ingreso de un legajo mayor a 1 menor a 9999
    Args:
    int: recibe un dato numero entero (legajo)
    returns:
    bool: True si el legajo esta dentro del rango solicitado, False en caso contrario (excediendo o siendo menor)
    """
    Valido=False
    if legajo >=1 and legajo <= 9999:
        Valido= True
    return Valido

def legajo_estudiante () -> bool:
    """
    Solicita al usuario el ingreso de un legajo numero valido, entre el rango solicitado
    args: 
    sin argumentos
    Returns:
    int: legajo numero ingresado
    """
    while True:
        legajo_numero= input("Ingrese el legajo_numero del estudiante: ")
    
        digito= True
        for numero in legajo_numero:
            if numero <"0" or numero > "9":
                    digito=False #en caso de que el caracter ingresado no sea numerico, se vuelve falso
        if digito == True: 
            legajo = int(legajo_numero)
            if validar_legajo(legajo):
                return legajo
        print("Legajo invalido, Debe ingresar un numero valido: ")
    

def validar_nota (nota:int)-> bool:
    """
    Valida que la nota ingresada sea un entero entre el 1 y el 10 inclusive
    
    Args:
    int: Nota numerica ingresada
    returns:
    bool: True si se ingresa la nota en el rango solicitado, False en caso de excederla 
    """
    nota_valida= False
    if nota >= 1 and nota <= 10:
        nota_valida= True
    return nota_valida

def nota_estudiante () -> int:
    """
    Solicita al usuario el ingreso de una nota valida, siendo esta numerica y en el rango solicitado (1 a 10)
    Args: si argumentos
    return:
    int: nota numerica ingresada (valida)
    """
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