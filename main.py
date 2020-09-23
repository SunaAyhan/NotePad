from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import os, sys
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import sqlite3
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.core.window import Window 
import textwrap 
from kivy.graphics import Color, Rectangle, Canvas
#Window.size = (720, 1280)

baglanti = sqlite3.connect("notlar.db") #Sql veritabanımızın olduğu dosya. Bu dosya ilk çalıştırmada otomatik oluşturulacak
sorgula = baglanti.cursor() #Sql diliyle yazdığımız sorguyu yolladığımız fonksiyon
secili_id = 'bos'
class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''
class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    def on_press(self):
        app = App.get_running_app()
        ScreenManager.get_screen(App.get_running_app().py,"NotesScreen").ids.metin.text = self.textLong
        global secili_id
        secili_id = self.id
        print(self.text)
Builder.load_file("self.kv")
class AnasayfaScreen(Screen):
    window_sizes=Window.size[1]/9
    def yeninot(self):
        app = App.get_running_app()
        global secili_id
        secili_id = 'bos'
        ScreenManager.get_screen(App.get_running_app().py,"NotesScreen").ids.metin.text = ''
    
    data_items = ListProperty([])
    def __init__(self, **kwargs):
        super(AnasayfaScreen, self).__init__(**kwargs)
        self.notlari_al()
    #Bu fonksiyon, veritabanındaki notlar tablosunun içindeki notları çeker ve RecycleView'e yazar
    def notlari_al(self):
        
        sql_sorgusu = """CREATE TABLE IF NOT EXISTS notlar ( 
                                id integer PRIMARY KEY AUTOINCREMENT,
                                note text NOT NULL
                            );"""
        sorgula.execute(sql_sorgusu) # Sql dilinde yazılmış bu sorgu ile, önce notlar tablosu oluşturulmuş mu bakıyoruz. Eğer yoksa oluşturuyoruz.
        sorgula.execute("SELECT * FROM notlar")#Sql dilinde yazılan sorgumuz ile notlar isimli tablodan verileri alıyoruz
        satirlar = sorgula.fetchall() #Tüm verileri satirlar isimli listeye yazıyoruz. 
 #burda data_items kv tarafındaki RecycleView in kullandığı liste. Önce bunu temizliyoruz
        self.data_items.clear()
        print(self.data_items)
        # For döngüsü ile data_items listesine verileri yazıyoruz.
        for i in satirlar:
            d = {'text':str(i[1]), 'id':i[0]}
            self.data_items.append(d)
        print(self.data_items)
        self.ids.rv.data = [{'text': (str(x['text'])[:20] + '..') if len(str(x['text'])) > 15 else str(x['text']), 'id': str(x['id']), 'textLong': str(x['text'])} for x in self.data_items]
        self.ids.rv.refresh_from_data()   
class NotesScreen(Screen):
    window_sizes=Window.size[1]/5.7
    window_sizesx=Window.size[1]/10
    def ekle(self):
        print(secili_id)
        if secili_id  == "bos":
            note = [self.ids.metin.text] #veritabanına yazacağım yazı             
            sorgula.execute("insert into notlar(note) values(?)",(note)) #Sql dilinde, veritabanındaki tabloya satır ekleme komutu
            #self.notlari_al() # veritabanına eklenen satırı RecycleView e de eklemek için bu fonksiyonu tekrar çağırıyoruz.
            baglanti.commit()
        else:
            sorgula.execute("update notlar set note = (?) where id = (?)",[(self.ids.metin.text),(secili_id)])
            baglanti.commit()
        ScreenManager.get_screen(App.get_running_app().py,"AnasayfaScreen").notlari_al()
            
    def sil(self):
        if secili_id != 'bos':
            sorgula.execute("delete from notlar where id = (?)",[secili_id])
            baglanti.commit()
        ScreenManager.get_screen(App.get_running_app().py,"AnasayfaScreen").notlari_al()

class deneme(App):
    secili_metin = StringProperty('')
    def build(self):
        self.py=ScreenManager()
        self.py.add_widget(AnasayfaScreen(name='AnasayfaScreen'))
        self.py.add_widget(NotesScreen(name='NotesScreen'))
        from kivy.core.window import Window
        Window.clearcolor = (0.60, 0.63, 0.62, 1)
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        return self.py

    def hook_keyboard(self, window, key, *largs):
        if key == 27:

            self.py.current = 'AnasayfaScreen'
        # do what you want, return True for stopping the propagation
        return True     
if __name__ == "__main__":
    Window.clearcolor = (1,0.5,1,0)

    deneme().run()