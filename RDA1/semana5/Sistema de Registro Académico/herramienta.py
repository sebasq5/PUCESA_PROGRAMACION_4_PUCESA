def pedir_matricula():
    while True:
        matricula = input("Ingrese la matrícula: ")
        if len(matricula) == 6:
            return matricula
        print("La matricula debe tener 6 caracteres.")
