import random  
mey = ["nar" , "muz" , "dut"]
#random.random dersek 0 ile 1 arasında rastgele bir sayı üretir
print(random.random())

#1 ile 20 arasında bir tam sayı rastgele seç
print(random.randint(1,20))

#rastgele bir meyve ismi seçer
print(random.choice(mey))


# yukarıdaki girdilere göre rastgele bir cümle seçimi
print(f"Haftalık {random.randint(1,5)}kg {random.choice(mey)} alınız.")

print(f"Her gün marketten {random.randint(2,8)} kg {random.choice(mey)} alıp eve getiririz.")

