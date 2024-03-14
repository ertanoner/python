import turtle

def ucgen():
    for a in range(3):
        turtle.forward(100)
        turtle.right(120)
       
def kare():
    for a in range(4):
        turtle.forward(100)
        turtle.right(90)
    
def dikdortgen():
        for a in range(2):
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(60)
            turtle.right(90)

def besgen():
    for a in range(5):
        turtle.forward(100)
        turtle.right(72)     
             
def altigen():
            for a in range(6):
                turtle.forward(100)
                turtle.right(60)
            
def sekiller():

    print("╔════════════════════════════════════════╗")
    print("║ GEOMETRİK ŞEKİLLER                     ║")
    print("║                                        ║")
    print("║ 1. ÜÇGEN                               ║")
    print("║ 2. KARE                                ║")
    print("║ 3. DİKDÖRTGEN                          ║")
    print("║ 4. BEŞGEN                              ║")
    print("║ 5. ALTIGEN                             ║")
    print("║                                        ║") 
    print("║ ç.ÇIKIŞ                                ║")     
    print("║    SEÇİMİNİZ?                          ║")
    print("╚════════════════════════════════════════╝")

    secim = input()
    if secim == "1" : ucgen()
    if secim == "2" : kare()
    if secim == "3" : dikdortgen()
    if secim == "4" : besgen()
    if secim == "5" : altigen()
    if secim == "ç" : exit()
    else : sekiller()

