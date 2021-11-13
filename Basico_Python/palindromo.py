
def palindromo(palabra):
    _palabra = palabra.replace(' ','')#elimina todo los espacio con replace
    _palabra = _palabra.lower()#pasamos todo a minuscula
    palabra_invertida = _palabra[::-1]
    if _palabra == palabra_invertida:
        return True
    else:
        return False 


def run():
    palabra = input("Escribe una palabra:")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
       print("Es Palindromo...")
    else:
       print('No es Palindromo...')


if __name__ == "__main__":
    run ()
