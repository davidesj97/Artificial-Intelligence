from tkinter import *
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import Inicio

# funcion interfaz registros
def registro():
    global nombre
    global apellidoP  # Globalizamos las variables para usarlas en otras funciones
    global apellidoM
    global nombre_entrada
    global apellidoP_entrada
    global apellidoM_entrada
    global pantalla1
    pantalla1 = Toplevel(Inicio.pantalla)# Esta pantalla es de un nivel superior a la principal
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
    Button(pantalla1, text="Registro Facial", width=15, height=1, command=registro_facial).pack()

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
            error_label = Label(pantalla1, text="No se detectó ningún rostro", fg="red", font=("Calibri", 11))
            error_label.pack()
            cap.release()  # Cerramos
            cv2.destroyAllWindows()
            return

    usuario_img = nombre.get()
    cv2.imwrite(usuario_img + ".jpg",
                frame)  # Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()  # Cerramos
    cv2.destroyAllWindows()

    nombre_entrada.delete(0, END)  # Limpiamos los text variables
    apellidoP_entrada.delete(0, END)
    apellidoM_entrada.delete(0, END)

    Label(pantalla1, text="Registro Facial Exitoso", fg="green", font=("Calibri", 11)).pack()

 # Detectamos el rostro y exportamos los pixeles
    def reg_rostro(img, lista_resultados):
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

    img = usuario_img + ".jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    reg_rostro(img, caras)


