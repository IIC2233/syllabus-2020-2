import csv
import os


def cargar_servicio(ruta):
    elementos = []
    header = ["nombre", "album", "artista", "genero"]
    with open(ruta, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        for line in reader:
            elementos.append({header[i]: line[i] for i in range(4)})

    return elementos


if __name__ == '__main__':
    # Cargamos los datos del servicio indicando la ruta
    ruta_datos_spotify = os.path.join("data", "facil", "spotify.csv")
    datos_spotify = cargar_servicio(ruta_datos_spotify)

    # Iteramos sobre cada dato de la plataforma Spotify
    for cancion in datos_spotify:
        print(cancion)

    # Confirmamos que los tipos sean los esperados
    print()
    print("Los datos están contenidos en:", type(datos_spotify))
    print("Cada elemento es del tipo:", type(cancion))
