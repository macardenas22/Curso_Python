#Generar un iterador que guarde la sucesión fibonacci de forma completa

import time #

#creamos clase representa los objetos de tipo iterador que vamos a instanciar

class FiboIter:
    #como no se requiere inicializar ningun atributo no requerimo colocar __init__
    
    def __iter__(self):
        self.n1 = 0 #numero para la sucesión
        self.n2 = 1 #numero para la sucesión
        self.counter = 0 #contador del iterador 
        return self #retorna el objeto en simismo 

    def __next__(self):
        if self.counter == 0:
            self.counter +=1
            return self.n1
        elif self.counter == 1:
            self.counter +=1
            return self.n2 
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux       #esto se puede resumir de la siguiente manera 
            self.n1 , self.n2 = self.n2 , self.aux
            self.counter +=1
            return self.aux

if __name__ == "__main__":
    #instanciamos con un objeto la clase, el objeto denominado fibonacci
    fibonacci = FiboIter()
    #recorremos el proceso 
    for element in fibonacci:
        print (element)
        time.sleep(1)
