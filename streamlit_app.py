import streamlit as st
import numpy as np

# Fungsi untuk menggambar hati
def corazon(n):
    x = 16 * np.sin(n) ** 3
    y = 13 * np.cos(n) - 5 * np.cos(2*n) - 2 * np.cos(3*n) - np.cos(4*n)
    return x, y

# Membuat tampilan Streamlit
st.title("Gambar Hati dengan Streamlit dan NumPy")

# Membuat rentang untuk n
n = np.linspace(0, 2 * np.pi, 1000)  # Rentang untuk n
x, y = corazon(n)  # Hitung x dan y untuk setiap titik

# Menampilkan gambar hati langsung dengan Streamlit
st.write("Berikut adalah gambar hati menggunakan Streamlit dan NumPy:")

# Plot hati menggunakan Streamlit's st.line_chart
st.line_chart(np.array([x, y]).T)  # Menampilkan data dalam format yang bisa dipahami oleh st.line_chart
