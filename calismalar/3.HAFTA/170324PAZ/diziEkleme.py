corbalar = ["Tarhana","Mercimek"]
#print(corbalar)
# print(corbalar[1])

yemek1 = "Makarna"
yemek2 = "Mantı"
yemek3 = "Döner"
yemekler = [yemek1,yemek2,yemek3]
#print(yemekler)

ey = input("Eklenecek yemek nedir?")
# yemekler.append(ey)  #append dizinin sonuna ekleme
yemekler.insert(1,ey)   # yeni eklenecek veri 1 numaralı indis olup diğerlerini kaydıracak

print("\nÇORBALAR.")
for a in corbalar:
    print(a)


print("\nYEMEKLER:")
for a in yemekler:
    print(a)

#print(yemekler[-1])
#print(yemekler[-2])