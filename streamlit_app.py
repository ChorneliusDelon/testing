import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menggambar hati
def corazon(n):
    x = 16 * np.sin(n) ** 3
    y = 13 * np.cos(n) - 5 * np.cos(2*n) - 2 * np.cos(3*n) - np.cos(4*n)
    return x, y

# Membuat tampilan Streamlit
st.title("Gambar Hati dengan Matplotlib")

# Membuat plot hati
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.axis('off')  # Menyembunyikan axis agar fokus pada gambar hati

for i in range(1, 15):
    n = np.linspace(0, 2 * np.pi, 1000)  # Rentang untuk n
    x, y = corazon(n)  # Hitung x dan y untuk setiap titik
    ax.plot(x * i, y * i, color='red', linewidth=1)  # Gambar hati dengan skala yang berbeda

# Menampilkan gambar menggunakan Streamlit
st.pyplot(fig)
