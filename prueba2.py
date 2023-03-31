from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import cv2
import Asistencia

class MyBoxLayout(BoxLayout):
    def bIniciar(self, instance):
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

    def bAsistencia(self, instance):

        Asistencia.form_asistencias()

    def cerrar(self):
        App.get_running_app().stop()


class MyApp(App):
    def build(self):
        layout = MyBoxLayout()

        # boton 1 y vincularlo a la biniciar

        boton1 = Button(text='INICIAR')
        boton1.bind(on_release=layout.bIniciar)
        layout.add_widget(boton1)

        # boton 2 y vincularlo a la basistencia

        boton2 = Button(text='ASISTENCIA')
        boton2.bind(on_release=layout.bAsistencia)
        layout.add_widget(boton2)

       # boton 2 y vincularlo a la basistencia

        boton3 = Button(text='CERRAR')
        boton3.bind(on_release=layout.cerrar)
        layout.add_widget(boton3)

        return layout


if __name__ == '__main__':
    MyApp().run()
