from estudiantes import EstudianteGryffindor, EstudianteSlytherin
from jugadores import Buscador, Golpeador, Cazador


class CazadorGryffindor:

    # Completar

    def __init__(self, nombre, saludo, numero_polera):
        pass

    def celebrar(self):
        print(self.nombre + ": Lo logramos equipo!")

    def competir(self):
        pass


class GolpeadorGryffindor:

    # Completar

    def __init__(self, nombre, saludo, numero_polera):
        pass

    def celebrar(self):
        print(self.nombre + ": Bien jugado chiques!")

    def competir(self):
        pass


class BuscadorGryffindor:

    # Completar

    def __init__(self, nombre, saludo, numero_polera):
        pass

    def celebrar(self):
        print(self.nombre + ": Sii! Lo logré gracias a mi equipo!")

    def competir(self):
        pass


class CazadorSlytherin:

    # Completar

    def __init__(self, nombre, saludo, numero_polera):
        pass

    def celebrar(self):
        print(self.nombre + ": Lo logré solito!")

    def competir(self):
        pass


class GolpeadorSlytherin:

    # Completar

    def __init__(self, nombre, saludo, numero_polera):
        pass

    def celebrar(self):
        print(self.nombre + ": Soy el mejor, malditos!")

    def competir(self):
        pass


class BuscadorSlytherin:

    # Completar

    def __init__(self, nombre, saludo, numero_polera):
        pass

    def celebrar(self):
        print(self.nombre + ": No son nada para mi")

    def competir(self):
        pass


if __name__ == '__main__':
    # Instancias de prueba
    buscador_gryf = BuscadorGryffindor('Pruebinelda', 'probando la clase BuscadorGryffindor', '42')
    golpeador_gryf = GolpeadorGryffindor('Pruebardo', 'probando la clase GolpeadorGryffindor', 'Pi')
    cazador_gryf = CazadorGryffindor('Pruebina', 'probando la clase CazadorGryffindor', 'e')
    buscador_slyth = BuscadorSlytherin('Pruebarmaldo', 'probando la clase BuscadorSlytherin', 'uwu')
    golpeador_slyth = GolpeadorSlytherin('Pruebincio Jr', 'probando la clase GolpeadorSlytherin', '42 denuevo')
    cazador_slyth = CazadorSlytherin('Pruebanessa', 'probando la clase CazadorSlytherin', ' (っ´ω`c)♡')
    # Pruebas de atributos
    print('Soy ' + buscador_gryf.nombre + ' y estoy ' + buscador_gryf.saludo + ', mi numero de polera es ' + buscador_gryf.numero_polera)
    print('Soy ' + golpeador_gryf.nombre + ' y estoy ' + golpeador_gryf.saludo + ', mi numero de polera es ' + golpeador_gryf.numero_polera)
    print('Soy ' + cazador_gryf.nombre + ' y estoy ' + cazador_gryf.saludo + ', mi numero de polera es ' + cazador_gryf.numero_polera)
    print('Soy ' + buscador_slyth.nombre + ' y estoy ' + buscador_slyth.saludo + ', mi numero de polera es ' + buscador_slyth.numero_polera)
    print('Soy ' + golpeador_slyth.nombre + ' y estoy ' + golpeador_slyth.saludo + ', mi numero de polera es ' + golpeador_slyth.numero_polera)
    print('Soy ' + cazador_slyth.nombre + ' y estoy ' + cazador_slyth.saludo + ', mi numero de polera es ' + cazador_slyth.numero_polera)
    # Pruebas de clases/subclase
    if isinstance(buscador_gryf, EstudianteGryffindor):
        print('BuscadorGryffindor hereda correctamente de EstudianteGryffindor!')
    if isinstance(golpeador_gryf, EstudianteGryffindor):
        print('GolpeadorGryffindor hereda correctamente de EstudianteGryffindor!')
    if isinstance(cazador_gryf, EstudianteGryffindor):
        print('CazadorGryffindor hereda correctamente de EstudianteGryffindor!')
    if isinstance(buscador_slyth, EstudianteSlytherin):
        print('BuscadorSlytherin hereda correctamente de EstudianteSlytherin!')
    if isinstance(golpeador_slyth, EstudianteSlytherin):
        print('GolpeadorSlytherin hereda correctamente de EstudianteSlytherin!')
    if isinstance(cazador_slyth, EstudianteSlytherin):
        print('CazadorSlytherin hereda correctamente de EstudianteSlytherin!')
    if isinstance(buscador_gryf, Buscador):
        print('BuscadorGryffindor hereda correctamente de Buscador!')
    if isinstance(golpeador_gryf, Golpeador):
        print('GolpeadorGryffindor hereda correctamente de Golpeador!')
    if isinstance(cazador_gryf, Cazador):
        print('CazadorGryffindor hereda correctamente de Cazador!')
    if isinstance(buscador_slyth, Buscador):
        print('BuscadorSlytherin hereda correctamente de Buscador!')
    if isinstance(golpeador_slyth, Golpeador):
        print('GolpeadorSlytherin hereda correctamente de Golpeador!')
    if isinstance(cazador_slyth, Cazador):
        print('CazadorSlytherin hereda correctamente de Cazador!')
