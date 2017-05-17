from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from functools import partial
from kivy.app import App
from kivy.uix.button import Button
from random import randrange
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.graphics import Rectangle, Color
import csv

class Galderak(Screen):

    def __init__(self):
        super(Galderak, self).__init__()
        self.name = "Galderak"

        mota = ""
        self.layout = BoxLayout(orientation="vertical")
        if mota == "mobile":
           botoiak = GridLayout(cols=1,spacing=20)
        else:
            botoiak = GridLayout(cols=2,spacing=20)
        atzera = BoxLayout(orientation='vertical')
        atzera.size_hint_y=0.2

        btnatzera = Button(text="Atzera")
        btnatzera.bind(on_press=self.atzera)
        self.btna = Button()
        self.btnb = Button()
        self.btnc = Button()
        self.btnd = Button()

        self.btna.bind(on_press=self.erantzunaF)
        self.btnb.bind(on_press=self.erantzunaF)
        self.btnc.bind(on_press=self.erantzunaF)
        self.btnd.bind(on_press=self.erantzunaF)

        self.galderaL = Label()

        botoiak.add_widget(self.btna)
        botoiak.add_widget(self.btnb)
        botoiak.add_widget(self.btnc)
        botoiak.add_widget(self.btnd)

        atzera.add_widget(Label())
        atzera.add_widget(btnatzera)
        self.kargatu()

        self.layout.add_widget(self.galderaL)
        self.layout.add_widget(botoiak)
        self.layout.add_widget(atzera)

        with self.layout.canvas.before:
                Color(0.5, 0, 0.5, 1) # colors range from 0-1 instead of 0-255
                self.rect = Rectangle(source="atzekoirudia.png",size=self.layout.size,
                            pos=self.layout.pos)


        self.layout.bind(pos=self.update_rect, size=self.update_rect)

        self.add_widget(self.layout)



    def kargatu(self,p = None):
        galderaGauzak = self.galderaG()
        list03 = [0, 1, 2, 3]

        a = list03[randrange(len(list03))]
        list03.remove(a)

        b = list03[randrange(len(list03))]
        list03.remove(b)

        c = list03[randrange(len(list03))]
        list03.remove(c)

        d = list03[randrange(len(list03))]
        list03.remove(d)

        self.btna.text=galderaGauzak[1][a]
        self.btna.background_normal = "botoia.png"
        self.btna.background_color = (1, 1, 1, 1)
        self.btnb.text=galderaGauzak[1][b]
        self.btnb.background_normal = "botoia.png"
        self.btnb.background_color = (1, 1, 1, 1)
        self.btnc.text=galderaGauzak[1][c]
        self.btnc.background_normal = "botoia.png"
        self.btnc.background_color = (1, 1, 1, 1)
        self.btnd.text=galderaGauzak[1][d]
        self.btnd.background_normal = "botoia.png"
        self.btnd.background_color = (1, 1, 1, 1)

        self.galderaL.text=galderaGauzak[0]
        self.zuzena = galderaGauzak[2]

    def update_rect(self,instance,value):
            self.rect.pos = instance.pos
            self.rect.size = instance.size

    def atzera(self,b):
        self.manager.current="menu"

    def galderaG(self):

        self.galderaGuztiak=[]
        with open('galderak.csv') as fin:
            reader=csv.reader(fin, skipinitialspace=True, quotechar="'")
            for row in reader:
                galdera = [row[0],[row[1],row[2],row[3],row[4]],row[1]]
                self.galderaGuztiak.append(galdera)
        zein = randrange(len(self.galderaGuztiak))


        return self.galderaGuztiak[zein]

    def erantzunaF(self,ze):
        if(ze.text==self.zuzena):
            ze.background_color = (0.0, 1.5, 0.0, 1.0)
            content = Button(text='Oso ongi asmatu duzu!',background_color=(0.0, 1.5, 0.0, 1.0))
            self.popup = Popup(title='',
            content=content,
            size_hint=(None, None), size=(400, 200))
            content.bind(on_press=self.komodin,on_dismiss = self.kargatu)
            self.popup.open()
        else:
            ze.background_color = (1.5, 0.0, 0.0, 1.0)
            content = Button(text='Ez duzu asmatu',background_color=(1.5, 0.0, 0.0, 1.0))
            self.popup = Popup(title='',
            content=content,
            size_hint=(None, None), size=(400, 200))
            content.bind(on_press=self.komodin,on_dismiss = self.kargatu)
            self.popup.open()
    def komodin(self,but):
        self.kargatu(but)
        self.popup.dismiss()
