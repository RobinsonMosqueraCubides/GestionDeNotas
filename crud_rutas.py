import sqlite3

# Conectar a la base de datos
def conectar():
    conn = sqlite3.connect('gestion_notas.db')
    return conn

# Crear una nueva ruta
def crear_ruta(nombre_ruta, materias):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Rutas (nombre_ruta, materias)
        VALUES (?, ?)
    ''', (nombre_ruta, materias))
    conn.commit()
    conn.close()
    print("Ruta creada con éxito")

# Leer (obtener) todas las rutas
def leer_rutas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Rutas')
    rutas = cursor.fetchall()
    conn.close()
    return rutas

# Actualizar una ruta
def actualizar_ruta(id_ruta, nombre_ruta, materias):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Rutas
        SET nombre_ruta = ?, materias = ?
        WHERE id = ?
    ''', (nombre_ruta, materias, id_ruta))
    conn.commit()
    conn.close()
    print("Ruta actualizada con éxito")

# Eliminar una ruta
def eliminar_ruta(id_ruta):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Rutas WHERE id = ?', (id_ruta,))
    conn.commit()
    conn.close()
    print("Ruta eliminada con éxito")

# Función para mostrar rutas
def mostrar_rutas():
    rutas = leer_rutas()
    print("ID | Nombre de la Ruta | Materias")
    for ruta in rutas:
        print(f"{ruta[0]} | {ruta[1]} | {ruta[2]}")
