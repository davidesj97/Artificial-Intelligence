from tkinter import *
import tkinter as tk
import Inicio

import cv2




# Funcion ejecutar camara para la asistencia Facial
def cam_asistencia_facial():
    # capturar el rostro
    cap = cv2.VideoCapture(0)  # Elegimos la camara
    while (True):
        ret, frame = cap.read()  # Leemos el video
        cv2.imshow(' Facial', frame)  # Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
            break

    cap.release()  # Cerramos
    cv2.destroyAllWindows()



