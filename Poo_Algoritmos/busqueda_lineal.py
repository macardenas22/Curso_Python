# esta funcion permite recibir por parametro dos valores  una lista y un valor de busqueda especifico, 
# con lo cual si se encuentra dicho valor en lista retornara un false o true si este valor objetivo se encuentra

import random #traemos el módulo random para generar numeros aleatorios 



def busqueda_lineal (list, objective):
    match = False

    for element in list: #Big 0(n)
        if element == objective:
            match = True
            break
    return match


if __name__ == "__main__":
    #solicitamos el tamaño de la lista por consola
    size_list = int(input('¿De qué tamaño será la lista?:') )
    objective = int (input('¿Qué Numero quieres encontrar?:'))

    #generamos con la función de randint números aleatorios de 0 a 100 hasta el rango establecido 
    #por el numero solicitado en consola (size_list) por medio de list comprenhensión
    list = [random.randint(0,100) for i in range(size_list)]

    encontrado = busqueda_lineal(list, objective) #ejecutamos la función para obtener false o true 
    print(list)
    #se genera al interior un condiconal simple de informar si está o no en lista 
    print(f"El elemento {objective} { 'está' if encontrado  else 'no está'} en la lista")