"""
Este módulo contiene los popups que muestran los eventos a los clientes
"""
import sys
from os import path
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel)
from PyQt5.QtGui import QPixmap, QMovie, QFont
from PyQt5.QtCore import pyqtSignal, QSize, Qt


class PopupExpulsar(QWidget):
    """
    Popup mostrado al expulsar un jugador de la nave
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_size = (480, 270)
        self.__init_ui()
        self.__connect_events()
        self.__retranslate_ui()

    def __init_ui(self):
        # Main widget declaration
        self.gif_label = QLabel(self)
        self.setMinimumSize(*(self.image_size))

        # Text
        self.text_label = QLabel(self)

        # Add to layout
        self.main_vertical_layout = QVBoxLayout(self)
        self.main_vertical_layout.addStretch(1)
        self.main_vertical_layout.addWidget(self.text_label)
        self.main_vertical_layout.addStretch(3)

    def __retranslate_ui(self):
        self.setWindowTitle("DCCrew DemoCratiCa - Ejection")
        # Text
        self.text_label.setStyleSheet("""
            color: white;
            font-size: 28px;
            """)
        self.text_label.setFont(QFont("Helvetica"))
        self.text_label.setAlignment(Qt.AlignCenter)
        # Gif
        path_gif = path.join("assets", "expulsado.gif")
        self.gif = QMovie(path_gif)
        self.gif.setSpeed(200)
        self.gif.setScaledSize(QSize(*self.image_size))
        self.gif_label.setMovie(self.gif)
        self.gif_label.setMinimumSize(QSize(*(self.image_size)))

    def __connect_events(self):
        pass

    def actualizar_label(self, username):
        self.text_label.setText(f"{username} ha sido expulsado...")
        self.gif.start()


class PopupFinal(QWidget):
    """
    Popup mostrado al finalizar la partida
    """

    show_popup_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_size = (960, 540)
        self.__init_ui()
        self.__connect_events()
        self.__retranslate_ui()

    def __init_ui(self):
        # Main widget declaration
        self.label_central = QLabel()
        self.imagen = QLabel(self)
        self.setMinimumSize(*(self.image_size))
        self.imagen.setMinimumSize(*(self.image_size))

    def __retranslate_ui(self):
        self.setWindowTitle("DCCrew DemoCratiCa - Fin")

    def __connect_events(self):
        self.show_popup_signal.connect(self.actualizar_label)

    def actualizar_label(self, condicion):
        path_imagen = path.join("assets", condicion)
        pixmap = QPixmap(path_imagen).scaledToHeight(self.image_size[1])
        self.imagen.setPixmap(pixmap)


class PopupCrewmate(QWidget):
    """
    Popup mostrado al comenzar la partida
    """

    show_popup_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_size = (480, 270)
        self.__init_ui()
        self.__connect_events()
        self.__retranslate_ui()

    def __init_ui(self):
        # Main widget declaration
        self.label_central = QLabel()
        self.imagen = QLabel(self)
        self.setMinimumSize(*(self.image_size))
        self.imagen.setMinimumSize(*(self.image_size))

    def __retranslate_ui(self):
        self.setWindowTitle("DCCrew DemoCratiCa - Comenzar")

    def __connect_events(self):
        self.show_popup_signal.connect(self.actualizar_label)

    def actualizar_label(self, tipo):
        path_imagen = ""
        if tipo == "crewmate":
            path_imagen = path.join("assets", "crewmate")
        elif tipo == "impostor":
            path_imagen = path.join("assets", "impostor")
        pixmap = QPixmap(path_imagen).scaledToHeight(self.image_size[1])
        self.imagen.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication([])
    window = PopupExpulsar()
    window.actualizar_label("cruz")
    window.show()
    sys.exit(app.exec_())
