import turtle
import random

# Ekranı oluştur
e = turtle.Screen()
e.title("Kaplumbağayı Yakala Oyunu")

# Turtle oluştur
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.speed(1)

# Yazılar için ayrı bir turtle
yazi = turtle.Turtle()
yazi.hideturtle()
yazi.penup()

# Değişkenler
time = 10
score = 0
oyun_bitti = False

# Yazıları güncelleme fonksiyonu
def guncelle_yazi():
    """Skor ve zaman yazısını sabit tutar"""
    yazi.clear()
    yazi.goto(-200, 200)
    yazi.write(f"Skor: {score}", align="left", font=("Arial", 16, "normal"))
    yazi.goto(150, 200)
    yazi.write(f"Time: {time}", align="right", font=("Arial", 16, "normal"))

# Turtle rastgele hareket etme fonksiyonu
def fonk():
    """Turtle'ı rastgele bir yere taşır"""
    if not oyun_bitti:
        rand1 = random.randint(-300, 300)
        rand2 = random.randint(-300, 300)
        t.goto(rand1, rand2)
        e.ontimer(fonk, 700)  # Her 0.7 saniyede tekrar çağırılır

# Turtle'a tıklanınca çalışan fonksiyon
def tiklandi(x, y):
    """Tıklama ile skor artırır ve zaman azaltır"""
    global score, time, oyun_bitti
    if not oyun_bitti:
        score += 1
        t.color("red")
        guncelle_yazi()  # Yazıyı güncelle
        time -= 1
        if time == 0:
            oyun_bitti = True
            yazi.goto(0, 0)
            yazi.write("Oyun Bitti!", align="center", font=("Arial", 24, "bold"))
            t.hideturtle()

# Başlangıç yazıları
guncelle_yazi()

# Turtle hareketini başlat
fonk()

# Turtle'a tıklama olayını bağla
t.onclick(tiklandi)

# Sonsuz döngü
turtle.mainloop()

