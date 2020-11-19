from functools import partial
from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from ventana_inicio import VentanaInicio
from sala_de_espera import SalaEspera
from ventana_principal import VentanaPrincipal
from popups import PopupCrewmate, PopupExpulsar, PopupFinal

class Controlador(QObject):

    mostrar_sala_espera_signal = pyqtSignal()
    mostrar_ventana_principal_signal = pyqtSignal()
    mostrar_popup_crewmate_signal = pyqtSignal(str)
    mostrar_popup_expulsar_signal = pyqtSignal(str)
    mostrar_popup_final_signal = pyqtSignal(str)
    actualizar_jugadores_signal = pyqtSignal(list)

    def __init__(self, parent):
        super().__init__()

        self.ventana_inicio = VentanaInicio()
        self.sala_espera = SalaEspera()
        self.ventana_principal = VentanaPrincipal()

        self.popup_crewmate = PopupCrewmate()
        self.popup_expulsar = PopupExpulsar()
        self.popup_final = PopupFinal()

        self.username = None
        self.impostor = False
        self.vivo = True
        self.mostrando_popup = False
        self.partida_terminada = False

        # Conectar señales
        self.ventana_inicio.enviar_username_signal.connect(parent.enviar)

        self.sala_espera.actualizar_jugadores_signal.connect(parent.enviar)
        self.sala_espera.comenzar_partida_signal.connect(parent.enviar)

        self.ventana_principal.enviar_texto_signal.connect(parent.enviar)
        self.ventana_principal.votar_signal.connect(parent.enviar)

        self.actualizar_jugadores_signal.connect(self.sala_espera.actualizar_jugadores)

        self.mostrar_sala_espera_signal.connect(self.mostrar_sala_espera)
        self.mostrar_ventana_principal_signal.connect(self.mostrar_principal)

        # Popups
        self.mostrar_popup_crewmate_signal.connect(self.mostrar_popup_crewmate)
        self.mostrar_popup_expulsar_signal.connect(self.mostrar_popup_expulsar)
        self.mostrar_popup_final_signal.connect(self.mostrar_popup_final)

    def mostrar_login(self):
        self.ventana_inicio.show()

    def mostrar_sala_espera(self):
        self.sala_espera.show()
        self.ventana_inicio.close()

    def mostrar_principal(self):
        self.sala_espera.close()
        self.popup_crewmate.hide()
        self.popup_expulsar.hide()
        self.popup_expulsar.gif.stop()
        self.mostrando_popup = False
        if not self.partida_terminada:
            self.ventana_principal.show()

    def mostrar_popup_crewmate(self, tipo):
        self.sala_espera.close()
        self.popup_crewmate.actualizar_label(tipo)
        self.popup_crewmate.show()
        self.mostrando_popup = True
        QTimer.singleShot(2500, self.mostrar_principal)

    def mostrar_popup_expulsar(self, username):
        self.ventana_principal.hide()
        self.popup_expulsar.actualizar_label(username)
        self.popup_expulsar.show()
        self.mostrando_popup = True
        QTimer.singleShot(3000, self.mostrar_principal)

    def mostrar_popup_final(self, resultado):
        if self.mostrando_popup:
            QTimer.singleShot(3000, partial(self.mostrar_popup_final, resultado))
        else:
            self.popup_final.actualizar_label(resultado)
            self.ventana_principal.close()
            self.popup_final.show()
            self.mostrando_popup = True

    def manejar_mensaje(self, mensaje):
        try:
            comando = mensaje["comando"]
        except KeyError:
            return []
        if comando == "receive_chat_message":
            self.ventana_principal.recibir_chat_signal.emit(mensaje["text"])
        elif comando == "log_in_accepted":
            self.username = mensaje["username"]
            self.mostrar_sala_espera_signal.emit()
        elif comando == "log_in_rejected":
            self.ventana_inicio.recibir_feedback_signal.emit(mensaje)
        elif comando == "actualizar_jugadores":
            self.actualizar_jugadores_signal.emit(mensaje["jugadores"])
        elif comando == "empezar":
            if mensaje["tipo"] == "impostor":
                self.impostor = True
            self.mostrar_popup_crewmate_signal.emit(mensaje["tipo"])
        elif comando == "jugadores_partida":
            self.ventana_principal.actualizar_botones_signal.emit(mensaje["lista_jugadores"])
        elif comando == "voto_correcto":
            self.ventana_principal.voto_emitido = True
        elif comando == "jugador_expulsado":
            jugador_expulsado = mensaje["jugador"]
            if jugador_expulsado == self.username:
                self.ventana_principal.vivo = False
                self.vivo = False
            self.ventana_principal.voto_emitido = False
            self.mostrar_popup_expulsar_signal.emit(jugador_expulsado)
        elif comando == "fin_de_partida":
            self.partida_terminada = True
            resultado = mensaje["resultado"]
            if resultado == "gana_impostor":
                if self.impostor:
                    self.mostrar_popup_final_signal.emit("impostor_victory")
                else:
                    self.mostrar_popup_final_signal.emit("crewmate_defeat")
            elif resultado == "ganan_crewmates":
                if self.impostor:
                    self.mostrar_popup_final_signal.emit("impostor_defeat")
                else:
                    self.mostrar_popup_final_signal.emit("crewmate_victory")
