# Se pueden importar los parámetros de varias formas diferentes:
# Descomenten cada parte para probar que funciona!

# Forma 1:

# import parametros

# Para utilizar los parámetros dentro de este archivo, tendríamos
# que llamarlo de la forma:
# variable = parametros.NUM_BARCOS
# print(variable)


# Forma 2:
# import parametros as nombre_personalizado

# En lugar de escribir parametros.CONSTANTE, escribimos
# nombre_personalizado.CONSTANTE, por ejemplo:
# variable = nombre_personalizado.NUM_BARCOS
# print(variable)


# Forma 3:
#from parametros import CONSTANTE

# Con esta forma, debemos mencionar cada constante que queramos importar
# por ejemplo:
#from parametros import NUM_BARCOS
# Luego, lo llamaríamos así:
# variable = NUM_BARCOS
# print(variable)

# Finalmente, un ejemplo de cómo usar la función print_tablero():
from tablero import print_tablero

tablero_enemigo = [['X', ' ', 'X'],[' ', ' ', ' '],['F', ' ', ' ']]
tablero_propio = [['B', ' ', ' '],['B', ' ', ' '],[' ', ' ', 'B']]
print_tablero(tablero_enemigo, tablero_propio)
