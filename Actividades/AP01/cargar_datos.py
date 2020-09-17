from entidades import DCComida, DCCliente


def cargar_comida(path):
    with open(path, 'r', encoding='utf-8') as file:
        for row in file:
            if row.split(',')[0] != 'id':
                datos = row.strip().split(',')
                yield DCComida(*datos)


def cargar_cliente(path):
    with open(path, 'r', encoding='utf-8') as file:
        for row in file:
            if row.split(',')[0] != 'id':
                datos = row.strip().split(',')
                ids_comidas = datos[3].split(';')
                ids_comidas = [int(id) for id in ids_comidas]
                yield DCCliente(datos[0], datos[1], datos[2], ids_comidas)


if __name__ == '__main__':
    generador_dcclientes = cargar_cliente('dcclientes.csv')
    generador_dccomidas = cargar_comida('dccomida.csv')
    print(type(generador_dccomidas))
    print(type(generador_dcclientes))
    for cliente in generador_dcclientes:
        print(cliente)
    for comida in generador_dccomidas:
        print(comida)
