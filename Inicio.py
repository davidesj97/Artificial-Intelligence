from tkinter import *
import tkinter as tk
import RegistroAsistencia
import IniciarA
import RegistroFacial


#Funcion pantalla principal

def pantalla_principal():
    global pantalla  # Globalizamos la variable para usarla en otras funciones
    pantalla = Tk()
    pantalla.configure(bg="#515A5A")
    pantalla.geometry("400x350")  # Asignamos el tamaño de la ventana
    pantalla.title("Reconocimiento facial")  # Asignamos el titulo de la pantalla


    #Vamos a Crear los Botones

    bIniciar = tk.Button(pantalla, text="Iniciar Asistencia",height = "1", width = "20", command=Iasistencia)
    bIniciar.pack(pady=30)

    bRegistroU = tk.Button(pantalla, text="Registrar Usuario",height = "1", width = "20",command=RegistroFacial.registro)
    bRegistroU.pack(pady=30)

    bAsistir = tk.Button(pantalla, text="Asistencias",height = "1", width = "20", command= lambda: [pantalla.destroy(), RegistroAsistencia.interfazasistecia()])
    bAsistir.pack(pady=30)


    bSalir = tk.Button(pantalla, text="Salir",height = "1", width = "20", command=pantalla.destroy)
    bSalir.pack(pady=30)

    pantalla.mainloop()

    # Funcion interfaz asistencia
def Iasistencia():
        global pantalla2
        pantalla2 = Toplevel(pantalla)
        pantalla2.title("ASISTENCIA")
        pantalla2.geometry("300x250")  # Creamos la ventana


        # boton inicio de asistencia

        Label(pantalla2, text="").pack()
        Button(pantalla2, text="Inicio de Asistencia", width=20, height=1, command=IniciarA.cam_asistencia_facial).pack()




if __name__ == "__main__":
 pantalla_principal()
