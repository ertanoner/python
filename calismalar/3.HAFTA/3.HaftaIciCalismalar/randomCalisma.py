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

liste = ['Ayşe', 'Fatma', 'Ahmet','Mehmet']
print(random.choice(liste))
