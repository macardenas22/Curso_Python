#importamos el modulo random
import random 

def bubble_sort(list):
    # obtendremos el largo de la lista con la función len()
    n = len(list)

    #recorremos la lista 
    for i in range(n): #0(n) (a)
        # el tamaño de la lista menos lo que ya recorremos menos 1 dado que tomamos es por indices y estos empiezan en 0
        for j in range(0, n - i - 1): #(a) * 0(n) = 0(n*n) = 0 (n**2)  es polinominial
            # se validará si el valor del indice list j es mayor que list j+1, si es así hara un swap (intercambio)
            #dándole el valor a list j el de list j+1 y a list j+1 el valor de list j 
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    #retornamos lista la cual fue la que gestionamos por indice.                
    return list
 
if __name__ =="__main__":
    #solicitamos el tamaño de la lista por consola
    size_list = int(input('¿De qué tamaño será la lista?:') )
    #generamos con la función de randint números aleatorios de 0 a 100 hasta el rango establecido 
    #por el numero solicitado en consola (size_list) por medio de list comprenhensión e imprimimos la lista
    list =[random.randint(0,100) for i in range(size_list)]
    print (list)

    #almacenamos el ordneamiento burbuja en una variable sorted_list y la imprimimos 
    sorted_list= bubble_sort(list)
    print(sorted_list)



