def harfnotu():
    print("Bu fonksiyon harf notu hesaplar")
    DN = int(input("Ders notunu giriniz: "))
    if DN > 100 or DN < 0 :print("Girilen not 1-100 arasında olmalıdır.")
    else:
        if DN> 84 :print("A aldınız, tebrikler")
        if DN< 85 and DN> 69 :print("B aldınız")
        if DN< 70 and DN> 54 :print("C aldınız")
        if DN< 55 and DN> 45 :print("D aldınız, sorumlu geçtiniz")
        if DN< 45 :print("E aldınız, kaldınız")
harfnotu()            
