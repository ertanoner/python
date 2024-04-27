# pyqt5 commentler  https://realpython.com/python-menus-toolbars/
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

# örnek sınıflı gösterim

from PyQt6.QtWidgets import *

class loginPenceresi(QMainWindow):
    def __init__(self,xx="Başlıksız"):
        super().__init__()
        self.setWindowTitle(xx)

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel('Kullanıcı adı:'))
        icerik.addWidget(QLineEdit('Kullanıcı adınız...'))
        icerik.addWidget(QLabel('Şifre:'))
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QPushButton('Giriş yap'))

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

uygulama = QApplication([])
pencere = loginPenceresi("Giriş")
pencere.show()
uygulama.exec()
