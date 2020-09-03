from collections import defaultdict

import estudiantes
import jugadores
import jugadores_estudiantes


def cargar_estudiantes(ruta_estudiantes):
    # Carga de datos desde archivo
    with open(ruta_estudiantes, "r", encoding="utf-8") as archivo_estudiantes:
        datos_estudiantes = archivo_estudiantes.readlines()[1:]

    # Los siguientes diccionarios relacionan
    # las casas y posiciones con sus respectivas clases
    clases_por_casa = {
        "Gryffindor": estudiantes.EstudianteGryffindor,
        "Slytherin": estudiantes.EstudianteSlytherin
    }
    clases_por_posicion = {
        "BuscadorGryffindor": jugadores_estudiantes.BuscadorGryffindor,
        "CazadorGryffindor": jugadores_estudiantes.CazadorGryffindor,
        "GolpeadorGryffindor": jugadores_estudiantes.GolpeadorGryffindor,
        "BuscadorSlytherin": jugadores_estudiantes.BuscadorSlytherin,
        "CazadorSlytherin": jugadores_estudiantes.CazadorSlytherin,
        "GolpeadorSlytherin": jugadores_estudiantes.GolpeadorSlytherin,
    }

    # Procesamiento de datos cargados
    espectadores = defaultdict(list)
    participantes = defaultdict(list)
    for estudiante in datos_estudiantes:
        # Separación del string
        estudiante = estudiante.strip().replace("\n", "")
        estudiante = estudiante.split(",")
        # Extracción de valores importantes
        casa = estudiante[2].title()
        posicion = estudiante[3].title()
        llave = f"{posicion}{casa}"
        # Creación de instancias
        if not posicion:
            instancia = clases_por_casa[llave](estudiante[0], estudiante[1])
            espectadores[llave].append(instancia)
        else:
            instancia = clases_por_posicion[llave](estudiante[0], estudiante[1], estudiante[4])
            participantes[llave].append(instancia)

    # Separación de participantes por casa
    participantes_por_casa = dict()
    participantes_por_casa["Gryffindor"] = [
        participantes["GolpeadorGryffindor"],
        participantes["CazadorGryffindor"],
        participantes["BuscadorGryffindor"],
    ]
    participantes_por_casa["Slytherin"] = [
        participantes["GolpeadorSlytherin"],
        participantes["CazadorSlytherin"],
        participantes["BuscadorSlytherin"],
    ]

    return espectadores, participantes_por_casa


def cargar_jugadores_externos(ruta_jugadores_externos):
    # Carga de datos desde archivo
    with open(ruta_jugadores_externos, "r", encoding="utf-8") as archivo_jugadores_externos:
        datos_jugadores_externos = archivo_jugadores_externos.readlines()[1:]

    # El siguientes diccionario relaciona
    # las posiciones con sus respectivas clases
    clases_por_posicion = {
        "Buscador": jugadores.Buscador,
        "Cazador": jugadores.Cazador,
        "Golpeador": jugadores.Golpeador,
    }

    # Procesamiento de datos cargados
    jugadores_externos = defaultdict(list)
    for jugador in datos_jugadores_externos:
        # Separación del string
        jugador = jugador.strip().replace("\n", "")
        jugador = jugador.split(",")
        # Extracción de valores importantes
        posicion = jugador[2].title()
        # Creación de instancias
        instancia = clases_por_posicion[posicion](jugador[0], jugador[1], jugador[3])
        jugadores_externos[posicion].append(instancia)

    # Formato compatible con estudiantes
    jugadores_profesionales = dict()
    jugadores_profesionales["Externos"] = [
        jugadores_externos["Golpeador"],
        jugadores_externos["Cazador"],
        jugadores_externos["Buscador"],
    ]

    return jugadores_profesionales


if __name__ == "__main__":
    # Carga los datos de los estudiantes (espectadores y participantes)
    cargar_estudiantes('estudiantes.csv')
    # Carga los datos de los jugadores externos (participantes)
    cargar_jugadores_externos('externos.csv')
