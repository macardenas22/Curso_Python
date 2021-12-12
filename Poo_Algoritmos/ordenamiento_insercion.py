import random

def sort_by_insertion(list):

    for index in range(1, len(list)):
        #creamos dos variable 1) que valor del indice y 2) el indice 
        # para este caso c_v = list[1] y c_p = 1
        current_value = list[index]
        current_position = index
        print(f'FOR: current_value = {current_value}\tcurrent_position = {current_position}')

        # Se generan las siguietnes validaciones and
        # 1) si la posición actual es mayor a 0 y 
        # 2) el valor de la lista[index-1] es mayor que el valor actual 
        # se hace un intercambio del valor del indice actual y actual -1
        while current_position > 0 and list[current_position - 1] > current_value:
            list[current_position] = list[current_position - 1]
            current_position -= 1
        #se realiza un swap donde el valor de indice posicion actual sera igual a valor actual 
        #y retornamos valor
        list[current_position] = current_value
    return list


if __name__ =="__main__":
    #solicitamos el tamaño de la lista por consola
    size_list = int(input('¿De qué tamaño será la lista?:') )
    #generamos con la función de randint números aleatorios de 0 a 100 hasta el rango establecido 
    #por el numero solicitado en consola (size_list) por medio de list comprenhensión e imprimimos la lista
    list =[random.randint(0,100) for i in range(size_list)]
    print (list)
    #almacenamos el ordenamiento por inserción en una variable sorted_list y la imprimimos 
    sorted_list = sort_by_insertion(list)
    print(sorted_list)
