from estudiantes import registrar_estudiante, mostrar_todos, mostrar_estudiante
from calificacion import asignar_calificacion
from herramienta import pedir_matricula

def menu():
    while True:
        print("\nMenu")
        print("1. Registrar estudiante")
        print("2. Asignar calificación")
        print("3. Mostrar información de estudiante")
        print("4. Mostrar todos los estudiantes")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            matricula = pedir_matricula()
            asignar_calificacion(matricula)
        elif opcion == "3":
            matricula = pedir_matricula()
            mostrar_estudiante(matricula)
        elif opcion == "4":
            mostrar_todos()
        elif opcion == "5":
            print("Esta ccerrando el programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
