## şifre ile Rehber menu açılımı Box lı - örnek sınıflı gösterim #

from PyQt6.QtWidgets import *
from PyQt5.QtWidgets import *
import re,json,ast,io

def sifreOlustur():
    kullaniciAdi="adm"
    sifre = "123"
    
    # dosya = open("rehberpwd.txt","w")
    # dosya.write(f"{kullaniciAdi} {sifre}")
    # dosya.close()
    
 
    
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
        dosya.write(f"{t1} {t2} {t3}\n")
        dosya.close()
    

    
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
        # dosya=open("rhbgirilenpwd.txt","a")
        # dosya.write(f"{t1} {t2}")
        # dosya.close()
        
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