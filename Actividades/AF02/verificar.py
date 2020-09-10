from estudiante import cargar_datos, cargar_datos_corto


def verificar_numero_alumno(alumno):  # Levanta la excepción correspondiente
    pass


def corregir_alumno(estudiante): # Captura la excepción anterior
    pass


# ************

def verificar_inscripcion_alumno(n_alumno, base_de_datos): # Levanta la excepción correspondiente
    pass


def inscripcion_valida(estudiante, base_de_datos):  # Captura la excepción anterior
    pass


# ************

def verificar_nota(nota):  # Levanta la excepción correspondiente
    pass


def corregir_nota(estudiante):  # Captura la excepción anterior
    pass


if __name__ == "__main__":
    datos = cargar_datos_corto("alumnos.txt")  # Se cargan los datos
    for alumno in datos.values():
        if alumno.carrera != "Profesor":
            corregir_alumno(alumno)
            inscripcion_valida(alumno, datos)
            corregir_nota(alumno)
