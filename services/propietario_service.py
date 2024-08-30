import sqlite3
from utils.db_utils import connect_db
from models.propietario import Propietario

def add_propietario():
    conn = connect_db()
    cursor = conn.cursor()

    nombre = input("Ingrese el nombre del propietario: ")
    direccion = input("Ingrese la direccion del propietario: ")
    contacto = input("Ingrese el contacto del propietario: ")

    cursor.execute('''
        INSERT INTO Propietario (Nombre, Direccion, Contacto)
        VALUES (?, ?, ?)''',
        (nombre, direccion, contacto)
    )

    conn.commit()
    conn.close()

def update_propietario():
    conn = connect_db()
    cursor = conn.cursor()

    id_propietario = input("Ingrese el id del propietario a actualizar: ")
    nombre = input("Ingrese el nuevo nombre del propietario: ")
    direccion = input("Ingrese el nuevo direccion del propietario: ")
    contacto = input("Ingrese el nuevo contacto del propietario: ")

    cursor.execute('''
        UPDATE Propietario
        SET Nombre = ?, Direccion = ?, Contacto = ?
        WHERE Id_Propietario = ?''',
        (nombre, direccion, contacto, id_propietario)
    )

    conn.commit()
    conn.close()

def delete_propietario():
    conn = connect_db()
    cursor = conn.cursor()

    id_propietario = input("Enter Propietario ID to delete: ")

    cursor.execute('''
        DELETE FROM Propietario WHERE Id_Propietario = ?''',
        (id_propietario,)
    )

    conn.commit()
    conn.close()

def get_propietario():
    conn = connect_db()
    cursor = conn.cursor()

    id_propietario = input("Ingrese el id del propietario a ver: ")

    cursor.execute('''
        SELECT * FROM Propietario WHERE Id_Propietario = ?''',
        (id_propietario,)
    )

    propietario = cursor.fetchone()
    if propietario:
        print(Propietario(*propietario))
    else:
        print("Propietario not found.")

    conn.close()
