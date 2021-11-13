from datetime import datetime #traemos la libreria y función datatime para obtener información de tiempos para la funcion

#función decorator execution_time 
def execution_time(func):
    #colocamos nuestra nested con la opción de ser utilizada por varias funciones indiferente de sus parametros con *args y **kwargs
    def wrapper(*args,**kwargs):
        #creamos una variable que contenga el metodo datetime.now()para tomar el valor de la hora de ejecución
        initial_time = datetime.now() 
        #Generamos a la ejecución por parmetro su ejecución indiferente de sus parametros con *args y **kwargs
        func(*args,**kwargs)
        #creamos una variable que contenga el metodo datetime.now()para tomar el valor de la hora de fin de ejecución
        final_time=datetime.now()
        #creamos una variable para que nos de el valor final de la ejecución entre tiempo final e inicial 
        time_elapsed = final_time - initial_time
        #imprimimos la variable con el metodo .total_seconds()  para obtener solo los segundos más el mensaje 
        print('Pasaron '+str(time_elapsed.total_seconds())+'segundos en la ejecución de la función')
    return wrapper #retornamos el valor 

@execution_time #colocamos la referencia al decorador 
def random_func():
    #dado que no vamos a utilizar variable para proceso específico colocamos _ en el for, y pass
    for _ in range (1,1000000):
        pass

@execution_time #colocamos la referencia al decorador 
def suma(a:int, b:int) ->int: #como posee return colocamos -> tipo variable 
    #con los parametros recibidos genera la suma de estos dos argumentos
    return a+b

@execution_time #colocamos la referencia al decorador 
def saludo(nombre:str):#obtiene por parametro un str y genera el saludo
    print(f'hola {nombre}')

def run():#ejecutamos la opción principal 
    random_func()
    suma(5,3) #remitimos los argumentos 5 y 3
    saludo("mauro")#remitimos el argumento str mauro 

if __name__ == "__main__":
    run()