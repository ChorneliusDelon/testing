import streamlit as st
import os

# Fungsi untuk membaca file HTML
def read_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Halaman awal
if "welcome_shown" not in st.session_state:
    st.session_state.welcome_shown = False

if not st.session_state.welcome_shown:
    html_path = "index.html"
    if os.path.exists(html_path):
        html_content = read_html(html_path)
        # Tampilkan file HTML
        st.components.v1.html(html_content, height=600, scrolling=False)

        # Tombol untuk melanjutkan
        if st.button("Lanjutkan"):
            st.session_state.welcome_shown = True
    else:
        st.error("File HTML tidak ditemukan.")
else:
    # Halaman utama aplikasi
    st.title("Coffee Shop Sederhana")
    st.subheader("Pesan Kopi atau Makanan")
    menu_items = {
        "Espresso": 15000,
        "Cappuccino": 20000,
        "Latte": 25000,
        "Mocha": 30000,
        "Croissant": 25000,
        "Brownies": 20000,
        "Cheesecake": 35000,
        "Donat": 15000,
    }

    selected_item = st.selectbox("Pilih Menu", list(menu_items.keys()))
    quantity = st.number_input("Jumlah (gelas/porsi)", min_value=1, step=1)
    if st.button("Pesan"):
        total_price = menu_items[selected_item] * quantity
        st.success(f"Anda memesan {quantity} {selected_item}. Total: Rp {total_price:,}.")
