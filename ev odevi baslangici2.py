##print("\033[1;32;40m")
# 201 ╔
# 205 ═
# 187 ╗
# 186 ║
# 200 ╚
# 188 ╝
import hesaplamalar.hesapmakinesi
import hesaplamalar.yas_hesabi
import hesaplamalar.oyunlar
import hesaplamalar.renk_secimi
import hesaplamalar.ders_secimi
import hesaplamalar.para_birimleri

def anamenu():
    print("╔════════════════════════════════════════╗")
    print("║ VEKTOREL DERS                          ║")
    print("║                                        ║")
    print("║ 1. HESAPMAKİNESİ                       ║")
    print("║ 2. YAŞ HESABI                          ║")
    print("║ 3. OYUNLAR                             ║")
    print("║ 4. RENKLER                             ║")
    print("║ 5. DERS SEÇİMİ                         ║")
    print("║ 6. PARA BİRİMLERİ                      ║")
    print("║                                        ║")
    print("║    SEÇİMİNİZ?                          ║")
    print("╚════════════════════════════════════════╝")   
    secim = input()
    if secim == "1" :
        hesaplamalar.hesapmakinesi.hmmenu()
        anamenu()
    elif secim == "2" :
        hesaplamalar.yas_hesabi.yhesap()
        anamenu()
    elif secim == "3" :
        hesaplamalar.oyunlar.oyun()
        anamenu()
    elif secim == "4" :
        hesaplamalar.renk_secimi.renk()
        anamenu()
    elif secim == "5" :
        hesaplamalar.ders_secimi.ders()
        anamenu()
    elif secim == "6" :
        hesaplamalar.para_birimleri.para()
        anamenu()
anamenu()

        
        
