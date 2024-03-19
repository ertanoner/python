import hesaplamalar.yilanOyunu

def oyun():

    print("╔════════════════════════════════════════╗")
    print("║ OYUNLAR                                ║")
    print("║                                        ║")
    print("║ 1. YILAN                               ║")
    print("║ 2. PACMAN                              ║")
    print("║ 3. RAID                                ║")
    print("║ 4. ATEŞ                                ║")
    print("║                                        ║")
    print("║SEÇİMİNİZ?                              ║")
    print("╚════════════════════════════════════════╝")
    secim = input()
    if secim == "1" :
        hesaplamalar.yilanOyunu.yilan()
        
