abc = open("rehber.txt", "a")
abc.write("Merhaba Python dosya dünyası.\nİkinci satıra geçtik!!\n")
abc.write("Üçüncü satır çalışmaya devam--")
abc.write("!!!\n\n\n")
abc.close()

f = open("rehber.txt", "r")
print(f.read())