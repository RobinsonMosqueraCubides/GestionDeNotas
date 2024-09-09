import sqlite3

def crear_tablas():
    conn = sqlite3.connect('gestión_notas.db')
    cursor = conn.cursor()

    # Crear tabla Rutas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Rutas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_ruta TEXT NOT NULL UNIQUE,
        materias TEXT NOT NULL
    )
    ''')

    # Crear tabla Estudiantes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        numero_identificacion TEXT NOT NULL UNIQUE,
        ruta TEXT NOT NULL,
        salon TEXT NOT NULL,
        horario TEXT NOT NULL
    )
    ''')

    # Crear tabla Docentes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Docentes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        numero_identificacion TEXT NOT NULL UNIQUE,
        ruta TEXT NOT NULL,
        materias TEXT NOT NULL,
        salon TEXT NOT NULL,
        horario TEXT NOT NULL
    )
    ''')

    # Crear tabla Salones
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Salones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        horario TEXT NOT NULL,
        capacidad INTEGER NOT NULL
    )
    ''')

    # Crear tabla Materias
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Materias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_materia TEXT NOT NULL UNIQUE,
        ruta TEXT NOT NULL
    )
    ''')

    # Crear tabla Notas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        estudiante_id INTEGER NOT NULL,
        materia_id INTEGER NOT NULL,
        tarea REAL NOT NULL,
        proyecto REAL NOT NULL,
        examen REAL NOT NULL,
        FOREIGN KEY (estudiante_id) REFERENCES Estudiantes(id),
        FOREIGN KEY (materia_id) REFERENCES Materias(id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_tablas()
