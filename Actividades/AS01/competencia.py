class Competencia:

    def __init__(self):
        self.jugadores = {}
        self.no_seleccionados = {}

    def enfrentamiento_buscadores(self, buscadores, vacantes):

        # Lista de jugadores seleccionados
        seleccionados = []

        # Los postulantes con mejor puntajes llenan las vacantes, quedan seleccionados
        for i in range(vacantes):
            entra = None
            mejor_habilidad = 0
            for buscador in buscadores:
                if buscador.competir() > mejor_habilidad:
                    entra = buscador
                    mejor_habilidad = buscador.competir()
            buscadores.remove(entra)
            seleccionados.append(entra)

        # Se almacenan los jugadores seleccionados y los no seleccionados en el equipo
        self.jugadores['buscadores'] = seleccionados
        self.no_seleccionados['buscadores'] = buscadores

        # Se felicita a les seleccionados
        print("¡Felicitamos a le/les buscadores seleccionados!")
        for jugador in self.jugadores['buscadores']:
            print("Felicidades jugador numero "+str(jugador.numero_polera))
            jugador.celebrar()
            print("\n")

    def enfrentamiento_golpeadores(self, golpeadores, vacantes):
        # Lista de jugadores seleccionados
        seleccionados = []

        # Los postulantes con mejor puntajes llenan las vacantes, quedan seleccionados
        for i in range(vacantes):
            entra = None
            mejor_habilidad = 0
            for golpeador in golpeadores:
                if golpeador.competir() > mejor_habilidad:
                    entra = golpeador
                    mejor_habilidad = golpeador.competir()
            golpeadores.remove(entra)
            seleccionados.append(entra)

        # Se almacenan los jugadores seleccionados y los no seleccionados en el equipo
        self.jugadores['golpeadores'] = seleccionados
        self.no_seleccionados['golpeadores'] = golpeadores

        # Se felicita a les seleccionados
        print("¡Felicitamos a le/les golpeadores seleccionados!")
        for jugador in self.jugadores['golpeadores']:
            print("Felicidades jugador numero "+str(jugador.numero_polera))
            jugador.celebrar()
            print("\n")

    def enfrentamiento_cazadores(self, cazadores, vacantes):
        # Lista de jugadores seleccionados
        seleccionados = []

        # Los postulantes con mejor puntajes llenan las vacantes, quedan seleccionados
        for i in range(vacantes):
            entra = None
            mejor_habilidad = 0
            for cazador in cazadores:
                if cazador.competir() > mejor_habilidad:
                    entra = cazador
                    mejor_habilidad = cazador.competir()
            cazadores.remove(entra)
            seleccionados.append(entra)

        # Se almacenan los jugadores seleccionados y los no seleccionados en el equipo
        self.jugadores['cazadores'] = seleccionados
        self.no_seleccionados['cazadores'] = cazadores

        # Se felicita a les seleccionados
        print("¡Felicitamos a le/les cazadores seleccionados!")
        for jugador in self.jugadores['cazadores']:
            print("Felicidades jugador numero "+str(jugador.numero_polera))
            jugador.celebrar()
            print("\n")
