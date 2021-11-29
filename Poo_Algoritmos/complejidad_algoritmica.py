#importamos el modulo time para medir el tiempo
#implementación iterativa y recursiva para comparar el comportamiento 
import time
import sys

#implementación iterativa por medio de un bucle
def factorial(n):
    response = 1

    while n > 1:
        response *= n
        n -=1
    
    return response


#implementación recursiva 
def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)



if __name__ == "__main__":
    n=2500
    sys.setrecursionlimit(n+10)
    start_time = time.time()
    factorial(n)
    finish_time = time.time()
    print(f'execution time with bucle was :{finish_time - start_time}')

    start_time = time.time()
    factorial_recursive(n)
    finish_time = time.time()
    print(f'execution time with recursive was :{finish_time - start_time}')