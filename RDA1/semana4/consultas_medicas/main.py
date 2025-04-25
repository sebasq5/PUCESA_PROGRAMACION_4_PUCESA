# main.py

from funciones import (
    registrar_paciente,
    registrar_consulta,
    mostrar_paciente,
    mostrar_todos_los_pacientes
)

def mostrar_menu():
    print("\n===== MENÚ =====")
    print("1. Registrar paciente")
    print("2. Registrar consulta")
    print("3. Ver un paciente")
    print("4. Ver todos los pacientes")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        op = input("Selecciona una opcion: ")
        if op == "1":
            registrar_paciente()
        elif op == "2":
            registrar_consulta()
        elif op == "3":
            mostrar_paciente()
        elif op == "4":
            mostrar_todos_los_pacientes()
        elif op == "5":
            print("Finalizando el programa.")
            break
        else:
            print("Esa opción no vale")

if __name__ == "__main__":
    main()
