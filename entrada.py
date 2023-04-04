import tkinter as tk
import Asistencia
import camara

def interfazinicial():
    # Creamos la ventana principal
    ventana = tk.Tk()
    ventana.title("RECONOCIMIENTO FACIAL")
    ventana.configure(bg="#515A5A")

    # Establecemos el tamaño de la ventana
    ventana.geometry("400x300")

    # Creamos los botones y los agregamos a la ventana

    start_button = tk.Button(ventana, text="Iniciar", command=camara.ejecucioncamara)
    start_button.pack(pady=30)

    assist_button = tk.Button(ventana, text="Asistencia", command= lambda: [ventana.destroy(), Asistencia.interfazasistecia()])
    assist_button.pack(pady=30)

    exit_button = tk.Button(ventana, text="Salir", command=ventana.destroy)
    exit_button.pack(pady=30)

    # Ejecutamos el loop principal de la aplicación
    ventana.mainloop()

if __name__ == "__main__":
    interfazinicial()
