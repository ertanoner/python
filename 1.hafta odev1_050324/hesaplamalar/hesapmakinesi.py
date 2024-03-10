def hmmenu():

    print("╔════════════════════════════════════════╗")
    print("║ HESAP MAKİNESİ                         ║")
    print("║                                        ║")
    print("║ 1. TOPLAMA                             ║")
    print("║ 2. ÇIKARMA                             ║")
    print("║ 3. ÇARPMA                              ║")
    print("║ 4. BÖLME                               ║")
    print("║                                        ║")
    print("║    SEÇİMİNİZ?                          ║")
    print("╚════════════════════════════════════════╝")
    secim = input()
    if secim == "1" :
            S1 = float(input("1. sayıyı giriniz:" ))
            S2 = float(input("2. sayıyı giriniz:" ))
            toplam = S1+S2
            print("Toplam:",toplam)
    if secim == "2" :
            S1 = float(input("1. sayıyı giriniz:" ))
            S2 = float(input("2. sayıyı giriniz:" ))
            fark = S1-S2
            print("Fark:",fark) 
    if secim == "3" :
            S1 = float(input("1. sayıyı giriniz:" ))
            S2 = float(input("2. sayıyı giriniz:" ))
            carpim = S1*S2
            print("Çarpım:",carpim)
    if secim == "4" :
            S1 = float(input("1. sayıyı giriniz:" ))
            S2 = float(input("2. sayıyı giriniz:" ))
            bolum = S1/S2
            print("Bölüm:",bolum) 
    input()
