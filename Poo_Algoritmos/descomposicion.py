class Lavadora:
    def __init__(self):
        pass #informamos que no viene ningun parametro para el cosntructor

    #creamos un default keyword de temperatura para fijar un parametro standar aunque este puede cambiar si se envia otro
    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_agua(temperatura) #ejecuta este metodo y toma el argumento temperatura 
        self._anadir_jabon() #ejecuta este metodo sin parametro
        self._lavar() #ejecuta este metodo sin parametro
        self._centrifugar() #ejecuta este metodo sin parametro

    def _llenar_tanque_agua(self,temperatura): # metodo con parametro o por defaultkw que imprime un mensaje 
        print(f'Llenando el tanque con agua {temperatura}') 

    def _anadir_jabon(self):  # metodo sin parametro o por defaultkw que imprime un mensaje 
        print('Añadiendo Jabón') 

    def _lavar(self):
        print('Lavando la Ropa')
    
    def _centrifugar(self):
        print('Centrifugando la ropa')


if __name__ == "__main__":
    lg = Lavadora() #creo un objeto instancia de la clase Lavadora 
    lg.lavar() #mensaje con default keyword 
    # >Llenando el tanque con agua caliente
    # >Añadiendo Jabón
    # >Lavando la Ropa
    # >Centrifugando la ropa

    mabe = Lavadora() #creo un 2do objeto instancia de la clase Lavadora 
    mabe.lavar('fria')# mensaje con parametro que descarta el default keyword "caliente"
    # >Llenando el tanque con agua fria
    # >Añadiendo Jabón
    # >Lavando la Ropa
    # >Centrifugando la ropa