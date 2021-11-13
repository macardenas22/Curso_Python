# def conversacion (mensaje):
#     print ('Hola')
#     print ('¿Cómo estás?')
#     print (mensaje) #hace ejecución del parametro
#     print ('Adios')

# opcion = int(input('Elige una Opción (1,2,3):'))

# if opcion == 1:
#     conversacion('Elegiste la opción 1')#se ejecuta la función y con el parametro se aplica el mensaje
# elif opcion == 2:
#     conversacion('Elegiste la opción 2')
# elif opcion == 3:
#     conversacion('Elegiste la opción 3')
# else:
#     print('Selecciona una opción correcta...')

#sumatoria con parametros y return
def suma (a,b):
    print ("se suman los numeros... ")
    resultado = a + b
    return resultado
sumatoria = suma(4,5)
print (sumatoria)

# conversor 
# def conversor (tipo_pesos,valor_dolar):
#     pesos = float(input("¿Cuantos pesos "+ tipo_pesos + "tienes?:"))
#     dolares = str(round(pesos / valor_dolar,2))
#     print("Tienes U$"+dolares+ "dolares")

# menu = """ 
# == Bienvenido al conversor de monedas 💰 ==

# 1 - Pesos Colombiano
# 2 - Pesos Argentino 
# 3 - Pesos Mexicanos

# Elige una opción: """

# opcion = int(input(menu))

# if opcion == 1:
#     conversor("Colombianos",3875)
# elif opcion == 2:
#     conversor("Argentinos",64)
# elif opcion == 3:
#     conversor("Mexicanos",24)
# else:
#     print("ingresa una opción correcta...")

