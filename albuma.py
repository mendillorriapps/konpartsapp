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

from Galderak import Galderak
from irudiaaukerak import irudiaaukerak

HERRIA = ''


class menu(Screen):

    def __init__(self,herriak=[],mota=''):
        super(menu, self).__init__()

        layout = BoxLayout(orientation='vertical')
        albuma = Button(text='Albuma')
        layout.add_widget(albuma)
        albuma.bind(on_press=self.albumera)

        bikoteak = Button(text='Bikoteak')
        layout.add_widget(bikoteak)
        bikoteak.bind(on_press=self.bikoteetara)

        self.galderak = Button(text='Galderak')
        layout.add_widget(galderak)
        galderak.bind(on_press=self.galderetara)

        self.izenak = Button(text='Izenak')
        layout.add_widget(izenak)
        izenak.bind(on_press=self.izenetara)

        self.add_widget(layout)

    def albumera(self,b):
        root.manager.current = "Albuma"
    def bikoteetara(self,b):
        root.manager.current = "Bikoteak"
    def galderetara(self,b):
        root.manager.current = "Galderak"
    def izenetara(self,b):
        root.manager.current = "Izenak"

class HerriaAukeratu(Screen):

    def __init__(self,herriak=[],mota=''):
        super(HerriaAukeratu, self).__init__()
        self.herriak = herriak
        self.name = 'HerriaAukeratu'
        self.mota = mota
        if self.mota == 'mobile':
            layout =BoxLayout(orientation="vertical")#GridLayout(cols=1,spacing=10,size_hint_y=None)
        else:
            layout = GridLayout(cols=2,spacing=10,size_hint_y=None)
            layout.bind(minimum_height=layout.setter('height'))
        for herria in self.herriak:
            bot = Button()
            bot.text = herria
            bot.sizee_hint_y = None
            bot.bind(on_press=self.albumera)
            layout.add_widget(bot)
            print(herria)

        #atzera = Button(tex='Atzera')
        #atzera.bind(on_press=self.switch_prev)

        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)

        self.add_widget(root)

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

    def herria(self,herria,azalpena1,azalpena2,mota):
        self.herrial.text = herria
        self.irudia1.source = '/home/euskera/Mahaigaina/Dokumentuak/Balon mundial.jpg'

        if mota != 'mobile':
            self.azalpena.text = azalpena1 + azalpena2
        else:
            self.azalpena1.text = azalpena1
            self.azalpena2.text = azalpena2
            self.irudia2.source = '/home/euskera/Mahaigaina/Dokumentuak/giphy.gif'

    def switch_prev(self, *args):
        self.manager.current = 'HerriaAukeratu'


class MyApp(App):

    def __init__(self,herriak=['iruñea','mendillorri','oibar','perrintxe']):
        super(MyApp, self).__init__()
        self.herriak = herriak

    def build(self):
        root = ScreenManager()

        DEVICE_TYPE = 'mobile'

        root.add_widget(HerriaAukeratu(self.herriak,DEVICE_TYPE))
        root.add_widget(Albuma())
        root.add_widget(Galderak())
        root.add_widget(irudiaaukerak())
        root.add_widget(Albuma())

        root.current = 'HerriaAukeratu'

        return root

if __name__=='__main__':
    Herriak = ['Ablitas','Aibar','Altsasu','Aoitz','Arre','Artajona','Baigorri','Barañain','Berriozar','Buñuel','Burlata','Buztintxuri','Karkaztelu','Cascante','Alde Zaharra','Cintruenigo','Cortes','Huarte','Irurtzun','Leitza','Lesaka','Lodosa','Lumbier','Mendillorri','Noain','Orkoien','Otsagabia','Iruña','Peralta','Perrintxe','Gares','San Juan','Sanduzelai','Tafalla','Tutera','Txantrea','Uharte Arakil','Uharte','Valtierra','Atarrabia','Zizur']
    MyApp(herriak=Herriak).run()