import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Fungsi untuk menghitung koordinat bentuk hati
def corazon(n):
    x = 16 * np.sin(n)**3
    y = 13 * np.cos(n) - 5 * np.cos(2*n) - 2 * np.cos(3*n) - np.cos(4*n)
    return x, y

# Judul aplikasi
st.title("Animasi Hati dengan Musik di Streamlit")
st.write("Simulasi bentuk hati dengan animasi dan musik yang dimainkan bersamaan.")

# Tombol untuk memulai animasi
start_animation = st.button("Mulai Animasi dan Musik")

# Jika tombol ditekan, mulai proses animasi dan musik
if start_animation:
    # Menambahkan musik
    audio_path = "ssstik.io_1731710601228.mp3"  # Ganti dengan path file musik yang ingin diputar
    st.audio(audio_path, start_time=0)  # Memutar musik otomatis

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.set_facecolor("black")
    ax.axis("off")  # Sembunyikan grid dan sumbu

    colors = ["red", "pink", "orange", "yellow", "purple"]  # Warna untuk lapisan

    # Animasi berlapis
    for i in range(1, 16):
        t = np.linspace(0, 2 * np.pi, 100)  # Titik-titik koordinat
        x, y = corazon(t)
        ax.plot(x * i, y * i, color=colors[i % len(colors)], alpha=0.7)

        # Tampilkan layer saat ini di Streamlit
        st.pyplot(fig)
        time.sleep(0.2)  # Jeda sejenak sebelum menambah lapisan

    st.write("Animasi selesai!")
