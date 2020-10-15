from PyQt5.QtCore import QObject, pyqtSignal


class Inicial(QObject):
    """Este es el backend del menú de inicio. Puedes ignorarlo"""

    senal_resultado_comparacion = pyqtSignal(bool)

    def __init__(self, lista_codigos):
        super().__init__()
        self.lista_codigos = lista_codigos

    def comparar_codigo(self, codigo):
        if codigo not in self.lista_codigos:
            self.senal_resultado_comparacion.emit(False)
        else:
            self.senal_resultado_comparacion.emit(True)


class Principal(QObject):
    """Este es backend del menú principal. Puedes ignorarlo"""
    senal_tarea_terminada = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.tareas_terminadas = 0

    def tarea_terminada(self, numero_tarea):
        self.tareas_terminadas += 1
        self.senal_tarea_terminada.emit((numero_tarea, self.tareas_terminadas))
