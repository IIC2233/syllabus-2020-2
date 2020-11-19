"""
Este módulo contiene la clase Jugador y funciones para su creación
"""
from threading import Lock
from random import shuffle

N_JUGADORES = 8

class Jugador:
    """
    Representa a un jugador, que puede ser humano o bot.
    Todos los jugadores parten como bots, y se asignan a humanos a medida
    que se establezcan conexiones.

    Atributos:
        id_jugador: Un entero único. Aumenta con cada instancia.
        socket_cliente: Un socket, es None si el jugador es bot.
        address: Una tupla, representa la dirección de red del cliente, es
          None si el jugador es bot.
        username: Un string, representa el nombre del cliente.

        ya_voto: Un bool, indica si el jugador ya votó en la ronda actual.
        votos_ronda: un int, indica cuantos votos ha recibido en la ronda.
        vivo: Un bool, indica si el jugador está vivo o no en una ronda.
    """

    id_ = 0

    # Este lock evita que se produzcan errores cuando dos jugadores votan al mismo tiempo
    votos_lock = Lock()

    def __init__(self, username):
        self.id_jugador = Jugador.id_
        self.username = username
        Jugador.id_ += 1
        # Todos los jugadores comienzan como bots, es decir, no tienen socket ni address.
        self.socket_cliente = None
        self.address = None

        # Atributos de ronda
        self.ya_voto = False
        self.__votos_ronda = 0
        self.vivo = True

    @property
    def votos_ronda(self):
        return self.__votos_ronda

    @votos_ronda.setter
    def votos_ronda(self, value):
        self.votos_lock.acquire()
        self.__votos_ronda = value
        self.votos_lock.release()

    def __str__(self):
        nombre = self.username if self.username is not None else "<SIN NOMBRE>"
        if self.socket_cliente is None:
            return f"[{str(self.id_jugador)}] {nombre} (BOT)"
        return f"[{str(self.id_jugador)}] {nombre} {str(self.address)}"



def leer_nombres(path):
    """
    Recibe el path del archivo de nombres.
    Retorna una lista con strings correspondientes.
    """
    lista_nombres = []
    with open(path) as archivo:
        nombres = archivo.readlines()
        for nombre in nombres:
            lista_nombres.append(nombre.strip())
    shuffle(lista_nombres)
    return lista_nombres[:N_JUGADORES]


def crear_lista_jugadores(lista_nombres):
    """
    Recibe una lista con strings de nombres
    Retorna una lista con instancias de la clase Jugador.
    """
    lista_jugadores = []
    for nombre in lista_nombres:
        jugador = Jugador(nombre.strip())
        lista_jugadores.append(jugador)
    return lista_jugadores
