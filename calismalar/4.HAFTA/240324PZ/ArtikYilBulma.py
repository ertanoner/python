# #liste içinde eleman var mı bakma
# thislist = ["elma", "muz", "kiraz"]
# if "elma" in thislist:
#   print("Evet, 'elma' listede var.")

# modulus 2024%4  2024 ü mod 4 e göre al kalanı göster

# for a in range (1900,2024):  # 1900 tılından 2024 yılına kadar artık yılları bulma
#     if a%4==0 : print(a,"artık yıl")
#     else: print (a,"artık yıl değil") 


a = int(input("Bugün veya geçmiş en yakın artık yılı giriniz:"))
for xx in range (a,-1,-4):
    print(xx,end=",")

