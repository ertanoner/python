﻿import hesaplamalar.cokgen
import hesaplamalar.prizma

def sekiller():

    print("╔════════════════════════════════════════╗")
    print("║ GEOMETRİK ŞEKİLLER                     ║")
    print("║                                        ║")
    print("║ 1. ÜÇGEN                               ║")
    print("║ 2. KARE                                ║")
    print("║ 3. DİKDÖRTGEN                          ║")
    print("║ 4. ÇOKGEN                              ║")
    print("║ 5. PRİZMA                              ║")
    print("║                                        ║")    
    print("║    SEÇİMİNİZ?                          ║")
    print("╚════════════════════════════════════════╝")
    secim = input()
    if secim == "4" :
        hesaplamalar.cokgen.cokgen()
        anamenu()
    elif secim == "5" :
        hesaplamalar.prizma.prizma()
        anamenu()