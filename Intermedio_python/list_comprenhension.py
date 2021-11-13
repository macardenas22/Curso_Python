def run():
    # squares = [] #creamos una lista vacia
    # for i in range(1,101):
    #     #durante el recorrido se guardará el valor del cuadrado de cada numero a través de append
    #     if i % 3 != 0:
    #         squares.append(i**2)

    #creamos con un list comprenhensión
    
    #para el elemento i en un rango de 1 al 100 imprima su valor 1 al cuadrado si i no es multiplo de 3
    squares = [i**2 for i in range (1,101) if i % 3 !=0]
    print(squares)
    #para el elemento i en un rango de 1 al 100000 imprima su valor 1 si i es multiplo de 4,6 y 9
    multi= [i for i in range (1,100000) if i % 4 == 0 and i % 9 == 0 and i % 6 == 0]
    print(multi)


    


    


if __name__=="__main__":
    run()