class Coordenada:
    #metodo constructor recibe por argumento un parametro de valor para x y y
    def __init__ (self,x,y):
        self.x = x #3  4
        self.y = y #30 8
    #metodo de instancia que recibe por argumento otra coordenada x y y
    def distancia(self,otra_coordenada):
        #x de init - x de otra coordenada de .x elevada a la dos 
        x_diff = (self.x - otra_coordenada.x)**2 #(3-4)^2 = 1
        #y de init - y de otra coordenada de .y elevada a la dos
        y_diff = (self.y - otra_coordenada.y)**2 #(30-8)^2 = 484
        #devuelve la raiz cuadrada de la suma de xdiff y ydiff
        return (x_diff + y_diff)**0.5 #sqr(485)

#entrypoint
if __name__ == "__main__":
    coord_1 = Coordenada(3,30)
    coord_2 = Coordenada(4,8)

    print(coord_1.distancia(coord_2)) #>>22.02
    #nos permite validar si objeto es instancia de la clase
    print(isinstance(coord_2,Coordenada)) 