"""
Este módulo contiene la clase Logica
"""
from threading import Lock
from random import choice


class Logica:
    """
    Funciona como "backend" del servidor.
    Posee métodos y atributos que describen y ejecutan el flujo de juego.
    """

    # Este lock evita que dos usuarios entren con el mismo nombre al mismo tiempo.
    log_in_lock = Lock()
    # Este lock evita que se produzcan errores cuando múltiples usuarios intentan iniciar partida.
    partida_lock = Lock()
    # Este lock administra el acceso a la lista de usuarios para evitar que se produzcan errores.
    lista_jugadores_lock = Lock()

    def __init__(self):
        # Comparte lista con Servidor (tienen la misma lista_jugadores)
        self.partida_en_progreso = False
        self.impostor = None
        self.lista_jugadores_partida = []

    def validar_username(self, username, lista_jugadores):
        """
        Recibe un nombre de usuario, y revisa si este ya está ocupado o no.
        """
        self.lista_jugadores_lock.acquire()
        # Revisar nombre jugadores conectados
        for jugador in lista_jugadores:
            if jugador.username == username:
                self.lista_jugadores_lock.release()
                return False
        self.lista_jugadores_lock.release()
        return True


    def inicializar_jugadores(self, lista_jugadores):
        for jugador in lista_jugadores:
            jugador.ya_voto = False
            jugador.votos_ronda = 0
            jugador.vivo = True

    def actualizar_lista_jugadores_partida(self, lista_jugadores):
        self.lista_jugadores_partida = []
        for j in lista_jugadores:
            self.lista_jugadores_partida.append([j.username, j.ya_voto, j.vivo])

    def votar_bots(self, lista_jugadores):
        """
        Ejecuta la votación de los bots de la partida
        El voto de los bots es al azar. Un bot puede votar por cualquier
        jugador vivo, incluyéndose a sí mismo.
        """
        for bot in lista_jugadores:
            # Si el jugador no es un bot o si el bot esta muerto
            if bot.socket_cliente is not None or not bot.vivo:
                continue
            opciones = []
            for jugador in lista_jugadores:
                if jugador.vivo:
                    opciones.append(jugador)
            jugador_a_votar = choice(opciones)
            jugador_a_votar.votos_ronda += 1
            bot.ya_voto = True

    def verificar_votos(self, lista_jugadores):
        """
        Revisa si todos los jugadores ya votaron.
        En caso que sí, revisa a aquel con más votos y lo expulsa.

        En caso de empate, se elimina uno de los empatados al azar, para
        agilizar el juego.

        Se retorna el jugador expulsado.
        En caso de que falte gente por votar, se retorna None.
        """
        # Revisar si falta gente por votar y revisar el más votado
        max_votos = 0
        for jugador in lista_jugadores:
            if jugador.votos_ronda > max_votos:
                max_votos = jugador.votos_ronda
            if jugador.vivo and not jugador.ya_voto:
                return None
        candidatos = []
        for jugador in lista_jugadores:
            if jugador.votos_ronda == max_votos:
                candidatos.append(jugador)
        # Expulsar jugador
        jugador_expulsado = choice(candidatos)
        jugador_expulsado.vivo = False
        # Reiniciar jugadores para siguiente ronda
        for jugador in lista_jugadores:
            jugador.votos_ronda = 0
            jugador.ya_voto = False
        return jugador_expulsado

    def votar_jugador(self, jugador_votante, username_votado, lista_jugadores, lista_respuestas):
        """
        Se recibe un objeto jugador, y el username por el cual este vota
        Luego de emitir el voto, se revisa si queda gente por votar.
        Si no queda gente por votar, se procede a eliminar al más votado.
        En caso de haber empate, se elige al azar entre los más votados.

        Si se expulsa al impostor, ganan los crewmantes directamente.
        Si quedan solo 2 jugadores (incluyendo el impostor), gana el impostor.
        Si se elimina al último jugador humano (no bot), gana el impostor.
        """
        if jugador_votante.ya_voto or not jugador_votante.vivo:
            return
        for j in lista_jugadores:
            if j.username == username_votado:
                j.votos_ronda += 1
                break
        jugador_votante.ya_voto = True
        # Intentar expulsar jugador:
        jugador_expulsado = self.verificar_votos(lista_jugadores)
        if jugador_expulsado is not None:
            respuesta = {
                "comando" : "jugador_expulsado",
                "jugador" : jugador_expulsado.username
            }
            tup = ("broadcast", respuesta)
            lista_respuestas.append(tup)
            # Revisar si el expulsado es impostor
            if jugador_expulsado == self.impostor:
                respuesta = {
                    "comando" : "fin_de_partida",
                    "resultado" : "ganan_crewmates"
                }
                tup = ("broadcast", respuesta)
                lista_respuestas.append(tup)
            else:
                # Revisar si quedan jugadores:
                crewmates_vivos = 0
                jugadores_humanos = 0
                for j in lista_jugadores:
                    if j.vivo:
                        crewmates_vivos += 1
                        if j.socket_cliente is not None:
                            jugadores_humanos += 1
                # Si quedan menos de 2 vivos (impostor + crewmate)
                if crewmates_vivos <= 2 or jugadores_humanos == 0:
                    respuesta = {
                        "comando" : "fin_de_partida",
                        "resultado" : "gana_impostor"
                    }
                    tup = ("broadcast", respuesta)
                    lista_respuestas.append(tup)
                else:
                    self.votar_bots(lista_jugadores)
        else:
            # Enviar respuesta de voto a cliente
            respuesta = {
                "comando" : "voto_correcto"
            }
            tup = ("individual", respuesta)
            lista_respuestas.append(tup)
        # Enviar mensaje de que ya votó a todos
        self.actualizar_lista_jugadores_partida(lista_jugadores)
        respuesta = {
            "comando" : "jugadores_partida",
            "lista_jugadores": self.lista_jugadores_partida
        }
        tup = ("broadcast", respuesta)
        lista_respuestas.append(tup)

    def comenzar_partida(self, lista_jugadores, lista_respuestas):
        self.partida_lock.acquire()
        # Revisa si la partida ya fue iniciada por otro participante
        if self.partida_en_progreso:
            return
        # Revisa si hay jugadores que aún no está listos
        for j in lista_jugadores:
            if j.username is None:
                self.partida_lock.release()
                return
        self.inicializar_jugadores(lista_jugadores)
        # Seleccionar impostor
        self.impostor = choice(lista_jugadores)
        self.partida_en_progreso = True
        # Informar jugadores
        if self.impostor.socket_cliente is not None:
            respuesta = {
                "comando" : "empezar",
                "tipo" : "impostor"
            }
            tup = ("impostor", respuesta)
            lista_respuestas.append(tup)
        respuesta = {
            "comando" : "empezar",
            "tipo" : "crewmate"
        }
        tup = ("crewmates", respuesta)
        lista_respuestas.append(tup)
        self.votar_bots(lista_jugadores)
        self.actualizar_lista_jugadores_partida(lista_jugadores)
        respuesta = {
            "comando" : "jugadores_partida",
            "lista_jugadores": self.lista_jugadores_partida
        }
        tup = ("broadcast", respuesta)
        lista_respuestas.append(tup)
        self.partida_lock.release()


    def manejar_mensaje(self, mensaje, jugador, lista_jugadores):
        """
        Maneja un mensaje recibido desde el cliente.
        """
        try:
            comando = mensaje["comando"]
        except KeyError:
            return []
        lista_respuestas = []
        if comando == "log_in":
            username = mensaje["username"]
            self.log_in_lock.acquire()
            if self.validar_username(username, lista_jugadores):
                jugador.username = username
                respuesta = {
                    "comando" : "log_in_accepted",
                    "username" : username
                }
            else:
                respuesta = {
                    "comando" : "log_in_rejected",
                    "feedback" : "El nombre de usuario ya está ocupado"
                }
            self.log_in_lock.release()
            tup = ("individual", respuesta)
            lista_respuestas.append(tup)

        elif comando == "send_chat_message":
            respuesta = {
                "comando" : "receive_chat_message",
                "text" : ">" + str(jugador.username) + ": " + mensaje["text"]
            }
            tup = ("broadcast", respuesta)
            lista_respuestas.append(tup)

        elif comando == "request_jugadores":
            self.lista_jugadores_lock.acquire()
            lista_usernames = [jugador.username for jugador in lista_jugadores]
            self.lista_jugadores_lock.release()
            respuesta = {
                "comando" : "actualizar_jugadores",
                "jugadores" : lista_usernames
            }
            tup = ("broadcast", respuesta)
            lista_respuestas.append(tup)

        elif comando == "comenzar_partida":
            self.comenzar_partida(lista_jugadores, lista_respuestas)

        elif comando == "votar_jugador":
            self.votar_jugador(jugador, mensaje["jugador"], lista_jugadores, lista_respuestas)
        return lista_respuestas
