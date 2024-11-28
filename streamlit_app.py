import streamlit as st
import mysql.connector

# Koneksi ke database
def create_connection():
    return mysql.connector.connect(
        host="localhost",      # Ganti dengan host database Anda
        user="root",           # Ganti dengan username MySQL Anda
        password="password",   # Ganti dengan password MySQL Anda
        database="coffee_shop" # Nama database
    )

# Ambil data menu dari database
def get_menu():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, price FROM menu")
    result = cursor.fetchall()
    connection.close()
    return result

# Simpan pesanan ke database
def save_order(name, menu_id, quantity, total_price):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO orders (customer_name, menu_id, quantity, total_price) VALUES (%s, %s, %s, %s)",
        (name, menu_id, quantity, total_price)
    )
    connection.commit()
    connection.close()

# Antarmuka Streamlit
st.title("Coffee Shop Sederhana")

# Tampilkan menu dari database
st.subheader("Pilih Menu Kopi")
menu = get_menu()
menu_names = [f"{item[1]} - Rp {item[2]:,}" for item in menu]
selected_menu = st.selectbox("Menu Kopi", menu_names)
selected_menu_id = menu[menu_names.index(selected_menu)][0]
selected_menu_price = menu[menu_names.index(selected_menu)][2]

quantity = st.number_input("Jumlah (gelas)", min_value=1, step=1)

# Input nama pelanggan
customer_name = st.text_input("Nama Pelanggan")

# Tampilkan total harga
if customer_name:
    total_price = quantity * selected_menu_price
    st.write(f"Total harga: Rp {total_price:,}")

    # Simpan pesanan ke database
    if st.button("Pesan"):
        save_order(customer_name, selected_menu_id, quantity, total_price)
        st.success("Pesanan berhasil disimpan!")
