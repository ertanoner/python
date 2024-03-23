#ev ödevi - bitmedi

import datetime, random
bugun = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
yil = int(datetime.datetime.now().strftime("%Y"))
ay = int(datetime.datetime.now().strftime("%m"))
gun = int(datetime.datetime.now().strftime("%d"))
print("Tarih saat =",bugun)
dgunu = input("Doğum tarihin nedir? (01.01.2000 gibi yaz)")
print(dgunu)
dyil = int(dgunu[6:10])  #input yapılan tarihin indis numaralarını giriyoruz.
day1 = int(dgunu[3:5])
dgun = int(dgunu[0:2])
print(dyil,day1,dgun)

yyil = 0
if ay>day1: 
    yyil = yil-dyil
    print("Yaşadığın yıl:",yyil)
else:
    yyil = yil-dyil-1    
    print("Yaşadığın yıl:",yyil)

print("Yaşadığın gün:",yyil*365)     

yay = 0
if gun>dgun:
    yay = ay-day1
    print(f"Yaşadığın yıl {yyil} ve yaşadığın ay {yay}")
else:
    yay = ay-day1-1
    print(f"Yaşadığın yıl {yyil} ve yaşadığın ay {yay}")    

