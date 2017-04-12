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

        dena = GridLayout(cols=4,spacing=20)

        A = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/erraldoia_00.png"
        B = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/erraldoia_01.png"
        C = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/erraldoia_02.png"
        D = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/erraldoia_03.png"
        C = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/erraldoia_05.png"
        D = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/erraldoia_06.png"
        E = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/erraldoia_07.png"
        F = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/erraldoia_08.png"

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
               btn1.background_normal = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/buelta.jpg"
               btn1.erraldoia =  irudia
               btn1.bind(on_press=self.jokatu)
               dena.add_widget(btn1)
        return dena

    def jokatu(self, botoia):
        if botoia.background_normal == botoia.erraldoia:
            botoia.background_normal = "/home/euskera/Mahaigaina/Dokumentuak/Irantzu/buelta.jpg"
        else:
            botoia.background_normal = botoia.erraldoia
        popup = Popup(title="Irabazlea",
            content=Label(text= ", ordenagailuak  aukeratu duelako "),
            size_hint=(None, None), size=(400, 400))
        #popup.open()




if __name__ == '__main__':
    MyApp().run()