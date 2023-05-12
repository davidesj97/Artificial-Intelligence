from tkinter import *
import tkinter as tk
import RegistroAsistencia
import IniciarA
import RegistroFacial
from tkinter import messagebox
import main


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

    bRegistroU = tk.Button(pantalla, text="Registrar Usuario",height = "1", width = "20",command=registro)
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


# funcion interfaz registros de usuarios

def registro():
    global n_control
    global nombre
    global apellidoP
    global apellidoM
    global n_control_entrada
    global nombre_entrada
    global apellidoP_entrada
    global apellidoM_entrada
    global pantalla1

    pantalla1 = Toplevel(pantalla)
    pantalla1.title("Registros Usuarios")
    pantalla1.geometry("400x250")

    n_control = IntVar()
    nombre = StringVar()
    apellidoP = StringVar()
    apellidoM = StringVar()

    Label(pantalla1, text="N.CONTROL * ").pack()
    n_control_entrada = Entry(pantalla1, textvariable=n_control)
    n_control_entrada.pack()

    Label(pantalla1, text="NOMBRE * ").pack()
    nombre_entrada = Entry(pantalla1, textvariable=nombre)
    nombre_entrada.pack()

    Label(pantalla1, text="APELLIDO PATERNO * ").pack()
    apellidoP_entrada = Entry(pantalla1, textvariable=apellidoP)
    apellidoP_entrada.pack()

    Label(pantalla1, text="APELLIDO MATERNO * ").pack()
    apellidoM_entrada = Entry(pantalla1, textvariable=apellidoM)
    apellidoM_entrada.pack()

    Label(pantalla1, text="").pack()

    Label(pantalla1, text="").pack()
    Button(pantalla1, text="Registro Facial", width=15, height=1, command=lambda: RegistroFacial.registro_facial() if validar_campos() else None).pack()

    # Agregar función para validar campos
    def validar_campos():
        global n_control
        global nombre
        global apellidoP
        global apellidoM

        if not  n_control.get() or not nombre.get() or not apellidoP.get() or not apellidoM.get():
            messagebox.showerror("Error", "Favor de llenar los campos faltantes.")
            pantalla1.destroy()  # cerrar ventana actual
            return False

        return True




if __name__ == "__main__":
 main.inicar()
