# import datetime
# print("Bugün:", datetime.date.today())  # Tarihi yazar

# from datetime import datetime
# print("Şimdi =", datetime.now())  #Şimdiki tarih ve saati gösterir

# import datetime
# print("Şimdi =", datetime.datetime.now())

# from datetime import datetime    #güncel saati gösteris
# for a in range (100000):
#   from datetime import datetime
#   print("Şimdi =", datetime.now())

# import datetime
# print("Tarih saat =", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))  #gün, ay, yıl, saat, dakika, saniye den istediklerimizi belirleyerek yazdırabiliriz


# import datetime
# print("Gün/Ay Dakika/Saniye =", datetime.datetime.now().strftime("%d/%m %M:%S")) 

# from datetime import date  #bugünü yazdırır.
# bg = date.today()
# print("Bugün:", bg)

import datetime
print("Yıl=", datetime.datetime.now().strftime("%Y")) 
a = datetime.datetime.now().strftime("%Y")               #şimdiki yıla 5 ekliyoruz
a = int(a)+5
print(a)

