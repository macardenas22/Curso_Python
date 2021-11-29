#función principal 
def funcion_decoradora(funcion):
	def wrapper(): #nest function - wrapper 
		print("Este es el último mensaje...")
		funcion() #ejecuta la función remitida por parametro 
		print("Este es el primer mensaje ;)")
	return wrapper #retorna la ejecución de la función 


#opción corta
@funcion_decoradora
def zumbido():
    print("Buzzzzzz")

def run():
    zumbido()


if __name__ == "__main__":
    run()


#opción larga
# def zumbido():
# 	print("Buzzzzzz")

# zumbido = funcion_decoradora(zumbido)
#zumbido()