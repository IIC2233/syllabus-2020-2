from collections import namedtuple, defaultdict


# Para esta parte necesitarás los contenidos de la semana 0
def cargar_datos(path):
    # Para esta función te puede servir el cuaderno 3 de la semana 0
    return None
        

# De aquí en adelante necesitarás los contenidos de la semana 1
def crear_ayudantes(datos):
    # Completar función
    return None

def encontrar_cargos(ayudantes):
    # Completar función
    return None

def ayudantes_por_cargo(ayudantes):
    # Completar función
    return None


if __name__ == '__main__':
    datos = cargar_datos('ayudantes.csv')
    if datos is not None:
        print('Se lograron leer los datos')
    else:
        print('Debes completar la carga de datos')

    ayudantes = crear_ayudantes(datos)
    if ayudantes is not None:
        print('\nLos ayudantes son:')
        for ayudante in ayudantes:
            print(ayudante)
    else:
        print('\nDebes completar la creación de Ayudantes')

    cargos = encontrar_cargos(ayudantes)
    if cargos is not None:
        print('\nLos cargos son:')
        for cargo in cargos:
            print(cargo)
    else:
        print('\nDebes completar la búsqueda de Cargos')

    clasificados = ayudantes_por_cargo(ayudantes)
    if clasificados is not None:
        print('\nLos ayudantes por cargos son:')
        for cargo in clasificados:
            print(f'\n{cargo}')
            for ayudante in clasificados[cargo]:
                print(ayudante)
    else:
        print('\nDebes completar la clasificación de Ayudantes')
        