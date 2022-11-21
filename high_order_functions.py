from functools import reduce
# Las funciones de orden superior son las que reciben como parametro a otra funcion, hay 3 importantes:
# Filter
my_list = [1, 3, 5, 7, 8, 10, 12, 15, 16]

odd = list(filter(lambda x: x % 2 == 0, my_list))
# Con filter eliminamos los elementos que NO CUMPLEN la condicion dada por la funcion

print(odd)

# Map
my_numbers = [1, 2, 3, 4, 5,]

squares = list(map(lambda x: x**2, my_numbers))
# Con map se aplica una operacion a todos los elementos de la lista, y la devuelve, MAP 
# no puede eliminar elementos, por lo que la lista resultante es del mismo tamaño que la original
print(squares)

# Reduce
new_list = [2, 2, 2, 2, 2]

reduced = reduce(lambda a, b: a * b, new_list)
# Reduce aplica la funcion dada a los elementos de la lista para reducirlos a un solo valor, 
# en este caso es asi: ((((2*2)*2)*2)*2), lo hace de izquierda a derecha.
print(reduced)