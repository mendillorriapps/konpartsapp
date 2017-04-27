import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import random


class MyApp(App):

    def build(self):

        self.lehenengoa=None
        self.asmatutakoak=[]
        dena = BoxLayout (orientation="vertical")
        fitxak = GridLayout(cols=4,spacing=20)
        dena.add_widget(fitxak)
        A = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/Mendillorri 1.jpg"
        B = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/Mendillorri 2.jpg"
        C = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/Txantrea 1.jpg"
        D = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/Txantrea 2.jpg"
        C = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/Txantrea txiki 1.jpg"
        D = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/Txantrea txiki 2.jpg"
        E = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/Txantrea txiki 3.jpg"
        F = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/Txantrea txiki 4.jpg"
        self.buelta = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/buelta.jpg"

        self.answer = list([A,A,B,B,C,C,D,D,E,E,F,F])
        random.shuffle(self.answer)
        self.answer = [self.answer[:4],
                       self.answer[4:8],
                       self.answer[8:12],
                       self.answer[12:16]]
        print(self.answer)
        for row in self.answer:
            for irudia in row:
               btn1 = Button()
               btn1.background_normal = self.buelta
               btn1.erraldoia =  irudia
               btn1.bind(on_press=self.jokatu)
               fitxak.add_widget(btn1)

        botoiak = BoxLayout (orientation="horizontal")
        botoiak.size_hint_y = 0.1
        btn2 = Button(text= "atzera")
        btn2.size_hint_y=0.1
        btn2.width=100
        btn2.bind(on_press=self.atzera)
        botoiak.add_widget(btn2)


        btn3 = Button(text= "jokatu berriz")
        btn3.size_hint_y=0.1
        btn3.width=100
        btn3.bind(on_press=self.jokatuberriz)
        botoiak.add_widget(btn3)

        dena.add_widget(botoiak)

        return dena

    def atzera (self,botoia):
        pass
    def jokatuberriz(self,botoia):
        pass
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




if __name__ == '__main__':
    MyApp().run()