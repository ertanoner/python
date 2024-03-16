#fonksiyonların değer döndürmesi için return komutunu kullanıyoruz

def topla(aa,bb):
    return f"Toplam:{aa+bb}"

def carp(x,yy):
    return f"Çarpım:{x*yy}"

sayi1 = int(input("1.sayı nedir?:"))
sayi2 = int(input("2.sayı nedir?:"))

# topla(sayi,sayi2) # tek başına işlemi yapar, print olmadan ekranda görünmez.
print (topla(sayi1,sayi2))
print (carp(sayi1,sayi2))



