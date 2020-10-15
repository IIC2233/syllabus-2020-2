from PyQt5.QtCore import QObject, pyqtSignal


class TareaCodigo(QObject):

    senal_nuevo_codigo_actual = pyqtSignal(str)
    senal_resultado_comparacion = pyqtSignal(bool)

    def __init__(self, codigo_correcto):
        """Es el init del backend de la tarea de código. Puedes ignorarlo."""
        super().__init__()
        self.codigo_correcto = codigo_correcto
        self.codigo_actual = ""
        self.terminado = False

    def boton_teclado_clickeado(self, tuple_info):
        """Este método actualiza la pantalla o compara el resultado según
        los botones presionados. Puedes ignorarlo."""
        nombre_boton_clickeado = tuple_info[0]
        numero_boton_clickeado = tuple_info[1]

        if not self.terminado:
            if nombre_boton_clickeado == "KeyNormalButton":
                self.codigo_actual += numero_boton_clickeado
                self.senal_nuevo_codigo_actual.emit(self.codigo_actual)

            elif nombre_boton_clickeado == "KeyDelButton":
                self.codigo_actual = self.codigo_actual[:-1]
                self.senal_nuevo_codigo_actual.emit(self.codigo_actual)

            else:
                self.comparar_codigos()

    # Completar
    def comparar_codigos(self):
        pass
