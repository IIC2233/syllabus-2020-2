import os
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel, QHBoxLayout, QProgressBar,
)
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QEventLoop, QTimer
from PyQt5.QtGui import QPixmap, QFont


class VentanaTareaDescarga(QWidget):

    senal_abrir_tarea = pyqtSignal()
    senal_tarea_terminada = pyqtSignal(int)

    def __init__(self, ancho, alto, tiempo_tarea, tiempo_msg_final):
        """Es el init de la ventana de la tarea. Puedes ignorarlo."""
        super().__init__()
        self.size = (ancho, alto)
        self.tiempo_tarea = tiempo_tarea
        self.tiempo_msg_final = tiempo_msg_final
        self.senal_abrir_tarea.connect(self.show)
        self.init_gui()

    def init_gui(self):
        # No modificar ->
        self.setWindowTitle("DCCrew")
        self.resize(*self.size)
        self.setFixedSize(*self.size)

        self.fondo = QLabel(self)
        self.fondo.setPixmap(QPixmap(os.path.join("frontend", "assets", "dwld_task_bg.png")))
        self.fondo.resize(*self.size)
        self.fondo.setScaledContents(True)

        self.area_widgets = QWidget(self)
        ancho = self.size[0]
        alto = self.size[1]
        self.area_widgets.setGeometry(ancho * 0.1, alto * 0.75, ancho * 0.8, alto * 0.12)

        self.barra_progreso = QProgressBar()
        self.cambiar_diseno_barra_progreso(self.barra_progreso)

        hbox = QHBoxLayout()

        self.boton_comenzar_tarea = QPushButton("Comenzar")
        self.cambiar_diseno_botones(self.boton_comenzar_tarea)
        # <-

        # Completar

        # No modificar ->
        hbox.addWidget(self.boton_comenzar_tarea)
        hbox.addWidget(self.barra_progreso)

        self.area_widgets.setLayout(hbox)
        # <-

    def cambiar_diseno_botones(self, boton):
        """Este método cambia el diseño de los botones de las tareas.
        Puedes ignorarlo."""
        boton.setMinimumSize(140, 60)
        boton.setStyleSheet('''QPushButton {background-color: #ffffff; color: #000000; 
        font-size: 23px;} QPushButton:disabled {background-color: #c0c0c0}''')
        boton.setFont(QFont("Courier"))

    def cambiar_diseno_barra_progreso(self, barra_progreso):
        """Este método cambia el diseño de la barra de progreso.
        Puedes ignorarlo."""
        barra_progreso.setMaximum(100)
        barra_progreso.setTextVisible(False)
        barra_progreso.setStyleSheet('''QProgressBar {background-color: #000000;} 
        QProgressBar::chunk {background-color: green; width: 10px; margin: 1px;}''')

    def comenzar_tarea(self):
        """Este método comienza la tarea. Puedes ignorarlo."""
        self.boton_comenzar_tarea.setEnabled(False)

        for progreso in range(1, 101):
            self.barra_progreso.setValue(progreso)

            loop = QEventLoop()
            QTimer.singleShot(self.tiempo_tarea * 10, loop.quit)
            loop.exec_()

        self.tarea_terminada()

    def tarea_terminada(self):
        """Este método muestra el mensaje de término de la tarea y regresa al menú principal.
        Puedes ignorarlo"""
        imagen_final = QLabel(self)
        imagen_final.setGeometry(0, self.size[1] / 2 - 150, self.size[0], 300)
        imagen_final.setPixmap(QPixmap(os.path.join("frontend", "assets", "terminado.png")))
        imagen_final.setScaledContents(True)
        imagen_final.raise_()
        imagen_final.show()

        loop = QEventLoop()
        QTimer.singleShot(self.tiempo_msg_final * 1000, loop.quit)
        loop.exec_()

        self.hide()
        self.senal_tarea_terminada.emit(1)
