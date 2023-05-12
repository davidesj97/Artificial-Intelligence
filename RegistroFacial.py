from tkinter import *
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
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

    Inicio.nombre_entrada.delete(0, END)  # Limpiamos los text variables
    Inicio.apellidoP_entrada.delete(0, END)
    Inicio.apellidoM_entrada.delete(0, END)

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
        pyplot.show()

    # Detectamos el rostro
    img = usuario_img + ".jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    Guardar_rostro(img, caras)



