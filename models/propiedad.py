class Propiedad:
    def __init__(self, id_propiedad, id_tipo, id_estado, id_operatoria_comercial, id_propietario, nombre, direccion, contacto):
        self.id_propiedad = id_propiedad
        self.id_tipo = id_tipo
        self.id_estado = id_estado
        self.id_operatoria_comercial = id_operatoria_comercial
        self.id_propietario = id_propietario
        self.nombre = nombre
        self.direccion = direccion
        self.contacto = contacto

    def __repr__(self):
        return f"Propiedad({self.nombre}, {self.direccion}, {self.contacto})"
