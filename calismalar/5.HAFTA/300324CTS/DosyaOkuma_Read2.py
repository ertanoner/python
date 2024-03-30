# readline() ile satır okunur
okunan = open("deneme1.txt","r")
a = okunan.read(5) #ilk beş karakteri alır
b = okunan.read(6) #ilk altı karakteri alır. Aşağı geçme karakterini de bir karakter olarak kabul eder.
print(a,b)
okunan.close()