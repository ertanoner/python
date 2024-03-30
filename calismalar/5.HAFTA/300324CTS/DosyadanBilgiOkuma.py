#deneme1.txt dosyasını okuyup hata var mı diye kontrol ediyor. Varsa çalışır, yoksa veya dosya ismi farklı ise orjinal hata yazısı yerine "bir hata oluştu" diye metin çıkar 
try:
    okunan = open("deneme1.txt","r")
    print(okunan.read())
    okunan.close()
except:
    print("Bir hata oluştu.")
