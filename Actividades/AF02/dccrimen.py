from estudiante import cargar_datos
from verificar import corregir_alumno, corregir_nota, inscripcion_valida


class GymPro(Exception): 
    #Completar
    pass

    def evitar_sospechas(self):
        # Completar
        pass
    

if __name__ == "__main__":
    datos = cargar_datos("alumnos.txt")
    nueva_base = dict()
    for alumno in datos.values():
        corregir_alumno(alumno)
        corregir_nota(alumno)
        nueva_base[alumno.n_alumno] = alumno
    for alumno in nueva_base.values():
        try:
            # Completar
            pass

        except:  # Recuerda especificar el tipo de excepción que vas a capturar
            # Completar
            pass
