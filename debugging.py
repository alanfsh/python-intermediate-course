def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input("Ingresa un número: "))
        if num <= 0:
            raise TypeError("Solo puedes ingresar números positivos")
            # Eleva el error y detiene el programa, el mensaje se asocia a te
        print(divisors(num))
        print("Fin de programa")
    except ValueError:
        print("Solo puedes ingresar números")
    except TypeError as te:
        # Toma el mensaje dado en raise si ese error ocurre --> te
        print(te)


if __name__ == '__main__':
    run()


# Run and Debug en VSCode --> Ademas se pueden poner breakpoints en alguna linea
# para detener alli el programa