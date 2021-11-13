
#constante DATA(porqué está en mayúscula y no se va a modificar)
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #creamos una dict para almacenar todos los nombre de: desarrolladores python, trabajodes platzi
    #para ello creamos un dict comprenhension donde guardará los nombres de cada elemento de Dict DATA segun condición
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]
    for worker in all_python_devs:
        print(worker)
    print("===========================")
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    for worker in all_platzi_workers:
        print(worker)
    print("===========================")
    # crea una lista de nombres con los adultos que sean mayor de 18 con High function filter y lambda
    adults = list(filter(lambda worker: worker["age"]>=18,DATA))
    #sobre escribimos la variable adults extraemos de la manera de solo los nombres 
    adults = list(map(lambda worker:worker["name"],adults))
    
    old_people= list(map(lambda worker:worker |{"old":worker["age"]>70},DATA))

    for worker in old_people:
        print(worker)    
    


if __name__ == "__main__":
    run()