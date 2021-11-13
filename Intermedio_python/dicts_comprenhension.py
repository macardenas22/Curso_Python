def run():
#forma básica    
#    my_dict = {}
#    for i in range(1,101):
#        if i%3 !=0:
#            my_dict[i]=i**3
   
#    print(my_dict)


   #Diccionarios key primeros 100 numeros naturales y sus valores sean elevados al cubo 
   my_dict = {i : i**3 for i in range (1,101) if i%3 !=0}
   print(my_dict)
   #key = mil primeros numeros naturales con sus raices cuadradas como valores
   my_dict2 = {i :round(i**(1/2),3)  for i in range (1,1001)}
   print(my_dict2)



if __name__=="__main__":
    run()