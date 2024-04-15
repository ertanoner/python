# Rehber Programı Ödev-2
import re, json, ast
def Rehbermenu():
    print("╔═════════════════════╗")
    print("║  REHBER PROGRAMI    ║")
    print("║                     ║")
    print("║  1-Kişi ekle        ║")
    print("║  2-Listele          ║")
    print("║  3-Kişi Ara         ║")
    print("║  4-Veri Düzelt      ║")
    print("║  5-Kişi Sil         ║")
    print("║  ç-Çıkış            ║")
    print("║                     ║")
    print("║  Seçimiz nedir?     ║")
    print("╚═════════════════════╝")
    secim = input("")
    if secim=="1":
        listele(); kisiEkle()
        listele(); Rehbermenu()
    if secim=="2":
        listele(); Rehbermenu()
    if secim=="3":
        ara(); Rehbermenu()
    if secim=="4":
        duzelt(); listele()
        Rehbermenu()
    if secim=="5":
        sil(); listele(); Rehbermenu()
        
def kisiEkle():
    dosya = open("RehberProgrami.txt","a")
    print("╠════════╣ KİŞİ EKLEME ╠════════╣")
    ad = input("Kaydedilecek ad ve soyad :")
    nu = input("Kaydedilecek numara      :")
    # kayitSayisi = dosya.read()
    # kayitSayisi = ast.literal_eval(kayitSayisi)
    # dosya.close()

    # veri = {"adi":ad,"num":nu}
    # dosya.write(f"{ad},{nu},")
    # ks = kayitSayisi+1
    # print(f"Veri {len(kayitSayisi)+1}.kayit olarak eklendi")
    # dosya.write(f'\n{str({"adi":ad,"numara":nu})},')
    
    dosya.write(str({"adi":ad,"num":nu})+",")
    dosya.close()
    
        # dosya.write(f'\n{str({"adi":ad,"num":no, "Kayıt Tarihi":bugun})},')
        # klasor.write(f'\n{str({"adi":ad,"numara":numara})},')

def listele():
    # try:
    #     with open("RehberProgrami.txt", "r") as dosya:
    #         okunan = dosya.read()
    #     print("╠═════╣ KİŞİ LİSTELEME ╠═════╣")

    #     cevirilen = ast.literal_eval(okunan)
    #     print(cevirilen)

    # except 
    #     print("Bir hata oluştu")    
        
        with open("RehberProgrami.txt", "r") as dosya:
            okunan = dosya.read()
        print("╠═════╣ KİŞİ LİSTELEME ╠═════╣")

        cevirilen = ast.literal_eval(okunan)
        print(cevirilen)      
        
def ara():
    with open("RehberProgrami.txt", "r") as dosya:
        okunan = dosya.read()
    print("╠════════════╣ KİŞİ ARAMA ╠════════════╣")
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Aranan isim nedir?")
    for a in cevirilen:
        if a["adi"]==aranan: print(a)
        
def duzelt():
    with open("RehberProgrami.txt", "r") as dosya:
        okunan = dosya.read()
    print("╠════════════╣ KİŞİ DÜZELTME ╠════════════╣")
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Düzeltilecek isim nedir? ")
    dosya.close()
    with open("RehberProgrami.txt","w") as dosya:
        for a in cevirilen:
            if a["adi"]==aranan:
                print(a)
                yeniAd = input("Yeni ad nedir? ")
                yeniNo = input("Yeni no nedir? ")
                a["adi"]=yeniAd
                a["num"]=yeniNo
            dosya.write(f"{str(a)},") 
            
def sil():
    with open("RehberProgrami.txt", "r") as dosya:
        okunan = dosya.read()
    print("╠════════════╣ KİŞİ SİLME ╠════════════╣")
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Silinecek isim nedir? ")
    dosya.close()
    with open("RehberProgrami.txt","w") as dosya:
        for a in cevirilen:
            if a["adi"]!=aranan:
                dosya.write(f"{str(a)},")       
        
        
Rehbermenu()