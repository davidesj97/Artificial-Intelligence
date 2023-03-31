import cv2


def ejecucioncamara():
#carga el clasificador frontal para detección de rostros


    '''Importamos el script .xml'''
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# inicia la captura de video desde la cámara
cap = cv2.VideoCapture(0)

while True:
    # lee un frame de la captura de video
    ret, frame = cap.read()

    # convierte el frame a escala de grises para la detección de rostros
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detecta rostros en el frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # dibuja un rectángulo alrededor de cada rostro detectado
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # muestra el frame resultante
    cv2.imshow('Detección de rostros', frame)

    # espera por la tecla 'q' para salir
    if cv2.waitKey(1) == ord('q'):
        break

# libera la captura de video y cierra la ventana
cap.release()

