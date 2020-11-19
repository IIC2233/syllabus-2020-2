"""
Interfaz de la ventana de sala de espera
"""
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout,
                             QPushButton, QGridLayout)
from PyQt5.QtCore import pyqtSignal, Qt


class SalaEspera(QMainWindow):
    """
    Interfaz gráfica de sala de espera
    """

    close_window_signal = pyqtSignal(bool)
    comenzar_partida_signal = pyqtSignal(dict)
    actualizar_jugadores_signal = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tamano_ventana = (400, 200)
        self.__init_ui()
        self.__connect_events()
        self.__retranslate_ui()

    def __init_ui(self):

        self.setMinimumSize(*self.tamano_ventana)
        # Main widget declaration
        self.central_widget = QWidget(self)
        self.layout_horizontal_superior = QHBoxLayout()
        self.layout_vertical_principal = QVBoxLayout(self.central_widget)
        self.jugadores_layout = QGridLayout()
        self.title_label = QLabel(self.central_widget)
        self.exit_button = QPushButton(self.central_widget)
        self.start_button = QPushButton(self.central_widget)

        # Add widgets to layout
        self.layout_horizontal_superior.addWidget(self.title_label)
        self.layout_horizontal_superior.addStretch()
        self.layout_horizontal_superior.addWidget(self.exit_button)
        self.layout_vertical_principal.addLayout(self.layout_horizontal_superior)
        self.layout_vertical_principal.addLayout(self.jugadores_layout)
        self.layout_vertical_principal.addWidget(self.start_button)

        # Set layout
        self.setCentralWidget(self.central_widget)

    def __retranslate_ui(self):
        self.setWindowTitle("DCCrew DemoCratiCa - Sala de Espera")
        self.title_label.setText("Jugadores:")
        self.title_label.setStyleSheet("font-size: 24px")
        self.exit_button.setText("Salir")
        self.start_button.setText("Comenzar Partida")

    def __connect_events(self):
        self.exit_button.clicked.connect(self.close)
        self.start_button.clicked.connect(self.comenzar_partida)

    def comenzar_partida(self):
        dict_ = {
            "comando" : "comenzar_partida"
        }
        self.comenzar_partida_signal.emit(dict_)

    def actualizar_jugadores(self, jugadores):
        """
        Actualiza jugadores disponibles en la pantalla
        """
        # Limpiar layout antigua
        for i in reversed(range(self.jugadores_layout.count())):
            self.jugadores_layout.itemAt(i).widget().setParent(None)
        # Añadir jugadores a layout
        j = -1
        for i, jugador in enumerate(jugadores):
            if i % 2 == 0:
                j += 1
            x = i % 2
            y = j
            jugador_label = QLabel(str(jugador))
            self.jugadores_layout.addWidget(jugador_label, y, x, Qt.AlignHCenter)

    def showEvent(self, event):
        dict_ = {
            "comando" : "request_jugadores"
        }
        self.actualizar_jugadores_signal.emit(dict_)
        super().showEvent(event)

    def closeEvent(self, event):
        self.close_window_signal.emit(True)
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication([])
    window = SalaEspera()
    window.actualizar_jugadores(["Jugador 1", "Jugador 2", "Jugador 3", "Jugador 4", "Jugador 5"])
    window.show()
    sys.exit(app.exec_())
