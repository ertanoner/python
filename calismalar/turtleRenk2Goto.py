import turtle
import random  
#random ile rastgele sayı üretilir.

# renkler[a] seçtiğimizde her döngüde renkler de tanıttığımız sıraya göre renklerde çizgi çizecek
renkler=["red","blue","magenta","yellow","pink"]
turtle.penup()  #başlangıç koordinatını değiştirirken çizim görünmeyecek
turtle.goto(-100,-100)
turtle.pendown()  #başlangıç koordinatını değiştirdikten sonra kalem çizmeye başlar
for a in range(4):
    # print(renkler[a])
    turtle.color(renkler[a])
    turtle.forward(100)
    turtle.right(90)
    
input()