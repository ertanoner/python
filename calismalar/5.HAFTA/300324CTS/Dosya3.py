#deneme dosyası oluşturulmamışsa oluşturur, varsa açıp devamına yazar. fonksiyon "f" ile fonks yazdırabiliriz.
a=5
with open("deneme1.txt","a") as xx:
    xx.write("\nMerhaba\n")
    xx.write(f"Puan:{a}")