import sqlite3

# Conectar a la base de datos
def conectar():
    conn = sqlite3.connect('gestion_notas.db')
    return conn

# Crear un nuevo salón
def crear_salon(nombre, horario, capacidad):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Salones (nombre, horario, capacidad)
        VALUES (?, ?, ?)
    ''', (nombre, horario, capacidad))
    conn.commit()
    conn.close()
    print("Salón creado con éxito")

# Leer (obtener) todos los salones
def leer_salones():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Salones')
    salones = cursor.fetchall()
    conn.close()
    return salones

# Actualizar un salón
def actualizar_salon(id_salon, nombre, horario, capacidad):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Salones
        SET nombre = ?, horario = ?, capacidad = ?
        WHERE id = ?
    ''', (nombre, horario, capacidad, id_salon))
    conn.commit()
    conn.close()
    print("Salón actualizado con éxito")

# Eliminar un salón
def eliminar_salon(id_salon):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Salones WHERE id = ?', (id_salon,))
    conn.commit()
    conn.close()
    print("Salón eliminado con éxito")

# Función para mostrar salones
def mostrar_salones():
    salones = leer_salones()
    print("ID | Nombre | Horario | Capacidad")
    for salon in salones:
        print(f"{salon[0]} | {salon[1]} | {salon[2]} | {salon[3]}")
