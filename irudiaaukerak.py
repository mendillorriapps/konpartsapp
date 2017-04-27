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
from random import shuffle,randint
import csv



class MyApp(App):
    def build(self):


        layout1 = GridLayout(cols=3)
        layout1.add_widget(Label(text=""))
        self.irudia=Image()
        layout1.add_widget(self.irudia)
        layout1.add_widget(Label(text=""))

        layout = GridLayout(cols=2,spacing=20)
        self.btn1 = Button()
        self.btn2 = Button()
        self.btn3 = Button()
        self.btn4 = Button()

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

        return layout2

    def kargatu (self):
        erraldoiak = self.irakurri()
        self.irudiona= list(erraldoiak.keys())[randint(0,len(erraldoiak.keys()))]
        irudia="/home/euskera/Mahaigaina/Dokumentuak/Amaia/Argazkiak/"+self.irudiona
        self.izena=erraldoiak[self.irudiona]["izena_eu"]
        self.izenak=list([self.izena,"Josepamunda","TokoToko","Braulia"])
        shuffle(self.izenak)
        self.irudia.source=irudia

        self.btn1.text=self.izenak[0]
        self.btn2.text=self.izenak[1]
        self.btn3.text=self.izenak[2]
        self.btn4.text=self.izenak[3]

    def egiaztatu(self,botoia):
        if self.izena == botoia.text:
            print ("ongi.png")
            self.kargatu()
            return True

        else:
            print("okerra.png")
            return False

    def irakurri(self):
        erraldoiak={}
        with open('/home/euskera/Mahaigaina/Dokumentuak/Amaia/erraldoiak.csv') as fin:
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

if __name__=="__main__":
    MyApp().run()
