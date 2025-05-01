from huesped import huespedes

reservas = []

def tipo_habitacion():
    print("\nTipos de habitación:")
    print("1. Sencilla")
    print("2. Doble")
    print("3. Suite")
    opcion = input("Selecciona (1-3): ")

    if opcion == "1":
        return "Sencilla"
    elif opcion == "2":
        return "Doble"
    elif opcion == "3":
        return "Suite"
    else:
        print("Opción no válida. Se asignará 'Sencilla' por defecto.")
        return "Sencilla"

def pedir_fecha(tipo):
    try:
        dia = int(input(f"Día de {tipo} (1-31): "))
        mes = int(input(f"Mes de {tipo} (1-12): "))
        anio = int(input(f"Año de {tipo} (2025-2030): "))
        if dia < 1 or dia > 31 or mes < 1 or mes > 12 or anio < 2025 or anio > 2030:
            print("Fecha inválida.")
            return None
        return f"{dia:02d}/{mes:02d}/{anio}"
    except ValueError:
        print("Entrada no válida.")
        return None

def crear_reserva(cedula):
    huesped = None
    for h in huespedes:
        if h.cedula == cedula:
            huesped = h
            break

    if not huesped:
        print("Huésped no encontrado.")
        return

    print(f"\nReservando para: {huesped.nombre}")
    entrada = pedir_fecha("entrada")
    if not entrada:
        return
    salida = pedir_fecha("salida")
    if not salida:
        return

    tipo = tipo_habitacion()

    reserva = [cedula, huesped.nombre, entrada, salida, tipo]
    reservas.append(reserva)
    print("Reserva registrada correctamente.")

def mostrar_reservas():
    print("\n=== Reservas registradas ===")
    if not reservas:
        print("No hay reservas.")
        return
    for r in reservas:
        print(f"{r[1]} | Entrada: {r[2]} | Salida: {r[3]} | Habitación: {r[4]}")
