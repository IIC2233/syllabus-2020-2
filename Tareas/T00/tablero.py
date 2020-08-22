'''
NO MODIFICAR

'''

def print_tablero_con_utf8(tablero_rival, tablero_propio):

    # Se obtienen las dimensiones del tablero
    n = len(tablero_rival)
    m = len(tablero_rival[0])

    # Se generan los nuevos tableros en forma de listas de listas con los nuevos caracteres
    tablero_rival = [['■' if x == ' ' or x == 'B' else x for x in y] for y in tablero_rival]
    tablero_propio = [['■' if x == ' ' else x for x in y] for y in tablero_propio]

    # Se imprimen las letras representando cada columna
    columnas = ' ' * 5
    for indice in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:m]:
        columnas += f' {indice}'

    print(columnas)
    print(' ' * 4 + '┌' + '─' * (2 * m + 1) + '┐')

    # Se generan las filas del mapa rival con sus respectivas celdas
    for indice in range(n):
        fila = ''
        if indice < 10:
            fila += f'  {indice} │'
        else:
            fila += f' {indice} │'

        fila += ' ' + ' '.join(tablero_rival[indice]) + ' │'
        print(fila)
    
    # Se separa el mapa rival con el mapa del jugador
    print(' ' * 4 + '─' + '─' * (2 * m + 1) + '─')

    # Se generan las filas del mapa del jugador con sus respectivas celdas
    for indice in range(n):
        fila = ''
        if indice < 10:
            fila += f'  {indice} │'
        else:
            fila += f' {indice} │'

        fila += ' ' + ' '.join(tablero_propio[indice]) + ' │'
        print(fila)

    print(' ' * 4 + '└' + '─' * (2 * m + 1) + '┘')

    # Se imprimen las últimas letras representando cada columna
    print(columnas)

def print_tablero_sin_utf8(tablero_rival, tablero_propio):

    # Se obtienen las dimensiones del tablero
    n = len(tablero_rival)
    m = len(tablero_rival[0])

    # Se generan los nuevos tableros en forma de listas de listas con los nuevos caracteres
    tablero_rival = [['_' if x == ' ' or x == 'B' else x for x in y] for y in tablero_rival]
    tablero_propio = [['_' if x == ' ' else x for x in y] for y in tablero_propio]

    # Se imprimen las letras representando cada columna
    columnas = ' ' * 4
    for indice in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:m]:
        columnas += f' {indice}'
    print(columnas, '\n')

    # Se generan las filas del mapa rival con sus respectivas celdas
    for indice in range(n):
        fila = ''
        if indice < 10:
            fila += f'  {indice} '
        else:
            fila += f' {indice} '

        fila += ' ' + ' '.join(tablero_rival[indice])
        print(fila)
    print()

    # Se generan las filas del mapa del jugador con sus respectivas celdas
    for indice in range(n):
        fila = ''
        if indice < 10:
            fila += f'  {indice} '
        else:
            fila += f' {indice} '

        fila += ' ' + ' '.join(tablero_propio[indice])
        print(fila)   
    print()

    # Se imprimen las últimas letras representando cada columna
    print(columnas)

'''
Función para imprimir el tablero de juego
Por defecto lleva el utf8 = True
'''

def print_tablero(tablero_rival, tablero_propio, utf8=True):
    if utf8:
        print_tablero_con_utf8(tablero_rival, tablero_propio)
    else:
        print_tablero_sin_utf8(tablero_rival, tablero_propio)
