def run():
    my_list=[1,"Hello",True,4.5]
    my_dict={"firstname":"Mauricio", "lastname": "Cárdenas"}
    super_list= [
        #creamos lista de diccionarios delimitados por {} y seguidos de , 
        {"firstname":"Mauricio", "lastname": "Cárdenas"},
        {"firstname":"Carolina", "lastname": "Benavides"},
        {"firstname":"Ricardo", "lastname": "Jiménez"},
        {"firstname":"Mauricio", "lastname": "Araoz"},
        {"firstname":"Robert", "lastname": "Posada"},
    ]

    super_dict={
        #creamos diccionarios que incluyen listas
        "naturals_nums" : [1,2,3,4,5],
        "integers_nums" : [-1,-2,0,1,2],
        "floating_nums" : [1.1,4.5,6.43],
    }

    for key, value in super_dict.items():
        print(f'{key} - {value}')

    for list in super_list:
        print(f'{list}')

if __name__ == '__main__':
    run()