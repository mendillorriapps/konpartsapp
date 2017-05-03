from kivy.uix.boxlayout import BoxLayout
from functools import partial
from kivy.app import App
from kivy.uix.button import Button
from random import randrange
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

class Galderak(Screen):

    def __init__(self):
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


        self.add_widget(self.layout)

    def atzera(self,b):
        self.manager.current="menu"

    def galderaG(self):


        galdera1=["Zein egunetan sortu zen Oibarreko konpartsa?",["abuztuak 15.","ekainak 15.","ekainak 16.","Ez dago."],"abuztuak 15"]
        galdera2=["Zenbat konpartsa daude?",["41","56","108","3"],"41"]
        galdera3=["Nola deitzen dira agoitzeko konpartsako bigarren bikotea?",["Karlos Noblea eta Magdalena Printzesa","Xabiertxo eta Maitane","Barron eta iker","Antso VII eta Juana eroa"],"Karlos Noblea eta Magdalena Printzesa"]
        galdera4=["Zer dira Arreko konpartsaren bikotea?",["zaldi bat eta margolari bat","abokatu bat eta preso bat","errege eta erregina bat","ez da Arreko konpartsa existitzen"],"zaldi bat eta margolari bat"]
        galdera5=["Zenbat erraldoi daukza Altsasuak?",["6","2","12","Ez dauzka bat ere"],"6"]
        galdera6=["Zein urtetan aurkeztu ziren Artaxoako erraldoiak?",["1995.urtean","1990.urtean","2013.urtean","1943.urtean"],"1995.urtean"]
        galdera7=["Zein urtetan sortu ziren Berriozarreko erraldoiak?",["1984","1987","1995","2012"],"1984"]
        galdera8=["Zein urtetan sortu ziren Berako erraldoiak?",["2010","1998","1995","1999"],"2010"]
        galdera9=["Noiz sortu zen Lekunberriko erraldoiak?",["Ez dira existitzen","1998","2012","2009"],"Ez dira existitzen"]
        galdera10=["Zein konpartsa da zaharrago?",["Agoitz","Bera","Biak urte berekoak dira","ezin da jakin"],"Agoitz"]
        galdera11=["Zein urtetan sortu ziren Ablitasko erraldoiak?",["2005","1999","2010","Ablitasen ez daude erraldoirik"],"2005"]
        galdera12=["Nondik lortu zuen Lakuntzak bere erraldoiak?",["Josu Iragik sortu egin zituen, herritarren laguntzarekin","Ez daukate erraldoirik","herritarrek sortu zituzten","Aragoitik atera zituzten"],"Josu Iragik sortu egin zituen, herritarren laguntzarekin"]
        galdera13=["Nongoak dira Lesakako erraldoiak?",["Kataluñakoak","Madrilgoak","Bizkaiakoak","Extremadurakoak"],"Kataluñakoak"]
        galdera14=["Nola deitzen dira lodosako erraldoiak?",["pimentonero eta isolina","lodosa eta navarra","ez daukate erraldoirik","Maite eta iñaki"],"pimentonero eta isolina"]
        galdera15=["Nola deitzen dira badostaingo erraldoiak?",["Badostainen ez daude erraldoirik","egues eta sarriguren","Javier eta Saioa","ez daukate izenik"],"Badostainen ez daude erraldoirik"]
        galdera16=["Zein enpresa sortu zuen irunberriko erraldoiak?",["Jugueteria Rechacha","la golosina","toys rus","eroski"],"Jugueteria Rechacha"]
        galdera17=["zenbat erraldoi daude Azkoienen?",["4","3","2","0"],"4"]
        galdera18=["zenbat erraldoi daude Tafallan?",["6","4","2","0"],"6"]
        galdera19=["Zein mitologiakoak dira Txantreako erraldoiak",["Euskal mitologiakoak","Erromatar mitologiakoak","greziar mitologiakoak","ez dira mitologiatik aterata"],"Euskal mitologiakoak"]
        galdera20=["Uharteko erraldoiak, uharte arakilgo erraldoiak baino zaharragoak dira?",["Bai","ez","urte berdinekoak dira","uharten ez dago konpartsarik"],"Bai"]
        galdera21=["Zenbat erraldoi daude antsoainen?",["4","6","2","0"],"4"]
        galdera22=["Nor igorri zuen 1860an gutun bat iruñeko udalari erraldoi bikote bat sortzeko asmoarekin?",["Tadeo Amorena","Josu Iragi","Karlos Noblea","martin kasai"],"Tadeo Amorena"]
        galdera23=["nori bururatu zitzaion butintxuriko konpartsa sortzea?",["Gaiteros Haizeberri Dultzaineroak taldeari","iruñeko udalari","nafarroako gobernuari","tadeo amorenari"],"Gaiteros Haizeberri Dultzaineroak taldeari"]
        galdera24=["noiz sortu ziren Noaingo erraldoiak?",["1982","1988","2008","2015"],"1982"]
        galdera25=["zenbat erraldoi daude Milagrosen?",["4","2","6","3"],"4"]
        galdera26=["orain dela zenbat urte sortu zen martzillako konpartsa?",["30","20","10","70"],"30"]
        galdera27=["Nori dago dedikatuta orkoieneko erraldoiak?",["Mikel eta Ageda deunei","iker eta amaia deunei","joseba asironi","nikolas eta franztisko deunei"],"Mikel eta Ageda deunei"]
        galdera28=["nori mandatu zioten Valtierrako erraldoiak egitea?",["Aitor Calleja","tadeo amorena","karlos noblea","asier markotegi"],"Aitor Calleja"]
        galdera29=["zein urtetan sortu ziren etxalarko erraldoiak?",["2004","1988","1999","2015"],"2004"]
        galdera30=["nor  zuzendu zuen miranda de argako erraldoiak?",["Rafa Miranda","Aitor Calleja","tadeo amorena","karlos noblea"],"Rafa Miranda"]
        galdera31=["zein herritan enkargatzen dira Basaizea Elkartea erraldoietaz?",["Baigorri","lekunberri","buztintxuri","mendillorri"],"Baigorri"]
        galdera32=["zein alkate onetsi zuen agoitzen erraldoiak jartzea?",["Miguel Ángel León","Rafa Miranda","Aitor Calleja","tadeo amorena"],"Miguel Ángel León"]
        galdera33=["zergatik Artzaina eta mahats-biltzailearen irudiak aukeratu ziren erraldoi bezala?",["argibide hauek oso arruntak omen zirelako Berriozarren","ausaz aukeratu ziren","alkateak aukeratu zituen","ez da inoiz jakin"],"argibide hauek oso arruntak omen zirelako Berriozarren"]
        galdera34=["Nork sortu zituen Barañaingo erraldoiak?",["Mari ganuza","Rafa Miranda","Aitor Calleja","tadeo amorena"],"Mari ganuza"]
        galdera35=["zenbat erraldoi daude lekunberrin?",["0","2","4","6"],"0"]
        galdera36=["nor irudikatzen dute buñueleko erraldoiak?",["Alfontso I.a (Borrokalaria) eta bere emazte Urraca ","Mikel eta Ageda deunei","nikolas eta franztisko deunei","ez dute inor irudikatzen"],"Alfontso I.a (Borrokalaria) eta bere emazte Urraca "]
        galdera37=["zer berezitasun daukate cascanteko erraldoiak?",["Txikiak dira (2.80m)","handiak dira(5,2m)","nafarroako zarrenak dira","berrienak dira"],"Txikiak dira (2.80m)"]
        galdera38=["zein urtetan sortu ziren cintruenigoko lehenengo erraldoi bikotea?",["1944","1998","1983","1993"],"1944"]
        galdera39=["nork sortu zituen Cintruenigoko erraldoien soinekoak?",["Primitiva Alvero","Marta Iglesias","Mercedes Milá","Saioa Ormazabal"],"Primitiva Alvero"]
        galdera40=["zer dira Vitorio eta Vicenta erraldoiak?",["bi oliba-biltzaile","errege-erregin","bi nekazari","marokotarrak"],"bi oliba-biltzaile"]
        galdera41=["zertarako erabili zituzten cortesko udalak erraldoiak?",["makildantza ezagutarazteko"," jendea denborapasa bat izateko","udalak ez zuten ezer egin erraldoiekin","Cortesen ez daude erraldoirik"],"makildantza ezagutarazteko"]
        galdera42=["noiz sortu zen Arreko konpartsa?",["2010","1998","2003","1976"],"2010"]
        galdera43=["zein enpresak sortu zituen lesakako erraldoiak?",["El Ingenio","jugueteria rechacha","la golosina","aytekin"],"El Ingenio"]
        galdera44=["zein egunetan aurkeztu ziren mendillorriko erraldoiak?",["Olentzero datorrenean","donibane jaian","mendillorriko pestetan","urteberri egunean"],"Olentzero datorrenean"]
        galdera45=["zein elkartetan landu egin ziren Otsagabiako erraldoiak?",["Gartxot elkartean","Elkar elkartean","Elhuyar elkartean","Unicef elkartean"],"Gartxot elkartean"]
        galdera46=["zein urtetan sortu zen Perrincheko erraldoiak?",["1943","ez daude erraldoirik","1998","2004"],"1943"]
        galdera47=["zein urtetan sortu ziren arizkurengo erraldoiak?",["Ez daude erraldoirik","1992","1983","1988"],"Ez daude erraldoirik"]
        galdera48=["zer errepresentatzen du Taraskak?",["Gaiztakeria","ongizatea","bizia","inteligentzia"],"Gaiztakeria"]
        galdera49=["zein erlijiotako erraldoiak etorri ziren 2011ko ekainaren 18an perrinchera?",["Kristauak","budistak","juduak","islam"],"Kristauak"]
        galdera50=["zer da orkoieneko mikel erraldoia?",["sokagilea da","pailazoa da","erregea da","nekazaria da"],"sokagilea da"]

        self.galderaGuztiak=[galdera1,galdera2,galdera3,galdera4,galdera5,galdera6,galdera7,galdera8,galdera9,galdera10,galdera11,galdera12,galdera13,galdera14,galdera15,galdera16,galdera17,galdera18,galdera19,galdera20,galdera21,galdera22,galdera23,galdera24,galdera25,galdera26,galdera27,galdera28,galdera29,galdera30,galdera31,galdera32,galdera33,galdera34,galdera35,galdera36,galdera37,galdera38,galdera39,galdera40,galdera41,galdera42,galdera43,galdera44,galdera45,galdera46,galdera47,galdera48,galdera49,galdera50]

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
