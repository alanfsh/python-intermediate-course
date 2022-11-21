def run():
    # numbers_cube = {}
    # for i in range(1, 101):
    #     if i % 3 !=0
    #     numbers_cube[i] = i**3
    
    # numbers_cube = {i: i**3 for i in range(1,101) if i % 3 != 0}
    # Dict comprehensions, genera un diccionario llave: valor, en el rango dado por for siempre que se cumpla el if

    root_squares = {i: round(i**0.5, 2) for i in range(1, 1001)}

    print(root_squares)
        


if __name__ == '__main__':
    run()