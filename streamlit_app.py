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

# Menentukan rentang n untuk menggambar hati
n = np.linspace(0, 2 * np.pi, 1000)
x, y = corazon(n)

# Gambar hati
ax.plot(x, y, color='red', linewidth=3)

# Menampilkan gambar menggunakan Streamlit
st.pyplot(fig)
