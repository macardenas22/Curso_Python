
def read():
    numbers=[] #creamos una lista vacia 
    #generamos la ruta el acceso, de lectura y el encoding para no tener problemas de escritura 
    with open("./archivos/numbers.txt","r",encoding="utf-8") as f:
        for line in f: #recorremos nuestro archivo 
            numbers.append(int(line)) # cada elemento recorrido se almacena en la lista 
    print(numbers)

def overwrite():
    names = ["Mauricio","Juan","Carlos","David","Andrés"]
    with open("./archivos/names.txt","w",encoding="utf-8") as f:
        for name in names:
            f.write(name)#permite escribir el elemento en el archivo de texto
            f.write("\n")#permite escribir el salto de linea en el archivo de texto

def write():
    names = ["Juan","Gustavo","Camilo","Alejandro"]
    with open("./archivos/names.txt","a",encoding="utf-8") as f:
        for name in names:
            f.write(name)#permite escribir el elemento en el archivo de texto
            f.write("\n")#permite escribir el salto de linea en el archivo de texto

def run():
    read()
    overwrite()
    write()
    overwrite()

if __name__ == "__main__":
    run()