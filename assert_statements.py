def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input("Ingresa un número: ")
    assert num.isnumeric() and int(num) > 0, "Solo puedes ingresar números positivos"
    # assert condicion_a_cumplir, Mensaje_de_error, corta el programa si no se cumple la condicion y despliega el mensaje
    # son menos usados, pero si se llegan a encontrar
    print(divisors(int(num)))
    print("Fin de programa")


if __name__ == '__main__':
    run()