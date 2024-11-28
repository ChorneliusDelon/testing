import streamlit as st

# Data menu
menu_items = {
    "Kopi": {
        "Espresso": 15000,
        "Cappuccino": 20000,
        "Latte": 25000,
        "Mocha": 30000,
    },
    "Makanan": {
        "Croissant": 25000,
        "Brownies": 20000,
        "Cheesecake": 35000,
        "Donat": 15000,
    },
}

# Fungsi untuk menghitung total harga
def calculate_total(order_list):
    total = sum(item["price"] * item["quantity"] for item in order_list)
    return total

# Judul aplikasi
st.title("Coffee Shop Sederhana")

# Pilih kategori menu
category = st.selectbox("Pilih Kategori Menu", list(menu_items.keys()))

# Pilih item menu
menu = menu_items[category]
selected_item = st.selectbox("Pilih Menu", list(menu.keys()))
price = menu[selected_item]

# Input jumlah
quantity = st.number_input("Jumlah (gelas/porsi)", min_value=1, step=1)

# Tombol tambah ke pesanan
if "order_list" not in st.session_state:
    st.session_state["order_list"] = []

if st.button("Tambah ke Pesanan"):
    st.session_state["order_list"].append({"item": selected_item, "price": price, "quantity": quantity})
    st.success(f"{quantity} {selected_item} berhasil ditambahkan ke pesanan!")

# Tampilkan pesanan
st.subheader("Pesanan Anda")
if st.session_state["order_list"]:
    for order in st.session_state["order_list"]:
        st.write(f"- {order['quantity']}x {order['item']} - Rp {order['price']:,}/item")
    
    total_price = calculate_total(st.session_state["order_list"])
    st.write(f"**Total Harga: Rp {total_price:,}**")

    # Simulasi pembayaran
    if st.button("Bayar"):
        st.session_state["order_list"] = []
        st.success("Pesanan Anda berhasil! Terima kasih telah memesan.")
else:
    st.write("Belum ada pesanan.")
