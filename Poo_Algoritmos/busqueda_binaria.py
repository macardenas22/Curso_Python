import random #importamos el modulo random para ejecutar la generación de numeros aleatorios

#Busqueda deberá recibir 4 parametros: la lista generada, un punto inicial, longitud de la lista y el objetivo

def busqueda_binaria(list,start,finish,objective):
    
    print(f"buscando {objective} entre {list[start]} y {list[finish-1]}")

    if start > finish: #si el comienzo es más grande que el final 
        return False
    #dividimos la lista en dos, para ello sumamos valores de inicio y fin y divimos por enteros (sin decimales) // 
    half= (start+finish)//2 #Genera una división de entero es decir toma el valor del modulo
    
    if list[half] == objective: #valida si el valor del indice list[Half] es igual al objetivo 
        return True
    elif list[half] < objective: #De lo contrario valida si el valor del indice list[half] menor que objetivo genere: 
        #si es cierto valor de de inicio sera half + 1 hasta el final se mantiene 
        return busqueda_binaria (list, half+1, finish, objective) 
    else:
        #De lo contrario el valor del final inicio sera half-1 y el valor start se mantendrá en 0
        return busqueda_binaria(list, start,half-1, objective) #si es falso valor de 0 hasta half-1 
    



if __name__ =="__main__":
    #solicitamos el tamaño de la lista por consola
    size_list = int(input('¿De qué tamaño será la lista?:') )
    objective = int (input('¿Qué Numero quieres encontrar?:'))

    #generamos con la función de randint números aleatorios de 0 a 100 hasta el rango establecido 
    #por el numero solicitado en consola (size_list) por medio de list comprenhensión, además con sort
    #ordenamos nuestra lista 
    list = sorted([random.randint(0,100) for i in range(size_list)])

    encontrado = busqueda_binaria(list,0,len(list),objective) #ejecutamos la función para obtener false o true 
    valor = 3 // 2
    print(valor)
    print(len(list))
    print(list)
    #se genera al interior un condiconal simple de informar si está o no en lista 
    print(f"El elemento {objective} { 'está' if encontrado  else 'no está'} en la lista")
