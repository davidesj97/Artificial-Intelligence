from tkinter import *
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
from tkinter import messagebox
from os import remove
import Inicio
import Conexion
import services.users as users

# Funcion para almacenar el registro facial
def registro_facial():

    # Vamos a capturar el rostro
    cap = cv2.VideoCapture(0)  # Elegimos la camara con la que vamos a hacer la deteccion
    while (True):
        ret, frame = cap.read()  # Leemos el video
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertimos la imagen a escala de grises
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  # Cargamos el clasificador de detección de rostros
        faces = face_cascade.detectMultiScale(rgb, scaleFactor=1.1, minNeighbors=5,
                                              minSize=(30, 30))  # Detectamos los rostros en la imagen

        # for (x, y, w, h) in faces:
        #     # Dibujamos un rectángulo alrededor del rostro detectado
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Registro Facial', frame)  # Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
            break


    usuario_img = Inicio.nombre.get()
    cv2.imwrite(usuario_img + ".jpg",
                frame)  # Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()  # Cerramos
    cv2.destroyAllWindows()

    # Detectamos el rostro y exportamos los pixeles
    def Guardar_rostro(img):
        conexion = Conexion.conexionDB()
        try:

            n_control = str(Inicio.n_control.get())#se convierte de entero a cadena
            nombre = Inicio.nombre.get()
            apellidoP = Inicio.apellidoP.get()
            apellidoM = Inicio.apellidoM.get()

            n_control_registrado = users.getUsers(n_control, conexion) # Buscamos si el no. de control ya esta registrado

            if n_control_registrado:
                # el número de control ya está registrado en la base de datos
                messagebox.showerror("Error de registro", "El número de control ya está registrado.")
                return
            else:
                # abrir el archivo de imagen y convertirlo en una secuencia de bytes
                with open(img, "rb") as f:
                    imagen_bytes = f.read()
                cursor = conexion.cursor()
                # crear una sentencia SQL para insertar el registro en la base de datos
                sentencia_sql = "INSERT INTO usuarios (n_control, nombre, apellidoP, apellidoM, rostro) VALUES (%s, %s, %s, %s, %s)"
                # ejecutar la sentencia SQL y pasar los bytes de la imagen como parámetro
                cursor.execute(sentencia_sql, (n_control, nombre, apellidoP, apellidoM, imagen_bytes,))
                # confirmar los cambios y cerrar la conexión a la base de datos
                conexion.commit()
            conexion.close()
            messagebox.showinfo("Registro exitoso", "El registro se completó con éxito:" + n_control + ", " + nombre + " " + apellidoP + " " + apellidoM)
        except IOError as error:
            print("Error al abrir el archivo de imagen: {}".format(error))

        except Exception as error:
            print("Error inesperado: {}".format(error))
        finally:
            if conexion.is_connected():
                conexion.rollback()
                conexion.close()
                print("Conexión a la base de datos cerrada.")

    # Detectamos el rostro
    img = usuario_img + ".jpg"
    Guardar_rostro(img)
    # Limpiamos los text variables
    Inicio.n_control_entrada.delete(0, END)
    Inicio.nombre_entrada.delete(0, END)
    Inicio.apellidoP_entrada.delete(0, END)
    Inicio.apellidoM_entrada.delete(0, END)
    # Eliminamos la imagen
    remove(usuario_img + ".jpg")

