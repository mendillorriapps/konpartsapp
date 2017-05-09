import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from  kivy.uix.image import Image

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.graphics import Color, Rectangle

import csv

from Galderak import Galderak
from irudiaaukerak import irudiaaukerak


HERRIA = ''


class menu(Screen):
    def __init__(self,herriak=[],mota=''):
        super(menu, self).__init__()

        self.name = "menu"

        layout = BoxLayout(orientation='vertical')
        albuma = Button(text='Albuma')
        layout.add_widget(albuma)
        albuma.bind(on_press=self.albumera)

        bikoteak = Button(text='Bikoteak')
        layout.add_widget(bikoteak)
        bikoteak.bind(on_press=self.bikoteetara)

        galderak = Button(text='Galderak')
        layout.add_widget(galderak)
        galderak.bind(on_press=self.galderetara)

        izenak = Button(text='Izenak')
        layout.add_widget(izenak)
        izenak.bind(on_press=self.izenetara)

        self.add_widget(layout)

    def albumera(self,b):
        self.manager.current = "HerriaAukeratu"
    def bikoteetara(self,b):
        self.manager.current = "Bikoteak"
    def galderetara(self,b):
        self.manager.current = "galderak"
    def izenetara(self,b):
        self.manager.current = "irudiaaukerak"


class HerriaAukeratu(Screen):

    def __init__(self,herriak=[],mota=''):
        super(HerriaAukeratu, self).__init__()
        self.herriak = herriak
        self.name = 'HerriaAukeratu'
        self.mota = mota
        if self.mota == 'mobile':
            #layout =BoxLayout(orientation="vertical")#GridLayout(cols=1,spacing=10,size_hint_y=None)
            layout = GridLayout(cols=1,spacing=10,size_hint_y=None)
            layout.bind(minimum_height=layout.setter('height'))
        else:
            layout = GridLayout(cols=2,spacing=10,size_hint_y=None)
            layout.bind(minimum_height=layout.setter('height'))
        for herria in self.herriak:
            bot = Button()
            bot.text = herria
            bot.size_hint_y = None
            bot.bind(on_press=self.albumera)
            layout.add_widget(bot)

        #atzera = Button(tex='Atzera')
        #atzera.bind(on_press=self.switch_prev)

        with layout.canvas.before:
                Color(0.5, 0, 0.5, 1) # colors range from 0-1 instead of 0-255
                self.rect = Rectangle(source="/home/euskera/Mahaigaina/Dokumentuak/perro-clonado-5.gif",size=layout.size,
                        pos=layout.pos)
        layout.bind(pos=self.update_rect, size=self.update_rect)

        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)


        self.add_widget(root)
    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def albumera(self,botoia):
             self.manager.get_screen('Albuma').herria(botoia.text,botoia.text,botoia.text,self.mota)
             self.manager.current = 'Albuma'

    #def switch_prev(self, *args):
        #self.manager.current = 'menu'


class Albuma(Screen):

    def __init__(self,mota='', **kwargs):
        super(Albuma, self).__init__(**kwargs)
        self.name = 'Albuma'

        if mota != 'mobile':
            layout = BoxLayout(orientation='vertical')

            self.herrial = Label(size_hint_y=0.45)
            layout.add_widget(self.herrial)

            layout2 = BoxLayout(orientation='horizontal')
            layout.add_widget(layout2)
            self.azalpena1 = Label()
            layout2.add_widget(self.azalpena1)
            self.irudia1 = Image()
            layout2.add_widget(self.irudia1)

            layout3 = BoxLayout(orientation='horizontal')
            self.irudia2=Image()
            layout3.add_widget(self.irudia2)
            layout.add_widget(layout3)
            self.azalpena2 = Label()
            layout3.add_widget(self.azalpena2)

            layoutx = BoxLayout(orientation='horizontal',size_hint_y=0.05)
            layout.add_widget(layoutx)

            layout4 = BoxLayout(orientation='horizontal',size_hint_y = 0.15)
            layout.add_widget(layout4)
            atzera = Button(text='Atzera')
            layout4.add_widget(atzera)
            atzera.bind(on_press=self.switch_prev)
            layout4.add_widget(Label(text=''))
            layout4.add_widget(Label(text=''))
            layout4.add_widget(Label(text=''))
            layout4.add_widget(Label(text=''))

            self.add_widget(layout)

        else:
            layout = BoxLayout(orientation='vertical')
            self.herrial = Label()
            layout.add_widget(self.herrial)

            self.irudia1 = Image()
            layout.add_widget(self.irudia1)

            self.azalpena1 = Label()
            layout.add_widget(self.azalpena1)

            self.add_widget(layout)

        with layout.canvas.before:
                Color(0.5, 0, 0.5, 1) # colors range from 0-1 instead of 0-255
                self.rect = Rectangle(source="/home/euskera/Mahaigaina/Dokumentuak/perro-clonado-5.gif",size=layout.size,
                    pos=layout.pos)
        layout.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


    def herria(self,herria,azalpena1,azalpena2,mota):
        self.herrial.text = herria
        self.irudia1.source = '/home/euskera/Mahaigaina/Dokumentuak/Balon mundial.jpg'

        if mota != 'mobile':
            self.azalpena.text = azalpena1 + azalpena2
        else:
            self.azalpena1.text = self.manager.erraldoiak[herria]["testua1_eu"]
            self.azalpena2.text = self.manager.erraldoiak[herria]["testua2_eu"]
            self.irudia2.source = self.manager.erraldoiak[herria]["irudia1"]

    def switch_prev(self, *args):
        self.manager.current = 'HerriaAukeratu'


class MyApp(App):

    def __init__(self,):
        super(MyApp, self).__init__()
        self.herriak = []
        self.erraldoiak = {}
        with open('erraldoiaktestuak.csv') as fin:
            reader=csv.reader(fin, skipinitialspace=True, quotechar="'")
            for row in reader:
                print(row)
                erraldoia = {}
                erraldoia ["herria_es"] = row[0]
                erraldoia ["herria_eu"] = row[1]
                erraldoia ["testua1_es"] = row[2]
                erraldoia ["testua2_es"] = row[3]
                erraldoia ["testua1_eu"] = row[4]
                erraldoia ["testua2_eu"] = row[5]
                erraldoia ["irudia1"] = row[6]
                erraldoia ["irudia2"] = row[7]


                self.erraldoiak[row[0]]=erraldoia
                self.herriak.append(row[0])

    def build(self):
        root = ScreenManager()

        DEVICE_TYPE = 'mobile'

        root.add_widget(menu())
        root.add_widget(HerriaAukeratu(self.herriak,DEVICE_TYPE))
        root.add_widget(Albuma())
        root.add_widget(Galderak())
        root.add_widget(irudiaaukerak())

        root.erraldoiak = self.erraldoiak
        root.current = 'menu'

        return root

if __name__=='__main__':
    MyApp().run()