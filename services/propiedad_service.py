import sqlite3
from utils.db_utils import connect_db
from models.propiedad import Propiedad
from tabulate import tabulate

headers = ["ID", "Nombre", "Propietario", "Tipo", "Estado", "Operatoria Comercial", "Dirección", "Contacto"]

def add_property():
    conn = connect_db()
    cursor = conn.cursor()

    id_tipo = input("Ingrese el tipo de propiedad (1- Casa, 2- Departamento): ")
    id_estado = input("Ingrese el estado de la propiedad (1- Disponible, 2- No disponible): ")
    id_operatoria_comercial = input("Ingrese la operacion comercial (1- Venta, 2- Alquiler): ")
    id_propietario = input("Ingrese el id del propietario: ")
    nombre = input("Ingrese el nombre de la propiedad: ")
    direccion = input("Ingrese la direccion de la propiedad: ")
    contacto = input("Ingrese el contacto de la propiedad: ")

    cursor.execute('''
        INSERT INTO Propiedad (Id_Tipo, Id_Estado, Id_Operatoria_Comercial, Id_Propietario, Nombre, Direccion, Contacto)
        VALUES (?, ?, ?, ?, ?, ?, ?)''',
        (id_tipo, id_estado, id_operatoria_comercial, id_propietario, nombre, direccion, contacto)
    )
    print("Propiedad agregada exitosamente.")
    print("ID de la propiedad: ", cursor.lastrowid)
    conn.commit()
    conn.close()

def update_property():
    conn = connect_db()
    cursor = conn.cursor()

    id_propiedad = input("Ingrese el id de la propiedad a actualizar: ")

    cursor.execute('SELECT * FROM Propiedad WHERE Id_Propiedad = ?', (id_propiedad,))
    propiedad = cursor.fetchone()

    if not propiedad:
        print("Propiedad no encontrada.")
        conn.close()
        return

    nombre = input("Ingrese el nuevo nombre de la propiedad: ")
    direccion = input("Ingrese la nueva dirección de la propiedad: ")
    contacto = input("Ingrese el nuevo contacto de la propiedad: ")

    cursor.execute('''
        UPDATE Propiedad
        SET Nombre = ?, Direccion = ?, Contacto = ?
        WHERE Id_Propiedad = ?''',
        (nombre, direccion, contacto, id_propiedad)
    )

    print("Propiedad actualizada exitosamente.")
    cursor.execute('''
        SELECT * FROM Propiedad WHERE Id_Propiedad = ?''',
        (id_propiedad,)
    )

    propiedad_actualizada = cursor.fetchone()
    print(tabulate([propiedad_actualizada], headers=headers, tablefmt="fancy_grid"))
    conn.commit()
    conn.close()

def delete_property():
    conn = connect_db()
    cursor = conn.cursor()

    id_propiedad = input("Ingrese el id de la propiedad a eliminar: ")

    # Verificar si el ID existe
    cursor.execute('SELECT * FROM Propiedad WHERE Id_Propiedad = ?', (id_propiedad,))
    propiedad = cursor.fetchone()

    if not propiedad:
        print("Propiedad no encontrada.")
        conn.close()
        return

    cursor.execute('''
        DELETE FROM Propiedad WHERE Id_Propiedad = ?''',
        (id_propiedad,)
    )

    print("Propiedad eliminada exitosamente.")
    conn.commit()
    conn.close()

def get_property():
    conn = connect_db()
    cursor = conn.cursor()

    id_propiedad = input("Ingrese el id de la propiedad a ver: ")

    cursor.execute('''
        SELECT * FROM Propiedad WHERE Id_Propiedad = ?''',
        (id_propiedad,)
    )

    propiedad = cursor.fetchone()

    if propiedad:
        print(tabulate([propiedad], headers=headers, tablefmt="fancy_grid"))
    else:
        print("Propiedad no encontrada.")

    conn.close()

def list_all_properties():
    conn = sqlite3.connect('real_estate.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT p.Id_Propiedad, p.Nombre, prop.Nombre as Nombre_Propietario, t.Nombre_Tipo, e.Nombre_Estado, o.Nombre_Operatoria_Comercial, prop.Direccion, prop.Contacto
        FROM Propiedad p
        JOIN Propietario prop ON p.Id_Propietario = prop.Id_Propietario
        JOIN Tipo t ON p.Id_Tipo = t.Id_Tipo
        JOIN Estado e ON p.Id_Estado = e.Id_Estado
        JOIN OperatoriaComercial o ON p.Id_Operatoria_Comercial = o.Id_Operatoria_Comercial
    ''')
    
    propiedades = cursor.fetchall()
    conn.close()

    print(tabulate(propiedades, headers=headers, tablefmt="fancy_grid"))



