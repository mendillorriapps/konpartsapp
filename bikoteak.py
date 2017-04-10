import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class MyApp(App):

    def build(self):

        dena = GridLayout(cols=4,spacing=20)

        A = "/home/euskera/Mahaigaina/Deskargak/erraldoia_00.png"
        B = "/home/euskera/Mahaigaina/Deskargak/erraldoia_01.png"
        C = "/home/euskera/Mahaigaina/Deskargak/erraldoia_02.png"
        D = "/home/euskera/Mahaigaina/Deskargak/erraldoia_03.png"
        C = "/home/euskera/Mahaigaina/Deskargak/erraldoia_05.png"
        D = "/home/euskera/Mahaigaina/Deskargak/erraldoia_06.png"
        E = "/home/euskera/Mahaigaina/Deskargak/erraldoia_07.png"
        F = "/home/euskera/Mahaigaina/Deskargak/erraldoia_08.png"

        self.answer = (A,A,B,B,C,C,D,D,E,E,F,F)
        random.shuffle(self.answer)
        self.answer = [self.answer[:4],
                       self.answer[4:8],
                       self.answer[8:12],
                       self.answer[12:]]
        for row in self.answer:
            for irudia in row:
               btn1 = Button(text="harria")
               btn1.bind(on_press=self.jokatu)
        self.start_time = time.monotonic()


        btn1 = Button(text="harria")
        btn1.bind(on_press=self.jokatu)

        btn2 = Button(text="papera")
        btn2.bind(on_press=self.jokatu)

        btn3 = Button(text="guraizeak")
        btn3.bind(on_press=self.jokatu)

        btn4 = Button(text="muskerra")
        btn4.bind(on_press=self.jokatu)

        btn5 = Button(text="Spock")
        btn5.bind(on_press=self.jokatu)

        dena.add_widget(btn1)
        dena.add_widget(btn2)
        dena.add_widget(btn3)
        dena.add_widget(btn4)
        dena.add_widget(btn5)
        return dena

    def jokatu(self, botoia):
        aukera = botoia.text
        popup = Popup(title="Irabazlea",
            content=Label(text= ", ordenagailuak  aukeratu duelako "),
            size_hint=(None, None), size=(400, 400))
        popup.open()


if __name__ == '__main__':
    MyApp().run()