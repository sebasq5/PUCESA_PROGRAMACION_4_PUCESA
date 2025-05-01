from herramienta import pedir_matricula

class Estudiante:
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.notas = []  

    def agregar_nota(self, materia, nota):
        self.notas.append((materia, nota))

estudiantes = []

def seleccionar_carrera():
    print("\nSeleccione una carrera:")
    print("1. Ing de Sistemas")
    print("2. Economía")
    print("3. Medicina")
    print("4. Ing Civil")

    opcion = input("Opción (1-4): ")

    if opcion == "1":
        return "Ing de Sistemas"
    elif opcion == "2":
        return "Economía"
    elif opcion == "3":
        return "Medicina"
    elif opcion == "4":
        return "Ing Civil"
    else:
        print("Opción inválida. Se asignará 'Ing de Sistemas' por defecto.")
        return "Ing de Sistemas"

def materia_por_carrera(carrera):
    if carrera == "Ing de Sistemas":
        return "Programación"
    elif carrera == "Economía":
        return "Contabilidad"
    elif carrera == "Medicina":
        return "Química"
    elif carrera == "Ing Civil":
        return "Física"
    else:
        return "General"

def registrar_estudiante():
    print("\n=== Registro de Estudiante ===")
    nombre = input("Nombre completo: ")
    matricula = pedir_matricula()
    carrera = seleccionar_carrera()
    nuevo = Estudiante(nombre, matricula, carrera)
    estudiantes.append(nuevo)
    print("Estudiante registrado con éxito.")

def mostrar_todos():
    print("\n=== Estudiantes registrados ===")
    if not estudiantes:
        print("No hay estudiantes.")
        return
    for e in estudiantes:
        print(f"{e.nombre} | Matrícula: {e.matricula} | Carrera: {e.carrera}")

def buscar_estudiante(matricula):
    for e in estudiantes:
        if e.matricula == matricula:
            return e
    return None

def mostrar_estudiante(matricula):
    estudiante = buscar_estudiante(matricula)
    if not estudiante:
        print("Estudiante no encontrado.")
        return
    print(f"\nNombre: {estudiante.nombre}")
    print(f"Matrícula: {estudiante.matricula}")
    print(f"Carrera: {estudiante.carrera}")
    if not estudiante.notas:
        print("No tiene calificaciones registradas.")
    else:
        print("Notas:")
        for materia, nota in estudiante.notas:
            print(f"  {materia}: {nota}")
