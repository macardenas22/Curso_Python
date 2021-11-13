
# def decorador(func): #decorador: función que recibe por parametro una función en este caso saludo() 
#     def envoltura(): #Envoltura que genera un nested function y ejecuta el parametro de la función recibida
#         print('Esto se añade a mi función original') #stment que ejecuta con print
#         func() #statement que ejecuta la función saludo recibida 
#     return envoltura #returna ejecución del closure

# def saludo(): #creación de la función que viajara como parametro y su statement 
#     print('¡Hola!')

# saludo = decorador(saludo)#conversión del la variable a función con estructura del closure de la función decorador 
# saludo() #ejecución de la función del closure con la nest function envoltura. 

# Podemos modificar la ejecución teniendo en cuenta la acción del @ sobre la función parametro para sociarla al decorador 
# @decorador
# def saludo():
#     print('¡Hola!')

# saludo = decorador(saludo)
#saludo()
#========================================================================================================================

def mayusculas(func)->str:#decorador: función que recibe por parametro una función en este caso sera mensaje() 
    def envoltura(texto:str)->str: #envoltura ahora deberá recibir para la ejecución cuando sea closure un parametro string
        return func(texto).upper()#dado que la función mensaje su estructura es (mensaje(nombre) asociamos el proceso
    return envoltura

@mayusculas
def mensaje(nombre:str)->str:
    return f'{nombre},recibiste un mensaje'

# mensaje = mayusculas(mensaje)
print(mensaje('Andrés'))