ad = input("Adınız: ")
print("Merhaba ",ad)
input()

k = float(input("Karenin bir kenar uzunluğunu giriniz: "))
cevre = k*4
print("Karenin çevresinin uzunluğu: ",cevre)
input()

k = float(input("Karenin bir kenar uzunluğunu giriniz: "))
alan = k*k
print("Karenin alanı ",alan)
input()

#klavyeden girilen 2 sayının toplamı
a = float(input("1.sayıyı giriniz: "))
b = float(input("2.sayıyı giriniz: "))
t = float(a+b) 
print("2 sayının toplamı:",t)
input()

#klavyeden girilen 2 sayının toplamı, farkı, çarpımı ve bölümü
a = float(input("1.sayıyı giriniz: "))
b = float(input("2.sayıyı giriniz: "))
toplam = float(a+b)
fark =  float(a-b)
carpim = float(a*b)
bolum = float(a/b)
print("2 sayının toplamı:",toplam, "2 sayının farkı: ",fark, "2 saynın çarpımı: ",carpim, "2 sayının bölümü :",bolum)
input()
#yaş hesabı
y = int(input("Doğum yılınızı giriniz: "))
print("Yaşınız: ",2024-y)
input()
#Yazılı not ortalaması
S1 = float(input("1. yazılı notunuzu giriniz :"))
S2 = float(input("2. yazılı notunuzu giriniz :"))
P = float(input("Performans notunuzu giriniz :"))
ortalama = (S1+S2+P)/3
print("Yıl sonu ortalamanız: ",ortalama)
input()
#Boya göre ideal kilo hesaplama
c = str(input("Cinsiyetinizi belirtiniz - Kadın için 'k'- Erkek için 'e':"))
b = float(input("Boyunuzu cm olarak giriniz :"))
ek = float((50+(2.3/2.54)*b-152.4))
kk = float((45.5+(2.3/2.54)*b-152.4))
if c == "e" : 
    print("İdeal kilonuz :",ek)
elif c == "k" : 
    print("İdeal kilonuz :",kk)
else : print("cinsiyeti 'e' veya 'k' olarak giriniz")
   
