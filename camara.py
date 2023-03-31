from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Interface1(BoxLayout):

    def __init__(self, **kwargs):
        super(Interface1, self).__init__(**kwargs)

        # agregar widgets a la interfaz
        self.add_widget(Button(text='Ir a interfaz 2', on_release=self.go_to_interface2))

    def go_to_interface2(self, *args):
        # cerrar la ventana actual y abrir la interfaz 2
        App.get_running_app().stop()
        MyApp2().run()

class Interface2(BoxLayout):

    def __init__(self, **kwargs):
        super(Interface2, self).__init__(**kwargs)

        # agregar widgets a la interfaz
        self.add_widget(Button(text='Ir a interfaz 1', on_release=self.go_to_interface1))

    def go_to_interface1(self, *args):
        # cerrar la ventana actual y abrir la interfaz 1
        App.get_running_app().stop()
        MyApp1().run()

class MyApp1(App):

    def build(self):
        return Interface1()

class MyApp2(App):

    def build(self):
        return Interface2()

if __name__ == '__main__':
    MyApp1().run()
