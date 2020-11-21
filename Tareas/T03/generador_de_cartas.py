from random import choices

# -------------------------------------------------------------------------------------------------
#                                       PARÁMETROS
# -------------------------------------------------------------------------------------------------
# Indica la cantidad de tipos de victoria
TIPOS_VICTORIA = 2
# Proporción cartas victoria:monopolio
CANTIDAD_VICTORIA = 10
CANTIDAD_MONOPOLIO = 4

# -------------------------------------------------------------------------------------------------
#                                       FUNCIÓN
# -------------------------------------------------------------------------------------------------


def sacar_cartas(cantidad_cartas):

    '''Función que genera un mazo y selecciona al azar la cantidad de cartas
    indicadas en el input.

    input: cantidad_cartas -> int
    output: lista de tuplas con las cartas -> list(tuple)'''
    mazo = []
    # Cartas de victoria
    for numero in range(1, TIPOS_VICTORIA + 1):
        mazo += [('victoria', str(numero))] * (CANTIDAD_VICTORIA // 2)

    # Cartas de monopolio
    mazo += [('monopolio', '1')] * CANTIDAD_MONOPOLIO
    return choices(mazo, k=cantidad_cartas)


if __name__ == "__main__":
    for i in (0, 1, 5, 20, 100):
        cartas = sacar_cartas(i)
        print(len(cartas), cartas, '\n')
