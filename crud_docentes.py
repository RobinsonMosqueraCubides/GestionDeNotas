import sqlite3

# Conectar a la base de datos
def conectar():
    conn = sqlite3.connect('gestion_notas.db')
    return conn

# Crear un nuevo docente
def crear_docente(nombre, apellido, numero_identificacion, ruta, materias, salon, horario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Docentes (nombre, apellido, numero_identificacion, ruta, materias, salon, horario)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, apellido, numero_identificacion, ruta, materias, salon, horario))
    conn.commit()
    conn.close()
    print("Docente creado con éxito")

# Leer (obtener) todos los docentes
def leer_docentes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Docentes')
    docentes = cursor.fetchall()
    conn.close()
    return docentes

# Actualizar un docente
def actualizar_docente(id_docente, nombre, apellido, numero_identificacion, ruta, materias, salon, horario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Docentes
        SET nombre = ?, apellido = ?, numero_identificacion = ?, ruta = ?, materias = ?, salon = ?, horario = ?
        WHERE id = ?
    ''', (nombre, apellido, numero_identificacion, ruta, materias, salon, horario, id_docente))
    conn.commit()
    conn.close()
    print("Docente actualizado con éxito")

# Eliminar un docente
def eliminar_docente(id_docente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Docentes WHERE id = ?', (id_docente,))
    conn.commit()
    conn.close()
    print("Docente eliminado con éxito")

# Función para mostrar docentes
def mostrar_docentes():
    docentes = leer_docentes()
    print("ID | Nombre | Apellido | Número de Identificación | Ruta | Materias | Salón | Horario")
    for docente in docentes:
        print(f"{docente[0]} | {docente[1]} | {docente[2]} | {docente[3]} | {docente[4]} | {docente[5]} | {docente[6]} | {docente[7]}")

