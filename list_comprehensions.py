def run():
    # list_square = []
    # for number in range(1, 101):
    #     if number % 3 != 0:
    #         list_square.append(number**2)
    #     else:
    #         continue

    # print(list_square)
    # list_square = [i**2 for i in range(1, 101) if i % 3 != 0]
    # print(list_square)

    multiples_list = [i for i in range(1, 99999) if i % 4 == 0 and i % 6 == 0 and i % 9 ==0]
    # Generamos una lista que agrega todas las i dentro de un rango dado por for siempre que cumpla las condiciones del if
    print(multiples_list)

if __name__ == '__main__':
    run()