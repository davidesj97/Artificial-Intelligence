import tkinter
import tkinter as tk
from tkinter import *
import cv2

ventana: Tk = tk.Tk()
ventana.title("ASISTENCIA")
ventana.geometry("300x300")
ventana.resizable(width=False, height=False)


# funcion camara
def v2():
    '''Importamos el script .xml'''
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)

    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('Camera', img)
        k = cv2.waitKey(30)
        if k == 27:  # 27 es el Ascii para Esc
            break
    cap.release()


# boton
boton = tkinter.Button(ventana, text="INICIAR", command=v2)
boton.place(x=50, y=100)

Boton2 = tkinter.Button(ventana, text="ASISTENCIAS")
Boton2.place(x=150, y=100)

ventana.mainloop()
