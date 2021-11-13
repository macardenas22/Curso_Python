def es_primo(numero:int)->bool:
    contador:int = 0

    resultado_final: int = [i for i in range(2, numero+1) if numero % i == 0]
    contador = len(resultado_final)

    if contador == 1:
        return True
    else:
        return False     

def run():
    numero:int = int(input("Ingresa un número :"))

    if es_primo(numero):
        print("Número Primo")
    else:
        print("No es Primo")


if __name__ =='__main__':
    run ()