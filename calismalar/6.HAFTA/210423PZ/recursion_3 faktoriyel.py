sonuc = 1
def selamla(xx):
    global sonuc
    
    sonuc *= xx
    print("Sayi:",xx)
    
    xx -= 1
    if xx > 1: selamla(xx)

a=int(input("faktoryeli alinacak sayiyi giriniz."))

selamla(a)
print("Sonuc:",sonuc)