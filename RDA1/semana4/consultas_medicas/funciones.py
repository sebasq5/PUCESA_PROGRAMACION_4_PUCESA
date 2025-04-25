# funciones.py

from paciente import Paciente
from paciente import Consulta  # Asegúrate de importar la clase Consulta

lista_pacientes = []

TIPOS_SANGRE = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

def elegir_tipo_sangre():
    print("Escoge tipo de sangre:")
    for i, tipo in enumerate(TIPOS_SANGRE):
        print(f"{i + 1}. {tipo}")
    while True:
        try:
            opcion = int(input("Número: "))
            if 1 <= opcion <= len(TIPOS_SANGRE):
                return TIPOS_SANGRE[opcion - 1]
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Entrada inválida, escribe un número.")

def pedir_cedula():
    """
    Esta función muestra las opciones de tipos de sangre y solicita al usuario que elija uno.
    Elige un tipo de sangre de una lista predefinida y lo devuelve como resultado.
    """
    while True:
        ced = input("Ingrese la cédula del paciente (10 números): ")

        # Verificamos que la cédula tenga exactamente 10 caracteres
        if len(ced) == 10:
            return ced  # Si tiene 10 caracteres, devolvemos la cédula
        else:
            print("La cédula debe tener exactamente 10 dígitos.")




def pedir_fecha():
    """
    Esta función solicita al usuario una fecha en formato año, mes, y día (con validaciones).
    Asegura que el año esté entre 2000 y 2025, el mes entre 1 y 12, y el día entre 1 y 31.
    Devuelve la fecha en formato 'YYYY-MM-DD'.
    """
    while True:
        try:
            anio = int(input("Ingrese el año: "))
            if not (2000 <= anio <= 2025):
                print("Año no valido, ingresa un año entre 2000 y 2025.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido para el año.")

    while True:
        try:
            mes = int(input("Ingrese el mes: "))
            if not (1 <= mes <= 12):
                print("Seleccion un mes valido (1-12).")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido para el mes.")

    while True:
        try:
            dia = int(input("Ingrese un dia: "))
            if not (1 <= dia <= 31):
                print("Día fuera de rango (1-31).")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido para el día.")

    return f"{anio:04d}-{mes:02d}-{dia:02d}"


def registrar_paciente():
    """
    Esta función solicita los datos de un nuevo paciente (nombre, cédula, edad, tipo de sangre) y los registra.
    Si la cédula ya existe, muestra un mensaje de error; si no, guarda al paciente en la lista de pacientes.
    """
    print("\nNuevo paciente")
    ced = pedir_cedula()

    if buscar_paciente_por_cedula(ced):
        
        print("Ya hay un paciente con esa cédula.")
        return

    nom = input("Nombre: ")
    edad = input("Edad: ")
    sangre = elegir_tipo_sangre()
    nuevo = Paciente(nom, ced, edad, sangre)
    lista_pacientes.append(nuevo)
    print("Paciente guardado correctamente.")

def buscar_paciente_por_cedula(ced):
    """
        Esta función busca un paciente en la lista por su cédula.
        Si encuentra el paciente, lo devuelve. Si no, devuelve None.
    """
    
    for p in lista_pacientes:
        if p.cedula == ced:
            return p
    return None

def registrar_consulta():
    """
    Esta función permite registrar una consulta médica para un paciente ya registrado.
    Solicita la cédula del paciente, la fecha de la consulta, el diagnóstico y el tratamiento.
    Si el paciente no está registrado, muestra un mensaje de error.
    """
    print("\nNueva consulta")
    ced = pedir_cedula()
    paciente = buscar_paciente_por_cedula(ced)
    if not paciente:
        print("No encontré a ese paciente.")
        return

    fecha = pedir_fecha()
    diag = input("Diagnóstico: ")
    trat = input("Tratamiento: ")

    try:
        consulta = Consulta(fecha, diag, trat)
        paciente.agregar_consulta(fecha, diag, trat)
        print("Consulta registrada correctamente.")
    except Exception as e:
        print(f"Error al guardar la consulta: {e}")

def mostrar_paciente():
    """
    Esta función muestra los datos completos de un paciente, incluyendo su historial de consultas.
    Solicita la cédula del paciente y si lo encuentra, muestra su información.
    Si no se encuentra, muestra un mensaje de error.
    """
    print("\nVer un paciente")
    ced = pedir_cedula()
    paciente = buscar_paciente_por_cedula(ced)
    if not paciente:
        print("No lo encontré.")
    else:
        paciente.mostrar_info()

def mostrar_todos_los_pacientes():
    """
    Esta función muestra todos los pacientes registrados.
    Si no hay pacientes registrados, muestra un mensaje de error.
    """
    print("\nTodos los pacientes")
    if not lista_pacientes:
        print("No hay pacientes registrados.")
    else:
        for p in lista_pacientes:
            print("-------------------")
            p.mostrar_info()
