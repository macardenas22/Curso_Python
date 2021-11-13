
def run():
    nombre = input('Ingresa tu nombre: ')
    saludo = f'Hola {nombre} bienvenido y te cuento que el largo de esta cadena es de...'
    largo = str(len(saludo))

    print(saludo+largo)



if __name__ == '__main__':
    run()