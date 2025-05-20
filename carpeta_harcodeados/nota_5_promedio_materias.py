def calcular_promedios_materias (matriz_notas:list, promedios_materias: list):
    for j in range (5):
        suma= 0
        for i in range (30):
            suma = suma + matriz_notas[i][j]
        promedio = suma / 30
        promedios_materias [j] = promedio
     
      #materia
def promedio_mayor  (promedios_materias: list, nombres_materias: list):
    
    mayor= promedios_materias [0]
    posicion= 0
    
    for i in range (1,5):
        if promedios_materias [i] > mayor:
            mayor = promedios_materias [i]
            posicion = i
    
    print(f"Materia con mayor promedio general: {nombres_materias[posicion]} | Promedio: {mayor}")

    
def promedio_maximo_materias (promedio_materias:list, nombres_materias: list):
    for i in range (4):
        for j in range ( i + 1,5):
           if promedio_materias[i] < promedio_materias[j]:
               
               aux= promedio_materias[i]
               promedio_materias[i]= promedio_materias[j]
               promedio_materias[j] = aux
               
               nombre_aux = nombres_materias[i]
               nombres_materias[i]= nombres_materias[j]
               nombres_materias[j] = nombre_aux
    for i in range (5):
        print (f"Materia: {nombres_materias[i]} | Promedio : {promedio_materias[i]}")
               
               
               