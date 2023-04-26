import tkinter as tk
from tkinter import ttk
import Inicio
def interfazasistecia():
    # Creamos la ventana principal
    ventana2 = tk.Tk()
    ventana2.title("ASISTENCIAS")

    # Creamos la tabla con 4 columnas y filas
    tabla = ttk.Treeview(ventana2, columns=("ID", "Nombre", "Apellido Paterno", "Apellido Materno"), show="headings")

    # Establecemos los encabezados de cada columna
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Apellido Paterno", text="Apellido Paterno")
    tabla.heading("Apellido Materno", text="Apellido Materno")
    tabla.pack(padx=10, pady=10)

    for i in range(6):
        tabla.insert("", tk.END, values=(f"{i + 1}", f"Nombre {i + 1}", f"Apellido Paterno {i + 1}",f"Apellido Materno {i + 1}"))

    # Creamos los botones para salir y regresar
    botonS = tk.Button(ventana2, text="SALIR", command=ventana2.quit)
    botonS.pack(pady=10)
    botonR = tk.Button(ventana2, text="REGRESAR", command= lambda: [ventana2.destroy(), Inicio.pantalla_principal()])
    botonR.pack(pady=10)

    return ventana2

if __name__ == "__main__":
    asistencia = interfazasistecia()
    asistencia.mainloop()
