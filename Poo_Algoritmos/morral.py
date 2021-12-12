
# función que recibe 4 parametros
def backpack (size_backpack,weight,values, n):
    
    # sino hay elementoos o se lleno el cupo retorna 0
    if n == 0 or size_backpack == 0:
        return 0

    #si el peso del elemento n es mayor que el tamaño morral retorna al siguiente elemento 
    if weight[n-1]> size_backpack:
        return backpack (size_backpack,weight,values, n-1) 
    #generar dos posibilidades 1 toma la sumatoria de valores y ejecuto el valor del morral restandole el peso 
    # y se revisa el siguiente elemento; genera una segunda opción que no escogio ningun valor y revisa el 
    #siguiente elemento 
    return max(values[n-1] + backpack(size_backpack - weight[n-1], weight,values, n-1),
                backpack (size_backpack,weight,values, n-1))





if __name__ == '__main__':
    values = [60,100,120]
    weight = [10,20,30]
    size_backpack = 30
    n = len(values)

    result = backpack (size_backpack,weight,values,n)
    print (result)

