class Aeropuerto:
    def __init__(self, aeropuerto_id, nombre):
        self.id = aeropuerto_id
        self.nombre = nombre
        self.conexiones = []

    def __repr__(self):
        return f"ID del aeropuerto:{self.id}"


class Conexion:
    def __init__(self, aeropuerto_inicio_id, aeropuerto_llegada_id, infectados):

        self.aeropuerto_inicio_id = aeropuerto_inicio_id
        self.aeropuerto_llegada_id = aeropuerto_llegada_id
        self.infectados = infectados

    def __repr__(self):
        return f"{self.aeropuerto_inicio_id}->{self.aeropuerto_llegada_id}"