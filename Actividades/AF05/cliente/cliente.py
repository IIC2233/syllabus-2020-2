"""
Modulo contiene implementación principal del cliente
"""
import json
import threading
import socket
from interfaz import Controlador


class Cliente:
    """
    Administra la conexión y la comunicación con el servidor.

    Atributos:
        host: string que representa la dirección del host (como una URL o una IP address).
        port: int que representa el número de puerto al cual conectarse.
        controlador: instancia de Controlador, maneja la interfaz gráfica del programa.
        conectado: booleano, indica si el cliente se encuentra conectado al servidor.
        socket_cliente: socket del cliente, conectado al servidor.
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port

        # Inicializar UI
        self.controlador = Controlador(self)

        # Crear socket IPv4, TCP
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Conectarse con el servidor
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True

            # Escuchar los mensajes del servidor
            thread = threading.Thread(
                target=self.escuchar_servidor,
                daemon=True
            )
            thread.start()
            self.controlador.mostrar_login()
        except ConnectionRefusedError:
            print(f"No se pudo conectar a {self.host}:{self.port}")
            self.socket_cliente.close()

    def escuchar_servidor(self):
        """Ciclo principal que escucha al servidor.

        Recibe mensajes desde el servidor, y genera una respuesta adecuada.
        """
        try:
            # Completar
            pass




        except ConnectionResetError:
            print("Error de conexión con el servidor")
        finally:
            self.socket_cliente.close()

    def enviar(self, mensaje):
        """Envía un mensaje a un cliente.

        Argumentos:
            mensaje (dict): Contiene la información a enviar. Debe ser serializable.
            socket_cliente (socket): El socket objetivo al cual enviar el mensaje.
        """
        # Completar
        pass







    def recibir(self):
        """Recibe un mensaje del servidor.

        Recibe el mensaje, lo decodifica usando el protocolo establecido,
        y lo des-serializa (via decodificar_mensaje).

        Retorna:
            dict: contiene el mensaje, después de ser decodificado.
        """
        # Completar
        pass







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
