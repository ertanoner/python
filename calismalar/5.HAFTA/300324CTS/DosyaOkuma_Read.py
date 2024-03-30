# readline() ile satır okunur
okunan = open("deneme1.txt","r")
print(okunan.readline())  #ilk satırı okur. ilk satır boşsa boş görünür. Birden fazla satır yazılırsa çıktıda araya boşluk atar
print(okunan.readline())  
print(okunan.readline(2))  # parantez içerisine yazdığımız rakam kadar karakter alır. Kalanı alt satıra yazar.
print(okunan.readline())  
print(okunan.readline())  
okunan.close()