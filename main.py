import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Conectar a la base de datos
def conectar_bd():
    return sqlite3.connect('gestión_notas.db')

# Función para obtener rutas
def obtener_rutas():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ruta FROM Rutas")
    rutas = [row[0] for row in cursor.fetchall()]
    conn.close()
    return rutas

def obtener_materias_por_ruta(ruta):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT materias FROM Rutas WHERE nombre_ruta = ?", (ruta,))
    materias = cursor.fetchone()[0]
    conn.close()
    return materias

# Función para actualizar las materias cuando se selecciona una ruta
def actualizar_materias(event, materia_var):
    ruta_seleccionada = event.widget.get()
    if ruta_seleccionada:
        materias = obtener_materias_por_ruta(ruta_seleccionada)
        materia_var.set(materias)

# Función para abrir la ventana de agregar estudiante
def abrir_agregar_estudiante():
    ventana_agregar = tk.Toplevel()
    ventana_agregar.title("Agregar Estudiante")
    ventana_agregar.geometry("500x400")

    etiqueta = tk.Label(ventana_agregar, text="Agregar Nuevo Estudiante", font=("Arial", 14))
    etiqueta.pack(pady=20)

    # Crear un marco (frame) para los campos de entrada
    frame_campos = tk.Frame(ventana_agregar)
    frame_campos.pack(pady=10)

    # Crear campos de entrada en dos columnas
    tk.Label(frame_campos, text="Nombre").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(frame_campos, text="Apellido").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(frame_campos, text="Número de Identificación").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(frame_campos, text="Ruta").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(frame_campos, text="Materias").grid(row=4, column=0, padx=10, pady=5)
    tk.Label(frame_campos, text="Salón").grid(row=5, column=0, padx=10, pady=5)
    tk.Label(frame_campos, text="Horario").grid(row=6, column=0, padx=10, pady=5)

    nombre_var = tk.StringVar()
    apellido_var = tk.StringVar()
    id_var = tk.StringVar()
    ruta_var = tk.StringVar()
    materia_var = tk.StringVar()
    salon_var = tk.StringVar()
    horario_var = tk.StringVar()

    tk.Entry(frame_campos, textvariable=nombre_var).grid(row=0, column=1, padx=10, pady=5)
    tk.Entry(frame_campos, textvariable=apellido_var).grid(row=1, column=1, padx=10, pady=5)
    tk.Entry(frame_campos, textvariable=id_var).grid(row=2, column=1, padx=10, pady=5)
    
    # Cargar rutas en el combo box
    rutas = obtener_rutas()
    ruta_combo = ttk.Combobox(frame_campos, textvariable=ruta_var, values=rutas)
    ruta_combo.grid(row=3, column=1, padx=10, pady=5)
    ruta_combo.bind("<<ComboboxSelected>>", lambda event: actualizar_materias(event, materia_var))
    
    tk.Entry(frame_campos, textvariable=materia_var).grid(row=4, column=1, padx=10, pady=5)
    tk.Entry(frame_campos, textvariable=salon_var).grid(row=5, column=1, padx=10, pady=5)
    tk.Entry(frame_campos, textvariable=horario_var).grid(row=6, column=1, padx=10, pady=5)

    # Botón para guardar el estudiante
    btn_guardar = tk.Button(ventana_agregar, text="Guardar Estudiante", command=lambda: guardar_estudiante(
        nombre_var, apellido_var, id_var, ruta_var, materia_var, salon_var, horario_var))
    btn_guardar.pack(pady=20)

# Función para guardar los datos del estudiante en la base de datos
def guardar_estudiante(nombre_var, apellido_var, id_var, ruta_var, materia_var, salon_var, horario_var):
    nombre = nombre_var.get()
    apellido = apellido_var.get()
    id_num = id_var.get()
    ruta = ruta_var.get()
    materias = materia_var.get()
    salon = salon_var.get()
    horario = horario_var.get()

    if all([nombre, apellido, id_num, ruta, materias, salon, horario]):
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Estudiantes (nombre, apellido, id_num, ruta, materias, salon, horario)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (nombre, apellido, id_num, ruta, materias, salon, horario))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Estudiante agregado correctamente")
    else:
        messagebox.showerror("Error", "Por favor, completa todos los campos")

# Función para abrir la ventana de gestión de estudiantes
def abrir_gestion_estudiantes():
    ventana_estudiantes = tk.Toplevel()
    ventana_estudiantes.title("Gestión de Estudiantes")
    ventana_estudiantes.geometry("400x300")

    etiqueta = tk.Label(ventana_estudiantes, text="Opciones de Estudiantes", font=("Arial", 14))
    etiqueta.pack(pady=20)

    btn_agregar_estudiante = tk.Button(ventana_estudiantes, text="Agregar Estudiante", width=25, height=2, command=abrir_agregar_estudiante)
    btn_agregar_estudiante.pack(pady=10)

    btn_modificar_estudiante = tk.Button(ventana_estudiantes, text="Modificar Estudiante", width=25, height=2)
    btn_modificar_estudiante.pack(pady=10)

    btn_agregar_notas = tk.Button(ventana_estudiantes, text="Agregar Notas", width=25, height=2)
    btn_agregar_notas.pack(pady=10)

# Crear la ventana principal
def crear_ventana_principal():
    ventana = tk.Tk()
    ventana.title("Gestión de Notas")
    ventana.geometry("800x600")

    etiqueta_bienvenida = tk.Label(ventana, text="Bienvenido al Sistema de Gestión de Notas", font=("Arial", 16))
    etiqueta_bienvenida.pack(pady=20)

    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=20)

    btn_gestion_estudiantes = tk.Button(frame_botones, text="Gestionar Estudiantes", width=25, height=2, command=abrir_gestion_estudiantes)
    btn_gestion_estudiantes.grid(row=0, column=0, padx=10, pady=10)

    btn_gestion_docentes = tk.Button(frame_botones, text="Gestionar Docentes", width=25, height=2)
    btn_gestion_docentes.grid(row=0, column=1, padx=10, pady=10)

    btn_gestion_salones = tk.Button(frame_botones, text="Gestionar Salones", width=25, height=2)
    btn_gestion_salones.grid(row=1, column=0, padx=10, pady=10)

    btn_gestion_rutas = tk.Button(frame_botones, text="Gestionar Rutas", width=25, height=2)
    btn_gestion_rutas.grid(row=1, column=1, padx=10, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana_principal()
