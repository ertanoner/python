import hesaplamalar.yilanOyunu
import hesaplamalar.tetris

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
        hesaplamalar.yilanOyunu.yilan()
        oyun()
    elif secim == "2" :
        hesaplamalar.tetris.tetris()
        oyun()