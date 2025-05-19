def mostrar_estudiante (numero_estudiante:int, nombres: list, lista_generos: list, lista_legajos:list, matriz_notas:list):
    """
    Esta funcion muestra los datos del estudiante elegido 
    Args:
    int: numero de estudiante
    list: nombres, lista_generos, lista_legajo, matriz_notas
    returns:
    no retorna nada
    """
    print(f"Número de estudiante: {numero_estudiante + 1}\tNombre: {nombres[numero_estudiante]}\t\tGénero: {lista_generos[numero_estudiante]}\t\tLegajo: {lista_legajos[numero_estudiante]}")

    for j in range(5):
        print(f"\t\t\tNota {j + 1}: {matriz_notas[numero_estudiante][j]}")
    print("")
def mostrar_todos_los_estudiantes(nombres: list, lista_generos: list, lista_legajos: list, matriz_notas: list):
    """
    Muestra los datos de todos los estudiantes
    Args: 
    list: nombres, lista_generos, lista_legajos, matriz_notas: 
    returns:
    no retorna nada
    """
    
    for i in range(30):
        mostrar_estudiante(i,nombres, lista_generos,lista_legajos, matriz_notas)
        
def buscar_por_legajo (legajo_buscado:int, nombres: list, lista_generos: list, lista_legajos: list, matriz_notas: list):
    """
    Busca para mostrar los datos de un estudiante segun su legajo
    Args:
    list: nombres, lista_generos, lista_legajos, matriz_notas
    int: legajo_buscado
    Returns:
    no retorna nada
    """
    encontrado= False
    for i in range (30):
        if lista_legajos [i] == legajo_buscado:
            mostrar_estudiante(i, nombres, lista_generos, lista_legajos, matriz_notas)
            encontrado=True
            break
    if encontrado == False:
        print("Legajo invalido: ")