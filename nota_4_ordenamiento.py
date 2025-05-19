from nota_1_validaciones import lower_propio
def ordenar_datos_asc_desc (nombres:list, lista_legajos: list, lista_generos: list, matriz_notas: list, lista_promedios: list, orden: str):
    for i in range(0,len(lista_promedios)- 1,1):
        for j in range (i + 1, len(lista_promedios),1):
                condicion= False
                if orden== "Ascendente":
                    if lista_promedios [i] > lista_promedios[j]:
                        condicion = True
                    elif lista_promedios[i] == lista_promedios[j]:
                        if nombres[i] > nombres[j]:
                            condicion= True
                if orden== "Descendente":
                    if lista_promedios [i] < lista_promedios[j]:
                        condicion = True
                    elif lista_promedios[i] == lista_promedios[j]:
                        if nombres[i] < nombres[j]:
                            condicion= True
                
                if condicion:       
                    aux= lista_promedios [i]
                    lista_promedios[i] = lista_promedios[j]
                    lista_promedios[j] = aux
                    
                    aux= nombres[i]
                    nombres[i]= nombres[j]
                    nombres[j] = aux
                    
                    aux = lista_generos [i]
                    lista_generos [i] = lista_generos[j]
                    lista_generos [j] = aux
                    
                    aux = lista_legajos [i]
                    lista_legajos[i]=lista_legajos[j]
                    lista_legajos[j]= aux
            