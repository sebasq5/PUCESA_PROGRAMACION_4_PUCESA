from huesped import registrar_huesped, mostrar_huespedes, huespedes
from reserva import crear_reserva, mostrar_reservas, reservas
from utilidades import pedir_cedula

def mostrar_menu():
    print("\n Menu")
    print("1. Registrar huésped")
    print("2. Crear reserva")
    print("3. Mostrar reservas")
    print("4. Mostrar huéspedes")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_huesped()

        elif opcion == "2":
            cedula = pedir_cedula()
            crear_reserva(cedula)

        elif opcion == "3":
            mostrar_reservas()

        elif opcion == "4":
            mostrar_huespedes()

        elif opcion == "5":
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
