## PARTE JSON

import os
import json


class Pelicula():

    def __init__(self, nombre, director, duracion, puntuacion):
        self.nombre = nombre
        self.director = director
        self.duracion = duracion
        self.puntuacion = puntuacion

    def __repr__(self):
        return (f'| {self.nombre:48s} | {self.director:22s} '
                f'| {self.duracion:16s} | {self.puntuacion:16s} |')

            
def desencriptar(string):
    simbolos = list("|¡!#$%&/+-(=)*];")
    letras_1 = list("aeiousrdmn12345-")
    letras_2 = list("ndsrtoaeiu67890-")

    string_encriptado = list(string)
    largo = len(string_encriptado)

    for posicion in range(largo):
        if string_encriptado[posicion] in simbolos:
            simbolo = string_encriptado.pop(posicion)
            if largo % 2 == 0:
                string_encriptado.insert(posicion, letras_1[simbolos.index(simbolo)])
            else:
                string_encriptado.insert(posicion, letras_2[simbolos.index(simbolo)])

    string_desencriptado = "".join(string_encriptado)
    return string_desencriptado


def cargar_peliculas(ruta):

    ### COMPLETAR ###
    pass
    

def desencriptado(diccionario):

    ### COMPLETAR ###
    pass


if __name__ == "__main__":
    
    print(f' {"-" * 113} ')
    print(f'| {"NOMBRE":48s} | {"DIRECTOR":22s} | {"DURACION":16s} | {"PUNTUACION":16s} |')
    print(f' {"-" * 113} ')

    for nombre_pelicula, datos in cargar_peliculas("peliculas.json").items():
        pelicula = Pelicula(nombre_pelicula, datos[1], datos[2], datos[3])
        print(pelicula)

    print(f' {"-" * 113} ')