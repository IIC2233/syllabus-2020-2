import random

from parametros import TAREAS_PATH, SABOTAJES_PATH, PROB_IMPOSTOR, BOMBA_NUCLEAR


def cargar_tareas():
    with open(TAREAS_PATH, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        tareas = list(map(lambda x: x.strip(), lines))

    return tareas


def cargar_sabotajes():
    with open(SABOTAJES_PATH, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        sabotajes = list(map(lambda x: x.strip(), lines))

    return sabotajes


def elegir_accion_impostor():
    accion = random.choices(
        ['Matar', 'Sabotear', 'Esconderse'],
        weights=PROB_IMPOSTOR,
    )[0]
    return accion


def print_progreso(color, actividad, progreso):
    pond = int(round(progreso * 8 / 100, 0))
    print(f'{color:9s}| {actividad:58s} |{("█"*pond):8s}|')


def print_anuncio(color, anuncio):
    print(f' ¡{color} {anuncio}! '.center(80, "="))


def print_sabotaje(sabotaje):
    print("*"*80)
    print('>> SONIDO DE ALERTA <<'.center(80, "*"))
    print(f' SABOTAJE EN CURSO: {sabotaje} '.center(80))
    print("*"*80)


def print_explosión():
    print(BOMBA_NUCLEAR)
    print("*"*80)
    print(' LA NAVE HA EXPLOTADO '.center(80, "*"))
    print("*"*80)
