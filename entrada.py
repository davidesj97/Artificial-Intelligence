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

    bIniciar = tk.Button(ventana, text="Iniciar", command=camara.ejecucioncamara)
    bIniciar.pack(pady=30)

    bAsistir = tk.Button(ventana, text="Asistencia", command= lambda: [ventana.destroy(), Asistencia.interfazasistecia()])
    bAsistir.pack(pady=30)

    bSalir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    bSalir.pack(pady=30)

    # Ejecutamos el loop principal de la aplicación
    ventana.mainloop()

if __name__ == "__main__":
    interfazinicial()
