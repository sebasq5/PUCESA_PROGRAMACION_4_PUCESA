from paciente import Paciente, Consulta 

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
    Solicita una cédula de 10 dígitos numéricos al usuario y la devuelve.
    """
    while True:
        ced = input("Ingrese la cédula del paciente (10 números): ")
        if len(ced) == 10 and all(c in "0123456789" for c in ced):
            return ced
        else:
            print("La cédula debe tener exactamente 10 dígitos numéricos.")

def pedir_edad():
    """
    Solicita una edad numérica válida entre 1 y 129.
    """
    while True:
        entrada = input("Edad: ")
        try:
            edad = int(entrada)
            if 0 < edad < 130:
                return edad
            else:
                print("Edad fuera de rango (1 a 129).")
        except ValueError:
            print("Entrada inválida. Escriba solo números.")

def pedir_fecha():
    """
    Solicita una fecha válida (año entre 2000 y 2025) sin usar datetime.
    Verifica que el día coincida con el mes y si el año es bisiesto.
    Devuelve una cadena en formato 'YYYY-MM-DD'.
    """
    def dias_del_mes(mes, anio):
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif mes in [4, 6, 9, 11]:
            return 30
        elif mes == 2:
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                return 29
            return 28
        return 0

    while True:
        try:
            anio = int(input("Ingrese el año: "))
            if anio < 2000 or anio > 2025:
                print("Año fuera de rango (2000 a 2025).")
                continue
            mes = int(input("Ingrese el mes: "))
            if mes < 1 or mes > 12:
                print("Mes inválido (1 a 12).")
                continue
            dia = int(input("Ingrese el día: "))
            max_dias = dias_del_mes(mes, anio)
            if dia < 1 or dia > max_dias:
                print(f"Día inválido para el mes seleccionado (1 a {max_dias}).")
                continue
            return f"{anio:04d}-{mes:02d}-{dia:02d}"
        except ValueError:
            print("Entrada inválida. Debe ingresar números enteros.")

def registrar_paciente():
    """
    Registra un nuevo paciente solicitando sus datos con validaciones.
    """
    print("\nNuevo paciente")
    ced = pedir_cedula()
    if buscar_paciente_por_cedula(ced):
        print("Ya hay un paciente con esa cédula.")
        return
    nom = input("Nombre: ")
    edad = pedir_edad()
    sangre = elegir_tipo_sangre()
    nuevo = Paciente(nom, ced, edad, sangre)
    lista_pacientes.append(nuevo)
    print("Paciente guardado correctamente.")

def buscar_paciente_por_cedula(ced):
    """
    Busca un paciente en la lista por su cédula.
    Devuelve el objeto paciente si lo encuentra, o None.
    """
    for p in lista_pacientes:
        if p.cedula == ced:
            return p
    return None

def registrar_consulta():
    """
    Registra una consulta médica para un paciente existente.
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
        paciente.agregar_consulta(fecha, diag, trat)
        print("Consulta registrada correctamente.")
    except Exception as e:
        print(f"Error al guardar la consulta: {e}")

def mostrar_paciente():
    """
    Muestra la información completa de un paciente según su cédula.
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
    Muestra todos los pacientes registrados con su información.
    """
    print("\nTodos los pacientes")
    if not lista_pacientes:
        print("No hay pacientes registrados.")
    else:
        for p in lista_pacientes:
            print("-------------------")
            p.mostrar_info()
