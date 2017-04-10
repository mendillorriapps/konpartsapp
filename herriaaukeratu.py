import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        if DEVICE_TYPE == 'mobile':
            layout = GridLayout(cols=1,spacing=10,size_hint_y=None)
        else:
            layout = GridLayout(cols=2,spacing=10,size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for herria in self.herriak:
            layout.add_widget(Button(text='{}'.format(herria),size_hint_y=None))
            #Button.bind(on_press=self.historia)

        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)

        return root

    def __init__(self,herriak=['iruñea','mendillorri','oibar','perrintxe']):
        super(MyApp, self).__init__()
        self.herriak = herriak

if __name__=="__main__":
    MyApp(['Ablitas','Aibar','Altsasu','Aoitz','Arre','Artajona','Baigorri','Barañain','Berriozar','Buñuel','Burlata','Buztintxuri','Karkaztelu','Cascante','Alde Zaharra','Cintruenigo','Cortes','Huarte','Irurtzun','Leitza','Lesaka','Lodosa','Lumbier','Mendillorri','Noain','Orkoien','Otsagabia','Iruña','Peralta','Perrintxe','Gares','San Juan','Sanduzelai','Tafalla','Tutera','Txantrea','Uharte Arakil','Uharte','Valtierra','Atarrabia','Zizur']).run()