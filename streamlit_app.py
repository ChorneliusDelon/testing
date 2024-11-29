import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menghitung koordinat bentuk hati
def corazon(n):
    x = 16 * np.sin(n)**3
    y = 13 * np.cos(n) - 5 * np.cos(2*n) - 2 * np.cos(3*n) - np.cos(4*n)
    return x, y

# Halaman utama Streamlit
st.title("Animasi Hati di Streamlit")
st.write("Ini adalah adaptasi dari kode turtle untuk Streamlit menggunakan Matplotlib.")

# Plot Matplotlib
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.set_facecolor("black")

# Warna untuk setiap lapisan
colors = ["red", "pink", "orange", "yellow", "purple"]

# Gambarkan beberapa layer bentuk hati
for i in range(1, 16):
    t = np.linspace(0, 2 * np.pi, 100)  # Menghasilkan 100 titik
    x, y = corazon(t)
    ax.plot(x * i, y * i, color=colors[i % len(colors)], alpha=0.7)

# Hilangkan grid dan axis
ax.axis("off")

# Tampilkan plot di Streamlit
st.pyplot(fig)
