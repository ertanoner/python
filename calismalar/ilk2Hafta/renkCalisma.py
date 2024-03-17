import os
os.system("color")
COLOR = {
    "BLUE": "\033[34m",
    "ENDC": "\033[0m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
}
print(COLOR["BLUE"], "blue" , COLOR["ENDC"])
print ("\n")
input()