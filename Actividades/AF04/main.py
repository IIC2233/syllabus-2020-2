from arboles import PlataformaMusical
from consultas import (crear_playlist, buscar_info_artista,
                       buscar_mejor_plataforma, buscar_artistas_parecidos,
                       crear_playlist)
from cargar_datos import cargar_servicio


def recibir_input(n_inputs):
    inp = input("> ")
    while inp not in [str(i) for i in range(n_inputs)]:
        print("Debes ingresar una opción válida")
        inp = input("> ")
    return inp


# =============================================================================
# Aquí se puede cambiar el modo del programa
# 'facil'  o  'dificil'
modo = "facil"
# =============================================================================

# Se carga e instancia Spotify
spotify = PlataformaMusical("Spotify")
spotify_info = cargar_servicio(f"data/{modo}/spotify.csv")
spotify.armar_arbol(spotify_info)

# Se carga e instancia Amazon Music
amazon_music = PlataformaMusical("Amazon Music")
amazon_music_info = cargar_servicio(f"data/{modo}/amazon_music.csv")
amazon_music.armar_arbol(amazon_music_info)

# Se carga e instancia YouTube Music
youtube_music = PlataformaMusical("YouTube Music")
youtube_music_info = cargar_servicio(f"data/{modo}/youtube_music.csv")
youtube_music.armar_arbol(youtube_music_info)

# =============================================================================
# Aquí comienza el manejo del menú del juego, puedes leer y aprender :)
# Pero por favor NO MODIFICAR esta sección

# Se definen algunas variables utilizadas en el flujo del programa
plataformas = [spotify, amazon_music, youtube_music]
info_plataformas = [spotify_info, amazon_music_info, youtube_music_info]
todos_generos = list({cancion["genero"] for plataforma in info_plataformas
                      for cancion in plataforma})

inp = ""
while inp != "0":
    print("\n\n")
    print("="*80)
    print(" Bienvenido a DCConcert ".center(80))
    print("="*80)
    print("\nElige una consulta a realizar:")

    print("[1] Visualizar Árbol\n[2] Buscar Información del Artista\n"
          "[3] Buscar Mejor Plataforma\n[4] Buscar Artistas Parecidos\n"
          "[5] Crear Playlist\n\n[0] Salir\n")
    inp = recibir_input(6)

    if inp == "1":
        print(" Visualizar Árbol ".center(80, "="))
        print("\nSelecciona una plataforma:\n[0] Spotify\n"
              "[1] Amazon Music\n[2] YouTube Music\n")
        inp_plat = recibir_input(3)
        plataforma = plataformas[int(inp_plat)]
        plataforma.visualizar_arbol(plataforma.raiz)

    elif inp == "2":
        print(" Buscar Información del Artista ".center(80, "="))
        print("\nSelecciona una plataforma:\n[0] Spotify\n"
              "[1] Amazon Music\n[2] YouTube Music\n")
        inp_plat = recibir_input(3)
        plataforma = plataformas[int(inp_plat)]

        print("\nIngresa el nombre del artista que te gustaría consultar:")
        artista = input("> ")

        buscar_info_artista(plataforma, artista)

    if inp == "3":
        print(" Buscar Mejor Plataforma ".center(80, "="))
        print("\nSelecciona un genero para elegir la mejor plataforma:")
        mitad = len(todos_generos)//2 + 1
        opciones = [f"[{i}] {todos_generos[i]}".ljust(40)
                    for i in range(mitad)]
        for i in range(mitad, len(todos_generos)):
            opciones[i - mitad] += f"[{i}] {todos_generos[i]}".ljust(40)
        print("\n".join(opciones))

        inp_gen = recibir_input(len(todos_generos))
        genero = todos_generos[int(inp_gen)]

        mejor_plataforma = buscar_mejor_plataforma(genero, plataformas)

        print(f"\nPara escuchar música {genero}, definitivamente creemos que "
              f"debes probar con: "
              f"{mejor_plataforma.raiz.valor if mejor_plataforma else ''}")

    elif inp == "4":
        print(" Buscar Artistas Parecidos ".center(80, "="))
        print("\nSelecciona una plataforma:\n[0] Spotify\n"
              "[1] Amazon Music\n[2] YouTube Music\n")
        inp_plat = recibir_input(3)
        plataforma = plataformas[int(inp_plat)]
        print("\nIngresa el nombre de una canción:")
        cancion = input("> ")

        recomendados = buscar_artistas_parecidos(cancion, plataforma.raiz)
        print(f"\nComo te ha gustado {cancion}, también te pueden gustar:")
        print(" - " + "\n - ".join(recomendados if recomendados else []))

    elif inp == "5":
        print(" Crear Playlist ".center(80, "="))
        print("\nSelecciona una plataforma:\n[0] Spotify\n"
              "[1] Amazon Music\n[2] YouTube Music\n")
        inp_plat = recibir_input(3)
        plataforma = plataformas[int(inp_plat)]

        print("\nSelecciona un genero para crear la mejor playlist:")
        mitad = len(todos_generos)//2 + 1
        opciones = [f"[{i}] {todos_generos[i]}".ljust(40)
                    for i in range(mitad)]
        for i in range(mitad, len(todos_generos)):
            opciones[i - mitad] += f"[{i}] {todos_generos[i]}".ljust(40)
        print("\n".join(opciones))

        inp_gen = recibir_input(len(todos_generos))
        genero = todos_generos[int(inp_gen)]

        p_claves = []
        palabra = ""
        while palabra.lower() != "q":
            print("\nIngresa palabras claves para mejorar "
                  "tu búsqueda, para terminar ingresa 'q':")
            print("Mis palabras:\n - " + "\n - ".join(p_claves))
            palabra = input("> ")
            if palabra.lower() not in ["", "q", " "]:
                p_claves.append(palabra)

        playlist = crear_playlist(plataforma.raiz, genero, p_claves)
        if playlist:
            print("\nTu playlist ideal contiene las siguientes canciones:")
            print(" - " + "\n - ".join(playlist) + "\n\n")
        else:
            print("\n Lamentablemente no pudimos armar una playlist con "
                  "los datos entregados, inténtalo de nuevo :) \n")

    input("\n--> Presione cualquier tecla para continuar <--")
