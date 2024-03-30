#yazarken string e çecirmek gerekir.
ogrenciler = ["Mahir", "Barış", "Şeyma", "Metin","Ertan"]
dosya = open("deneme3.txt","w")
dosya.write(str(ogrenciler))
dosya.close()

okunan = open("deneme3.txt")
liste = okunan.read()
print(liste)
okunan.close()