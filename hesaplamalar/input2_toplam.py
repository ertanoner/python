def yhesap():
    print("Yaş Hesaplayıcı")
    ad = input("Adın nedir?")
    print(f"merhaba {ad}")
    yil = input (f"Hangi yılda doğdun {ad}?")
    print("{} demek {} yaşındasın".format(ad,2024-int(yil)))
    print(f"{ad} demek {2024-int(yil)} yaşındasın")
    print(ad,"demek", 2024-int(yil),"yaşındasın")
    input()
