from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

def form_asistencias():
    class MyInterface(BoxLayout):

        def __init__(self, **kwargs):
            super(MyInterface, self).__init__(**kwargs)

            # agregar widgets a la interfaz
            self.add_widget(Label(text="ASISTENCIAS"))

    class MyApp(App):

        def build(self):
            return MyInterface()

    MyApp().run()

if __name__ == '__main__':
    form_asistencias()
