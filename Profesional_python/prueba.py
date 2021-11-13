#crear iterador (estructura + iter)
my_list = [1,2,3,4,5]
my_iter= iter(my_list)

#iteramos con el iterador y el iterable next 

while True:#generamos while ya que hasta que su valor sea True será infinito
    try:
        element = next(my_iter) #creamos el iterable a través de la variable element y la función next asociado a my_iter
        print(element) #imprimimos
    except StopIteration:
        break #cuando no existan más elementos finalice el proceso 


