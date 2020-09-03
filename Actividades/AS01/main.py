import parametros
from cargar_datos import cargar_estudiantes, cargar_jugadores_externos
from competencia import Competencia


if __name__ == "__main__":

    # Cargamos e instanciamos Estudiantes y Jugadores
    ESPECTADORES, PARTICIPANTES = cargar_estudiantes("estudiantes.csv")
    JUGADORES_EXTERNOS = cargar_jugadores_externos("externos.csv")
    # Unimos los jugadores externos a los participantes
    PARTICIPANTES["Externos"] = JUGADORES_EXTERNOS["Externos"]

    # Se instancia la clase que simulará la competencia entre jugadores
    competencia = Competencia()

    aplausos_slytherin = 0
    abucheos_slytherin = 0
    aplausos_gryffindor = 0
    abucheos_gryffindor = 0
    # Aplausos y abucheos Slytherin
    for estudiante in ESPECTADORES['Slytherin']:
        if estudiante.aplaudir():
            aplausos_slytherin += 1
        if estudiante.abuchear():
            abucheos_slytherin += 1

    # Aplausos y abucheos Gryffindor
    for estudiante in ESPECTADORES['Gryffindor']:
        if estudiante.aplaudir():
            aplausos_gryffindor += 1
        if estudiante.abuchear():
            abucheos_gryffindor += 1

    print("\n")

    # Reasignamos cualidades de Slytherin
    for i in range(len(PARTICIPANTES['Slytherin'])):
        for jugador in PARTICIPANTES['Slytherin'][i]:
            if (aplausos_slytherin - abucheos_gryffindor) != 0:
                jugador.nerviosismo /= (aplausos_slytherin - abucheos_gryffindor)
            jugador.ambicion += aplausos_slytherin

    # Reasignamos cualidades de Gryffindor
    for i in range(len(PARTICIPANTES['Gryffindor'])):
        for jugador in PARTICIPANTES['Gryffindor'][i]:
            if (aplausos_gryffindor - abucheos_slytherin) != 0:
                jugador.nerviosismo /= (aplausos_gryffindor - abucheos_slytherin)
            jugador.valor += aplausos_gryffindor

    # Enfrentamiento entre cazadores
    golpeadores = []
    for jugador in PARTICIPANTES['Slytherin'][0]:
        golpeadores.append(jugador)
    for jugador in PARTICIPANTES['Gryffindor'][0]:
        golpeadores.append(jugador)
    for jugador in PARTICIPANTES['Externos'][0]:
        golpeadores.append(jugador)

    competencia.enfrentamiento_golpeadores(golpeadores, parametros.VACANTES_GOLPEADORES)

    # Enfrentamiento entre cazadores
    cazadores = []
    for jugador in PARTICIPANTES['Slytherin'][1]:
        cazadores.append(jugador)
    for jugador in PARTICIPANTES['Gryffindor'][1]:
        cazadores.append(jugador)
    for jugador in PARTICIPANTES['Externos'][1]:
        cazadores.append(jugador)

    competencia.enfrentamiento_cazadores(cazadores, parametros.VACANTES_CAZADORES)

    # Enfrentamiento entre buscadores
    buscadores = []
    for jugador in PARTICIPANTES['Slytherin'][2]:
        buscadores.append(jugador)
    for jugador in PARTICIPANTES['Gryffindor'][2]:
        buscadores.append(jugador)
    for jugador in PARTICIPANTES['Externos'][2]:
        buscadores.append(jugador)

    competencia.enfrentamiento_buscadores(buscadores, parametros.VACANTES_BUSCADORES)
