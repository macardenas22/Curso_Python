#definiremos que el parametro string será de tipo String y retornará -> un bool false o true
def is_palindrome(string : str)-> bool:
    # reemplazará la cadena los vacios por nada y además convertira en minuscula 
    string = string.replace(" ","").lower()
    #generará validación de la cadena al derecho y al revés(uso del slide)
    return string == string[::1]



def run():
    #se imprime la ejecución de la función con un argumento dentro 
    print(is_palindrome(1000))


#Entry point del modulo 
if __name__ == "__main__":
    run()
