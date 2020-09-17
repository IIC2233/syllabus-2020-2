from functools import reduce
from cargar_datos import cargar_comida, cargar_cliente


def obtener_comida(id_, comidas):
    # Aquí debes utilizar \mil{filter} y asociar el id a su 
    # respectiva comida de la lista comidas y retornar su instancia.
    pass


def obtener_comidas(ids, comidas):
    # Aquí debes utilizar map y la función id_a_comida(id, comidas)
    pass


def precio_total(comidas_cliente):
    # Aquí debes utilizar reduce para sumar el precio de todos los productos y retornar el total.
    pass


def top_clientes(clientes, comidas):
    precio_total_por_cliente = map(
        lambda cliente: (cliente, precio_total(obtener_comidas(cliente.ids_comida, comidas))),
        clientes
    )
    mejores_5_clientes = sorted(
        precio_total_por_cliente,
        key=lambda tupla_cliente: tupla_cliente[1],
        reverse=True
    )[:5]
    return sorted(list(map(lambda tupla_cliente: str(tupla_cliente[0]), mejores_5_clientes)))


def filtrar_dieciocheros(cliente, list_comida):
    # Deben filtrar si posee al menos 1 articulo dieciochero
    pass


def comidas_dieciocheras_por_cliente(cliente, list_comida):
    return [list_comida[id_comida].dieciochera for id_comida in cliente.ids_comida]


def clientes_dieciocheros(list_clientes, list_comida):
    # Función que crea los diccionarios dieciocheros y apagados
    clientes_dieciocheros = {}
    clientes_apagados = []
    for cliente in list_clientes:
        # Aqui es donde se guarda el retorno de filtrar_dieciocheros
        clientes_dieciocheros[cliente.nombre] = filtrar_dieciocheros(cliente, list_comida)
        if clientes_dieciocheros[cliente.nombre] == []:
            clientes_dieciocheros.pop(cliente.nombre)
            clientes_apagados.append(cliente.nombre)
    dieciocheros = sorted(clientes_dieciocheros, key=clientes_dieciocheros.get, reverse=True)
    print('     LOS DIECIOCHEROS:')
    for cliente in dieciocheros:
        print(cliente)
    print('''-----------------------------
    LOS APAGADOS:''')
    for cliente in clientes_apagados:
        print(cliente)


if __name__ == '__main__':
    nombre_archivo_clientes = 'dcclientes.csv'
    nombre_archivo_comidas = 'dccomida.csv'
    for cliente in cargar_cliente(nombre_archivo_clientes):
        # Comida comprada por cada cliente
        print(cliente.obtener_comida_comprada(cargar_comida('dccomida.csv')))

    lista_clientes = list(cargar_cliente(nombre_archivo_clientes))
    lista_comidas =  list(cargar_comida(nombre_archivo_comidas))
    mejores_clientes = top_clientes(lista_clientes, lista_comidas)
    print(f'Top 5 Clientes')
    for cliente in mejores_clientes:
        print(cliente)

    clientes_dieciocheros(lista_clientes, lista_comidas)
