import streamlit as st
import mysql.connector
from datetime import datetime
import pandas as pd

# Koneksi ke Database
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cafe_system"
    )

# Fungsi Login
def login(username, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Fungsi Dashboard Admin
def admin_dashboard():
    st.title("Dashboard Admin")
    st.sidebar.header("Navigasi")
    menu = st.sidebar.radio("Pilih Menu", ["Kelola Menu", "Laporan", "Buat Akun Kasir"])

    if menu == "Kelola Menu":
        st.subheader("Kelola Menu")
        with st.form("form_menu"):
            name = st.text_input("Nama Menu")
            price = st.number_input("Harga", min_value=0.0)
            category = st.selectbox("Kategori", ["Makanan", "Minuman"])
            is_best_seller = st.checkbox("Best Seller")
            submit = st.form_submit_button("Simpan")

            if submit:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO menu (name, price, category, is_best_seller) VALUES (%s, %s, %s, %s)",
                    (name, price, category, is_best_seller)
                )
                conn.commit()
                conn.close()
                st.success("Menu berhasil ditambahkan!")

        # Tampilkan Data Menu
        conn = get_connection()
        menu_data = pd.read_sql("SELECT * FROM menu", conn)
        conn.close()
        st.dataframe(menu_data)

    elif menu == "Laporan":
        st.subheader("Laporan Penjualan")
        # Tampilkan laporan harian, mingguan, dll.
        # Kode akan ditambahkan...

    elif menu == "Buat Akun Kasir":
        st.subheader("Buat Akun Kasir")
        with st.form("form_kasir"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Buat Akun")

            if submit:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, 'kasir')", (username, password))
                conn.commit()
                conn.close()
                st.success("Akun kasir berhasil dibuat!")

# Fungsi Dashboard Kasir
def kasir_dashboard():
    st.title("Dashboard Kasir")
    # Tampilkan menu, buat pesanan, dll.
    # Kode akan ditambahkan...

# Login Page
st.title("Aplikasi Pemesanan Cafe")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    user = login(username, password)
    if user:
        if user['role'] == 'admin':
            admin_dashboard()
        elif user['role'] == 'kasir':
            kasir_dashboard()
    else:
        st.error("Username atau Password salah!")
