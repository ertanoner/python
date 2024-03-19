6##print("\033[1;32;40m")
# 201 ╔
# 205 ═
# 187 ╗
# 186 ║
# 200 ╚
# 188 ╝
import hesaplamalar.hesapmakinesi
import hesaplamalar.yas_hesabi
import hesaplamalar.oyunlar
import hesaplamalar.cisimHavadaKalmaSuesi
import hesaplamalar.harfnotu
import hesaplamalar.dovizKURU
import hesaplamalar.programlama_dilleri
import hesaplamalar.geometrik_sekiller
import hesaplamalar.arabalar
import hesaplamalar.renk_secimi


def anamenu():

    print("╔════════════════════════════════════════╗")
    print("║ VEKTOREL 1. PROJE                      ║")
    print("║                                        ║")
    print("║ 1.  HESAPMAKİNESİ                      ║")
    print("║ 2.  YAŞ HESABI                         ║")
    print("║ 3.  OYUNLAR                            ║")
    print("║ 4.  CİSMİN DÜŞME SÜRESİ                ║")
    print("║ 5.  PUAN HARF NOTU BELİRLEME           ║")
    print("║ 6.  DÖVİZ KUR ÇEVİRİCİSİ               ║") 
    print("║ 7.  PROGRAMLAMA DİLLERİ HAKINDA BİLGİ  ║")
    print("║ 8.  GEOMETRİK ŞEKİLLER                 ║")
    print("║ 9.  OTOMOBİL MARKALARI                 ║")  
    print("║ 10. RENK SEÇİMİ                        ║")
    print("║                                        ║")      
    print("║ ç  : ÇIKIŞ                             ║")
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
        hesaplamalar.cisimHavadaKalmaSuesi.cisim()
        anamenu()
    elif secim == "5" :
        hesaplamalar.harfnotu.harfnotu()
        anamenu()
    elif secim == "6" :
        hesaplamalar.dovizKURU.doviz()
        anamenu()
    elif secim == "7" :
        hesaplamalar.programlama_dilleri.diller()
        anamenu()
    elif secim == "8" :
        hesaplamalar.geometrik_sekiller.sekiller()
        anamenu()
    elif secim == "9" :
        hesaplamalar.arabalar.arabalar()
        anamenu()
    elif secim == "10" :
        hesaplamalar.renk_secimi.renk()
        anamenu()
    elif secim == "ç" : exit()
anamenu()