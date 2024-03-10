import yilanOyunu

def oyun():

    print("╔════════════════════════════════════════╗")
    print("║ OYUNLAR                                ║")
    print("║                                        ║")
    print("║ 1. YILAN                               ║")
    print("║ 2. ADAM ASMACA                         ║")
    print("║ 3. RAID                                ║")
    print("║ 4. ATEŞ                                ║")
    print("║                                        ║")
    print("║SEÇİMİNİZ?                              ║")
    print("╚════════════════════════════════════════╝")
    secim = input()
    if secim == "1" :
        yilanOyunu.yilan()
        oyun()
    elif secim == "2" :
        