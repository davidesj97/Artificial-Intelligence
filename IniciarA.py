import Inicio
import RegistroFacial
from tkinter import *
import face_recognition as fr
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import time
import services.assistance as assistance 


# Funcion ejecutar camara para la asistencia Facial
def cam_asistencia_facial():
    # Establecer el tamaño deseado para el video capturado
    capture_width = 840
    capture_height = 640

    # Calcular las coordenadas del rectángulo centrado
    rect_width = 280  # Ancho del rectángulo
    rect_height = 340  # Altura del rectángulo

    # capturar el rostro
    cap = cv2.VideoCapture(0)  # Elegimos la camara

    # Establecer el tamaño de captura
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, capture_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, capture_height)

    x1 = (capture_width - rect_width) // 2  # Coordenada x de la esquina superior izquierda
    y1 = (capture_height - rect_height) // 2  # Coordenada y de la esquina superior izquierda
    x2 = x1 + rect_width  # Coordenada x de la esquina inferior derecha
    y2 = y1 + rect_height  # Coordenada y de la esquina inferior derecha

    # Iniciar el temporizador
    start_time = time.time()

    # Inicializar el contador
    counter = 0
    while (True):
        ret, frame = cap.read()  # Leemos el video

        # Dibujar solo las líneas en las esquinas
        line_type = cv2.LINE_8  # Tipo de línea 8-connected (discontinua)

        cv2.line(frame, (x1, y1), (x1, y1+40), (0, 255, 0), 8, lineType=line_type)  # Línea superior izquierda
        cv2.line(frame, (x1, y1), (x1+40, y1), (0, 255, 0), 8, lineType=line_type)  # Línea superior izquierda
        cv2.line(frame, (x2, y1), (x2, y1+40), (0, 255, 0), 8, lineType=line_type)  # Línea superior derecha
        cv2.line(frame, (x2, y1), (x2-40, y1), (0, 255, 0), 8, lineType=line_type)  # Línea superior derecha
        cv2.line(frame, (x1, y2), (x1, y2-40), (0, 255, 0), 8, lineType=line_type)  # Línea inferior izquierda
        cv2.line(frame, (x1, y2), (x1+40, y2), (0, 255, 0), 8, lineType=line_type)  # Línea inferior izquierda
        cv2.line(frame, (x2, y2), (x2, y2-40), (0, 255, 0), 8, lineType=line_type)  # Línea inferior derecha
        cv2.line(frame, (x2, y2), (x2-40, y2), (0, 255, 0), 8, lineType=line_type)  # Línea inferior derecha

        # Realizar la detección de rostros dentro del rectángulo centrado
        roi = frame[y1:y2, x1:x2]
        rgb_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
        face_locations = fr.face_locations(rgb_roi)

        # Obtener el tiempo transcurrido desde el inicio en segundos
        elapsed_time = int(time.time() - start_time)

        if(len(face_locations) == 1):
            # Incrementar el contador cada segundo
            if elapsed_time >= counter:
                counter += 1
                print(counter)
        else:
            counter = 0
            start_time = time.time()  # Reiniciar el tiempo de inicio

        if(counter == 4):
            counter += 1
            face_encodings = fr.face_encodings(rgb_roi, face_locations)[0]
            assistance.register(face_encodings)
        
        cv2.imshow(' Facial', frame)  # Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
            break

    cap.release()  # Cerramos
    cv2.destroyAllWindows()


