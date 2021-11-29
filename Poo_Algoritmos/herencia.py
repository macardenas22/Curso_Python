class Rectangulo:
    def __init__(self,altura, base):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

#denominamos una herencia cuando colocamos como parametro de una clase el nombre de la Clase, por ejemplo, 
#cuadrado hereda de Rectangulo 
class Cuadrado(Rectangulo):
  
    def __init__(self, lado):
        #ahora para heredar colocaremos en nuestro constructor la palabra super() y la cantidad de variables 
        #que se heredan de la superclase, para este caso se asocian que los valores de lado reemplazaran a las variables 
        #base y altura pero su llegada es por argumento de lado todo esto para hallar el area de un cuadrado que 
        #es lado^2 por ello asociará dos veces el lado 
        super().__init__(lado,lado) 


if __name__=="__main__":
    #instanciamos la clase Rectangulo 
    rectangulo = Rectangulo(4,5)
    #ejecutamos el metodo area para esta instancia 
    print(rectangulo.area())
    #instanciamos la subclase cuadrado que hereda de rectangulo
    cuadrado = Cuadrado(lado=5)
    #ahora dado que cuadrado hereda de rectangulo el metodo instancia area podremos llamarlo 
    print(cuadrado.area())
