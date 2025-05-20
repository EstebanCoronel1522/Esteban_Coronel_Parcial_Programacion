"""cantidad_estudiantes= 30
cantidad_materias= 5
matriz_notas= [[0] * cantidad_materias for i in range (cantidad_estudiantes)]
nombres= [""] * cantidad_estudiantes
lista_generos= [""]* cantidad_estudiantes
lista_legajos= [""]* cantidad_estudiantes
lista_promedios= [0.0] * cantidad_estudiantes"""
from datos_harcodeados import *
from nota_1_validaciones import *
from nota_2_mostrar_datos import *
from nota_3_promedios_estudiantes import *
from nota_4_ordenamiento import *
from nota_5_promedio_materias import * 
lista_promedios = [0] * 30
promedios_materias = [0] * 5
datos_cargados=False
#datos_cargados=False
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Cargar datos Estudiantes")
    print("2. Mostrar estudiante/s")
    print("3. Calcular y mostrar promedios")
    print("4. Ordenar por promedio")
    print("5. Mostrar materia/s con mayor promedio")
    print("6. Buscar estudiante por legajo")
    print("7. Salir")

    opcion = input("Ingrese una opción (1-7): ")

    if opcion >= "1" and opcion <= "7":
        opcion = int(opcion)

        match opcion:
            case 1:
                #cargar_datos()
                
                datos_cargados= True
            case 2:
                if datos_cargados:
                    mostrar_todos_los_estudiantes(nombres, generos, legajos, matriz_notas)
                else:
                    print("ERROR: Primero debe cargar los datos (opción 1).")
            case 3:
                if datos_cargados:
                    calcular_promedios(matriz_notas, lista_promedios)
                    mostrar_todos_los_promedios(lista_promedios)
                    
                else:
                    print("ERROR: Primero debe cargar los datos (opción 1).")
            case 4:
                if datos_cargados:
                    calcular_promedios(matriz_notas, lista_promedios)
                    orden = input("Ingrese tipo de orden (Ascendente / Descendente): ")
                    orden = lower_propio(orden)
                    ordenar_datos_asc_desc(nombres, legajos, generos, matriz_notas, lista_promedios, orden)
                    mostrar_todos_los_estudiantes(nombres, generos, legajos, matriz_notas)
                    mostrar_todos_los_promedios(lista_promedios)
                else:
                    print("ERROR: Primero debe cargar los datos (opción 1).")
            case 5:
                if datos_cargados:
                    calcular_promedios_materias(matriz_notas, promedios_materias)
                    promedio_mayor(promedios_materias, nombres_materias )
                    promedio_maximo_materias(promedios_materias, nombres_materias )
                else:
                    print("ERROR: Primero debe cargar los datos (opción 1).")
            case 6:
                if datos_cargados:
                    legajo = legajo_estudiante()
                    buscar_por_legajo(legajo, nombres, generos, legajos, matriz_notas)
                else:
                    print("ERROR: Primero debe cargar los datos (opción 1).")
            case 7:
                print("Programa finalizado.")
                break
    else:
        print("Opción inválida. Intente nuevamente.")