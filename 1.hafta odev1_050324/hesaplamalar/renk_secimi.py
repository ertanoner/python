"""class Colors:
    ANSI color codes 
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"  """

import os
os.system("color")
COLOR = {
    "BLUE": "\033[34m",
    "ENDC": "\033[0m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "PURPLE ": "\033[0;35m"
}
def renk():

    print("╔════════════════════════════════════════╗")
    print("║ RENKLER                                ║")
    print("║                                        ║")
    print("║ 1. MAVİ                                ║")
    print("║ 2. KIRMIZI                             ║")
    print("║ 3. YEŞİL                               ║")
    print("║ 4. SARI                                ║")
    print("║ 5. MOR                                 ║")
    print("║                                        ║")
    print("║SEÇİMİNİZ?                              ║")
    print("╚════════════════════════════════════════╝")
    secim = input()
    if secim == "1" :
        print(COLOR["BLUE"], "MAVİ", COLOR["ENDC"])
        print ("\n")
        input()
    elif secim == "2" :
        print(COLOR["RED"], "KIRMIZI", COLOR["ENDC"])
        print ("\n")
        input()
    elif secim == "3" :
        print(COLOR["GREEN"], "YEŞİL", COLOR["ENDC"])
        print ("\n")
        input() 
    elif secim == "4" :
        print(COLOR["YELLOW"], "SARI", COLOR["ENDC"])
        print ("\n")
        input()            
    elif secim == "5" :
        print(COLOR["PURPLE"], "MOR", COLOR["ENDC"])
        print ("\n")
        input()  