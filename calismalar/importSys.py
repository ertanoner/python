import os
os.system("color")
COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
    "BORDO": "\033[31m",
}
print(COLOR["GREEN"], "Yeşil yazı", COLOR["ENDC"])
print(COLOR["BLUE"], "Mavi yazı", COLOR["ENDC"])
print(COLOR["HEADER"], "pembe", COLOR["ENDC"])
print(COLOR["BORDO"], "Bordo", COLOR["BLUE"],"Mavi", COLOR["ENDC"])