import tkinter as tk
from tkinter import ttk
import entrada
def interfazasistecia():
    # Creamos la ventana principal
    ventana2 = tk.Tk()
    ventana2.title("ASISTENCIAS")

    # Creamos la tabla con 4 columnas y filas
    table = ttk.Treeview(ventana2, columns=("ID", "Nombre", "Apellido Paterno", "Apellido Materno"), show="headings")

    # Establecemos los encabezados de cada columna
    table.heading("ID", text="ID")
    table.heading("Nombre", text="Nombre")
    table.heading("Apellido Paterno", text="Apellido Paterno")
    table.heading("Apellido Materno", text="Apellido Materno")
    table.pack(padx=10, pady=10)

    for i in range(6):
        table.insert("", tk.END, values=(f"{i + 1}", f"Nombre {i + 1}", f"Apellido Paterno {i + 1}",f"Apellido Materno {i + 1}"))

    # Creamos los botones para salir y regresar
    exit_button = tk.Button(ventana2, text="SALIR", command=ventana2.quit)
    exit_button.pack(pady=10)
    exit_button = tk.Button(ventana2, text="REGRESAR", command= lambda: [ventana2.destroy(), entrada.interfazinicial()])
    exit_button.pack(pady=10)

    return ventana2

if __name__ == "__main__":
    asistencia = interfazasistecia()
    asistencia.mainloop()
