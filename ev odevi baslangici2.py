##print("\033[1;32;40m")
# 201 ╔
# 205 ═
# 187 ╗
# 186 ║
# 200 ╚
# 188 ╝
import hesaplamalar.hesapmakinesi
import hesaplamalar.input2_toplam
print("╔════════════════════════════════════════╗")
print("║ VEKTOREL DERS                          ║")
print("║                                        ║")
print("║ 1. HESAPMAKİNESİ                       ║")
print("║ 2. YAŞ HESABI                          ║")
print("║ 3. ÇİZİMLER                            ║")
print("║ 4. SAĞLIK                              ║")
print("║                                        ║")
print("║ 5. SEÇİMİNİZ?                          ║")
print("╚════════════════════════════════════════╝")   
secim = input()
if secim == "1" :
    hesaplamalar.hesapmakinesi.hmmenu()
elif secim == "2" :
    hesaplamalar.input2_toplam.yhesap()
 
    
