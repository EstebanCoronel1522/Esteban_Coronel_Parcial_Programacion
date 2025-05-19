nombres= [0] *30
generos= [0] *30
legajos= [0] *30
nombres_materias = ["Matemática", "AySO", "Ingles", "Geografia", "Programación"]
matriz_notas = []
for i in range(30):
    fila = [0] * 5
    matriz_notas += [fila]


def lower_propio(cadena:str)-> str:
    palabra_minusculas = ""
    caracter=""
    for i in range(len(cadena)):
        if ord(cadena[i]) >= 65 and ord(cadena[i]) <= 90:
            caracter = chr(ord(cadena[i]) + 32)   
        else:
            caracter = cadena[i]
        palabra_minusculas += caracter
    return palabra_minusculas


def cargar_datos():
    """
    Carga los datos de 30 estudiantes en listas paralelas y una matriz de 30x5.
    """
    for i in range(30):
        print("")
        print("Cargando datos del estudiante número", i + 1)
        
        nombre = nombre_estudiante()
        genero = genero_estudiante()
        legajo = legajo_estudiante()
        
        nombres[i] = nombre
        generos[i] = genero
        legajos[i] = legajo

        for j in range(5):
            print (f"Ingrese la nota del estudiante en {nombres_materias[j]}:")
            nota = nota_estudiante()
            matriz_notas[i][j] = nota

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
    sin_numeros=True
    while i < len(nombre):
        if nombre[i] != " ": 
            resultado= True 
        if (nombre[i] < "A" or (nombre[i] > "Z" and nombre[i] < "a") or nombre[i] > "z") and nombre[i] != " ":
            sin_numeros= False
        i=i + 1
    if sin_numeros == False:
        resultado= False
    
      
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
        bool: True si es un genero valido, false en su caso contrario
    """
    resultado= False
    if genero == "m" or genero == "f" or genero == "x":
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
        genero= lower_propio(genero)
        if validar_genero(genero): #Verifica que en la funcion validar_genero no se ingrese un dato distinto a "M" "F" "X", si es True, sale del while
            break
        print ("Error, Genero incorrecto, debe ser 'F'', 'M', O 'X'.")
    return genero


def validar_legajo (legajo:int)-> bool:
    """
    Solicita el ingreso de un legajo de 5 cifras númericas
    Args:
    int: recibe un dato numero entero (legajo)
    returns:
    bool: True si el legajo esta dentro del rango solicitado, False en caso contrario (excediendo o siendo menor)
    """
    Valido=False
    if legajo >=1 and legajo <= 99999:
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
        contador= 0
        for numero in legajo_numero:
            if numero <"0" or numero > "9":
                    digito=False #en caso de que el caracter ingresado no sea numerico, se vuelve falso
            contador =  contador + 1
        if digito == True and contador == 5:
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
                print("ERROR: La nota debe estar entre 1 y 10.") 
        else:
            print("ERROR: Ingreso inválido. Intente nuevamente.")
    return nota
    