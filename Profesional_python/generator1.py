import time #para ver los elementos del generador 

#generamos función
def fibo_gen(numMax:int=None)->int:
    n1 = 0
    n2 = 1
    counter= 0
    
    while True:
        if counter  == 0:
            counter +=1
            yield n1 #pausa el proceso para valorar el siguiente condicional dado que este se cumplió 
        elif counter  == 1:
            counter +=1
            yield n2 #pausa el proceso para valorar el siguiente condicional dado que este se cumplió
        elif numMax == None:
            aux = n1 + n2 #creamos nueva variable para contener n1,n2
            #usamos un swap 
            n1, n2 = n2, aux #n1 ahora valdrá n2; n2 ahora valdrá aux
            counter +=1
            yield aux
        else: 
            aux = n1 + n2 #creamos nueva variable para contener n1,n2
            if aux <= numMax:
                #usamos un swap 
                n1, n2 = n2, aux #n1 ahora valdrá n2; n2 ahora valdrá aux
                counter +=1
                yield aux
            else: 
                raise StopIteration

if __name__ == "__main__":
    fibonacci = fibo_gen() #instanciamos la variable con la función

    for element in fibonacci:
        print(element)
        time.sleep(1)
 