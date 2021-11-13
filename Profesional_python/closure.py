#Explicación Base y ejemplo ejecutable solo deben quitarse los comentarios propios del codigo

# def main():
#     a = 1 
#     def nested():
#         print(a)
#     return nested #retorna un valor a main 

# my_func = main() #la variable almacena el valor de main
# del(main) #del permite borrar variables o funciones y aca borramos main
# #dado que guarde una función main al ejecutar el my_fun ahora como una función trae el uno aunque se borro main 
# my_func() 

#========================================================================================================================

def make_multipler(x): #función global que recibe primer parametro y sera parte de variable de función closure
    
    def multipler(n): #función nested que tomará el parametro x  y multiplicará por parametro ejecutado con closure
        return x * n
    return multipler


time10 = make_multipler(10) #creamos una variable para la nest function enviado el parametro global por 10
time4 = make_multipler(4) #creamos una variable para la nest function enviado el parametro global por 10

print(time10(3))#Se ejecuta la nest func que tiene el valor de 10 y ahora ejecuta multipler con valor de 3
print(time10(5))#Se ejecuta la nest func que tiene el valor de 10 y ahora ejecuta multipler con valor de 3
print(time4(5))#Se ejecuta la nest func que tiene el valor de 4 y ahora ejecuta multipler con valor de 5

#podemos ejecutar las dos variables nest function 
print(time10(time4(2))) #se ejecuta el valor de time4 que será el valor de n para time10 con el valor time4

#=========================================================================================================================
