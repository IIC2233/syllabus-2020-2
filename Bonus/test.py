# Actividad Bonus IIC2233 2020-2

import wikipedia
import json
from consultas import (
    consulta1, consulta2, consulta3, consulta4, consulta5, consulta6
    )
from consultas import (
    PATRON1, PATRON2, PATRON3, PATRON4, PATRON5, PATRON6
    )


class Test:

    def __init__(self, argumentos, output_esperado, funcion):

        self.argumentos = argumentos
        self.output_esperado = output_esperado
        self.funcion = funcion
        self.resultados = []

    def probar_casos(self):

        self.resultados = []
        print(f"\n{'-' * 16}",
              f"Probando CONSULTA {self.funcion.__name__}",
              f"{'-' * 16}\n")

        # El resultado de cada función debe ser una lista de tuplas,
        # donde cada tupla es (match, inicio, fin)

        for i, (args, output_esperado) in enumerate(zip(
            self.argumentos, self.output_esperado
        )):
            try:
                # Intentamos ejecutar la función a testear para obtener
                # la respuesta
                respuesta = self.funcion(*args)
            except Exception as e:
                # En caso de error, se imprime, se salta al siguiente test,
                # y se agrega un None a los resultados
                print(f"Error al ejecutar función en test #{i}: {e}\n")
                self.resultados.append(None)
                continue

            # Ahora se compara si está correcto
            try:
                # Se compara el resultado con el output esperado en otro método
                correcto = self.comparar(respuesta, output_esperado)
                if correcto:
                    mensaje = f"Respuestas en test #{i} coinciden"
                else:
                    mensaje = f"ERROR: no coinciden respuestas en test #{i}"
                print(mensaje)
            except Exception as e:
                # En caso de error al comparar, se imprime y la respuesta
                # es incorrecta
                print(f"Error al comparar respuestas en test #{i}: {e}")
                correcto = False
            finally:
                # Se guarda el resultado
                self.resultados.append(correcto)
                print()

        # Se imprimen el resumen
        print(f"Casos probados: {len(self.argumentos)}")
        print(f"Correctos: {sum(1 if r is True else 0 for r in self.resultados)}")
        print(f"Incorrectos: {sum(1 if r is False else 0 for r in self.resultados)}")
        print(f"Errores: {sum(1 if r is None else 0 for r in self.resultados)}")

    def comparar(self, respuesta, output_esperado):

        if isinstance(respuesta, list) and isinstance(output_esperado, list):
            if len(respuesta) != len(output_esperado):
                return False

            # Quitamos None para ordenar sin problemas
            respuesta = [e for e in respuesta if e is not None]
            output_esperado = [e for e in output_esperado if e is not None]

            # Comparamos largo nuevamente
            if len(respuesta) != len(output_esperado):
                return False

            # En las listas ignoramos el orden
            return self.comparar(
                tuple(sorted(respuesta)), tuple(sorted(output_esperado))
                )

        elif isinstance(respuesta, tuple) and isinstance(output_esperado, tuple):
            if len(respuesta) != len(output_esperado):
                return False
            return all(
                self.comparar(respuesta[i], output_esperado[i]) for i in range(len(respuesta))
                )
        return respuesta == output_esperado


if __name__ == "__main__":

    textoChile = wikipedia.page("Chile", auto_suggest=False).content

    argumentos_1 = [
        (textoChile, PATRON1)
    ]

    argumentos_2 = [
        (textoChile, PATRON2)
    ]

    argumentos_3 = [
        (textoChile, PATRON3)
    ]

    argumentos_4 = [
        (textoChile, PATRON4)
    ]

    argumentos_5 = [
        (textoChile, PATRON5)
    ]

    argumentos_6 = [
        (textoChile, PATRON6)
    ]

    output_esperado_1 = [
        [
            ('External links', 78875, 78889),
            ('Further reading', 78851, 78866),
            ('References', 78796, 78806),
            ('See also', 78702, 78710),
            ('Culture', 69439, 69446),
            ('Infrastructure', 67426, 67440),
            ('Economy', 57809, 57816),
            ('Demographics', 45267, 45279),
            ('Geography', 33695, 33704),
            ('Government and politics', 21732, 21755),
            ('History', 3859, 3866),
            ('Etymology', 2507, 2516)
        ]
    ]

    output_esperado_2 = [
        [
            ('Citations', 78832, 78841),
            ('Notes', 78816, 78821),
            ('Cultural heritage', 77603, 77620),
            ('Sports', 74389, 74395),
            ('Cinema', 73897, 73903),
            ('Folklore', 73230, 73238),
            ('Cuisine', 72501, 72508),
            ('Literature', 71500, 71510),
            ('Music and dance', 70278, 70293),
            ('Telecommunications', 68659, 68677),
            ('Transport', 67450, 67459),
            ('Tourism', 64356, 64363),
            ('Agriculture', 63209, 63220),
            ('Mineral resources', 62715, 62732),
            ('Health', 56915, 56921),
            ('Education', 55358, 55367),
            ('Languages', 53871, 53880),
            ('Religion', 51074, 51082),
            ('Ancestry and ethnicity', 45801, 45823),
            ('Hydrography', 44238, 44249),
            ('Topography', 39657, 39667),
            ('Biodiversity', 36517, 36529),
            ('Climate', 35970, 35977),
            ('Military', 31458, 31466),
            ('National symbols', 30447, 30463),
            ('Largest cities', 30422, 30436),
            ('Administrative divisions', 29858, 29882),
            ('Border disputes with Peru and Argentina', 27963, 28002),
            ('Foreign relations', 25390, 25407),
            ('21st century', 19331, 19343),
            ('20th century', 11329, 11341),
            ('Independence and nation building', 7936, 7968),
            ('Spanish colonization', 4758, 4778),
            ('Early history', 3876, 3889)
        ]
    ]

    output_esperado_3 = [
        [
            ('Pinochet era (1973–1990)', 16830, 16854),
            ('Flora and fauna', 37068, 37083),
            ('Mythology', 73727, 73736)
        ]
    ]

    output_esperado_4 = [
        [
            ('Etymology', 2520, 3855),
            ('Further reading', 78870, 78871),
            ('See also', 78714, 78792),
            ('External links', 78893, 79342)
        ]
    ]

    output_esperado_5 = [
        [
            ('Early history', 3894, 4753),
            ('Spanish colonization', 4783, 7931),
            ('Independence and nation building', 7973, 11324),
            ('20th century', 11346, 19326),
            ('Foreign relations', 25412, 27958),
            ('Border disputes with Peru and Argentina', 28007, 29853),
            ('Administrative divisions', 29887, 30417),
            ('Largest cities', 30441, 30442),
            ('National symbols', 30468, 31453),
            ('Climate', 35982, 36512),
            ('Biodiversity', 36534, 39652),
            ('Topography', 39672, 44233),
            ('Ancestry and ethnicity', 45828, 51069),
            ('Religion', 51087, 53866),
            ('Languages', 53885, 55353),
            ('Education', 55372, 56910),
            ('Mineral resources', 62737, 63204),
            ('Agriculture', 63225, 64351),
            ('Transport', 67464, 68654),
            ('Music and dance', 70298, 71495),
            ('Literature', 71515, 72496),
            ('Cuisine', 72513, 73225),
            ('Folklore', 73243, 73892),
            ('Cinema', 73908, 74384),
            ('Sports', 74400, 77598),
            ('Notes', 78826, 78827),
            ('21st century', 19348, 21728),
            ('Military', 31471, 33691),
            ('Hydrography', 44254, 45263),
            ('Health', 56926, 57805),
            ('Tourism', 64368, 67422),
            ('Telecommunications', 68682, 69435),
            ('Cultural heritage', 77625, 78698),
            ('Citations', 78846, 78847)
        ]
    ]

    output_esperado_6 = [
        [
            ('20th century', 11346, 19326),
            ('Biodiversity', 36534, 39652),
            ('Folklore', 73243, 73892)
        ]
    ]

    # Prueba cada consulta
    test_1 = Test(argumentos_1, output_esperado_1, consulta1)
    test_1.probar_casos()

    test_2 = Test(argumentos_2, output_esperado_2, consulta2)
    test_2.probar_casos()

    test_3 = Test(argumentos_3, output_esperado_3, consulta3)
    test_3.probar_casos()

    test_4 = Test(argumentos_4, output_esperado_4, consulta4)
    test_4.probar_casos()

    test_5 = Test(argumentos_5, output_esperado_5, consulta5)
    test_5.probar_casos()

    test_6 = Test(argumentos_6, output_esperado_6, consulta6)
    test_6.probar_casos()
