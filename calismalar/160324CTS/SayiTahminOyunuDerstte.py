import random
bas = 1
son = 100
hak = 5
puan = 100
tutulan = random.randint(bas,son)
print(tutulan)
print(f"Ben {bas} ile {son} arası bir sayı tuttum.")
print(f"{hak} hakkın var.")

for xx in range(hak):
    tahmin = int(input("tahminin nedir?"))
    if tahmin == tutulan:
        print("Bildin.")
        print("Puanın:", puan)
        break
    elif tahmin > tutulan:
        print("Tahminin büyük.")
        puan -= 100//hak
        print("Puanın:", puan)
        
    elif tahmin < tutulan:
        print("Tahminin küçük.")
        puan -= 100//hak
        print("Puanın:", puan)

    if xx == hak-1: print("Kaybettin")    