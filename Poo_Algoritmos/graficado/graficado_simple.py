#recordar que en el ambiente virtual debe estar instalado bokeh y el archivo en 
#la carpeta graficado

from bokeh.plotting import figure, output_file, show

if __name__ =="__main__":
    #damos nombre al output de la grafica 
    output_file('graficado_simple.html')
    #usamos la función de figure para realizar la figura
    fig = figure()  

    # por consola cuantos valores se querran graficar 
    total_values = int(input('¿Cuántos valores quieres graficar :?'))
    #con el numero ingresado se creará un grando anexado a una lista para los valores en X
    x_values = list(range(total_values))
    #creamos una lista para las variables en y 
    y_values = []

    for x in x_values:
        #recorremos los valores en x y solicitamos por consola el ingreso para
        #los valores en y en x; y adjuntamos a la lista 
        values = int(input(f'coloca valor en Y y para {x}...'))
        y_values.append(values)

    #usamos por la funcion figure() asociado en figura, colocamos como parametro
    #los valores en x, y, y el grosor de la linea
    fig.line(x_values,y_values, line_width=2)    
    #muestre el archivo en un archivo en html
    show(fig)
    
