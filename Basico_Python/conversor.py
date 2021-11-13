pesos = input("¿Cuántos pesos colombianos tienes?:")
pesos = float(pesos)
valor_dolar=3875
dolares = pesos/valor_dolar
dolares =round(dolares,2)
dolares = str(dolares)
print("Tienes U$"+dolares+" dólares")

dolares = float(input("cuántos dolares tienes:"))
valor_pesos = 3875
pesos = str (round(dolares*valor_pesos,2))
print ("Tienes $"+pesos+" Pesos Colombianos")

#nuevo conversor con amplitud del menú

menu = """ 
== Bienvenido al conversor de monedas 💰 ==

1 - Pesos Colombiano
2 - Pesos Argentino 
3 - Pesos Mexicanos

Elige una opción: """

opcion = input(menu)
if opcion == '1':
    pesos = float(input("¿Cuántos pesos colombianos tienes?:"))
    valor_dolar=3875
    dolares = round (pesos/valor_dolar,2)
    dolares = str(dolares)
    print("Tienes U$"+dolares+" dólares")
elif opcion == '2':
    pesos = float(input("¿Cuántos pesos Argentinos tienes?:"))
    valor_dolar=65
    dolares = round (pesos/valor_dolar,2)
    dolares = str(dolares)
    print("Tienes U$"+dolares+" dólares")
elif opcion == '3':
    pesos = float(input("¿Cuántos pesos Mexicanos tienes?:"))
    valor_dolar=24
    dolares = round (pesos/valor_dolar,2)
    dolares = str(dolares)
    print("Tienes U$"+dolares+" dólares")
else:
    print("ingresa una opción correcta...")

