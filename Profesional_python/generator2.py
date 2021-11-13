import time #para ver los elementos del generador 

#generamos función
def fibo_gen(numMax:int)->int: #a través del argumento limitaremos el proceso de la iteración
    n1 = 0 #valor n1
    n2 = 1 #valor n2
    
    while True:
        if n1 <= numMax:
            yield n1 #ejecute el valor de n1
            n1, n2 = n2, n1+n2 #n1 ahora valdrá n2; n2 ahora valdrá n1+n2
        else:
            break#si se cumple la condición rompa el programa 

if __name__ == "__main__":
    fibonacci = fibo_gen(200) #instanciamos la variable con la función y enviando el parametro 200

    for element in fibonacci:
        print(element)
        time.sleep(0.5)
 