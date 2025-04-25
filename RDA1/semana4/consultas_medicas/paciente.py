class Consulta:
    def __init__(self, fecha, diagnostico, tratamiento):
        # Constructor que inicializa los detalles de la consulta
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento

    def mostrar_detalle(self):
        # Método para mostrar los detalles de la consulta
        print(f"  Fecha: {self.fecha} | Diagnóstico: {self.diagnostico} | Tratamiento: {self.tratamiento}")

class Paciente:
    def __init__(self, nombre, cedula, edad, tipo_sangre):
        # Muestra la información básica del paciente
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tipo_sangre = tipo_sangre
        self.consultas = []

    def agregar_consulta(self, fecha, diagnostico, tratamiento):
        # Método para agregar una consulta al historial del paciente
        consulta = Consulta(fecha, diagnostico, tratamiento)
        self.consultas.append(consulta)

    def mostrar_info(self):
        # mostrar informacion del paciente
        print(f"\nNombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de sangre: {self.tipo_sangre}")
        print("Historial de Consultas:")
        if self.consultas:
            for consulta in self.consultas:
                consulta.mostrar_detalle()
        else:
            print("  No tiene consultas registradas.")
