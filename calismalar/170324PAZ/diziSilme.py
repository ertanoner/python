yemek1 = "Makarna"
yemek2 = "Mantı"
yemek3 = "Döner"
yemekler = [yemek1,yemek2,yemek3]
#print(yemekler)

#ey = input("Silinecek yemek indisi nedir?")
# yemekler.append(ey)  #append dizinin sonuna ekleme
# yemekler.pop()  # parantez içi boş ise en sondaki döner silinecek
print(yemekler)
sy = input("Silinecek yemek:")

for a in range (len(yemekler)):
    print("a değeri:",a)
    print(yemekler[a])
    if yemekler[a] == sy :
        yemekler.pop(a)
        break



#yemekler.pop(1)  # parantez içindeki indise ait veriyi siler


print("\nYEMEKLER:")
for a in yemekler:
    print(a)

#print(yemekler[-1])
#print(yemekler[-2])