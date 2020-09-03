from estudiantes import Programago
import random
import parametros as p
from abc import ABC, abstractmethod


class Jugador:
    def __init__(self, nombre, saludo, numero_polera):

        # Completar

        self.nerviosismo = None
        self.velocidad = None
        self.equilibrio = None
        self.numero_polera = numero_polera
        self.saludo = saludo
        self.nombre = nombre


class Buscador:
    def __init__(self, nombre, saludo, numero_polera):

        # Completar

        self.asignar_cualidades()

    def asignar_cualidades(self):
        self.nerviosismo = random.uniform(p.NERVIOSISMO_BUSCADOR_MIN, p.NERVIOSISMO_BUSCADOR_MAX)
        self.velocidad = random.uniform(p.VELOCIDAD_BUSCADOR_MIN, p.VELOCIDAD_BUSCADOR_MAX)
        self.equilibrio = random.uniform(p.EQUILIBRIO_BUSCADOR_MIN, p.EQUILIBRIO_BUSCADOR_MAX)

    def competir(self):
        pass


class Golpeador:
    def __init__(self, nombre, saludo, numero_polera):

        # Completar

        self.asignar_cualidades()

    def asignar_cualidades(self):
        self.nerviosismo = random.uniform(p.NERVIOSISMO_GOLPEADOR_MIN, p.NERVIOSISMO_GOLPEADOR_MAX)
        self.velocidad = random.uniform(p.VELOCIDAD_GOLPEADOR_MIN, p.VELOCIDAD_GOLPEADOR_MAX)
        self.equilibrio = random.uniform(p.EQUILIBRIO_GOLPEADOR_MIN, p.EQUILIBRIO_GOLPEADOR_MAX)

    def competir(self):
        pass


class Cazador:
    def __init__(self, nombre, saludo, numero_polera):
        self.asignar_cualidades()

        # Completar

    def asignar_cualidades(self):
        self.nerviosismo = random.uniform(p.NERVIOSISMO_CAZADOR_MIN, p.NERVIOSISMO_CAZADOR_MAX)
        self.velocidad = random.uniform(p.VELOCIDAD_CAZADOR_MIN, p.VELOCIDAD_CAZADOR_MAX)
        self.equilibrio = random.uniform(p.EQUILIBRIO_CAZADOR_MIN, p.EQUILIBRIO_CAZADOR_MAX)

    def competir(self):
        pass


if __name__ == '__main__':
    # Instancias de prueba
    buscador = Buscador('Pruebinelda', 'probando la clase Buscador', '42')
    golpeador = Golpeador('Pruebardo', 'probando la clase Golpeador', 'Pi')
    cazador = Cazador('Pruebina', 'probando la clase Cazador', 'e')
    # Pruebas de atributos
    print('Soy ' + buscador.nombre + ' y estoy ' + buscador.saludo + ', mi numero de polera es ' + buscador.numero_polera)
    print('Soy ' + golpeador.nombre + ' y estoy ' + golpeador.saludo + ', mi numero de polera es ' + golpeador.numero_polera)
    print('Soy ' + cazador.nombre + ' y estoy ' + cazador.saludo + ', mi numero de polera es ' + cazador.numero_polera)
    # Pruebas de clases/subclase
    if isinstance(buscador, Jugador):
        print('Buscador hereda correctamente de Jugador!')
    if isinstance(golpeador, Jugador):
        print('Golpeador hereda correctamente de Jugador!')
    if isinstance(cazador, Jugador):
        print('Cazador hereda correctamente de Jugador!')
