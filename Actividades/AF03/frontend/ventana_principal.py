import os
import random
import parametros as p
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout
)
from PyQt5.QtCore import pyqtSignal, QSize, QTimer, QEventLoop
from PyQt5.QtGui import QFont, QPixmap, QMovie


class VentanaPrincipal(QMainWindow):

    senal_abrir_menu_principal = pyqtSignal()

    def __init__(self, ancho, alto, altura_botones, gif_time):
        """Es el init de la ventana del menú. Puedes ignorarlo."""
        super().__init__()
        self.size = (ancho, alto)
        self.resize(*self.size)
        self.altura_botones = altura_botones
        self.gif_time = gif_time
        self.senal_abrir_menu_principal.connect(self.show)
        self.senal_abrir_tarea_codigo = None
        self.senal_abrir_tarea_descarga = None
        self.init_gui()

    def init_gui(self):
        """Este método crea los elementos básicos del menú principal.
        Puedes ignorarlo."""
        self.setWindowTitle("DCCrew")
        self.setFixedSize(*self.size)

        self.fondo = QLabel(self)
        self.fondo.setPixmap(QPixmap(os.path.join("frontend", "assets", "logo_dccrew.png")))
        self.fondo.setGeometry(0, 0, *self.size)
        self.fondo.setScaledContents(True)

        self.area_tareas = QWidget(self)
        ancho = self.size[0]
        alto = self.size[1]
        self.area_tareas.setGeometry(0.1 * ancho, 0.5 * alto, 0.8 * ancho, self.altura_botones * 4 + 30)

        self.crear_botones()

    def crear_botones(self):

        # No modificar ->
        vbox = QVBoxLayout()

        titulo_layout_tareas = QLabel("Escoge una tarea")
        titulo_layout_tareas.setMinimumHeight(self.altura_botones)
        titulo_layout_tareas.setStyleSheet("color: #ffffff; font-size: 32px; font-weight: bold;")
        titulo_layout_tareas.setFont(QFont("Courier"))
        vbox.addWidget(titulo_layout_tareas)
        # <-

        # Completar: Crear los botones de las tareas, conectarlos al método y  añadirlos al "vbox"

        # No modificar ->
        self.contador_tareas = QLabel("Tareas hechas: 0/2")
        self.contador_tareas.setMinimumHeight(self.altura_botones - 10)
        self.contador_tareas.setStyleSheet("color: #ffffff; font-size: 32px; font-weight: bold;")
        self.contador_tareas.setFont(QFont("Courier"))
        vbox.addWidget(self.contador_tareas)

        self.area_tareas.setLayout(vbox)
        # <-

    def cambiar_diseno_botones(self, boton):
        """Este método cambia el diseño de los botones de las tareas.
        Puedes ignorarlo."""
        boton.setStyleSheet('''QPushButton {background-color: #ffffff; color: #000000; 
        font-size: 23px;} QPushButton:disabled {background-color: #c0c0c0}''')

        boton.setFont(QFont("Courier"))
        boton.setMinimumHeight(self.altura_botones)

    def boton_tarea_clickeado(self):
        # No modificar ->
        numero_tarea = int(self.sender().text()[-1])
        self.hide()
        # <-

        # Completar

    def tarea_terminada(self, info_tarea):
        # No modificar <-
        numero_tarea = info_tarea[0]
        tareas_terminadas = info_tarea[1]
        # <-

        # Completar

        # No modificar ->
        self.show()
        if tareas_terminadas == 2:
            self.terminar_juego()
        # <-

    def terminar_juego(self):
        """Este método se encarga de determinar si luego de terminar las
        tareas ganas o pierdes. Puedes ignorarlo."""
        self.area_tareas.hide()

        self.setFixedSize(*self.size)

        numero_random = random.random()
        if numero_random <= p.PROB_GANAR:
            self.mostrar_imagen_final(True)

        else:
            gif_label = QLabel(self)
            gif_label.resize(*self.size)
            gif = QMovie(os.path.join("frontend", "assets", "kill.gif"))
            gif_label.setMovie(gif)
            gif_label.setScaledContents(True)
            gif_label.show()
            gif.start()

            loop = QEventLoop()
            QTimer.singleShot(self.gif_time * 1000, loop.quit)
            loop.exec_()

            self.mostrar_imagen_final(False)

    def mostrar_imagen_final(self, es_victoria):
        """Este método muestra la imagen final según sea victoria o derrota.
        Puedes ignorarlo."""
        imagen_final = QLabel(self)
        imagen_final.resize(*self.size)
        imagen_final.setScaledContents(True)

        if es_victoria:
            imagen_final.setPixmap(QPixmap(os.path.join("frontend", "assets", "victory.jpg")))
        else:
            imagen_final.setPixmap(QPixmap(os.path.join("frontend", "assets", "defeat.png")))

        imagen_final.show()
