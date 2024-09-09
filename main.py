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
    cursor.execute("SELECT materia1, materia2, materia3, materia4, materia5, materia6, materia7 FROM Rutas WHERE nombre_ruta = ?", (ruta,))
    materias = cursor.fetchone()
    conn.close()
    return materias if materias else ["" for _ in range(7)]

# Función para cargar rutas en el Treeview
def cargar_rutas():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_ruta, materia1, materia2, materia3, materia4, materia5, materia6, materia7 FROM Rutas")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

# Función para actualizar las materias cuando se selecciona una ruta
def actualizar_materias(event, materia_vars):
    ruta_seleccionada = event.widget.get()
    if ruta_seleccionada:
        materias = obtener_materias_por_ruta(ruta_seleccionada)
        for i, var in enumerate(materia_vars):
            var.set(materias[i])

# Función para abrir la ventana de agregar estudiante
def abrir_agregar_estudiante():
    ventana_agregar = tk.Toplevel()
    ventana_agregar.title("Agregar Estudiante")
    ventana_agregar.geometry("500x400")

    etiqueta = tk.Label(ventana_agregar, text="Agregar Nuevo Estudiante", font=("Arial", 14))
    etiqueta.grid(row=0, column=0, columnspan=2, pady=20)

    # Crear un marco (frame) para los campos de entrada
    frame_campos = tk.Frame(ventana_agregar)
    frame_campos.grid(row=1, column=0, columnspan=2, pady=10)

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
    ruta_combo.bind("<<ComboboxSelected>>", lambda event: actualizar_materias(event, [materia_var]))

    tk.Entry(frame_campos, textvariable=materia_var).grid(row=4, column=1, padx=10, pady=5)
    tk.Entry(frame_campos, textvariable=salon_var).grid(row=5, column=1, padx=10, pady=5)
    tk.Entry(frame_campos, textvariable=horario_var).grid(row=6, column=1, padx=10, pady=5)

    # Botón para guardar el estudiante
    btn_guardar = tk.Button(ventana_agregar, text="Guardar Estudiante", command=lambda: guardar_estudiante(
        nombre_var, apellido_var, id_var, ruta_var, materia_var, salon_var, horario_var))
    btn_guardar.grid(row=2, column=0, columnspan=2, pady=20)

# Función para guardar los datos del estudiante
def guardar_estudiante(nombre_var, apellido_var, id_var, ruta_var, materia_var, salon_var, horario_var):
    datos = {
        "Nombre": nombre_var.get(),
        "Apellido": apellido_var.get(),
        "Número de Identificación": id_var.get(),
        "Ruta": ruta_var.get(),
        "Materias": materia_var.get(),
        "Salón": salon_var.get(),
        "Horario": horario_var.get()
    }
    if all(datos.values()):
        conn = conectar_bd()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Estudiantes (nombre, apellido, id, ruta, materias, salon, horario)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (datos['Nombre'], datos['Apellido'], datos['Número de Identificación'], datos['Ruta'], datos['Materias'], datos['Salón'], datos['Horario']))
        conn.commit()
        conn.close()
        messagebox.showinfo("Éxito", "Estudiante agregado correctamente")
    else:
        messagebox.showerror("Error", "Por favor, completa todos los campos")

# Función para abrir la ventana de gestión de rutas
def abrir_gestion_rutas():
    ventana_rutas = tk.Toplevel()
    ventana_rutas.title("Gestión de Rutas")
    ventana_rutas.geometry("800x600")

    # Crear un marco (frame) para agregar rutas
    frame_agregar = tk.Frame(ventana_rutas)
    frame_agregar.grid(row=0, column=0, padx=10, pady=10, sticky="n")

    tk.Label(frame_agregar, text="Agregar Ruta", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)

    tk.Label(frame_agregar, text="Nombre de Ruta").grid(row=1, column=0, padx=10, pady=5)
    nombre_ruta_var = tk.StringVar()
    tk.Entry(frame_agregar, textvariable=nombre_ruta_var).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame_agregar, text="Materia 1").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(frame_agregar, text="Materia 2").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(frame_agregar, text="Materia 3").grid(row=4, column=0, padx=10, pady=5)
    tk.Label(frame_agregar, text="Materia 4").grid(row=5, column=0, padx=10, pady=5)
    tk.Label(frame_agregar, text="Materia 5").grid(row=6, column=0, padx=10, pady=5)
    tk.Label(frame_agregar, text="Materia 6").grid(row=7, column=0, padx=10, pady=5)
    tk.Label(frame_agregar, text="Materia 7").grid(row=8, column=0, padx=10, pady=5)

    materias_vars = [tk.StringVar() for _ in range(7)]
    for i, var in enumerate(materias_vars):
        tk.Entry(frame_agregar, textvariable=var).grid(row=2+i, column=1, padx=10, pady=5)

    btn_agregar = tk.Button(frame_agregar, text="Agregar Ruta", command=lambda: agregar_ruta(nombre_ruta_var.get(), [var.get() for var in materias_vars]))
    btn_agregar.grid(row=9, column=0, columnspan=2, pady=20)

    # Crear un marco (frame) para mostrar rutas
    frame_mostrar = tk.Frame(ventana_rutas)
    frame_mostrar.grid(row=0, column=1, padx=10, pady=10, sticky="n")

    tk.Label(frame_mostrar, text="Mostrar Rutas", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=20)

    columns = ("nombre_ruta", "materia1", "materia2", "materia3", "materia4", "materia5", "materia6", "materia7")
    global tree
    tree = ttk.Treeview(frame_mostrar, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.grid(row=1, column=0, columnspan=2, pady=10)

    cargar_rutas()

# Función para agregar una ruta a la base de datos
def agregar_ruta(nombre_ruta, materias):
    if nombre_ruta and all(materias):
        conn = conectar_bd()
        cursor = conn.cursor()
        # Verificar si la ruta ya existe
        cursor.execute("SELECT 1 FROM Rutas WHERE nombre_ruta = ?", (nombre_ruta,))
        if cursor.fetchone():
            messagebox.showerror("Error", "La ruta ya existe")
        else:
            cursor.execute('''
                INSERT INTO Rutas (nombre_ruta, materia1, materia2, materia3, materia4, materia5, materia6, materia7)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nombre_ruta, *materias))
            conn.commit()
            messagebox.showinfo("Éxito", "Ruta agregada correctamente")
            cargar_rutas()  # Actualizar la lista de rutas después de agregar una nueva
        conn.close()
    else:
        messagebox.showerror("Error", "Por favor, completa todos los campos")

# Función para abrir la ventana de gestión de salones
# Función para abrir la ventana de gestión de salones
def abrir_gestion_salones():
    ventana_salones = tk.Toplevel()
    ventana_salones.title("Gestión de Salones")
    ventana_salones.geometry("600x400")

    # Crear un marco (frame) para los salones existentes
    frame_existentes = tk.Frame(ventana_salones)
    frame_existentes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Crear un marco (frame) para agregar nuevos salones
    frame_agregar = tk.Frame(ventana_salones)
    frame_agregar.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Mostrar los salones existentes
    tk.Label(frame_existentes, text="Salones Existentes", font=("Arial", 14)).pack(pady=10)
    columnas = ("Nombre", "Capacidad", "Estudiantes")
    tree = ttk.Treeview(frame_existentes, columns=columnas, show="headings")
    tree.pack(fill=tk.BOTH, expand=True)
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    cargar_salones(tree)

    # Agregar nuevos salones
    tk.Label(frame_agregar, text="Agregar Nuevo Salón", font=("Arial", 14)).pack(pady=10)
    tk.Label(frame_agregar, text="Nombre").pack(pady=5)
    nombre_var = tk.StringVar()
    tk.Entry(frame_agregar, textvariable=nombre_var).pack(pady=5)

    tk.Label(frame_agregar, text="Capacidad").pack(pady=5)
    capacidad_var = tk.IntVar()
    tk.Entry(frame_agregar, textvariable=capacidad_var).pack(pady=5)

    btn_agregar = tk.Button(frame_agregar, text="Agregar Salón", command=lambda: agregar_salon(nombre_var.get(), capacidad_var.get()))
    btn_agregar.pack(pady=20)

# Función para agregar un salón a la base de datos
def agregar_salon(nombre, capacidad):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Salones (nombre, capacidad) VALUES (?, ?)", (nombre, capacidad))
        conn.commit()
        messagebox.showinfo("Éxito", "Salón agregado correctamente")
        cargar_salones(tree)  # Actualiza la lista de salones
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "El salón ya existe")
    finally:
        conn.close()

# Función para cargar salones existentes
def cargar_salones(tree):
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nombre, capacidad, 
               (SELECT COUNT(*) FROM Estudiantes WHERE salon = Salones.nombre) AS estudiantes 
        FROM Salones
    """)
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

# Crear ventana principal
def crear_ventana_principal():
    ventana_principal = tk.Tk()
    ventana_principal.title("Sistema de Gestión de Notas")
    ventana_principal.geometry("300x200")

    tk.Label(ventana_principal, text="Bienvenido al Sistema de Gestión de Notas", font=("Arial", 14)).pack(pady=20)

    tk.Button(ventana_principal, text="Gestión de Estudiantes", command=abrir_agregar_estudiante).pack(pady=10)
    tk.Button(ventana_principal, text="Gestión de Rutas", command=abrir_gestion_rutas).pack(pady=10)
    tk.Button(ventana_principal, text="Gestión de Salones", command=abrir_gestion_salones).pack(pady=10)

    ventana_principal.mainloop()

if __name__ == "__main__":
    crear_ventana_principal()
