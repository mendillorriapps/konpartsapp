#from kivy.uix.canvas import Canvas
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from random import shuffle





class MyApp(App):
    def build(self):
        self.izena=""
        if Image=="erraldoia_00.png":
            self.izena="Campesino Miguel"

        self.izenak=list([self.izena,"Josepamunda","TokoToko","Braulia"])
        shuffle(self.izenak)
        layout1 = GridLayout(cols=3)
        layout1.add_widget(Label(text=""))
        layout1.add_widget(Image(source="/home/euskera/Mahaigaina/Dokumentuak/Amaia/Erraldoiak/ERRALDOIEN ARGAZKIAK/erraldoia_67.png"))
        layout1.add_widget(Label(text=""))

        layout = GridLayout(cols=2,spacing=20)
        btn1 = Button(text=self.izenak[0])
        btn1.bind(on_press=self.egiaztatu)
        layout.add_widget(btn1)

        btn2 = Button(text=self.izenak[1])
        btn2.bind(on_press=self.egiaztatu)
        layout.add_widget(btn2)

        btn3 = Button(text=self.izenak[2])
        btn3.bind(on_press=self.egiaztatu)
        layout.add_widget(btn3)

        btn4 = Button(text=self.izenak[3])
        btn4.bind(on_press=self.egiaztatu)
        layout.add_widget(btn4)


        layout2= BoxLayout(orientation="vertical")
        layout2.add_widget(layout1)
        layout2.add_widget(layout)

        return layout2

    def egiaztatu(self,botoia):
        if self.izena == botoia.text:
            print ("ongi.png")
            return ("ongi.png")

        else:
            print("okerra.png")
            return ("okerra.png")

if __name__=="__main__":
    MyApp().run()
