class Tipo:
    def __init__(self, id_tipo, nombre_tipo):
        self.id_tipo = id_tipo
        self.nombre_tipo = nombre_tipo

    def __repr__(self):
        return f"Tipo({self.nombre_tipo})"
