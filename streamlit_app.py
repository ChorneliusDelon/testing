import streamlit as st
from PIL import Image

# Menampilkan gambar hati yang disimpan
img = Image.open("heart.png")
st.image(img, caption="Gambar Hati", use_column_width=True)
