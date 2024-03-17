import turtle
import random  
#random ile rastgele sayı üretilir.
# renkler[a] seçtiğimizde her döngüde renkler de tanıttığımız sıraya göre renklerde çizgi çizecek
renkler=["red","blue","magenta","yellow","pink"]
turtle.speed(10)

for xx in range(random.randint(1,10)):  #kare sayısı da rastgele
    
    turtle.penup()  #başlangıç koordinatını değiştirirken çizim görünmeyecek
    
    turtle.goto(random.randint(-400,400),random.randint(-400,400)) #random goto ile rastgele farklı noktalarda çizim
   
    turtle.pendown()  #başlangıç koordinatını değiştirdikten sonra kalem çizmeye başlar
   
    ku = random.randint(50,200)  # 50 ile 200 arasında bir kenar uzunluğu rastgele seçilecek ve rastgele kare boyutu olacak.
    for a in range(4):
        # print(renkler[a])
        turtle.color(random.choice(renkler))
        turtle.forward(ku)  #yukarıdaki ku tanımlandı
        turtle.right(90)
    
input()