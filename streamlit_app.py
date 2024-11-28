import streamlit as st
from PIL import Image
import turtle
import math

# Mengatur layar dan Turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.color("red")
t.hideturtle()

# Fungsi untuk menggambar bentuk hati
def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

# Menyiapkan Turtle untuk menggambar
t.penup()
t.goto(15, 0)

# Gambar hati
for i in range(0, 100, 2):
    t.pendown()
    x, y = corazon(i / 10)
    t.goto(x, y)

# Simpan gambar ke file
canvas = screen.getcanvas()
canvas.postscript(file="heart.eps")  # Simpan sebagai EPS

# Mengubah EPS ke PNG menggunakan PIL
from PIL import Image
img = Image.open("heart.eps")
img.save("heart.png")

# Tutup layar Turtle
turtle.done()


# Menampilkan gambar hati yang disimpan
img = Image.open("heart.png")
st.image(img, caption="Gambar Hati", use_column_width=True)
