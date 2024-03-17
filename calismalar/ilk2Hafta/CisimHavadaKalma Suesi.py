#h yüksekliğinden t saniyede yere düşüp kalan cisim hesabı: h=½*g*t2 
t = float(input("cisim kaç saniyede tamamiyle yere düşüp kalıyor?"))
h = 0.5*9.81*t**2
print("Cisim {} metre yükseklikten düşmüştür.".format(h))
input()

import math
h = float(input("cisim kaç metre yükseklikten düşüyor?: "))
t = float(math.sqrt(h/(9.81*0.5)))
print("Cisim {} metre yükseklikten {} saniyede yere düşüp kalıyor.".format(h,t))
input()