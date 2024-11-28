import sqlite3
import streamlit as st

# Buat atau sambungkan ke database SQLite
conn = sqlite3.connect("coffee_shop.db")
cursor = conn.cursor()

# Buat tabel jika belum ada
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price INTEGER NOT NULL
)
""")
conn.commit()

# Fungsi CRUD
def create_order(item, quantity, price):
    cursor.execute("INSERT INTO orders (item, quantity, price) VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()

def read_orders():
    cursor.execute("SELECT * FROM orders")
    return cursor.fetchall()

def update_order(order_id, item, quantity, price):
    cursor.execute("UPDATE orders SET item = ?, quantity = ?, price = ? WHERE id = ?", (item, quantity, price, order_id))
    conn.commit()

def delete_order(order_id):
    cursor.execute("DELETE FROM orders WHERE id = ?", (order_id,))
    conn.commit()

# Aplikasi Streamlit
st.title("CRUD Coffee Shop")

menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Operasi CRUD", menu)

if choice == "Create":
    st.subheader("Create Pesanan Baru")
    item = st.text_input("Nama Item")
    quantity = st.number_input("Jumlah", min_value=1, step=1)
    price = st.number_input("Harga per Item (Rp)", min_value=0, step=1000)

    if st.button("Tambah Pesanan"):
        create_order(item, quantity, price)
        st.success(f"Pesanan {item} berhasil ditambahkan.")

elif choice == "Read":
    st.subheader("Daftar Pesanan")
    orders = read_orders()
    for order in orders:
        st.write(f"ID: {order[0]}, Item: {order[1]}, Jumlah: {order[2]}, Harga: Rp {order[3]:,}")

elif choice == "Update":
    st.subheader("Update Pesanan")
    orders = read_orders()
    order_id = st.selectbox("Pilih ID Pesanan", [order[0] for order in orders])

    selected_order = [order for order in orders if order[0] == order_id][0]
    new_item = st.text_input("Nama Item", value=selected_order[1])
    new_quantity = st.number_input("Jumlah", min_value=1, step=1, value=selected_order[2])
    new_price = st.number_input("Harga per Item (Rp)", min_value=0, step=1000, value=selected_order[3])

    if st.button("Update Pesanan"):
        update_order(order_id, new_item, new_quantity, new_price)
        st.success(f"Pesanan ID {order_id} berhasil diupdate.")

elif choice == "Delete":
    st.subheader("Delete Pesanan")
    orders = read_orders()
    order_id = st.selectbox("Pilih ID Pesanan", [order[0] for order in orders])

    if st.button("Hapus Pesanan"):
        delete_order(order_id)
        st.success(f"Pesanan ID {order_id} berhasil dihapus.")
