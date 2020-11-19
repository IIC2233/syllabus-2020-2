"""
Modulo contiene implementación principal del servidor
"""
import json
import socket
import threading
from jugadores import crear_lista_jugadores, leer_nombres
from logica import Logica


class Servidor:
    """
    Administra la conexión y la comunicación con los clientes

    Atributos:
        host: string que representa la dirección del host (como una URL o una IP address).
        port: int que representa el número de puerto en el cual el servidor recibirá conexiones.
        log_activado: booleano, controla si el programa "printea" en la consola (ver método log).
        socket_server: socket del servidor, encargado de recibir conexiones.
        lista_jugadores: lista de instancias de Jugadores.
    """

    # Este lock administra el acceso a la lista de usuarios para evitar que se produzcan errores.
    lista_jugadores_lock = threading.Lock()

    def __init__(self, host, port, log_activado=True):
        self.host = host
        self.port = port
        self.log_activado = log_activado

        self.log("Inicializando servidor...")

        # Crear socket IPv4, TCP
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Ligar socket
        self.socket_server.bind((self.host, self.port))

        # Permite escuchar
        self.socket_server.listen()
        self.log(f"Servidor escuchando en {self.host}:{self.port}")
        self.log("Servidor aceptando conexiones")

        # Inicializar lista de jugadores con bots
        self.lista_nombres_bots = leer_nombres("nombres.txt")
        self.lista_jugadores = crear_lista_jugadores(self.lista_nombres_bots)

        self.logica = Logica()

        # Crea y comienza thread encargado de aceptar clientes
        thread = threading.Thread(target=self.aceptar_clientes, daemon=True)
        thread.start()

    def aceptar_clientes(self):
        """Ciclo principal que acepta clientes.
        """
        # Completar
        pass








    def escuchar_cliente(self, jugador):
        """Ciclo principal que escucha a un cliente.

        Recibe mensajes de un cliente, y genera una respuesta adecuada o levanta
        una acción según el mensaje recibido. Puede ser ejecutado en un thread,
        para permitir múltiples clientes paralelos.

        Argumentos:
            jugador (Jugador): El objeto jugador del cliente a escuchar.
        """
        try:
            # Completar
            pass





        except ConnectionResetError:
            self.log(f"Error: conexión con {jugador} fue reseteada.")
        self.log(f"Cerrando conexión con {jugador}.")
        self.eliminar_cliente(jugador)

    def enviar_lista_respuestas(self, jugador, lista_respuestas):
        """Envía las respuestas a los clientes respectivos.

        Argumentos:
            jugador (Jugador): El jugador actual del cual se recibió el mensaje inicial
            lista_respuestas (lista de tuplas): Las respuestas a enviar retornadas por
              manejar_mensaje, clasificadas en una tupla según su destino
        """
        for tup in lista_respuestas:
            msg = tup[1]
            if tup[0] == "individual":
                self.enviar(msg, jugador.socket_cliente)
            elif tup[0] == "broadcast":
                self.enviar_a_todos(msg)
            elif tup[0] == "impostor":
                self.enviar(msg, self.logica.impostor.socket_cliente)
            elif tup[0] == "crewmates":
                for j in self.lista_jugadores:
                    if j != self.logica.impostor and j.socket_cliente is not None:
                        self.enviar(msg, j.socket_cliente)

    def enviar(self, mensaje, socket_cliente):
        """Envía un mensaje a un cliente.

        Argumentos:
            mensaje (dict): Contiene la información a enviar. Debe ser serializable.
            socket_cliente (socket): El socket objetivo al cual enviar el mensaje.
        """
        # Completar
        pass








    def enviar_a_todos(self, mensaje):
        """Envía mensaje a todos los usuarios conectados.

        Argumentos:
            mensaje (dict): Contiene la información a enviar. Debe ser serializable.
        """
        for jugador in self.lista_jugadores:
            try:
                if jugador.socket_cliente is not None:
                    self.enviar(mensaje, jugador.socket_cliente)
            except ConnectionError:
                self.eliminar_cliente(jugador)

    def recibir(self, socket_cliente):
        """Recibe un mensaje del cliente.

        Recibe el mensaje, lo decodifica usando el protocolo establecido,
        y lo des-serializa (via decodificar_mensaje).

        Argumentos:
            socket_cliente (socket): El socket del cliente del cual recibir.

        Retorna:
            dict: contiene el mensaje, después de ser decodificado.
        """
        # Completar
        pass








    def log(self, mensaje_consola):
        """Imprime un mensaje a la consola, sólo si la funcionalidad está activada.

        Argumentos:
            mensaje_consola (str): mensaje a imprimir.
        """
        if self.log_activado:
            print(mensaje_consola)

    def eliminar_cliente(self, jugador):
        """Elimina un jugador de lista_jugadores (lo transforma a bot).

        Argumentos:
            jugador (Jugador): el objeto jugador del cliente a sacar de la lista.
        """
        self.lista_jugadores_lock.acquire()
        self.log(f"Borrando socket del cliente {jugador}.")
        index = self.lista_jugadores.index(jugador)
        # Volver a asignar nombre por defecto a jugador
        jugador.username = self.lista_nombres_bots[index]
        # Cerrar socket
        jugador.socket_cliente.close()
        jugador.socket_cliente = None
        jugador.address = None
        self.lista_jugadores_lock.release()

    @staticmethod
    def codificar_mensaje(mensaje):
        """Codifica y serializa un mensaje usando JSON.

        Argumentos:
            mensaje (dict): Contiene llaves de strings, con información útil a enviar a cliente.
              Los valores del diccionario deben ser serializables.

        Retorna:
            bytes: El mensaje serializado
        """
        try:
            # Create JSON object
            json_mensaje = json.dumps(mensaje)
            # Encode JSON object
            bytes_mensaje = json_mensaje.encode()

            return bytes_mensaje
        except json.JSONDecodeError:
            print("No se pudo codificar el mensaje")
            return b""

    @staticmethod
    def decodificar_mensaje(bytes_mensaje):
        """Decodifica y des-serializa bytes usando JSON.

        Argumentos:
            bytes_mensaje (bytes): Representa el mensaje serializado. Debe ser des-serializable
                y decodificable.

        Retorna:
            dict: El mensaje des-serializado, en su forma original.
        """
        try:
            mensaje = json.loads(bytes_mensaje)
            return mensaje
        except json.JSONDecodeError:
            print("No se pudo decodificar el mensaje")
            return dict()
