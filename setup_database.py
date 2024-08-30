import sqlite3

def setup_database():
    conn = sqlite3.connect('real_estate.db')
    cursor = conn.cursor()

    # Create Propietario table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Propietario (
            Id_Propietario INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Direccion TEXT,
            Contacto TEXT
        )
    ''')

    # Create Tipo table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tipo (
            Id_Tipo INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre_Tipo TEXT NOT NULL
        )
    ''')

    # Create Estado table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Estado (
            Id_Estado INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre_Estado TEXT NOT NULL
        )
    ''')

    # Create OperatoriaComercial table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS OperatoriaComercial (
            Id_Operatoria_Comercial INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre_Operatoria_Comercial TEXT NOT NULL
        )
    ''')

    # Create Propiedad table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Propiedad (
            Id_Propiedad INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Contacto TEXT,
            Direccion TEXT,
            Id_Propietario INTEGER,
            Id_Tipo INTEGER,
            Id_Estado INTEGER,
            Id_Operatoria_Comercial INTEGER,
            FOREIGN KEY (Id_Propietario) REFERENCES Propietario(Id_Propietario),
            FOREIGN KEY (Id_Tipo) REFERENCES Tipo(Id_Tipo),
            FOREIGN KEY (Id_Estado) REFERENCES Estado(Id_Estado),
            FOREIGN KEY (Id_Operatoria_Comercial) REFERENCES OperatoriaComercial(Id_Operatoria_Comercial)
        )
    ''')

    # Insert sample data into Propietario
    cursor.executemany('''
        INSERT INTO Propietario (Nombre, Direccion, Contacto)
        VALUES (?, ?, ?)
    ''', [
        ("Juan Perez", "Caseros 823", "3542-553366"),
        ("Maria Sanchez", "San Luis 902", "3541-887765")
    ])
    
    # Insert sample data into Tipo
    cursor.executemany('''
        INSERT INTO Tipo (Nombre_Tipo)
        VALUES (?)
    ''', [
        ("Casa",),
        ("Departamento",)
    ])

    # Insert sample data into Estado
    cursor.executemany('''
        INSERT INTO Estado (Nombre_Estado)
        VALUES (?)
    ''', [
        ("Disponible",),
        ("No disponible",)
    ])

    # Insert sample data into OperatoriaComercial
    cursor.executemany('''
        INSERT INTO OperatoriaComercial (Nombre_Operatoria_Comercial)
        VALUES (?)
    ''', [
        ("Venta",),
        ("Alquiler",)
    ])

    # Insert sample data into Propiedad
    cursor.executemany('''
        INSERT INTO Propiedad (Nombre, Contacto, Direccion, Id_Propietario, Id_Tipo, Id_Estado, Id_Operatoria_Comercial)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', [
        ("Casa 2 dormitorios con cochera", "3542-553366", "Caseros 823", 1, 1, 1, 1),
        ("Departamento 1 dormitorio en zona céntrica","434-354353", "San Juan 907", 2, 2, 2, 2),
        ("Casa 3 dormitorios con cochera", "3542-55366", "La Paz 73", 1, 1, 1, 1),
        ("Departamento 1 dormitorio en Carlos Paz","434-34353", "San Luis 67", 2, 2, 2, 2),
        ("Departamento 2 dormitorios","434-34353", "Bolivar 87", 2, 2, 2, 2),
        ("Casa 4 dormitorios con cochera", "3542-55366", "La Paz 853", 1, 1, 1, 1),
        ("Departamento 1 dormitorio en zona céntrica","434-354353", "San Juan 902", 2, 2, 2, 2),
        ("Departamento 2 dormitorios","434-34353", "Cárcano 87", 2, 2, 2, 2),
        ("Casa 5 dormitorios con cochera", "3542-55366", "La Paz 833", 1, 1, 1, 1),
        ("Departamento 1 dormitorio en Mar del Plata","434-34353", "San Luis 67", 2, 2, 2, 2),
        ("Departamento 2 dormitorios","434-34353", "Rosas 87", 2, 2, 2, 2),
        ("Casa 6 dormitorios frente al mar", "3542-55366", "La Paz 23", 1, 1, 1, 1),
        ("Departamento 1 dormitorio en zona céntrica","434-354353", "San Juan 909", 2, 2, 2, 2),
        ("Departamento 2 dormitorios","434-34353", "Perú 87", 2, 2, 2, 2),
        ("Casa 7 dormitorios con cochera", "3542-55366", "La Paz 823", 1, 1, 1, 1),
        ("Departamento 1 dormitorio en zona rural","434-34353", "San Luis 67", 2, 2, 2, 2),
        ("Departamento 2 dormitorios","434-34353", "Las Flores 87", 2, 2, 1, 2),
        ("Casa 8 dormitorios con piscina", "3542-55366", "La Paz 823", 1, 1, 1, 2),
        ("Departamento 1 dormitorio en Cariló","434-354353", "San Juan 902", 2, 2, 2, 2),
        ("Departamento 2 dormitorios","434-34353", "San Martín 87", 2, 2, 2, 2),
        ("Casa 2 dormitorios con cochera", "3542-55366", "La Paz 823", 2, 1, 1, 1),
        ("Departamento 1 dormitorio en zona céntrica","434-354353", "San Juan 94", 2, 1, 1, 2),
        ("Departamento 2 dormitorios","434-34353", "San Martín 67", 2, 1, 2, 1),
    ])

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
