def pedir_cedula():
    while True:
        cedula = input("Ingrese la cédula (10 números): ")
        if len(cedula) == 10:
            return cedula
        print("La cédula debe tener exactamente 10 dígitos.")
