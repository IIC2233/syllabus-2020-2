import os
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout,
)
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QEventLoop, QTimer
from PyQt5.QtGui import QIcon, QPixmap


class VentanaTareaCodigo(QWidget):

    senal_abrir_tarea = pyqtSignal()
    senal_tarea_terminada = pyqtSignal(int)
    senal_boton_teclado_clickeado = pyqtSignal(tuple)

    def __init__(self, ancho, alto, codigo_correcto, tiempo_msg_final):
        """Es el init de la ventana de la tarea. Puedes ignorarlo."""
        super().__init__()
        self.size = (ancho, alto)
        self.codigo_correcto = codigo_correcto
        self.tiempo_msg_final = tiempo_msg_final
        self.senal_abrir_tarea.connect(self.show)
        self.init_gui()

    def init_gui(self):
        """Este método crea los elementos básicos de la ventana.
        Puedes ignorarlo."""
        self.setWindowTitle("DCCrew")
        self.resize(*self.size)
        self.setFixedSize(*self.size)

        self.fondo = QLabel(self)
        self.fondo.setPixmap(QPixmap(os.path.join("frontend", "assets", "code_task_bg.png")))
        self.fondo.resize(*self.size)
        self.fondo.setScaledContents(True)

        self.cargar_teclado()

    def cargar_teclado(self):
        """Este método carga la estructura base de la ventana.
        Puedes ignorarlo."""
        fondo_teclado = QLabel(self)
        fondo_teclado.setStyleSheet("background-color: black; border: 6px solid #e0e0e0;")
        ancho = self.size[0]
        alto = self.size[1]
        fondo_teclado.setGeometry(0.07 * ancho, 0.07 * alto, 0.86 * ancho, 0.86 * alto)

        area_teclado = QWidget(self)
        area_teclado.setGeometry(ancho * 0.25, 0.1 * alto, 0.5 * ancho, 0.8 * alto)

        self.pantalla_teclado = QLabel(self)
        self.pantalla_teclado.setStyleSheet('''background-color: #090404; border: 3px solid #d9c128; 
        color: #d9c128; font-size: 30px; font-weight: bold;''')
        self.pantalla_teclado.setAlignment(Qt.AlignCenter)
        self.pantalla_teclado.setMinimumHeight(0.12 * alto)
        self.pantalla_teclado.raise_()

        self.teclado = QGridLayout()
        for i in range(3):
            for j in range(3):
                boton = QPushButton(str(3 * i + j + 1), self)
                boton.clicked.connect(self.boton_teclado_clickeado)
                self.cambiar_diseno_botones(boton, "KeyNormalButton")
                self.teclado.addWidget(boton, i, j)

        boton = QPushButton()
        boton.clicked.connect(self.boton_teclado_clickeado)
        boton.setIcon(QIcon(os.path.join("frontend", "assets", "not_ok.png")))
        boton.setIconSize(QSize(50, 50))
        self.cambiar_diseno_botones(boton, "KeyDelButton")
        self.teclado.addWidget(boton, 3, 0)

        boton = QPushButton("0")
        boton.clicked.connect(self.boton_teclado_clickeado)
        self.cambiar_diseno_botones(boton, "KeyNormalButton")
        self.teclado.addWidget(boton, 3, 1)

        boton = QPushButton()
        boton.clicked.connect(self.boton_teclado_clickeado)
        boton.setIcon(QIcon(os.path.join("frontend", "assets", "ok.png")))
        boton.setIconSize(QSize(50, 50))
        self.cambiar_diseno_botones(boton, "KeySendButton")
        self.teclado.addWidget(boton, 3, 2)

        self.codigo_correcto = QLabel(f"Código: {self.codigo_correcto}", self)
        self.codigo_correcto.setStyleSheet("color: #a0a0a0; font-size: 25px; font-weight: bold;")
        self.codigo_correcto.setMinimumHeight(0.115 * self.size[1])

        vbox = QVBoxLayout()
        vbox.addWidget(self.pantalla_teclado)
        vbox.addStretch(1)
        vbox.addLayout(self.teclado)
        vbox.addStretch(1)
        vbox.addWidget(self.codigo_correcto)

        area_teclado.setLayout(vbox)
        area_teclado.show()

    def cambiar_diseno_botones(self, boton, nombre_boton):
        """Este método cambia el diseño de los botones del teclado.
        Puedes ignorarlo."""
        boton.setObjectName(nombre_boton)
        boton.setMinimumHeight(0.115 * self.size[1])
        boton.setStyleSheet("background-color: #696969; color: #70d143; font-size: 23px;")

    def boton_teclado_clickeado(self):
        """Este método se encarga de transmitir la señal de un botón clickeado.
        Puedes ignorarlo."""
        boton_clickeado = self.sender()
        self.senal_boton_teclado_clickeado.emit((boton_clickeado.objectName(), boton_clickeado.text()))

    def actualizar_pantalla(self, codigo_actual):
        # Completar
        pass

    def recibir_comparacion(self, son_iguales):
        # Completar
        pass

    def tarea_terminada(self):
        """Este método muestra el mensaje de término de la tarea y regresa al menú principal.
        Puedes ignorarlo"""
        imagen_final = QLabel(self)
        imagen_final.setGeometry(0, self.size[1] / 2 - 150, self.size[0], 300)
        imagen_final.setPixmap(QPixmap(os.path.join("frontend", "assets", "terminado.png")))
        imagen_final.setScaledContents(True)
        imagen_final.raise_()
        imagen_final.show()

        # Este loop funciona similar a un time.sleep(secs/1000)
        loop = QEventLoop()
        QTimer.singleShot(self.tiempo_msg_final * 1000, loop.quit)
        loop.exec_()

        self.hide()
        self.senal_tarea_terminada.emit(2)
