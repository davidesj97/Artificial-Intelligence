import tkinter as tk
from tkinter import ttk
import Conexion
import Inicio

def interfazasistencia():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Registros de Asistencias")

    # Crear el árbol para mostrar los registros
    tree = ttk.Treeview(root)
    tree["columns"] = ("n_control", "nombre", "apellidoP", "apellidoM")

    # Configurar encabezados de las columnas
    tree.heading("n_control", text="Número de Control")
    tree.heading("nombre", text="Nombre")
    tree.heading("apellidoP", text="Apellido Paterno")
    tree.heading("apellidoM", text="Apellido Materno")

    # Conectar a la base de datos
    conn = Conexion.conexionDB()
    cursor = conn.cursor()

    # Obtener registros de la base de datos y agregarlos al árbol
    cursor.execute("SELECT * FROM asistencias")

    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)
    # Cerrar la conexión
    conn.close()

    # Empacar el árbol
    tree.pack()

    # Crear los botones para salir y regresar
    botonS = tk.Button(root, text="SALIR", command=root.quit)
    botonS.pack(pady=10)
    botonR = tk.Button(root, text="REGRESAR", command=lambda: [root.destroy(), Inicio.pantalla_principal()])
    botonR.pack(pady=10)

    # Ejecutar la aplicación
    root.mainloop()

# Llamar a la función para mostrar la interfaz
if __name__ == "__main__":
    asistencia = interfazasistencia()
    asistencia.mainloop()
