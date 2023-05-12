from tkinter import *
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import mysql.connector
import Inicio
from tkinter import messagebox

# Funcion para almacenar el registro facial
def registro_facial():

    # Vamos a capturar el rostro
    cap = cv2.VideoCapture(0)  # Elegimos la camara con la que vamos a hacer la deteccion
    while (True):
        ret, frame = cap.read()  # Leemos el video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convertimos la imagen a escala de grises
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  # Cargamos el clasificador de detección de rostros
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,
                                              minSize=(30, 30))  # Detectamos los rostros en la imagen

        for (x, y, w, h) in faces:
            # Dibujamos un rectángulo alrededor del rostro detectado
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Registro Facial', frame)  # Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
            break


    usuario_img = Inicio.nombre.get()
    cv2.imwrite(usuario_img + ".jpg",
                frame)  # Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()  # Cerramos
    cv2.destroyAllWindows()

    # Detectamos el rostro y exportamos los pixeles
    def Guardar_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1, y1, ancho, alto = lista_resultados[i]['box']
            x2, y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i + 1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg, (150, 200),interpolation=cv2.INTER_CUBIC)  # Guardamos la imagen con un tamaño de 150x200
            cv2.imwrite(usuario_img + ".jpg", cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])
        # pyplot.show()
        try:
            # establecer la conexión a la base de datos
            conexionDataBase = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='facial_recognition',
                port='3307'
            )
            # abrir el archivo de imagen y convertirlo en una secuencia de bytes
            with open(img, "rb") as f:
                imagen_bytes = f.read()

            n_control = str(Inicio.n_control.get())#se convierte de entero a cadena
            nombre = Inicio.nombre.get()
            apellidoP = Inicio.apellidoP.get()
            apellidoM = Inicio.apellidoM.get()

            # verificar si el número de control ya está registrado en la base de datos
            cursor = conexionDataBase.cursor()
            consulta_sql = "SELECT * FROM usuarios WHERE n_control = %s"
            cursor.execute(consulta_sql, (n_control,))
            resultados = cursor.fetchall()
            if resultados:
                # el número de control ya está registrado en la base de datos
                messagebox.showerror("Error de registro", "El número de control ya está registrado.")
                return
            else:
                # crear una sentencia SQL para insertar el registro en la base de datos
                sentencia_sql = "INSERT INTO usuarios (n_control, nombre, apellidoP, apellidoM, rostro) VALUES (%s, %s, %s, %s, %s)"
                # ejecutar la sentencia SQL y pasar los bytes de la imagen como parámetro
                cursor.execute(sentencia_sql, (n_control, nombre, apellidoP, apellidoM, imagen_bytes,))
                # confirmar los cambios y cerrar la conexión a la base de datos
                conexionDataBase.commit()
            conexionDataBase.close()
            messagebox.showinfo("Registro exitoso", "El registro se completó con éxito:" + n_control + ", " + nombre + " " + apellidoP + " " + apellidoM)
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))

        except IOError as error:
            print("Error al abrir el archivo de imagen: {}".format(error))

        except Exception as error:
            print("Error inesperado: {}".format(error))
        finally:
            if conexionDataBase.is_connected():
                conexionDataBase.rollback()
                conexionDataBase.close()
                print("Conexión a la base de datos cerrada.")

    # Detectamos el rostro
    img = usuario_img + ".jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    Guardar_rostro(img, caras)
    # Limpiamos los text variables
    Inicio.n_control_entrada.delete(0, END)
    Inicio.nombre_entrada.delete(0, END)
    Inicio.apellidoP_entrada.delete(0, END)
    Inicio.apellidoM_entrada.delete(0, END)

