# Actividad Bonus IIC2233 2020=2

import wikipedia
import json
from consultas import (
    consulta1, consulta2, consulta3, consulta4, consulta5, consulta6
    )
from consultas import (
    PATRON1, PATRON2, PATRON3, PATRON4, PATRON5, PATRON6
    )

import os.path
import os

# Páginas de wikipedia a utilizar como tests
TEXTOS_WIKIPEDIA = ["Chile", "Argentina", "Peru", "Brazil",
                    "Colombia", "United States", "France", "China"]

# Offset máximo permitido para las respuestas de los alumnos
# (pensando en whitespaces, puntos finales, etc.)
OFFSET_PERMITIDO = 10

# Path a los dumps de wikipedia con tal de evitar tiempos de carga
WIKI_DUMPS_DIR = os.path.abspath('wiki')

# Crear un archivo con las respuestas esperadas de cada página de wikipedia
# el archivo estará en $WIKI_DUMPS_DIR/solution_dump.txt
SOLUTION_DUMP = False

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
        probados = len(self.argumentos)
        correctos = sum(1 if r is True else 0 for r in self.resultados)
        incorrectos = sum(1 if r is False else 0 for r in self.resultados)
        errores = sum(1 if r is None else 0 for r in self.resultados)
        if correctos == probados:
            puntos = 1.0
        elif correctos >= 0.75*probados:
            puntos = 0.5
        else:
            puntos = 0

        print(f"Casos probados: {probados}")
        print(f"Correctos: {correctos}")
        print(f"Incorrectos: {incorrectos}")
        print(f"Errores: {errores}")
        print(f"Puntos consulta {self.funcion.__name__}: {puntos}")

        return puntos

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

        elif isinstance(respuesta, str) and isinstance(output_esperado, str):
            # Ignorar whitespace
            return respuesta.strip() == output_esperado.strip()

        elif isinstance(respuesta, int) and isinstance(output_esperado, int):
            # Permitir offset
            return abs(respuesta - output_esperado) <= OFFSET_PERMITIDO

        return respuesta == output_esperado



if __name__ == "__main__":

    from solucion import (
        SOLUCION1, SOLUCION2, SOLUCION3, SOLUCION4, SOLUCION5, SOLUCION6
    )

    from solucion import (
        solucion1, solucion2, solucion3, solucion4, solucion5, solucion6
    )

    argumentos_1 = []
    argumentos_2 = []
    argumentos_3 = []
    argumentos_4 = []
    argumentos_5 = []
    argumentos_6 = []

    output_esperado_1 = []
    output_esperado_2 = []
    output_esperado_3 = []
    output_esperado_4 = []
    output_esperado_5 = []
    output_esperado_6 = []


    if not os.path.isdir(WIKI_DUMPS_DIR):
        os.mkdir(WIKI_DUMPS_DIR)

    for wiki_page in TEXTOS_WIKIPEDIA:

        wiki_dump_path = os.path.join(WIKI_DUMPS_DIR, f"{wiki_page}.txt")

        try:
            with open(wiki_dump_path) as dmp_file:
                texto = dmp_file.read()
        except IOError:
            print(f"Cargando wiki: \"{wiki_page}\"...")
            texto = wikipedia.page(wiki_page, auto_suggest=False).content
            with open(wiki_dump_path, 'w') as dmp_file:
                dmp_file.write(texto)

        argumentos_1.append((texto, PATRON1))
        argumentos_2.append((texto, PATRON2))
        argumentos_3.append((texto, PATRON3))
        argumentos_4.append((texto, PATRON4))
        argumentos_5.append((texto, PATRON5))
        argumentos_6.append((texto, PATRON6))

        output_esperado_1.append(solucion1(texto, SOLUCION1))
        output_esperado_2.append(solucion2(texto, SOLUCION2))
        output_esperado_3.append(solucion3(texto, SOLUCION3))
        output_esperado_4.append(solucion4(texto, SOLUCION4))
        output_esperado_5.append(solucion5(texto, SOLUCION5))
        output_esperado_6.append(solucion6(texto, SOLUCION6))


    # Prueba cada consulta
    test_1 = Test(argumentos_1, output_esperado_1, consulta1)
    puntos_1 = test_1.probar_casos()

    test_2 = Test(argumentos_2, output_esperado_2, consulta2)
    puntos_2 = test_2.probar_casos()

    test_3 = Test(argumentos_3, output_esperado_3, consulta3)
    puntos_3 = test_3.probar_casos()

    test_4 = Test(argumentos_4, output_esperado_4, consulta4)
    puntos_4 = test_4.probar_casos()

    test_5 = Test(argumentos_5, output_esperado_5, consulta5)
    puntos_5 = test_5.probar_casos()

    test_6 = Test(argumentos_6, output_esperado_6, consulta6)
    puntos_6 = test_6.probar_casos()

    if SOLUTION_DUMP:
        solution_dump = ""

        outputs_esperados = [
            output_esperado_1,
            output_esperado_2,
            output_esperado_3,
            output_esperado_4,
            output_esperado_5,
            output_esperado_6
        ]

        for i, wiki_page in enumerate(TEXTOS_WIKIPEDIA):
            solution_dump += f"{'=' * 16} WIKI: \"{wiki_page}\" {'=' * 16}\n\n"

            for j, output_esperado in enumerate(outputs_esperados):
                solution_dump += f"{'-' * 8} query {j} {'-' * 8}\n"

                for t in output_esperado[i]:
                    solution_dump += str(t) + '\n'

                solution_dump += '\n'
        solution_dump += '\n'

        with open(os.path.join(WIKI_DUMPS_DIR, 'solution_dump.txt'), 'w') as dmp:
            dmp.write(solution_dump)

    # Entregar el resultado total?
    print(f"\n{'-' * 16}",
            f"Puntos por CONSULTA",
            f"{'-' * 16}\n")
    print(f"Consulta1: {puntos_1}")
    print(f"Consulta2: {puntos_2}")
    print(f"Consulta3: {puntos_3}")
    print(f"Consulta4: {puntos_4}")
    print(f"Consulta5: {puntos_5}")
    print(f"Consulta6: {puntos_6}")
    puntos_totales = puntos_1 + puntos_2 + puntos_3 + puntos_4 + puntos_5 + puntos_6
    print(f"TOTAL: {puntos_totales} / 6.0\n")
    output = f"{puntos_1};{puntos_2};{puntos_3};{puntos_4};{puntos_5};{puntos_6};{puntos_totales}"

