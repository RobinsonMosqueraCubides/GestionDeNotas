import sqlite3

def conectar_bd():
    return sqlite3.connect('gestión_notas.db')

def crear_base_datos():
    conn = conectar_bd()
    cursor = conn.cursor()
    
    # Eliminar la tabla si ya existe (opcional, solo si quieres recrearla)
    cursor.execute('DROP TABLE IF EXISTS Rutas')

    # Crear la tabla con la estructura correcta
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Rutas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_ruta TEXT UNIQUE NOT NULL,
            materia1 TEXT NOT NULL,
            materia2 TEXT NOT NULL,
            materia3 TEXT NOT NULL,
            materia4 TEXT NOT NULL,
            materia5 TEXT NOT NULL,
            materia6 TEXT NOT NULL,
            materia7 TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_base_datos()
    print("Base de datos creada o actualizada correctamente.")
