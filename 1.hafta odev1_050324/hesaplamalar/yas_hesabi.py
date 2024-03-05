def yhesap():
    print("Yaş Hesaplayıcı")
    ad = input("Adın nedir?")
    print(f"merhaba {ad}")
    yil = input (f"Hangi yılda doğdun {ad}?")
    print(ad,"demek", 2024-int(yil),"yaşındasın")
    input()
