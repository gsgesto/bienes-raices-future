class Estado:
    def __init__(self, id_estado, nombre_estado):
        self.id_estado = id_estado
        self.nombre_estado = nombre_estado

    def __repr__(self):
        return f"Estado({self.nombre_estado})"
