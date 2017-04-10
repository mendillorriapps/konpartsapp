from kivy.uix.boxlayout import BoxLayout
from functools import partial
from kivy.app import App
from kivy.uix.button import Button
from random import Random, randrange
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        galderaGauzak = self.galderaG()

        layout = BoxLayout(orientation='vertical')
        ErantzunakL = BoxLayout(orientation='vertical')

        self.btna = Button(text=galderaGauzak[1][0])
        btnb = Button(text=galderaGauzak[1][1])
        btnc = Button(text=galderaGauzak[1][2])
        btnd = Button(text=galderaGauzak[1][3])

        buttoncallbacka = partial(self.erantzunaF,self.btna,galderaGauzak[2])
        buttoncallbackb = partial(self.erantzunaF,btnb,galderaGauzak[2])
        buttoncallbackc = partial(self.erantzunaF,btnc,galderaGauzak[2])
        buttoncallbackd = partial(self.erantzunaF,btnd,galderaGauzak[2])


        self.btna.bind(on_press=buttoncallbacka)
        btnb.bind(on_press=buttoncallbackb)
        btnc.bind(on_press=buttoncallbackc)
        btnd.bind(on_press=buttoncallbackd)

        galderaL = Label(text=galderaGauzak[0])

        ErantzunakL.add_widget(self.btna)
        ErantzunakL.add_widget(btnb)
        ErantzunakL.add_widget(btnc)
        ErantzunakL.add_widget(btnd)

        layout.add_widget(galderaL)
        layout.add_widget(ErantzunakL)


        return layout


    def galderaG(self):
        galdera1=["nose",[",","l","8","afsf"],"8"]
        galdera2=["sss",["aa","dd","gg","kk"],"kk"]
        galdera3=["ssaasd",["asdasdf","ww","qq","ee"],"ww"]

        self.galderaGuztiak=[galdera1,galdera2,galdera3]

        zein = randrange(len(self.galderaGuztiak))


        return self.galderaGuztiak[zein]
    def erantzunaF(self,ze,be,ins):
        if(ze.text==be):
            self.f = 1
            self.btna.background_color = 1.0, 0.0, 0.0, 1.0
        else:
            self.f = 0





MyApp().run()