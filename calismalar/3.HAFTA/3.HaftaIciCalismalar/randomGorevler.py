import random
#print(random.random())   # random.random komutu 0 ile 1 arasında rastgele bir sayı seçer.

#print (random.randint(1, 10))  # random.randint komutu belirtilen rakamlar arasından bir tam sayı seçer.
 
#print(random.uniform (1,100)) # Rastgele float: 1.0 <= x <100.0

#sayilar = range(50)
#print(random.sample(sayilar,3))  # sayılar değişkeninde belirlenen 0 dan 50 ye kadar olan sayılardan rastgele 3 tanesini sırasız seçer.

#isimler = ['Ahmet', 'Mehmet', 'Fikret', 'Saffet' , 'Hikmet']
#print(random.sample(isimler,3)) # isimler listesinde belirtilen isimlerden rastgele 3 tanesinin seçimi
 

#l=list(range(10))
#print (l)

#random.shuffle(l) #0 ile 9 arasında list te tanımlanmış sayıları rastgele sırayla yazar.
#print(l)

#liste = ['Ayşe', 'Fatma', 'Ahmet','Mehmet']
#print(random.choice(liste)) #listeden rastgele 1 isim seçer


#1.Görev:Ekrana rastgele 10 sayı yazan programı

#sayilar = range(1000000)
#print(random.sample(sayilar,10))

#2. Görev: Ekrana rastgele bir sayıyı 10 kere yazan bir program

#sayilar = range(1000000)
#x = random.sample(sayilar,1)
#print(x*10)


#3. Görev: Sayı tahmin oyunu
# baslangic=1
# son=100
# hak = 5
# puan=100
# secilen = random.randint(baslangic,son)
# print(secilen)
# print(f"{baslangic} ile {son} arasında rastgele belirlenen sayıyı tahmin ediniz.")
# print(f"{hak} hakkınız var.")

# for a in range(hak):
#     tahmin = int(input("Tahmininiz nedir?: "))
#     if tahmin == secilen:
#         print("Bildiniz.")
#         print("Puanınız:",puan)
#         break

#     elif tahmin > secilen:
#         print("Tahmininiz büyük.")
#         puan -= 100//hak
#         print("Puanınız:", puan)
        
#     elif tahmin < secilen:
#         print("Tahminin küçük.")
#         puan -= 100//hak
#         print("Puanınız:", puan)

#     if a == hak-1: print("Kaybettiniz")   



sinif = ['Ahmet', 'Mehmet', 'Fikret','Saffet','Hikmet','Nusret','Behçet','Damla','Eda','Çağla']
print(sinif)
print("Enter'e basarak sınıftan rastgele bir isim seçiniz")
input()
print(random.choice(sinif)) #listeden rastgele 1 isim seçer


