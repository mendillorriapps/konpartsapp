import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=3)
	layout.add_widget=Label(text=''size_hint_x=0.3,width=100)
	layout.add_widget=Label(text='TITULUA')
	layout.add_widget=Label(text=''size_hint_x=0.3,width=100)

	layout2 = GridLayout(cols=2)
	layout2.add_widget=Label(text='')
	layout2.add_widget=Image()

	layout3 = GridLayout(cols=2)
	layout3.add_widget=Image()
	layout3.add_widget=Label(text='')
	
if __name__=='__main__':
    MyApp().run()