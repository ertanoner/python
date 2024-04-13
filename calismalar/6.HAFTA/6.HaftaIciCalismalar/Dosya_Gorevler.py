#  #  Dosya oluşturma ve yazma GÖREVLER-1

# dos=open("rehber.tel", "w")
# dos.close()

# #  Dosya oluşturma ve yazma GÖREVLER-2
# ad = input("Kaydedilecek kişi adı ve soyadı:      ")
# no = input("Kaydedilecek kişi numarası: ")

# dosya = open("rehber.tel","a")

# dosya.write(f'\n{str({"adi":ad,"num":no})},')
# dosya.close()


# # Dosya oluşturma ve yazma GÖREVLER-3

# ad = input("Kaydedilecek kişi adı ve soyadı:      ")
# no = input("Kaydedilecek kişi numarası: ")

# dosya = open("rehber.tel","a")

# dosya.write(f'\n{str({"adi":ad,"num":no})},')
# dosya.close()

# okunan = open("rehber.tel","r")
# print(okunan.read())
# okunan.close()

# #  Dosya oluşturma ve yazma GÖREVLER-4

# ad = input("Adınızı giriniz..:")
# kla = open("merhaba.py","w")
# kla.write(f'print("Merhaba {ad}")')
# kla.close()

# #  Dosya oluşturma ve yazma GÖREVLER-5
# fas = open("ertan.txt", "w")
# fas.write("Adı:Ertan Öner, Sınıfı:10/A, Numarası:6106 ")
# fas.close()


# # Dosya oluşturma ve yazma GÖREVLER-6 - Kayıt tarihinde datetime.date komut satırı da çıkıyor. Sorulacak.

# import datetime
# bugun = datetime.date.today()
# ad = input("Kaydedilecek kişi adı ve soyadı:      ")
# no = input("Kaydedilecek kişi numarası: ")

# dosya = open("rehber.dat","a")

# dosya.write(f'\n{str({"adi":ad,"num":no, "Kayıt Tarihi":bugun})},')

# dosya.close()

# okunan3 = open("rehber.dat","r")
# print(okunan3.read())
# okunan3.close()




# # Dosya oluşturma ve yazma GÖREVLER-7

# for a in range(100):
#     dosya = open(f"vektorel-{a+1}.txt","w")
#     dosya.close()





# #  Dosya oluşturma ve yazma GÖREVLER-8   kayitSayisi çalışmadı, random numaranın tekrar verilmesi engellenmeli
# import random
# import ast
# ad = input("Kaydedilecek kişi adı ve soyadı:      ")
# numara = random.randint(100, 1000)

# klasor = open("ogrenciler.txt","a")
# klasor.write(f'\n{str({"adi":ad,"numara":numara})},')
# klasor.close()

# okunan = open("ogrenciler.txt","r")
# print(okunan.read())
# okunan.close()

###Bu kısım çalışmadı
# kayitSayisi = okunan.read()
# cevirilen = ast.literal_eval(kayitSayisi)
# print(f"Veri {len(cevirilen)+1}.kayit olarak eklendi")
# okunan.close()

# Dosya oluşturma ve yazma GÖREVLER-9    input ile girilen ismi dosya ismi olarak yazdıramadım.

# isim = input("İsminizi giriniz: ")
# dosya = open(+isim+".txt","w")
# dosya.write(f'{str({"Adınız:" :isim})}')
# dosya.close()



#    S1 = float(input("1. degeri giriniz:"))
#     S2 = float(input("2. degeri giriniz:"))
#     T = float(S1+S2)
#     F = float(S1-S2)
#     print("Toplam:{} , Fark:, {}".format(T,F))
