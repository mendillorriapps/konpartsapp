import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import random
from kivy.uix.screenmanager import Screen




class Bikoteak(Screen):


    def __init__(self):
        self.name="Bikoteak"



        dena = BoxLayout (orientation="vertical")


        with layout.canvas.before:
                Color(0.5, 0, 0.5, 1) # colors range from 0-1 instead of 0-255
                self.rect = Rectangle(source="background.jpg",size=layout.size,
                            pos=layout.pos)
        layout.bind(pos=self.update_rect, size=self.update_rect)

        self.fitxak = GridLayout(cols=4,spacing=20)
        dena.add_widget(self.fitxak)
        self.buelta = "Argazkiak/buelta.jpg"

        for row in range(12):
           btn1 = Button()
           btn1.background_normal = self.buelta
           btn1.bind(on_press=self.jokatu)
           self.fitxak.add_widget(btn1)

        self.jokatuberriz()

        botoiak = BoxLayout (orientation="horizontal")
        botoiak.size_hint_y = 0.1
        btn2 = Button(text= "atzera")
        btn2.size_hint_y=0.1
        btn2.width=100
        btn2.bind(on_press=self.atzera)
        botoiak.add_widget(btn2)
        botoia.background_normal='button (7).png'


        btn3 = Button(text= "jokatu berriz")
        btn3.size_hint_y=0.1
        btn3.width=100
        btn3.bind(on_press=self.jokatuberriz)
        botoiak.add_widget(btn3)
        botoia.background_normal='botoia.png'
        dena.add_widget(botoiak)

        return self.add_widget(dena)

    def atzera (self,botoia):
        self.manager.current = "menu"

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

    def jokatuberriz(self,botoia=None):
        self.lehenengoa=None
        self.asmatutakoak=[]
        print("joka")

        erraldoiak = self.irakurri()
        erraldoizenak=list(erraldoiak.keys())
        hautatutakoak=sample(erraldoizenak,8)

        A = "Argazkiak/" + hautatutakoak[0]
        B = "Argazkiak/" + hautatutakoak[1]
        C = "Argazkiak/" + hautatutakoak[2]
        D = "Argazkiak/" + hautatutakoak[3]
        C = "Argazkiak/" + hautatutakoak[4]
        D = "Argazkiak/" + hautatutakoak[5]
        E = "Argazkiak/" + hautatutakoak[6]
        F = "Argazkiak/" + hautatutakoak[7]

        self.answer = list([A,A,B,B,C,C,D,D,E,E,F,F])
        random.shuffle(self.answer)
        print(self.answer)

        for i,child in enumerate(self.fitxak.children):
            child.erraldoia =  self.answer[i]
            child.background_normal = self.buelta

    def jokatu(self, botoia):
        if not self.lehenengoa:
            self.lehenengoa=botoia
            if (botoia.background_normal == botoia.erraldoia)and(botoia not in self.asmatutakoak):
                botoia.background_normal = self.buelta
            else:
                botoia.background_normal = botoia.erraldoia
        else:
            botoia.background_normal = botoia.erraldoia
            if botoia.erraldoia!=self.lehenengoa.erraldoia:
                if botoia not in self.asmatutakoak:
                    botoia.background_normal = self.buelta
                if self.lehenengoa not in self.asmatutakoak:
                    self.lehenengoa.background_normal = self.buelta
            else:
                self.asmatutakoak.append(botoia)
                self.asmatutakoak.append(self.lehenengoa)
            self.lehenengoa=None
            if len(self.asmatutakoak)== 12:
                print ("irabazi")

