#aylar ve 29 çeken şubat ayının liste şeklinde düzenlemesi çalışması eklenecek

import datetime, random

# aylar30 = [04,06,09,11]
# aylar29 = [02]
# aylar28 = [02]
# aylar31 = [01,03,05,07,08,10,12]
# artikYillar = [2024,2020,2016,2012,2008,2004,2000,1996,1992,1988,1984,1980,1976,1972,1968,1964,1960,1956,1952,1948,1944,1940,1936,1932,1928,1924,1920,1916,1912,1908,1904,1900]


bugun = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
yil = int(datetime.datetime.now().strftime("%Y"))
ay =  int(datetime.datetime.now().strftime("%m"))
gun = int(datetime.datetime.now().strftime("%d"))
print("Tarih saat =",bugun)
dgunu = input("Doğum tarihin nedir? (01.01.2000 gibi yaz)")
print(dgunu)
dyil = int(dgunu[6:10])
day = int(dgunu[3:5])
dgun = int(dgunu[0:2])

yeniay=ay
yeniyil=yil

if gun>=dgun : ygun = gun-dgun
else: ygun = gun+30-dgun; yeniay=ay-1

if yeniay>=day : yay=yeniay-day 
else: yay= yeniay+12-day; yeniyil=yil-1

yyil=yeniyil-dyil


print(f"{yyil} yıl {yay} ay ve {ygun} gündür hayattasınız.")








# yyil = 0
# if ay>day1: 
#     yyil = yil-dyil
#     print("Yaşadığın yıl:",yyil)
# else:
#     yyil = yil-dyil-1    
#     print("Yaşadığın yıl:",yyil)

# print("Yaşadığın gün:",yyil*365)     

# yay = 0
# if gun>dgun:
#     yay = ay-day1
#     print(f"Yaşadığın yıl {yyil} ve yaşadığın ay {yay}")
# else:
#     yay = ay-day1-1
#     print(f"Yaşadığın yıl {yyil} ve yaşadığın ay {yay}")    

