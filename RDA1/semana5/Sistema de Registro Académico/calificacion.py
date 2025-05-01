from estudiantes import buscar_estudiante, materia_por_carrera

def asignar_calificacion(matricula):
    estudiante = buscar_estudiante(matricula)
    if not estudiante:
        print("Estudiante no encontrado.")
        return

    materia = materia_por_carrera(estudiante.carrera)
    try:
        nota = float(input(f"Ingrese nota de {materia}: "))
        if nota < 0 or nota > 50:
            print("Ingrese una nota entre 0 a 100.")
            return
        estudiante.agregar_nota(materia, nota)
        print("Calificación registrada.")
    except ValueError:
        print("Nota inválida.")
