class CasillaDeVotacion:
    
    #método constructor sin retorno
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None #no posee valor

    #uso de decorador @property para generar el get del atributo región
    @property
    def region(self):
        return self._region
    #uso decorador setter el cual contien el mismo nombre de atributo región
    @region.setter
    def region(self, region):
        #a través de un if recorre una lista con regiones y si esta se encuentra agregará el valor a región 
        #de lo contrario levantará un Value Error por qeu no existe 
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self._pais}')


if __name__ == "__main__":
    #creas una nueva instancia de CasillaDeVotación 
    casilla = CasillaDeVotacion(12345,['Ciudad de México', 'Bogotá', 'Medellín'])
    casilla.region = "Bogotá"
    print(casilla.region)


