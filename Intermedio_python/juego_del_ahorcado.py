import os
import random



def show(palabra):
    amount_palabra =len(palabra)
    print("_ "* amount_palabra)    
    print("|".join(palabra))
    
    
    # print(f"\n {palabra} \n")
    # letter = input("Ingresa una letra:")

    # print (palabra.index('a'))
   
   
   
   
   
    # for p in enumerate(palabra):
    #     print (p)
    # try:
    #     if letter.isnumeric or len(letter)>1 or letter=="":
    #         raise ValueError("Recuerda que debes ingresar una letra")
        
    # except ValueError as ve:
    #     print(ve)


def words():
    data=[]
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        data=[line.strip() for line in f] 
        dict_datos = {key:value for key,value in enumerate(data)}
    return dict_datos


    



def run():
    os.system("clear")
    print("¡Adivina la Palabra! \n")
    words()


if __name__ == "__main__":
    run()


#se debe limpiar automaticamente la pantalla y mostrar 
# ¡Adivina la Palabra!    ok
# colocara cuantas underscore existan asociadas a la palabra: sol = _ _ _
#y un mensaje que diga "ingresa una letra:"

# Exception en el proceso de espacios letras o signos 
#si la letra existe llenara uno de los espacios: _o_ #si consigue la palabra generará una frase que diga ¡Ganaste!: la palabra es SOL
#las palabras son aleatoria; se incorporar comprenhension (list or dict), y manejo de archivos; utilizar archivo data.txt  y leerlo para obtener las palabras 
#funcion enumerate() y get de los diccionarios; sentencia os.system("cls")
#añadir sistema de puntos dibujar el ahoracado con codigo ascii y/o mejorar la interfaz
