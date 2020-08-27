from entidades import Criatura, Entrenador
from batalla import BatallasCriaturas
from cargar_datos import (cargar_criaturas, cargar_rivales, crear_jugador)


if __name__ == "__main__":
    rivales = cargar_rivales("rivales.csv")
    nombre = input("Por favor, ingresa tu nombre de entrenador: ")
    jugador = crear_jugador(nombre)
    batalla = BatallasCriaturas(jugador, rivales)
    batalla.ejecutar_simulación()
    