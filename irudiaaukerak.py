from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from random import shuffle,randint,sample
import csv
import random
from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle, Color

class irudiaaukerak(Screen):

    def __init__(self):
        super(irudiaaukerak, self).__init__()
        self.name="irudiaaukerak"

        layout1 = GridLayout(cols=4)
        layout1.add_widget(Label(text=""))
        self.irudia=Image()
        layout1.add_widget(self.irudia)
        layout1.add_widget(Label(text=""))

        layout = GridLayout(cols=2,spacing=20)
        self.btn1 = Button()
        self.btn1.background_normal="botoia.png"

        self.btn2 = Button()
        self.btn2.background_normal="botoia.png"

        self.btn3 = Button()
        self.btn3.background_normal="botoia.png"

        self.btn4 = Button()
        self.btn4.background_normal="botoia.png"


        self.btn1.bind(on_press=self.egiaztatu)
        layout.add_widget(self.btn1)


        self.btn2.bind(on_press=self.egiaztatu)
        layout.add_widget(self.btn2)


        self.btn3.bind(on_press=self.egiaztatu)
        layout.add_widget(self.btn3)


        self.btn4.bind(on_press=self.egiaztatu)
        layout.add_widget(self.btn4)



        layout2= BoxLayout(orientation="vertical")
        layout2.add_widget(layout1)
        layout2.add_widget(layout)

        self.kargatu()

        btn5 = Button(text="atzera")
        btn5.background_normal='atzera.png'
        btn5.size_hint_y=0.2
        btn5.size_hint_x=0.3
        btn5.bind(on_press=self.itxi)

        with layout2.canvas.before:
                Color(0.5, 0, 0.5, 1) # colors range from 0-1 instead of 0-255
                self.rect = Rectangle(source="atzekoirudia.png",size=layout2.size,
                            pos=layout2.pos)


        layout2.bind(pos=self.update_rect, size=self.update_rect)

        layout2.add_widget(btn5)


        self.add_widget(layout2)

    def update_rect(self,instance,value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size


    def itxi(self,botoia):
        self.manager.current="menu"


    def kargatu (self):
        erraldoiak = self.irakurri()
        erraldoizenak=list(erraldoiak.keys())
        hautatutakoak=sample(erraldoizenak,4)
        self.irudiona= hautatutakoak[0]
        irudia="Argazkiak/"+self.irudiona
        self.izena=erraldoiak[self.irudiona]["izena_eu"]

        self.irudia.source=irudia
        izenak=[self.izena,erraldoiak[hautatutakoak[1]]["izena_eu"],erraldoiak[hautatutakoak[2]]["izena_eu"],erraldoiak[hautatutakoak[3]]["izena_eu"]]
        shuffle(izenak)
        self.btn1.text=izenak[0]
        self.btn2.text=izenak[1]
        self.btn3.text=izenak[2]
        self.btn4.text=izenak[3]

    def egiaztatu(self,botoia):
        if self.izena == botoia.text:
            self.kargatu()
            return True

        else:
            return False

    def irakurri(self):
        erraldoiak={}
        with open('erraldoiak.csv') as fin:
            reader=csv.reader(fin, skipinitialspace=True, quotechar="'")
            for row in reader:
                erraldoia = {}
                erraldoia ["irudia"] = row[0]
                erraldoia ["izena_es"] = row[1]
                erraldoia ["izena_eu"] = row[2]
                erraldoia ["herria_es"] = row[3]
                erraldoia ["herria_eu"] = row[4]

                erraldoiak[row[0]]=erraldoia

        return erraldoiak
