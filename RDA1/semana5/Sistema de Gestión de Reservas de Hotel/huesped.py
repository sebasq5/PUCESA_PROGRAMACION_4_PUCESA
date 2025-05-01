from utilidades import pedir_cedula

class Huesped:
    def __init__(self, nombre, cedula, correo):
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo

huespedes = []

def registrar_huesped():
    print("\n=== Registro de Huésped ===")
    nombre = input("Nombre completo: ")
    cedula = pedir_cedula()
    correo = input("Correo electrónico: ")
    nuevo = Huesped(nombre, cedula, correo)
    huespedes.append(nuevo)
    print("Huésped registrado con éxito.")

def mostrar_huespedes():
    print("\n=== Huéspedes registrados ===")
    if not huespedes:
        print("No hay huéspedes registrados.")
    for h in huespedes:
        print(f"{h.nombre} | Cédula: {h.cedula} | Correo: {h.correo}")
