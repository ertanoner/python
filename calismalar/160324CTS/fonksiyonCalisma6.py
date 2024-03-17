#fonksiyonların değer döndürmesi için return komutunu kullanıyoruz
#bb=0 yazarsak ve alttaki bir işlemde 2. sayıyı girmez isek bb değerini tanımladığımız 0 değerini alır


def topla(aa,bb=0):
    return aa+bb

def carp(x,yy=1):
    return x*yy

sayi1 = int(input("1.sayı nedir?:"))
sayi2 = int(input("2.sayı nedir?:"))

# topla(sayi,sayi2) # tek başına işlemi yapar, print olmadan ekranda görünmez.
print (topla(sayi1))
print (carp(sayi1))
print(f"Toplam:{topla(sayi1,sayi2)}")
print(f"Carpım:{carp(sayi1,sayi2)}")


