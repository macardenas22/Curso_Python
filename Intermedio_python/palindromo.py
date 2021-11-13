
def palindrome(string):
    try:
        if len(string) == 0: #si no se coloca nada - largo = 0 -  se eleve un nuevo error
            raise ValueError("No se puede ingresar una cadena vacía") #se eleva un nuevo error que tenga este mensaje
        return string == string[::-1]
    except ValueError as ve: #excepto que suceda un valueError de nombre 've' ejecute un mensaje y devuelva false, 
        print(ve)
        return False

def run():
    try:
        print(palindrome(""))
    except TypeError:
        print("Solo se pueden ingresar Strings")


if __name__ == "__main__":
    run()