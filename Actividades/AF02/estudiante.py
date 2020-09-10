# NO MODIFICAR ESTE ARCHIVO


class Estudiante:
    def __init__(self, nombre, numero, generacion, carrera, nota):
        self.nombre = nombre
        self.n_alumno = numero
        self.generacion = generacion
        self.carrera = carrera
        self.promedio = self.colocar_nota(nota)

    def colocar_nota(self, nota):
        try:
            return int(nota)
        except ValueError as error:
            try:
                return float(nota)
            except ValueError as error:
                return str(nota)


# cargar datos

def cargar_datos(archivo):
    with open(archivo, "rt", encoding="utf-8") as archivo:
        texto = archivo.readlines()
    base_de_datos = dict()
    for estudiante in texto:
        atributos = estudiante.split(";")
        alumno = Estudiante(*atributos)
        alumno.generacion = int(alumno.generacion)
        base_de_datos[alumno.n_alumno] = alumno
    return base_de_datos


def cargar_datos_corto(archivo):
    with open(archivo, "rt", encoding="utf-8") as archivo:
        texto = archivo.readlines()
    base_de_datos = dict()
    for estudiante in texto[:6]:
        atributos = estudiante.split(";")
        alumno = Estudiante(*atributos)
        alumno.generacion = int(alumno.generacion)
        base_de_datos[alumno.n_alumno] = alumno
    return base_de_datos
