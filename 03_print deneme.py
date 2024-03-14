import turtle
import os
os.system("color")
COLOR = {
    "BLUE": "\033[94m",
    "ENDC": "\033[0m",
    "BORDO": "\033[31m",
    }
print(COLOR["BORDO"], "Bordo", COLOR["BLUE"],"Mavi", COLOR["ENDC"])
print ("\n")
for i in range(3):
    print (f"\033[1;{i};40m Rengarenk  \n")
    turtle.forward(100)
    turtle.right(120)

print (COLOR["ENDC"])