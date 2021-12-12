import random

def sorting_by_mixture(list):
  
#fase 1 - Minimizamos el largo de las lista hasta que este sea 1
    #si la lista mayor a uno realizará, dividirá el largo de la lista y tomamos el cociente
    if len(list) > 1:
        #dividiremos el largo de la lista en dos 
        half = len(list)//2
        #ahora generaremos lista del valor medio de indice hacia la izquierda hasta 0 y
        # de la derecha hasta el final de largo en posición de la lista 
        left = list[:half]
        right = list[half:]

        print(left,'*'* 5, right)

        #generamos llamadas recursivas hacemos que las listas sean de longitud 1 elemento
        sorting_by_mixture(left)
        sorting_by_mixture(right)

#fase 2 - Permite generar el proceso de comparación mientras se pueda y recombinando las listas en una sola
        i = 0 #iterador para recorrer las dos sublistas 
        j = 0 #iterador para recorrer las dos sublistas 
        k = 0 #iterador para la lista principal 

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

        print(f'izquierda {left}, derecha {right}')
        print(list)
        print(' - ' * 50) 

    return list    


if __name__ == "__main__":
    #solicitamos el tamaño de la lista por consola
    size_list = int(input('¿De qué tamaño será la lista?:') )

    list = [random.randint(0,100) for i in range(size_list)]
    print(list)
    print('-' *20)

    sorted_list = sorting_by_mixture(list)
    print(sorted_list)
