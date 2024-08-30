class OperatoriaComercial:
    def __init__(self, id_operatoria_comercial, nombre_operatoria_comercial):
        self.id_operatoria_comercial = id_operatoria_comercial
        self.nombre_operatoria_comercial = nombre_operatoria_comercial

    def __repr__(self):
        return f"OperatoriaComercial({self.nombre_operatoria_comercial})"
