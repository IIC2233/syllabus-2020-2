import sys
from ventanas import VentanaInicial, VentanaPeliculas, VentanaFinal
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])
    ventana_inicial = VentanaInicial()
    ventana_peliculas = VentanaPeliculas()
    ventana_final = VentanaFinal()

    ventana_inicial.senal_abrir_ventana_peliculas.connect(ventana_peliculas.init_gui)
    ventana_peliculas.senal_abrir_ventana_final.connect(ventana_final.gui_init)
    ventana_final.senal_volver.connect(ventana_peliculas.reaparecer)
    sys.exit(app.exec_())
