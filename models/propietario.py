class Propietario:
    def __init__(self, id_propietario, nombre, direccion, contacto, id_propiedad):
        self.id_propietario = id_propietario
        self.nombre = nombre
        self.direccion = direccion
        self.contacto = contacto
        self.id_propiedad = id_propiedad

    def __repr__(self):
        return f"Propietario({self.nombre}, {self.direccion}, {self.contacto})"
