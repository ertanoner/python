#fonksiyonların değer döndürmesi için return komutunu kullanıyoruz

def topla(aa,bb):
    return aa+bb

def carp(x,yy):
    return x*yy

sayi1 = int(input("1.sayı nedir?:"))
sayi2 = int(input("2.sayı nedir?:"))

# topla(sayi,sayi2) # tek başına işlemi yapar, print olmadan ekranda görünmez.
print (topla(sayi1,sayi2))
print (carp(sayi1,sayi2))
print(f"Toplam:{topla(sayi1,sayi2)}")
print(f"Carpım:{carp(sayi1,sayi2)}")


