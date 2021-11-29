class Millas:
	def __init__(self, distancia = 0):
		self.distancia = distancia

	def convertir_a_kilometros(self):
		return (self.distancia * 1.609344)

# Creamos un nuevo objeto
avion = Millas()
avion.distancia = 200 # Indicamos la distancia cambiando el valor del atributo distancia del objeto
# Obtenemos el atributo distancia
print(avion.distancia) #>>200
# Obtenemos el método convertir_a_kilometros
print(avion.convertir_a_kilometros()) #>>>321.8688


