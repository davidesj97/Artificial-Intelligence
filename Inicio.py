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

# funcion interfaz registros
def registro():
    global nombre
    global apellidoP  # Globalizamos las variables para usarlas en otras funciones
    global apellidoM
    global nombre_entrada
    global apellidoP_entrada
    global apellidoM_entrada
    global pantalla1
    pantalla1 = Toplevel(pantalla)# Esta pantalla es de un nivel superior a la principal
    pantalla1.title("Registros Usuarios")
    pantalla1.geometry("300x250")  # Asignamos el tamaño de la ventana

    # --------- Empezaremos a crear las entradas ----------------------------------------

    nombre = StringVar()
    apellidoP = StringVar()
    apellidoM = StringVar()


    Label(pantalla1, text="NOMBRE * ").pack()  # Mostramos en la pantalla 1 el usuario
    nombre_entrada = Entry(pantalla1, textvariable=nombre)  # Creamos un text variable para que el usuario ingrese la info
    nombre_entrada.pack()

    Label(pantalla1, text="APELLIDO PATERNO * ").pack()  # Mostramos en la pantalla 1 la contraseña
    apellidoP_entrada = Entry(pantalla1, textvariable=apellidoP)  # Creamos un text variable para que el usuario ingrese la contra
    apellidoP_entrada.pack()

    Label(pantalla1, text="APELLIDO MATERNO * ").pack()  # Mostramos en la pantalla 1 la contraseña
    apellidoM_entrada = Entry(pantalla1,textvariable=apellidoM)  # Creamos un text variable para que el usuario ingrese la contra
    apellidoM_entrada.pack()

    Label(pantalla1, text="").pack()  # Dejamos un espacio para la creacion del boton

    # ------------ Vamos a crear el boton para hacer el registro facial --------------------
    Label(pantalla1, text="").pack()
    Button(pantalla1, text="Registro Facial", width=15, height=1, command=RegistroFacial.registro_facial).pack()

if __name__ == "__main__":
 pantalla_principal()
