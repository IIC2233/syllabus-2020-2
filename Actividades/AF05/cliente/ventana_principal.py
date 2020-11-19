"""
Interfaz de la ventana principal (votación) del programa
"""
import sys
from functools import partial
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel,
                             QGridLayout, QPushButton)
# from PyQt5.QtGui import QCloseEvent
from PyQt5.QtCore import pyqtSignal
from chat_widget import ChatWidget


class VentanaPrincipal(QMainWindow):
    """
    Interfaz gráfica de ventana principal (votación)
    """

    cerrar_ventana_signal = pyqtSignal(bool)
    recibir_chat_signal = pyqtSignal(str)
    actualizar_botones_signal = pyqtSignal(list)
    votar_signal = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.voto_emitido = False
        self.vivo = True

        self.__init_ui()
        self.__connect_events()
        self.__retranslate_ui()

    def __init_ui(self):

        # Main widget declaration
        self.central_widget = QWidget(self)
        self.main_horizontal_layout = QHBoxLayout(self.central_widget)
        self.chat_vertical_layout = QVBoxLayout()
        self.button_layout = QGridLayout()
        self.chat_button_layout = QHBoxLayout()
        self.chat_widget = ChatWidget(self.central_widget)
        self.back_button = QPushButton(self.central_widget)

        # Flatten signals
        self.enviar_texto_signal = self.chat_widget.enviar_texto_signal

        # Add widgets to layout
        self.chat_button_layout.addStretch()
        self.chat_button_layout.addWidget(self.back_button)
        self.chat_vertical_layout.addLayout(self.chat_button_layout)
        self.chat_vertical_layout.addWidget(self.chat_widget)
        self.main_horizontal_layout.addLayout(self.button_layout)
        self.main_horizontal_layout.addLayout(self.chat_vertical_layout)

        # Set layout
        self.setCentralWidget(self.central_widget)

    def __retranslate_ui(self):
        self.setWindowTitle("DCCrew DemoCratiCa - Ventana Principal")
        self.back_button.setText("Salir")

    def __connect_events(self):
        self.back_button.clicked.connect(self.close)
        self.actualizar_botones_signal.connect(self.actualizar_botones)
        self.recibir_chat_signal.connect(self.chat_widget.add_message)

    def actualizar_botones(self, lista_jugadores):
        # Limpiar layout antigua
        for i in reversed(range(self.button_layout.count())):
            self.button_layout.itemAt(i).widget().setParent(None)
        # Añadir jugadores a layout
        j = -1
        for i, jugador in enumerate(lista_jugadores):
            if i % 2 == 0:
                j += 1
            x = i % 2
            y = j
            jugador_widget = QWidget(self)
            nombre_label = QLabel(jugador[0], jugador_widget)
            if jugador[1]:
                voto_label = QLabel("Ya votó", jugador_widget)
            else:
                voto_label = QLabel("Aún no vota", jugador_widget)
            if jugador[2]:
                estado_label = QLabel("Vivo")
            else:
                estado_label = QLabel("Muerto")

            button = QPushButton("VOTAR", jugador_widget)
            button.clicked.connect(partial(self.click_votar, jugador[0]))
            # Si el jugador está muerto o ya se votó
            if self.voto_emitido or not jugador[2] or not self.vivo:
                button.setDisabled(True)

            layout_h = QHBoxLayout()
            layout_v = QVBoxLayout()

            layout_v.addWidget(nombre_label)
            layout_v.addWidget(estado_label)
            layout_v.addWidget(voto_label)
            layout_h.addLayout(layout_v)
            layout_h.addWidget(button)

            jugador_widget.setLayout(layout_h)
            self.button_layout.addWidget(jugador_widget, y, x)

    def click_votar(self, nombre):
        mensaje = {
            "comando" : "votar_jugador",
            "jugador" : nombre
        }
        self.votar_signal.emit(mensaje)

    def closeEvent(self, event):
        self.cerrar_ventana_signal.emit(True)
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication([])
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec_())
