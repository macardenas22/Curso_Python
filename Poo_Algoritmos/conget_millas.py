class Millas:
    #Metodo Constructor
	def __init__(self,distancia=0):
		self._distancia = distancia

	#Metodo Instancia: como quiero utilizar una instancia privada del constructor coloco self
	def convertir_a_kilometros(self):
	 	return (self._distancia * 1.609344)

	@property
	def distancia(self):
		return self._distancia

	@distancia.setter
	def distancia(self,distancia):
	 	self._distancia = distancia


if __name__ == "__main__":
	avion = Millas(500)
	print(avion.distancia)
	print(avion.convertir_a_kilometros())
	avion.distancia = 200
	print(avion.distancia)
	print(avion.convertir_a_kilometros())
