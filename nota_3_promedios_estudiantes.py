def calcular_promedios (matriz_notas: list, lista_promedios: list):
    """
    Esta funcion recibe las notas de los 30 estudiantes en las 5 materias, devolviendo su promedio
    Args: 
    list: matriz_notas, lista_promedios
    returns:
    no retorna nada
    """
    for i in range (30):
        suma=0 
        for j in range(5):
            suma= suma + matriz_notas[i][j]
        promedio= suma / 5
        lista_promedios [i] = promedio

def mostrar_promedios(numero_estudiante:int, lista_promedios:list):
    """
    Esta funcion permite mostrar el promedio del estudiante en pantalla
    args:
    list: numero_estudiante, lista_promedios
    returns: no retorna nada
    """
    print(f"Estudiante {numero_estudiante + 1} - Promedio: {lista_promedios[numero_estudiante]}\n")

def mostrar_todos_los_promedios(lista_promedios:list):
    """
    Esta funcion recorre los 30 estudiantes motrandote sus promedios en pantalla
    Args: 
    list: lista_promedios
    returns:
    no retorna nada
    """
    for i in range (30):
        print (f"Estudiante {i + 1} - Promedio: {lista_promedios[i]}\t ")