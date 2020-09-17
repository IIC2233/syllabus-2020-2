class DCCliente:
    def __init__(self, id, nombre, comuna, ids_comida):
        self.id = int(id)
        self.nombre = nombre
        self.comuna = comuna
        self.ids_comida = ids_comida

    def obtener_comida_comprada(self, comidas):
        comida_comprada = list(filter(lambda comida: comida.id in self.ids_comida, comidas))
        nombres_comidas_comprada = list(map(lambda comida: comida.nombre, comida_comprada))
        return self.nombre + ' compró: ' + ', '.join(nombres_comidas_comprada)

    def __str__(self):
        texto = f'Id: {str(self.id): ^5s} Nombre: {self.nombre: ^22s}  Comuna: {self.comuna: ^20s}\n'
        return texto


class DCComida:
    def __init__(self, id, nombre, precio, dieciochera):
        self.id = int(id)
        self.nombre = nombre
        self.precio = int(precio)
        self.dieciochera = bool(dieciochera)

    def __str__(self):
        texto = f'Id: {str(self.id): ^5s} Nombre: {self.nombre: ^22s}  Precio: {str(self.precio):}'
        texto += f'     Dieciochero: {self.dieciochera}'
        return texto
