#oyun menusu
import hesaplamalar.tetris
import hesaplamalar.yilanOyunu
import hesaplamalar.adamAsmaca
import hesaplamalar.amiralBatti

def oyun():

    print("╔════════════════════════════════════════╗")
    print("║ OYUNLAR                                ║")
    print("║                                        ║")
    print("║ 1. YILAN                               ║")
    print("║ 2. TETRIS                              ║")
    print("║ 3. ADAM ASMACA                         ║")
    print("║ 4. AMIRAL BATTI                        ║")
    print("║                                        ║")
    print("║SEÇİMİNİZ?                              ║")
    print("╚════════════════════════════════════════╝")
    secim = input()
    if secim == "1" :
        hesaplamalar.yilanOyunu.yilan()
        oyun()
    if secim == "2" :
        hesaplamalar.tetris.tetris()
        oyun()
    if secim == "3" :
        hesaplamalar.adamAsmaca.adam()
        oyun()
    if secim == "4" :
        hesaplamalar.amiralBatti.amiral()
        oyun()