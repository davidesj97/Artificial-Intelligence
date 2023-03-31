from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import cv2
import Asistencia
import camara


class interfaz1(BoxLayout):
    def bIniciar(self, instance):
        App.get_running_app().stop()
        # corre interfaz asistencia
        camara.ejecucioncamara().run()

    def bAsistencia(self, instance):
        App.get_running_app().stop()
        #corre interfaz asistencia
        Asistencia.form_asistencias().run()


    def cerrar(self):
        App.get_running_app().stop()


class MyApp(App):
    def build(self):
        layout = interfaz1()

        # boton 1 y vincularlo a la biniciar

        boton1 = Button(text='INICIAR')
        boton1.bind(on_release=layout.bIniciar)
        layout.add_widget(boton1)

        # boton 2 y vincularlo a la basistencia

        boton2 = Button(text='ASISTENCIA')
        boton2.bind(on_release=layout.bAsistencia)
        layout.add_widget(boton2)

       # boton 3 cerrar

        boton3 = Button(text='CERRAR')
        boton3.bind(on_release=layout.cerrar)
        layout.add_widget(boton3)

        return layout



if __name__ == '__main__':
    MyApp().run()
