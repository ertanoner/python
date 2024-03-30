#yazarken stringe çevirmek gerekir
a = 5
b = 4
c = a+b
dosya = open("deneme2.txt","w")
dosya.write(str(c))
dosya.close()

okunan = open("deneme2.txt")
aa = okunan.read()
print(aa)
print(aa*2)   #aa stringini 2 kez yan yana yazdırdı.
print(int(aa)*2)   #aa stringini int e çev,r,p 2 ile çarpttı.
okunan.close()