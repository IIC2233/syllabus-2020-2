## Evaluación de recuperación IIC2233 2020-2

import pyrematch as re

## -------------------------------------------------------------------
## DEFINIR AQUI LOS PATRONES PARA CONSTRUIR CADA EXPRESION REGULAR
## NO CAMBIAR LOS NOMBRES DE LAS VARIABLES
SOLUCION1 = "(^|\n)== !title{[^=]+} =="
SOLUCION2 = "(^|\n)=== !subtitle{[^=]+} ==="
SOLUCION3 = "(^|\n)==== !subsubtitle{[^=]+} ====\n!content{[^=]*}((\n=)|$)"
SOLUCION4 = "(^|\n)== !title{[^=]*} ==\n!content{[^=]*}(\n== |$)"
SOLUCION5 = "(^|\n)=== !subtitle{[^=]+} ===\n!content{([^=]|(====))*}((\n== )|(\n=== )|^)"
SOLUCION6 = "=== !subtitle{[^=]+} ===\n!content{([^=]|(====))*====([^=]|(====))*}((\n== )|(\n=== )|$)"



## -------------------------------------------------------------------
## Complete a continuación el código de cada consulta.
## Cada consulta recibe el patrón correspondiente para construir la expresión regular, y el texto sobre el cual se aplicará.
## Cada consulta debe retornar una lista de tuplas, donde cada tupla contiene el match encontrado, su posición de inicio y su posición de término.


## CONSULTA 1
def solucion1(texto, patron):
    regex = re.compile(patron)
    resultado = []
    for match in regex.finditer(texto):
        tupla = (match.group('title'), match.start('title'), match.end('title'))
        resultado.append(tupla)
    return resultado


## CONSULTA 2
def solucion2(texto, patron):
    regex = re.compile(patron)
    resultado = []
    for match in regex.finditer(texto):
        tupla = (match.group('subtitle'), match.start('subtitle'), match.end('subtitle'))
        resultado.append(tupla)
    return resultado


## CONSULTA 3
def solucion3(texto, patron):
    regex = re.compile(patron)
    resultado = []
    for match in regex.finditer(texto):
        tupla = (match.group('subsubtitle'), match.start('subsubtitle'), match.end('subsubtitle'))
        resultado.append(tupla)
    return resultado

## CONSULTA 4
def solucion4(texto, patron):
    regex = re.compile(patron)
    resultado = []
    for match in regex.finditer(texto):
        tupla = (match.group('title'), match.start('content'), match.end('content'))
        resultado.append(tupla)
    return resultado

## CONSULTA 5
def solucion5(texto, patron):
    regex = re.compile(patron)
    resultado = []
    for match in regex.finditer(texto):
        tupla = (match.group('subtitle'), match.start('content'), match.end('content'))
        resultado.append(tupla)
    return resultado

## CONSULTA 6
def solucion6(texto, patron):
    regex = re.compile(patron)
    resultado = []
    for match in regex.finditer(texto):
        tupla = (match.group('subtitle'), match.start('content'), match.end('content'))
        resultado.append(tupla)
    return resultado
