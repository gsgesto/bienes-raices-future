
from utils.db_utils import connect_db
from models.propiedad import Propiedad
from tabulate import tabulate



def list_properties_by_status_and_operation(id_estado, id_operacion=None):
    conn = connect_db()
    cursor = conn.cursor()

    if id_operacion:
        cursor.execute('''
            SELECT p.Id_Propiedad, p.Nombre, prop.Nombre as Nombre_Propietario, t.Nombre_Tipo, e.Nombre_Estado, o.Nombre_Operatoria_Comercial, prop.Direccion, prop.Contacto
            FROM Propiedad p
            JOIN Propietario prop ON p.Id_Propietario = prop.Id_Propietario
            JOIN Tipo t ON p.Id_Tipo = t.Id_Tipo
            JOIN Estado e ON p.Id_Estado = e.Id_Estado
            JOIN OperatoriaComercial o ON p.Id_Operatoria_Comercial = o.Id_Operatoria_Comercial
            WHERE e.Id_Estado = ? AND o.Id_Operatoria_Comercial = ?
        ''', (id_estado, id_operacion))
    else:
        cursor.execute('''
            SELECT p.Id_Propiedad, p.Nombre, prop.Nombre as Nombre_Propietario, t.Nombre_Tipo, e.Nombre_Estado, o.Nombre_Operatoria_Comercial, prop.Direccion, prop.Contacto
            FROM Propiedad p
            JOIN Propietario prop ON p.Id_Propietario = prop.Id_Propietario
            JOIN Tipo t ON p.Id_Tipo = t.Id_Tipo
            JOIN Estado e ON p.Id_Estado = e.Id_Estado
            JOIN OperatoriaComercial o ON p.Id_Operatoria_Comercial = o.Id_Operatoria_Comercial
            WHERE e.Id_Estado = ?
        ''', (id_estado,))

    propiedades = cursor.fetchall()
    conn.close()

    headers = ["ID", "Nombre", "Propietario", "Tipo", "Estado", "Operatoria Comercial", "Dirección", "Contacto"]

    print(tabulate(propiedades, headers=headers, tablefmt="fancy_grid"))

def list_properties_for_sale():
    return list_properties_by_status_and_operation(1, 1)

def list_properties_for_rent():
    return list_properties_by_status_and_operation(1, 2)

def list_sold_properties():
    return list_properties_by_status_and_operation(2, 1)

def list_rented_properties():
    return list_properties_by_status_and_operation(2, 2)