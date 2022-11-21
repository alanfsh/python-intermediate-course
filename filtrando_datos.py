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
# Si la variable esta en MAYUSCULAS --> Entonces es una CONSTANTE

def run():
    # all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]     # Con comprehensions
    # all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]   # Con COMPREHENSION
    
    # Con FILTER Y MAP
    # adults = list(filter(lambda worker: worker["age"] >= 18, DATA))
    # adults_name = list(map(lambda worker: worker["name"], adults))
    # old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] >= 70}}, DATA))       # Python 3.5 to 3.8
    # old_people = list(map(lambda worker: {worker |"old": worker["age"] >= 60}}, DATA))          # En Python 3.9 o superior
    # A todos los diccionarios en DATA le sumamos una llave llamada old: True o False segun si es mayor
    # a 60 años, creamos una lista y lo sumamos

    # Con FILTER Y LAMBDA
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))

    # Con FILTER Y LAMBDA
    all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))

    # Con LIST COMPREHENSIONS
    adults = [worker["name"] for worker in DATA if worker["age"] >= 18]

    old_people = [worker["name"] for worker in DATA if worker["age"] >= 60]


    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()