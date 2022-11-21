def run():
    my_list = [1, 'Hello', 2.5,]
    my_dict = {"firstname": "Juan", "lastname": "Perez"}

    super_list = [
       {"firstname": "Juan", "lastname": "Perez"},
       {"firstname": "Pedro", "lastname": "Gomez"},
       {"firstname": "Hugo", "lastname": "Juarez"},
       {"firstname": "Roberto", "lastname": "Andrade"},
    ]

    super_dict = {
        "natural_numbers": [1, 2, 3, 4, 5],
        "float_numbers": [1.2, 3.5, 6.4, 5.6, 7.8],
        "integer_numbers": [-1, -2, 0, 3, 4,],
    }

    for key, value in super_dict.items():
        print(key, " - ", value)


if __name__ == '__main__':
    run()