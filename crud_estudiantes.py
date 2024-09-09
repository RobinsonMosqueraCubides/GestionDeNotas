import sqlite3

# Conectar a la base de datos
def conectar():
    conn = sqlite3.connect('gestion_notas.db')
    return conn

# Crear un nuevo estudiante
def crear_estudiante(nombre, apellido, numero_identificacion, ruta, materias, salon, horario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Estudiantes (nombre, apellido, numero_identificacion, ruta, materias, salon, horario)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, apellido, numero_identificacion, ruta, materias, salon, horario))
    conn.commit()
    conn.close()
    print("Estudiante creado con éxito")

# Leer (obtener) todos los estudiantes
def leer_estudiantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Estudiantes')
    estudiantes = cursor.fetchall()
    conn.close()
    return estudiantes

# Actualizar un estudiante
def actualizar_estudiante(id_estudiante, nombre, apellido, numero_identificacion, ruta, materias, salon, horario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Estudiantes
        SET nombre = ?, apellido = ?, numero_identificacion = ?, ruta = ?, materias = ?, salon = ?, horario = ?
        WHERE id = ?
    ''', (nombre, apellido, numero_identificacion, ruta, materias, salon, horario, id_estudiante))
    conn.commit()
    conn.close()
    print("Estudiante actualizado con éxito")

# Eliminar un estudiante
def eliminar_estudiante(id_estudiante):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Estudiantes WHERE id = ?', (id_estudiante,))
    conn.commit()
    conn.close()
    print("Estudiante eliminado con éxito")

# Función para mostrar estudiantes
def mostrar_estudiantes():
    estudiantes = leer_estudiantes()
    print("ID | Nombre | Apellido | Número de Identificación | Ruta | Materias | Salón | Horario")
    for estudiante in estudiantes:
        print(f"{estudiante[0]} | {estudiante[1]} | {estudiante[2]} | {estudiante[3]} | {estudiante[4]} | {estudiante[5]} | {estudiante[6]} | {estudiante[7]}")

