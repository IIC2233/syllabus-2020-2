# Basado en https://variable-scope.com/posts/hexagon-tilings-with-python

import math

# -------------------------------------------------------------------------------------------------
#                                       GENERADOR DE GRILLA
# -------------------------------------------------------------------------------------------------


class  GeneradorGrillaHexagonal:

    '''
    Contiene los métodos y atributos necesarios para generar una grilla hexagonal.

    Atributos:
        tamaño_arista : int
            tamaño en pixeles que tendrán las aristas de la grilla
        padding_interior : int
            corresponde a un padding interior para que la grilla muestre hexágonos completos
        ancho_columna : int
            property que almacena el ancho en pixeles que tendrá cada columna de la grilla
        alto_fila : int
            property que almacena el alto en pixeles que tendrá cada fila de la grilla
    '''

    def __init__(self, tamaño_arista):

        '''
        Constructor para la clase GeneradorGrillaHexagonal.

        Parámetros:
            tamaño_arista (int) : tamaño en pixeles que tendrán las aristas de la grilla.
        '''

        self.tamaño_arista = tamaño_arista
        self.padding_interior = tamaño_arista/2

    @property
    def ancho_columna(self):
        return self.tamaño_arista * 3

    @property
    def alto_fila(self):
        return math.sin(math.pi / 3) * self.tamaño_arista

    def generar_hexagono(self, fila, col, padding_x, padding_y):
        '''
        A partir de una posicion en la grilla, genera un hexágono en dicha posición.

        Parametros:
            fila (int) : número de fila en que se ubica.
            col (int) : número de columna en que se ubica.
            padding_x (int) : cantidad de pixeles horizontales que se debe trasladar el hexagono.
            padding_y (int) : cantidad de pixeles verticales que se debe trasladar el hexagono
        
        Retorna:
            Generador que entrega las coordenadas (x, y) en que se ubica cada vértice del hexagono.
        '''
        x = ((col + 0.5 * (fila % 2)) * self.ancho_columna) + self.padding_interior
        y = fila * self.alto_fila

        for angulo in range(0, 360, 60):
            x += math.cos(math.radians(angulo)) * self.tamaño_arista
            y += math.sin(math.radians(angulo)) * self.tamaño_arista
            yield (round(round(x,2)) + padding_x, round(round(y,2)) + padding_y)
    
    def generar_grilla(self, dimensiones, padding_x, padding_y):
        '''
        A partir de la cantidad de filas y columnas que tendrá el mapa, genera las posiciones en que deberá
        ir cada nodo en la interfaz.

        Parametros:
            dimensiones (list) : lista de la forma [fila, columna], la cual indica la cantidad de filas y columnas que tendrá el mapa
            padding_x (int) : cantidad de pixeles horizontales que se debe trasladar el mapa.
            padding_y (int) : cantidad de pixeles verticales que se debe trasladar el mapa.
        
        Retorna:
            id_vertices(dict) : diccionario cuyas llaves son los ID de los nodos, y valores corresponden a una tupla (x, y)
            , que representa la posición en la interfaz en donde debe ubicarse cada nodo.
        ''' 
        vertices_grilla = set()
        for fila_aux in range(dimensiones[0]):
            for col_aux in range(dimensiones[1]):
                hexagono = list(self.generar_hexagono(fila_aux, col_aux, padding_x, padding_y))
                for vertice in hexagono:
                    vertices_grilla.add(vertice)
        
        vertices_grilla = list(vertices_grilla)
        vertices_grilla.sort(key = lambda x: (x[1], x[0]))

        id_vertices = {}
        for punto in enumerate(vertices_grilla):
            id_vertices[str(punto[0])] = punto[1]

        return id_vertices
