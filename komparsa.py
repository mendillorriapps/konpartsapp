import kivy


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class komparsa (App):
    def build(self):
        layout = GridLayout(cols=3,spacing=20)
        layout.add_widget(Button(text='Hello 1'))
        layout.add_widget(Button(text='World 1'))
        layout.add_widget(Button(text='Hello 2'))
        layout.add_widget(Button(text='World 2'))
        layout.add_widget(Button(text='Hello 2'))
        layout.add_widget(Button(text='World 2'))
        layout.add_widget(Button(text='Hello 2'))
        layout.add_widget(Button(text='World 2'))
        layout.add_widget(Button(text='Hello 2'))
        layout.add_widget(Button(text='World 2'))
        layout.add_widget(Button(text='Hello 2'))
        layout.add_widget(Button(text='World 2'))


        l = BoxLayout(orientation="vertical")
        l.add_widget(Label(text="Bikoteak bilatu"))
        l.add_widget(Button(text='Hasi'))
        l.add_widget(layout)


        return l

if __name__ == '__main__':
    komparsa().run()