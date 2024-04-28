## pyqt5 commentler  https://realpython.com/python-menus-toolbars/
# 
# örnek 1
# from PyQt5.QtWidgets import *
# app = QApplication([])
# pencere = QWidget()
# pencere.show()
# pencere.setWindowTitle('Deneme')
# pencere.resize(300,50)    #pencere boyutunu 300x50 açar, istersek boyutu mouse ile değiştirebiliriz
# # pencere.setFixedSize(100, 100)   #pencere boyutu sabit kalir
# app.exec()  # exec komutu pencereyi ekranda tutar.


# # örnek 2
# import sys
# from PyQt5.QtWidgets import *
# app = QApplication(sys.argv)
# window = QMainWindow()
# window.show()
# # Start the event loop.
# app.exec()


# # örenk 3
# import sys
# # from PyQt5.QtWidgets import QApplication, QPushButton
# from PyQt5.QtWidgets import *
# app = QApplication(sys.argv)
# window = QPushButton("Tıkla")
# window.show()
# app.exec()

# ## örnek 4
# # PyQt6 yı import et
# from PyQt6.QtWidgets import *
# # Uygulama oluşturma
# app = QApplication([])
# # buraya araçlar(widgets) ekleme
# label = QLabel('Merhaba!')
# label.show()
# # Uygulamayı çalıştırma
# app.exec()


# # örnek 5 - Ekrana düğme(buton) ve etiket (label) ekleyin
# import sys
# from PyQt6.QtWidgets import *
# app = QApplication(sys.argv)
# x = QWidget()
# x.show()  
# window1 = QPushButton("Tıkla")
# window1.show()  
# aa = QLabel("Merhaba")
# aa.show()
# app.exec()



# # örnek 6 -  Buton ekleyelim
# from PyQt6.QtWidgets import *
# aa = QApplication([])
# ww = QWidget()
# #icerik = QVBoxLayout()  # Q vertical box layout ından çoğaltılan içerik
# icerik = QHBoxLayout()  # Q horizontal box layout ından çoğaltılan içerik
# icerik.addWidget(QPushButton('Tıkla'))
# icerik.addWidget(QPushButton('Dene'))
# icerik.addWidget(QLabel('Bilgi'))
# ww.setLayout(icerik)  #w ana penceredir.
# ww.show()
# aa.exec()


# # örnek 7 - Tıklama algılama
# from PyQt6.QtWidgets import *
# app = QApplication([])
# button = QPushButton('Click')
# def on_button_clicked():
#     alert = QMessageBox()
#     alert.setText('Tıkladın!')
#     alert.exec()

# button.clicked.connect(on_button_clicked)
# button.show()
# app.exec()


# # örnek 8

# from PyQt6.QtWidgets import *
# aa = QApplication([])
# ww = QWidget()  #pencere
# ww1 = QWidget()  #pencere

# def icerikOlustur(xx):
#     xx.addWidget(QLabel('Kullanici Adi:'))
#     xx.addWidget(QLineEdit('Kullanici Adiniz....'))
#     xx.addWidget(QLabel('Sifre:'))
#     xx.addWidget(QLineEdit())
#     xx.addWidget(QPushButton('Giriş yap'))

# icerik = QVBoxLayout()
# icerikOlustur(icerik)
# ww.setLayout(icerik)
# ww.show()  

# icerik2 = QHBoxLayout()
# icerikOlustur(icerik2)
# ww1.setLayout(icerik2)
# ww1.show()  

# aa.exec()



# # örnek 9  sınıfsız gösterim

# from PyQt6.QtWidgets import *

# uygulama = QApplication([])

# pencere = QMainWindow()
# pencere.setWindowTitle("Çeviri")

# icerik = QVBoxLayout()
# # icerik = QHBoxLayout()
# icerik.addWidget(QLabel("Çevrilecek: "))
# icerik.addWidget(QLineEdit())
# icerik.addWidget(QPushButton("Çevir"))
# icerik.addWidget(QLabel("Sonuç: "))

# araclar = QWidget()
# araclar.setLayout(icerik)
# pencere.setCentralWidget(araclar)
# pencere.show()

# uygulama.exec()


# # örenk sınıflı gösterim

# from PyQt6.QtWidgets import *

# class ceviriPenceresi(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Çeviri")

#         icerik = QVBoxLayout()
#           #icerik = QHBoxLayout()
#         icerik.addWidget(QLabel("Çevrilecek: "))
#         icerik.addWidget(QLineEdit())
#         icerik.addWidget(QPushButton("Çevir"))
#         icerik.addWidget(QLabel("Sonuç: "))
#         araclar = QWidget()
#         araclar.setLayout(icerik)
#         self.setCentralWidget(araclar)

# uygulama = QApplication([])

# pencere = ceviriPenceresi()
# pencere2 = ceviriPenceresi()
# pencere3 = ceviriPenceresi()

# pencere.show()
# pencere2.show()
# pencere3.show()

# uygulama.exec() 






# şifre ile Rehber menu açılımı Box lı - örnek sınıflı gösterim

from PyQt6.QtWidgets import *
import re,json,ast,io

def sifreOlustur():
    kullaniciAdi="adm"
    sifre = "123"
    
    dosya = open("rehberpwd.txt","w")
    dosya.write(f"{kullaniciAdi} {sifre}")
    dosya.close()
    
 
    
class Ekleme(QMainWindow):
    def __init__(self,xx="Ekleme"):
        super().__init__()
        self.setWindowTitle(xx)      
    
     
          
        icerik = QVBoxLayout()   
        icerik.addWidget(QLabel('İsminizi Giriniz:')) # vertical box a bir widget ekledik.
        self.edit1 = QLineEdit()
        icerik.addWidget(self.edit1)
        icerik.addWidget(QLabel('Soyadınızı Giriniz:')) 
        self.edit2 = QLineEdit()
        icerik.addWidget(self.edit2)
        icerik.addWidget(QLabel('Telefon Numaranızı Giriniz:')) 
        self.edit3 = QLineEdit()
        icerik.addWidget(self.edit3)
        
        self.dugme1 = QPushButton('Kişi ekle')
        icerik.addWidget(self.dugme1)
        
        araclar = QWidget()  # QWidget ten bir kalıp oluşturduk.
        araclar.setLayout(icerik) 
        self.setCentralWidget(araclar)
        self.dugme1.clicked.connect(self.ekle)  #) aşağıdaki def fonksiyonunu çağırıyor.
  
    def ekle(self): 
        
        t1 =  self.edit1.text()
        t2 =  self.edit2.text()
        t3 =  self.edit3.text()
        print("ekle çalıştır",t1,t2,t3) 
        dosya=open("rhbgirilenpwd.txt","a")
        dosya.write(f"{t1} {t2} {t3}")
        dosya.close()
        
                   
    #     if devam_mi():
    #         continue
    #     else:
    #         break
        
    # def devam_mi():
    #     a = input("yeni kayit girmek istiyor musunuz? (evet,hayir): ")
    #     if a.lower().startswith("e"):
    #         return True
    #     else:
    #         False  

    
class anaEkran(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle(xx)  

        icerik = QVBoxLayout()   
        self.dugme1 = QPushButton('Ekle')
        icerik.addWidget(self.dugme1)
        self.dugme2 = QPushButton('Listele')
        icerik.addWidget(self.dugme2)
        self.dugme3 = QPushButton('Sil')
        icerik.addWidget(self.dugme3)
        
        self.dugme1.clicked.connect(self.ekle)
        self.dugme2.clicked.connect(self.listele)
        self.dugme3.clicked.connect(self.silme)

        araclar = QWidget() 
        araclar.setLayout(icerik) 
        self.setCentralWidget(araclar)
        
    def ekle(self):
        print("Ekleme tıklandı")
        self.close()
        self.ap = Ekleme()  #☺ ekleme class ı oluşturacağız yukarıda
        self.ap.show()

    def listele(self):
        print("Listeleme tıklandı")
        
    def silme(self):
        print("Silme tıklandı")

class loginPenceresi(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle(xx)   #QMainWindow e ait self 

        icerik = QVBoxLayout()   # sınıftan nesne örneği çıkarıyoruz. sınıf: QVBoxLayout() , bundan icerik isimli nesne örenği oluşturduk.
        icerik.addWidget(QLabel('Kullanıcı adı:')) # vertical box a bir widget ekledik.
        self.edit1 = QLineEdit('\nKullanıcı adınız...')
        icerik.addWidget(self.edit1)
        icerik.addWidget(QLabel('Şifre:'))
        self.edit2 = QLineEdit('..Sifreniz...')
        icerik.addWidget(self.edit2)
        self.dugme1 = QPushButton('Giriş yap')
        icerik.addWidget(self.dugme1)

        self.dugme1.clicked.connect(self.kontrolEt)
       
        araclar = QWidget()  # QWidget ten bir kalıp oluşturduk.
        araclar.setLayout(icerik) 
        self.setCentralWidget(araclar)

    def kontrolEt(self):
        print("Düğmeye tıklandı.")   
        t1 =  self.edit1.text()
        t2 =  self.edit2.text()
        print("Edit1 içeriği", t1)
        dosya=open("rhbgirilenpwd.txt","a")
        dosya.write(f"{t1} {t2}")
        dosya.close()
        
        if t1 == "adm" and t2 == "11" :      # sifre ekleme
            print("Giriş ok")
            self.close()
            self.ap = anaEkran()
            self.ap.show()
        else:
            print("İzin yok")
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Bilgilendirme!")
            dlg.setText("İzin yok")
            dlg.exec()    

sifreOlustur()

uygulama = QApplication([])
pencere = loginPenceresi("Giriş1")
# anaPencere = anaEkran("MENU")
pencere.show()
# anaPencere.show()
uygulama.exec()
# self.edit2.setEchoMode(QLineEdit.EchoMode.Password)