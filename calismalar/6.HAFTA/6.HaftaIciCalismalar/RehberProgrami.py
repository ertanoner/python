# Rehber Programı Ödev-2
import re, json, ast
def RehberMenu()
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
        listele(); RehberMenu()
    if secim=="2":
        listele(); RehberMenu()
    if secim=="3":
        ara(); RehberMenu()
    if secim=="4":
        duzelt(); listele()
        RehberMenu()
    if secim=="5":
        sil(); listele(); RehberMenu()
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
    dosya.write(str({"adi":ad,"num":nu})+",")
    # dosya.write(str({"id":ks,"adi":ad,"num":nu})+",")
    dosya.close()