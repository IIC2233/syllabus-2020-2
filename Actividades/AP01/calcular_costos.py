from math import exp
from cargar_datos import cargar_comida, cargar_cliente


def modificador_costo(cantidad_pedidos):
    ### NO MODIFICAR ####
    func = (1 / (2 + exp(2 * cantidad_pedidos) * (-1 + 1 / 0.9))) + 0.525
    return func


def costo(costo_inicial):
    # En esta función debes implementar yield
    # Debe retornar un generador
    pass


def calcular_costo_envio(comidas, costo_base_envio):
    # Debes ocupar el método next para calcular el costo de envio del cliente 
    # según el número de productos que tenga. Debes retornar este costo de envio final.
    pass


if __name__ == '__main__':
    costo_base = 4000
    dcclientes = cargar_cliente('dcclientes.csv')
    print(f'El costo base de envio es ${costo_base}')
    for cliente in dcclientes:
        # Calculamos el costo de envio para cada cliente
        costo_envio = calcular_costo_envio(cliente.comidas, costo_base)
        print(f'El costo de envio para {cliente.nombre} es ${costo_envio}')