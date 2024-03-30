#abc.write şeklinde sadece str leri yazdırabiliriz.
dosya = open("Toplama.py", "w")
dosya.write("#2 sayinin toplami:")
dosya.write("\nS1=input('1.sayiyi giriniz:')")
dosya.write("\nS2=input('2.sayiyi giriniz:')")
dosya.write("\nprint(S1+S2)")
dosya.close()
