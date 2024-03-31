#dosyalar adlı klasör vs code un çalıştığı klasörün altında var mı diye kontrol ediyor.
import os
liste = os.listdir()
durum = "yok"
for a in liste:
    if a == "dosyalar": durum = "var"
    
    
print(durum)

