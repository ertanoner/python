import random
import io
import ast
ad = input("Kaydedilecek kişi adı ve soyadı:      ")
numara = random.randint(100, 1000)

klasor = open("ogrenciler2.txt","a")
klasor.write(f'\n{str({"adi":ad,"numara":numara})},')
klasor.close()

okunan = open("ogrenciler2.txt","r")
print(okunan.read())
okunan.close()

