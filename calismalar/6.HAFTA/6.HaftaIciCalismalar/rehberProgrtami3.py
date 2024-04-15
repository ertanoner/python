import re,json,ast,io
dosya = open("RehberProgrami3.txt","a")
dosya.close()

def kayit_ekle(dosya):
    
    dosya = open("RehberProgrami3.txt","a")
    
    while True:
        isim = input("isim giriniz: ")
        soyad = input("soyad giriniz: ")
        numara = input("numara giriniz: ")
        
        
        dosya.write(str({"isim":isim,"soyad":soyad,"numara":numara})+",")
        
         
        if devam_mi():
            continue
        else:
            break
        
dosya.close()

def emin_misin():
    a = input("emin misin (evet,hayir): ")
    if a.lower().startswith("e"):
        return True
    else:
        False


def devam_mi():
    a = input("devam etmek istiyor musun (evet,hayir): ")
    if a.lower().startswith("e"):
        return True
    else:
        False
        



def kayit_listele(dosya):
    dosya = open("RehberProgrami3.txt","r")
    okunan = dosya.read()
    cevirilen = ast.literal_eval(okunan)
    print(cevirilen)
    

def kayit_ara(dosya):
    dosya = open("RehberProgrami3.txt","r")
    okunan = dosya.read()
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Aranan isim nedir?")
    for a in cevirilen:
        if a["isim"]==aranan: print(a)
        else : print("Bu isimde bir kayit yok.")
        break
      


def kayit_sil(dosya):
    dosya = open("RehberProgrami3.txt","r")
    okunan = dosya.read()
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Silinecek isim nedir? ")
    dosya.close()
    with open("RehberProgrami3.txt","w") as silme:
        for a in cevirilen:
            if a["isim"]!=aranan:
                silme.write(f"{str(a)},")  
     

dosya.close()

while True:
    a = int(input("""
    1) kayit ekle
    2) kayitlari listele
    3) kayit ara
    4) kayit sil
    5) çikiş
    
    """))
    if a == 1:
        kayit_ekle(dosya)
    elif a == 2:
        kayit_listele(dosya)
    elif a == 3:
        kayit_ara(dosya)
    elif a == 4:
        kayit_sil(dosya)
    elif a == 5:
        break