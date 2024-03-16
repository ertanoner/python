import turtle
import random  
#random ile rastgele sayı üretilir.

# renkler[a] seçtiğimizde her döngüde renkler de tanıttığımız sıraya göre renklerde çizgi çizecek
renkler=["red","blue","magenta","yellow","pink"]
for a in range(4):
    # print(renkler[a])
    #random burada rastgele renkler seçecek
    turtle.color(random.choice(renkler))
    turtle.forward(100)
    turtle.right(90)
    
input()