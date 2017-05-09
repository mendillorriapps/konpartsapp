from kivy.uix.boxlayout import BoxLayout
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
        self.name = "galderak"
        galderaGauzak = self.galderaG()

        self.layout = BoxLayout(orientation='vertical')
        atzera = BoxLayout(orientation='vertical')
        atzera.size_hint_y=0.2
        ErantzunakL = BoxLayout(orientation='vertical')


        list03 = [0, 1, 2, 3]

        a = list03[randrange(len(list03))]
        list03.remove(a)

        b = list03[randrange(len(list03))]
        list03.remove(b)

        c = list03[randrange(len(list03))]
        list03.remove(c)

        d = list03[randrange(len(list03))]
        list03.remove(d)

        btnatzera = Button(text="Atzera")
        btnatzera.bind(on_press=self.atzera)

        self.btna = Button(text=galderaGauzak[1][a])
        self.btnb = Button(text=galderaGauzak[1][b])
        self.btnc = Button(text=galderaGauzak[1][c])
        self.btnd = Button(text=galderaGauzak[1][d])

        buttoncallbacka = partial(self.erantzunaF,self.btna,galderaGauzak[2])
        buttoncallbackb = partial(self.erantzunaF,self.btnb,galderaGauzak[2])
        buttoncallbackc = partial(self.erantzunaF,self.btnc,galderaGauzak[2])
        buttoncallbackd = partial(self.erantzunaF,self.btnd,galderaGauzak[2])


        self.btna.bind(on_press=buttoncallbacka)
        self.btnb.bind(on_press=buttoncallbackb)
        self.btnc.bind(on_press=buttoncallbackc)
        self.btnd.bind(on_press=buttoncallbackd)

        galderaL = Label(text=galderaGauzak[0])

        ErantzunakL.add_widget(self.btna)
        ErantzunakL.add_widget(self.btnb)
        ErantzunakL.add_widget(self.btnc)
        ErantzunakL.add_widget(self.btnd)

        atzera.add_widget(Label())
        atzera.add_widget(btnatzera)


        self.layout.add_widget(galderaL)
        self.layout.add_widget(ErantzunakL)
        self.layout.add_widget(atzera)

        with self.layout.canvas.before:
                Color(0.5, 0, 0.5, 1) # colors range from 0-1 instead of 0-255
                self.rect = Rectangle(source="atzekoirudia.png",size=self.layout.size,
                            pos=self.layout.pos)


        self.layout.bind(pos=self.update_rect, size=self.update_rect)

        self.add_widget(self.layout)

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
    def erantzunaF(self,ze,be,ins):
        if(ze.text==be):
            ze.background_color = (0.0, 1.5, 0.0, 1.0)
            content = Button(text='Oso ongi asmatu duzu!')
            self.popup = Popup(title='',
            content=content,
            size_hint=(None, None), size=(400, 400))
            content.bind(on_press=self.rebuild)
            self.popup.open()
        else:
            ze.background_color = (1.5, 0.0, 0.0, 1.0)
            content = Button(text='Ez duzu asmatu')
            self.popup = Popup(title='',
            content=content,
            size_hint=(None, None), size=(400, 400))
            content.bind(on_press=self.rebuild,on_dismiss = self.rebuild)
            self.popup.open()
    def rebuild(self,ins):
        self.popup.dismiss()
        self.layout.clear_widgets()
        return Galderak().run()
