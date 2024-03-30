#yazarken string e çecirmek gerekir.
ad = no = " "  # while da hiçbirşey yoksa çalıştırma dedik, başlangıçta birşey olsun diye boşluk ekledik.

dosya = open("dosyalar/rehber.txt","a") # dosyalar klasörünü python un çalışma dosyasının içinde biz oluşturacağız.
while ad != "" or no != "" :
    
    ad = input("Kaydedilecek kişi adı:")
    no = input("Kaydedilecek no:      ")

    ogrenci = {
    "Adi" : ad ,
    "Numarasi" : no
    }
    dosya.write(f"{str(ogrenci)},\n")

dosya.close()


okunan = open("dosyalar/rehber.txt")
bb=okunan.readlines()
aa = bb

for a in aa:
    print(a)
okunan.close()