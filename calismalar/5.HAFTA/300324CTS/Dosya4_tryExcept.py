try:
    dosya = open("rehber.txt","r")
    print("   Rehber Kayıt Listesi ")        
    print("═════════════════════════════")
    a = 1        
    for kayit in dosya.readlines():
        print(a, kayit)
        a += 1
except:
    print("Dosya bulunamadı.")
    print("Devam etmek için Enter'a basın.")
    input()
