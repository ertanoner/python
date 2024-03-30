
with open("sayilar.txt","a") as xx:
    for a in range(10):
     #   xx.write(a)   #Dosyaya int yazılamaz
       xx.write(f"\"{a}") 
   