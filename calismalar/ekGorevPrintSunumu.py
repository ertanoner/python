import os
os.system("color")
COLOR = {
    "BLUE": "\033[94m",
    "ENDC": "\033[0m",
    "BORDO": "\033[31m",
}
print(COLOR["BORDO"], "Bordo", COLOR["BLUE"],"Mavi", COLOR["ENDC"])
print ("\n")

for i in range(30,37):
    print (f"\033[1;{i};40m Rengarenk  \n")
print (COLOR["ENDC"])

cevap = str(input("Almanya'nın başkentini küçük harflerle yazınız:"))
if cevap == "berlin" : print(COLOR["BLUE"],"Doğru")
else : print(COLOR["BORDO"],"Yanlış")
print (COLOR["ENDC"])
print ("\n")
