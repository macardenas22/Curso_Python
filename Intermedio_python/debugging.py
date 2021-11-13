def divisors(num):
    divisors=[]
    try:
    
        if num  < 0 or num == 0 :#error generado a no ser detectado por el sistema se crea un valueError
            raise ValueError("El número a ingresar debe ser positivo o mayor a Cero 0...") 
        
        for i in range (1, num+1): 
            if num % i == 0:
                divisors.append(i)
        return divisors
    
    except ValueError as ve: #si se genera el error se evidencia en un print su contenido 
        print(ve)
        
def run():
    try:
        num = int(input("ingresa un numero..."))
        print(divisors(num))
        print("termino mi programa")
    except ValueError: #primer try para el teermino de error por tipo en vez de numero coloca una letra
        print("Debes ingresar un numero...")



if __name__ == "__main__":
    run()
