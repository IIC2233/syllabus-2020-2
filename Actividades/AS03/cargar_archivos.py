import os


def cargar_aeropuertos(ruta):
    with open(os.path.join(ruta), "rt", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            aid, nombre = linea.strip().split(",")
            yield int(aid), nombre


def cargar_conexiones(ruta):
    with open(os.path.join(ruta), "rt", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            id_partida, id_llegada, infectados = linea.strip().split(",")
            yield int(id_partida), int(id_llegada), int(infectados)
