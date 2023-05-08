from tkinter import *
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import mysql.connector
import Inicio

# Funcion para almacenar el registro facial
def registro_facial():

    # Vamos a capturar el rostro
    cap = cv2.VideoCapture(0)  # Elegimos la camara con la que vamos a hacer la deteccion
    while (True):
        ret, frame = cap.read()  # Leemos el video
        cv2.imshow('Registro Facial', frame)  # Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
            break

        # Detección de rostros
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convertimos la imagen a escala de grises
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  # Cargamos el clasificador de detección de rostros
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,minSize=(30, 30))  # Detectamos los rostros en la imagen

        if len(faces) == 0:  # Si no se detecta ningún rostro, mostramos un mensaje de error
            error_label = Label(Inicio.pantalla1, text="No se detectó ningún rostro", fg="red", font=("Calibri", 11))
            error_label.pack()
            cap.release()  # Cerramos
            cv2.destroyAllWindows()
            return

    usuario_img = Inicio.nombre.get()
    cv2.imwrite(usuario_img + ".jpg",
                frame)  # Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()  # Cerramos
    cv2.destroyAllWindows()

    Label(Inicio.pantalla1, text="Registro Facial Exitoso", fg="green", font=("Calibri", 11)).pack()



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
                password='12345',
                database='usuarios'
            )
            # abrir el archivo de imagen y convertirlo en una secuencia de bytes
            with open(img, "rb") as f:
                imagen_bytes = f.read()

            nombre = Inicio.nombre.get()
            apellidoP = Inicio.apellidoP.get()
            apellidoM = Inicio.apellidoM.get()

            # crear una sentencia SQL para insertar la imagen en la base de datos
            sentencia_sql = "INSERT INTO asistencias (nombre, apellidoP, apellidoM, rostro) VALUES (%s, %s, %s, %s)"
            # ejecutar la sentencia SQL y pasar los bytes de la imagen como parámetro
            cursor = conexionDataBase.cursor()
            cursor.execute(sentencia_sql, (nombre, apellidoP, apellidoM, imagen_bytes,))
            # confirmar los cambios y cerrar la conexión a la base de datos
            conexionDataBase.commit()
            conexionDataBase.close()
            print("Imagen Guardada")
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
    Inicio.nombre_entrada.delete(0, END)
    Inicio.apellidoP_entrada.delete(0, END)
    Inicio.apellidoM_entrada.delete(0, END)




