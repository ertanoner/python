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



# örnek 6 -  Buton ekleyelim
from PyQt6.QtWidgets import *
aa = QApplication([])

ww = QWidget()

#icerik = QVBoxLayout()  # Q vertical box layout ından çoğaltılan içerik
icerik = QHBoxLayout()  # Q horizontal box layout ından çoğaltılan içerik

icerik.addWidget(QPushButton('Tıkla'))
icerik.addWidget(QPushButton('Dene'))
icerik.addWidget(QLabel('Bilgi'))

ww.setLayout(icerik)  #w ana penceredir.

ww.show()
aa.exec()


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


