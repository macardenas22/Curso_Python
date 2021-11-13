#Generar un iterador que guarde la sucesión fibonacci de forma completa hasta un numero maximo o sin un valor 
import time # permite generar funciones asociadas a tiempo en consola para ver un objeto 

#creamos clase representa los objetos de tipo iterador que vamos a instanciar

class FiboIter:
    def __init__(self,numMax:int = None): #generamos un constructor el cual podra recibir o no un parametro numerico
        self.numMax = numMax #recibirá este parametro 
    
    def __iter__(self): #Iniciador del proceso del iterable en __next__
        self.n1 = 0 #numero1 para la sucesión
        self.n2 = 1 #numero2 para la sucesión
        self.counter = 0 #contador del iterador 
        return self #retorna el objeto en simismo 

    def __next__(self):
            #validamos primero proceso 
            if self.counter == 0: #si contador es igual a cero retorna el valor de n1
                self.counter +=1
                return self.n1
            
            elif self.counter == 1: #si contador es igual a cero retorna el valor de n1
                self.counter +=1
                return self.n2 

            elif self.numMax == None: #si numMax no recibio parametro recorrar n veces bajo el valor del auxiliar
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux       #esto se puede resumir de la siguiente manera 
                self.n1 , self.n2 = self.n2 , self.aux
                self.counter +=1
                return self.aux
            
            else:
                #para el caso que numMax tiene un argumento en constructor 
                self.aux = self.n1 + self.n2 #sume los valores n1 y n2 y valide comprobación 
                if  self.aux <= self.numMax: #si numero aux es menor o igual a numMax ejecute y retorne 
                    # self.n1 = self.n2
                    # self.n2 = self.aux #esto se puede resumir de la siguiente manera por un swap
                    self.n1 , self.n2 = self.n2 , self.aux #swap 
                    self.counter +=1
                    return self.aux
                else: #genere elevación de error y detenga el proceso en caso que se cumpla el if 
                    raise StopIteration

if __name__ == "__main__":
    #instanciamos con un objeto la clase, el objeto denominado fibonacci
    fibonacci = FiboIter(600) #en este caso tiene parametro el objeto fibonacci si fuese vacio se cumple el ultimo elif
    #recorremos el proceso 
    for element in fibonacci: #recorremos fibonacci, imprimimos elementos de acuerdo a si hay o no parametro.
        print (element)
        time.sleep(1)
