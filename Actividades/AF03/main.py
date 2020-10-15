import sys

from PyQt5.QtWidgets import QApplication

import parametros as p
from backend.logica_ventanas import Inicial, Principal
from backend.tarea_codigo import TareaCodigo
from frontend.tarea_codigo import VentanaTareaCodigo
from frontend.tarea_descarga import VentanaTareaDescarga
from frontend.ventana_inicial import VentanaInicial
from frontend.ventana_principal import VentanaPrincipal


def hook(type_error, traceback):
    print(type_error)
    print(traceback)


if __name__ == '__main__':
    # No modificar ->
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)

    # Ventana inicio (front-end)
    ventana_inicio = VentanaInicial(p.ANCHO, p.ALTO, p.RUTA_LOGO)
    # Ventana inicio (back-end)
    logica_inicio = Inicial(p.LISTA_CODIGOS)
    # Ventana inicio (señales)
    ventana_inicio.senal_comparar_codigo.connect(logica_inicio.comparar_codigo)
    logica_inicio.senal_resultado_comparacion.connect(ventana_inicio.recibir_comparacion)

    # Ventana principal (front-end)
    ventana_principal = VentanaPrincipal(p.ANCHO, p.ALTO, p.ALTURA_BOTONES_MENUS, p.DURACION_GIF)
    # Ventana principal (back-end)
    logica_principal = Principal()
    # Ventana principal (señales)
    ventana_inicio.senal_abrir_menu_principal.connect(ventana_principal.senal_abrir_menu_principal)
    logica_principal.senal_tarea_terminada.connect(ventana_principal.tarea_terminada)

    # Tarea 1 (front-end)
    ventana_tarea_descarga = VentanaTareaDescarga(
        p.ANCHO, p.ALTO, p.DURACION_TAREA_DESCARGA, p.DURACION_FIN_TAREA,
    )

    # Tarea 2 (front-end)
    ventana_tarea_codigo = VentanaTareaCodigo(p.ANCHO, p.ALTO, p.CODIGO_TAREA, p.DURACION_FIN_TAREA)
    # Tarea 2 (back-end)
    logica_tarea_codigo = TareaCodigo(p.CODIGO_TAREA)
    # <-

    # Completar


    # No modificar ->
    ventana_principal.senal_abrir_tarea_descarga = ventana_tarea_descarga.senal_abrir_tarea
    ventana_tarea_descarga.senal_tarea_terminada.connect(logica_principal.tarea_terminada)

    ventana_principal.senal_abrir_tarea_codigo = ventana_tarea_codigo.senal_abrir_tarea
    ventana_tarea_codigo.senal_tarea_terminada.connect(logica_principal.tarea_terminada)

    ventana_inicio.show()
    app.exec()
    # <-
