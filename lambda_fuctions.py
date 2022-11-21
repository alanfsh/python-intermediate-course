# Son funciones que no se declaran, solo pueden tener una linea de codigo

palidrome = lambda string: string == string[::-1]
# Aqui se declara la funcion lambda, recibe un string y luego los comparamos
# y a la variable palindrome se asigna lo que devuelve, en este caso True
print(palidrome('somos')) 
# Se invoca la funcion

list = [1, 2, 3, 4, 5]

list_square = [i**2 for i in list]

print(list_square)