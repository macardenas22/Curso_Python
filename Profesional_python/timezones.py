from datetime import datetime #importamos el modulo y clase datetime
import pytz #importamos el modulo pytz

#instanciamos en la variable con la función timezone y colocamos el parametro del timezone
my_city_timezone = pytz.timezone('America/Bogota')
#instanciamos en la variable el metodo datatime la hora que para este caso es bogotá 
my_city_time = datetime.now(my_city_timezone)
#imprimirá la ciudad, el datetime y el tipo de string del formato dia/mes/año, hora,minuto,seg.
print("Bogotá:", my_city_time.strftime("%d/%m/%Y, %H:%M:%S"))

#Repetimos lo mismo pero cambiando la timezone y el nombre de la ciudad en el print 
my_city_timezone = pytz.timezone('America/Mexico_City')
my_city_time = datetime.now(my_city_timezone)
print("Ciudad de México:", my_city_time.strftime("%d/%m/%Y, %H:%M:%S"))

#Repetimos lo mismo pero cambiando la timezone y el nombre de la ciudad en el print 
my_city_timezone = pytz.timezone('America/Caracas')
my_city_time = datetime.now(my_city_timezone)
print("Caracas:", my_city_time.strftime("%d/%m/%Y, %H:%M:%S"))