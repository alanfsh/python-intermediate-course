def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
    # open("ruta/del/archivo.txt", "modo w, r o a", encoding es para que interprete los caracteres)
    # Modos: r --> READ, w --> WRITE(SOBREESCRIBE), a --> APPEND(AGREGAR A LO QUE EXISTE)
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names= ["Juan", "Pedro", "Pablo", "Carlos", "Rocío"]
    with open("./archivos/names.txt", "w", encoding="utf-8") as doc_names:
        for name in names:
            doc_names.write(name)    # .write() escribe algo dentro del archivo
            doc_names.write("\n")


def run():
    write()


if __name__ == "__main__":
    run()