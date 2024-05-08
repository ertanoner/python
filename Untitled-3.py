class Erkek ():
    ad = "ahmet"
    soyad = "ali"
    no = 5327777777
    meslek = "öğretmen"
    yas = input(f"{ad} {soyad} ın yasını giriniz:")
print(Erkek.ad)
print(Erkek.soyad)
print(Erkek.no)
print(Erkek.meslek)
print(f'{Erkek.ad} {Erkek.soyad} in yaşı {Erkek.yas}, mesleği {Erkek.meslek} ve telefon numarası {Erkek.no} dir')