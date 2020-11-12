import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,\
                          QHBoxLayout, QVBoxLayout, QLineEdit, QGridLayout
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import  Qt
from parametros import ANCHO_VENTANA, ALTO_VENTANA, ANCHO_PELICULA_VP, ALTO_PELICULA_VP, \
                    ANCHO_PELICULA_VF, ALTO_PELICULA_VF, ANCHO_VI, ALTO_VI
from PyQt5 import QtGui                     
import os
import pickle
sys.path.append(os.path.join('..', 'Actividad json'))
from peliculas import  cargar_peliculas

class BotonHover(QPushButton):

    def __init__(self,text,parent=None):
        super().__init__(parent)
        self.setStyleSheet("background:linear-gradient(to bottom, #f9f9f9 5%, #e9e9e9 100%);background-color:#f9f9f9;border-radius:6px;border:1px solid #dcdcdc;color:#666666;font-family:Arial;font-size:15px;font-weight:bold;padding:6px 24px;")
        self.setText(text)

    def enterEvent(self, a0):
        if a0:
            self.setStyleSheet("background:linear-gradient(to bottom, #e9e9e9 5%, #f9f9f9 100%);background-color:#e9e9e9;border-radius:6px;border:1px solid #dcdcdc;color:#666666;font-family:Arial;font-size:15px;font-weight:bold;padding:6px 24px;")

    def leaveEvent(self, a0):
        if a0:
            self.setStyleSheet("background:linear-gradient(to bottom, #f9f9f9 5%, #e9e9e9 100%);background-color:#f9f9f9;border-radius:6px;border:1px solid #dcdcdc;color:#666666;font-family:Arial;font-size:15px;font-weight:bold;padding:6px 24px;")


class LabelPeliculas(QLabel):

    clickeado= pyqtSignal(int, str)

    def __init__(self, parent, path, info, indice, *args):
        super().__init__(parent, *args)
        self.info = info
        self.indice = indice
        self.path = path
        self.setWindowIcon(QtGui.QIcon('icon.png')) 

        pixeles = QPixmap(path)
        pixel_chico = pixeles.scaled(ANCHO_PELICULA_VP, ALTO_PELICULA_VP)
        self.setPixmap(pixel_chico)


    def mousePressEvent(self, event):
        self.clickeado.emit(self.indice, self.path)

class VentanaInicial(QWidget):

    senal_abrir_ventana_peliculas = pyqtSignal(str, list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.setWindowIcon(QtGui.QIcon('icon.png')) 

    def init_gui(self):

        self.setGeometry(200, 200, ANCHO_VENTANA, ALTO_VENTANA)
        self.boton_1 = BotonHover('Ponagale weno')
        self.boton_1.clicked.connect(self.entrar)
        self.usuario = QLineEdit()
        self.usuario.setPlaceholderText('Ingresa tu usuario')
        self.usuario.setStyleSheet("background-color:white")
        self.clave = QLineEdit()
        self.clave.setPlaceholderText('Ingresa tu clave')
        self.clave.setStyleSheet("background-color:white")
        self.label = QLabel('Bienvenido a DCCine! :D')
        self.label.setFont(QFont('Times', 30))
        self.label.setStyleSheet("color:white")

        self.logo = QLabel()
        self.logo.resize(300, 100)
        pixmap = QPixmap('logo2.jpeg')
        self.logo.setPixmap(pixmap)
        self.logo.setScaledContents(True)
        self.setStyleSheet("background-color:black")

        self.setWindowTitle('DCCine')

        vbox1 =  QVBoxLayout()
        vbox1.addStretch(1)
        vbox1.addWidget(self.usuario)
        vbox1.addStretch(1)
        vbox1.addWidget(self.clave)
        vbox1.addStretch(1)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addLayout(vbox1)
        hbox1.addStretch(1)
        hbox1.addWidget(self.boton_1)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.label)
        hbox2.addStretch(1)

        vboxT =  QVBoxLayout()
        vboxT.addStretch(1)
        vboxT.addWidget(self.logo)
        vboxT.addStretch(1)
        vboxT.addLayout(hbox2)
        vboxT.addStretch(1)
        vboxT.addLayout(hbox1)
        vboxT.addStretch(1)



        self.setLayout(vboxT)


        self.show()
    def keyPressEvent(self, a0):
        if a0.key() == 16777220:
            self.entrar()
    def entrar(self):


        with open('datos_secretos.bin', 'rb') as archivo:
            usuarios, paths = pickle.load(archivo)

        if self.usuario.text() in usuarios.keys():
            if usuarios[self.usuario.text()][0] ==  self.clave.text():
                self.hide()
                self.senal_abrir_ventana_peliculas.emit(self.usuario.text(),
                usuarios[self.usuario.text()][1])
            else:
                self.label.setText('Usuario  o Clave incorrecto. Intente denuevo')
        else:
            self.label.setText('Usuario  o Clave incorrecto. Intente denuevo')


class VentanaPeliculas(QWidget):

    senal_abrir_ventana_final = pyqtSignal(list, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowIcon(QtGui.QIcon('icon.png')) 
        self.imagenes = []
        self.peliculas = dict() #nombre de pelicula con valores la info [] de aquellas

    def init_gui(self, usuario, lista_peliculas):

        with open('datos_secretos.bin', 'rb') as archivo:
            usuarios, paths = pickle.load(archivo)

        self.setGeometry(200, 200, ANCHO_VENTANA, ALTO_VENTANA)
        self.setStyleSheet("background-color:black")
        posiciones = [(i, j) for i in range(3) for j in range(5)]
        self.grilla = QGridLayout()
        self.titulo = QLabel('Menu de Peliculas')
        self.titulo.setFont(QFont('Times', 30))
        self.titulo.setStyleSheet("color:white")
        self.usuario = QLabel(f'Usuario: {usuario}')
        self.usuario.setFont(QFont('Times', 30))
        self.usuario.setStyleSheet("color:white")
        self.paths_peliculas = [os.path.join('..', 'Actividad bytes', 'caratulas', paths[indice]) for indice in lista_peliculas]
        info = cargar_peliculas(os.path.join('..', 'Actividad json', 'peliculas.json')) #None si no han completado JSON

        #nuevo diccionario: {indice: [nombre, Director, duracion, puntuacion]}
        if info:
            info_final = dict()
            for nombre in info.keys():
                indice, director, duracion, puntuacion = info[nombre]
                info_final[indice] = [nombre, director, duracion, puntuacion]
        else:
            info_final  = None


        for posicion, indice in zip(posiciones, lista_peliculas):
            if os.path.exists(os.path.join('..', 'Actividad bytes', 'caratulas', paths[indice])):
                path = os.path.join('..', 'Actividad bytes', 'caratulas', paths[indice])
            else:
                path = 'chayanne.jpg'
            if info_final:
                info_pel = info_final[int(indice)]
            else:
                info_pel = ['','','','']
            label = LabelPeliculas(self, path, info_pel, len(self.imagenes))
            label.clickeado.connect(self.recibir_click)
            self.imagenes.append(label)
            self.grilla.addWidget(label, *posicion)



        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.titulo)
        hbox.addStretch(1)
        hbox.addWidget(self.usuario)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addLayout(self.grilla)
        vbox.addStretch(1)


        self.setLayout(vbox)
        self.setWindowTitle('DCCine')
        self.show()

    def recibir_click(self, indice):
        self.senal_abrir_ventana_final.emit(self.imagenes[indice].info, self.imagenes[indice].path)
        self.hide()

    def reaparecer(self):
        self.show()

class VentanaFinal(QWidget):

    senal_volver = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('icon.png')) 
        self.label = None
        self.duracion = 0
        self.puntiacion = 0
        self.director = 0
        self.creado = False
        self.dic_peliculas =  cargar_peliculas(os.path.join('..', 'Actividad json', 'peliculas.json'))

    def gui_init(self, info, path): #info es una lista
        self.setGeometry(200, 200, ANCHO_VENTANA, ALTO_VENTANA)
        self.setWindowTitle('Menu de Pelicula')
        self.setStyleSheet("background-color:black")


        #abrimos info y separamos los componentes:
        if info:
            self.titulo = info[0]
            self.director = info[1]
            self.duracion = info[2]
            self.puntuacion = info[3]
        else:
            self.titulo = ''
            self.director = ''
            self.duracion = ''
            self.puntuacion = '1'

        if self.creado:
            self.reemplazar_elementos(path, self.titulo, self.director, self.duracion, self.puntuacion)
            return
        self.creado =  True

        self.boton = BotonHover('Volver')
        self.boton.clicked.connect(self.volver)
        self.label_titulo = QLabel(f'Titulo: {self.titulo}')
        self.label_titulo.setFont(QFont('Times', 20))
        self.label_titulo.setStyleSheet("color:white")
        self.label_director = QLabel(f'Director: {self.director}')
        self.label_director.setStyleSheet("color:white")
        self.label_director.setFont(QFont('Times', 20))
        self.label_duracion = QLabel(f'Duración:  {self.duracion}')
        self.label_duracion.setFont(QFont('Times', 20))
        self.label_duracion.setStyleSheet("color:white")
        self.label_puntuacion = QLabel(f'Puntuación: {self.puntuacion}/10')
        self.label_puntuacion.setFont(QFont('Times', 20))
        self.label_puntuacion.setStyleSheet("color:white")


        vbox1 = QVBoxLayout()
        vbox1.addStretch(1)
        vbox1.addWidget(self.label_titulo)
        vbox1.addStretch(1)
        vbox1.addWidget(self.label_director)
        vbox1.addStretch(1)
        vbox1.addWidget(self.label_duracion)
        vbox1.addStretch(1)
        vbox1.addWidget(self.label_puntuacion)
        vbox1.addStretch(1)

        #creamos la imagen:
        self.label = QLabel(self)
        pixeles = QPixmap(path)
        pixel_chico = pixeles.scaled(ANCHO_PELICULA_VF, ALTO_PELICULA_VF)
        self.label.setPixmap(pixel_chico)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.label)
        hbox.addStretch(1)
        hbox.addLayout(vbox1)
        hbox.addStretch(1)

        vbox2 = QVBoxLayout()
        vbox2.addStretch(1)
        vbox2.addLayout(hbox)
        vbox2.addStretch(1)
        vbox2.addWidget(self.boton)
        vbox2.addStretch(1)

        self.hbox2 = QHBoxLayout()
        self.hbox2.addStretch(1)
        self.hbox2.addLayout(vbox2)
        self.hbox2.addStretch(1)


        self.setLayout(self.hbox2)
        self.setWindowTitle('DCCine')
        self.show()

    def reemplazar_elementos(self, path, titulo, director, duracion, puntos):
        self.label_duracion.setText(f'Duración:  {duracion}')
        self.label_duracion.setStyleSheet("color:white")
        self.label_titulo.setText(f'Titulo: {titulo}')
        self.label_titulo.setStyleSheet("color:white")
        self.label_puntuacion.setText(f'Puntuación: {puntos}/10')
        self.label_puntuacion.setStyleSheet("color:white")
        self.label_director.setText(f'Director: {director}')
        self.label_director.setStyleSheet("color:white")
        pixeles = QPixmap(path)
        pixel_chico = pixeles.scaled(300, 360)
        self.label.setPixmap(pixel_chico)

        self.show()

    def volver(self):
        self.hide()
        self.senal_volver.emit()

if __name__ == '__main__':
    peliculas = cargar_peliculas(os.path.join('..', 'Actividad json', 'peliculas.json'))
    print(peliculas)
    print(type(peliculas))
